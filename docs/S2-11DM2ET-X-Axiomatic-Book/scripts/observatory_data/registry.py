"""Observatory registry — real facilities only; synthetics dismissed."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

# Package: .../scripts/observatory_data → repo root is parents[2]
_REPO = Path(__file__).resolve().parents[2]
DATA_ROOT = _REPO / "data" / "RFFT_datasets"
REAL_ROOT = DATA_ROOT / "real"
REGISTRY_PATH = DATA_ROOT / "REGISTRY.json"

DISMISSED_SYNTHETIC_IDS = frozenset(
    {
        "pure_noise",
        "pure_G4",
        "G4_plus_noise",
        "off_target_600",
        "AM_G4",
        "coloured_noise",
        "multi_harmonic",
        "multi_k_residual_placeholder",
    }
)


def load_registry(path: Path | None = None) -> dict[str, Any]:
    p = path or REGISTRY_PATH
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def list_observatories(reg: dict[str, Any] | None = None) -> list[str]:
    reg = reg or load_registry()
    return sorted(reg.get("observatories", {}).keys())


def get_entry(dataset_id: str, reg: dict[str, Any] | None = None) -> dict[str, Any]:
    reg = reg or load_registry()
    if dataset_id in DISMISSED_SYNTHETIC_IDS or dataset_id in reg.get("policy", {}).get(
        "dismissed_ids", []
    ):
        raise ValueError(
            f"Dataset '{dataset_id}' is DISMISSED synthetic test data and "
            "cannot be used for free-first discovery analysis. "
            "Use an Observatories registry id instead "
            f"(e.g. {list_observatories(reg)[:3]}…)."
        )
    obs = reg.get("observatories", {})
    if dataset_id not in obs:
        known = ", ".join(list_observatories(reg))
        raise KeyError(
            f"Unknown dataset_id '{dataset_id}'. Known observatories: {known}"
        )
    return obs[dataset_id]


def dismiss_synthetic(dataset_id: str) -> None:
    """Raise if the id is a dismissed synthetic; otherwise return."""
    if dataset_id in DISMISSED_SYNTHETIC_IDS:
        raise ValueError(
            f"'{dataset_id}' is fabricated synthetic test data — dismissed. "
            "Load real observatory series via load_series(<registry_id>)."
        )


def staging_dir(dataset_id: str, reg: dict[str, Any] | None = None) -> Path:
    entry = get_entry(dataset_id, reg)
    sub = entry.get("staging_subdir", dataset_id)
    path = REAL_ROOT / sub
    path.mkdir(parents=True, exist_ok=True)
    return path
