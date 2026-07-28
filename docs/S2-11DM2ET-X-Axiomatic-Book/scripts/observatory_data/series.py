"""Uniform series container for free-first R-FFT."""
from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any

import numpy as np


@dataclass
class ObservatorySeries:
    """A real (or explicitly empty) observatory time series for R-FFT."""

    dataset_id: str
    facility: str
    values: np.ndarray
    times: np.ndarray  # seconds from series start (or absolute if note says so)
    dt: float | None  # None if unevenly sampled
    uniform: bool
    source_url: str
    provenance: dict[str, Any] = field(default_factory=dict)
    is_real: bool = True
    notes: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.values = np.asarray(self.values, dtype=np.float64).ravel()
        self.times = np.asarray(self.times, dtype=np.float64).ravel()
        if len(self.values) != len(self.times):
            raise ValueError("values and times length mismatch")
        if not self.is_real:
            raise ValueError(
                "ObservatorySeries refuses is_real=False — synthetics are dismissed"
            )

    @property
    def n(self) -> int:
        return len(self.values)

    def to_uniform(
        self,
        dt: float | None = None,
        method: str = "linear",
    ) -> tuple[np.ndarray, float]:
        """
        Return (uniform_values, dt) suitable for r_fft_5399.full_r_fft_analysis.

        Uneven series are linearly interpolated onto a regular grid spanning
        [t_min, t_max]. This is a documented pre-processing step, not a claim
        of native uniform sampling.
        """
        if self.uniform and self.dt is not None and self.dt > 0:
            return self.values.copy(), float(self.dt)

        t = self.times
        y = self.values
        order = np.argsort(t)
        t = t[order]
        y = y[order]
        # drop duplicate times
        _, uniq = np.unique(t, return_index=True)
        t = t[uniq]
        y = y[uniq]
        if len(t) < 4:
            raise ValueError("need >= 4 unique samples to build a uniform series")

        span = float(t[-1] - t[0])
        if span <= 0:
            raise ValueError("non-positive time span")
        if dt is None:
            # median positive cadence, floored so n stays tractable
            d = np.diff(t)
            d = d[d > 0]
            dt = float(np.median(d)) if len(d) else span / max(len(t) - 1, 1)
        dt = float(dt)
        if dt <= 0:
            raise ValueError("dt must be positive")
        n = max(int(np.floor(span / dt)) + 1, 4)
        # hard cap: refuse accidental micro-dt explosions
        max_n = 2_000_000
        if n > max_n:
            dt = span / (max_n - 1)
            n = max_n
        t_u = t[0] + np.arange(n, dtype=np.float64) * dt
        if method != "linear":
            raise ValueError("only method='linear' is supported")
        y_u = np.interp(t_u, t, y)
        return y_u, dt

    def to_dict(self) -> dict[str, Any]:
        d = asdict(self)
        d["values"] = self.values.tolist()
        d["times"] = self.times.tolist()
        d["n"] = self.n
        return d
