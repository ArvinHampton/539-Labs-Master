"""Real observatory data access for free-first R-FFT-539.9 analysis."""

from .registry import (
    DATA_ROOT,
    REGISTRY_PATH,
    dismiss_synthetic,
    list_observatories,
    load_registry,
)
from .series import ObservatorySeries
from .loaders import (
    fetch_dataset,
    load_series,
    stage_status,
)
from .nds2_pure import NDS2Client, fetch_gwosc_aux
from .physionet_eeg import physionet_eeg_to_arrays

__all__ = [
    "DATA_ROOT",
    "REGISTRY_PATH",
    "NDS2Client",
    "ObservatorySeries",
    "dismiss_synthetic",
    "fetch_dataset",
    "fetch_gwosc_aux",
    "list_observatories",
    "load_registry",
    "load_series",
    "physionet_eeg_to_arrays",
    "stage_status",
]
