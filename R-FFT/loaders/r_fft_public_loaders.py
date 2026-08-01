"""
R-FFT-539.9 public dataset loaders (expanded Observatories edition)
Use on the machine that has scripts/r_fft_5399.py and network access.

Free-first discipline is mandatory on every series.
"""

import numpy as np
import os

# ------------------------------------------------------------------
# Synthetic helpers (staged files)
# ------------------------------------------------------------------

def load_synthetic(npz_path):
    """Load a staged .npz from the synthetic suite."""
    data = np.load(npz_path)
    return data["t"], data["signal"], float(data["fs"])

def load_synthetic_dir(base_dir="/home/workdir/artifacts/RFFT_datasets/synthetic"):
    """Return dict of all staged synthetic series."""
    out = {}
    for f in os.listdir(base_dir):
        if f.endswith(".npz"):
            name = f.replace(".npz", "")
            t, sig, fs = load_synthetic(os.path.join(base_dir, f))
            out[name] = {"t": t, "signal": sig, "fs": fs}
    return out

# ------------------------------------------------------------------
# LIGO / Virgo / KAGRA (GWpy + NDS2)
# ------------------------------------------------------------------

def load_ligo_aux(channel="L1:ISI-GND_STS_HAM5_X_BLRMS_100M_300M.rms",
                  start=1266624018, duration=3600*6, host="nds.gwosc.org"):
    """
    Fetch a LIGO O3 second-trend auxiliary channel (already 1 Hz).
    Requires: pip install gwpy
    Example channels:
      H1:ISI-GND_STS_ITMY_Z_BLRMS_30M_100M.rms
      L1:ISI-GND_STS_HAM5_X_BLRMS_100M_300M.rms
      H1:ISI-GND_BRS_ETMY_RX_BLRMS_30M_100M.rms
    """
    try:
        from gwpy.timeseries import TimeSeries
        ts = TimeSeries.fetch(channel, start=start, end=start+duration, host=host)
        t = ts.times.value - ts.times.value[0]
        signal = ts.value.astype(float)
        fs = float(ts.sample_rate.value)
        return t, signal, fs
    except Exception as e:
        raise RuntimeError(f"GWpy LIGO fetch failed: {e}")

def load_virgo_example(channel="V1:Hrec_hoft_16384Hz",
                       start=1266624018, duration=3600, host="nds.gwosc.org",
                       target_fs=1.0):
    """
    Fetch a Virgo strain segment and downsample to target_fs (default 1 Hz).
    Requires gwpy. Adjust channel name to an available open-data product.
    """
    try:
        from gwpy.timeseries import TimeSeries
        ts = TimeSeries.fetch(channel, start=start, end=start+duration, host=host)
        if ts.sample_rate.value > target_fs:
            ts = ts.resample(target_fs)
        t = ts.times.value - ts.times.value[0]
        signal = ts.value.astype(float)
        fs = float(ts.sample_rate.value)
        return t, signal, fs
    except Exception as e:
        raise RuntimeError(f"GWpy Virgo fetch failed: {e}")

def load_kagra_example(channel="K1:Hrec_hoft_16384Hz",
                       start=1266624018, duration=3600, host="nds.gwosc.org",
                       target_fs=1.0):
    """
    Fetch a KAGRA strain segment (where released) and downsample.
    Requires gwpy. Channel availability depends on the joint-run open-data release.
    """
    try:
        from gwpy.timeseries import TimeSeries
        ts = TimeSeries.fetch(channel, start=start, end=start+duration, host=host)
        if ts.sample_rate.value > target_fs:
            ts = ts.resample(target_fs)
        t = ts.times.value - ts.times.value[0]
        signal = ts.value.astype(float)
        fs = float(ts.sample_rate.value)
        return t, signal, fs
    except Exception as e:
        raise RuntimeError(f"GWpy KAGRA fetch failed: {e}")

# ------------------------------------------------------------------
# NANOGrav residual conversion notes
# ------------------------------------------------------------------

def nanograv_residual_to_even(t_mjd, residual_us, target_dt_days=1.0):
    """
    Convert irregular NANOGrav post-fit residuals to an evenly sampled vector.

    Parameters
    ----------
    t_mjd : array-like
        Observation epochs in MJD.
    residual_us : array-like
        Residual values (microseconds) at those epochs.
    target_dt_days : float
        Desired uniform cadence in days.

    Returns
    -------
    t_sec, resid_even, fs
        Evenly sampled time in seconds, residual vector, sample rate in Hz.
    """
    t_mjd = np.asarray(t_mjd, dtype=float)
    residual_us = np.asarray(residual_us, dtype=float)
    order = np.argsort(t_mjd)
    t_mjd = t_mjd[order]
    residual_us = residual_us[order]

    t0 = t_mjd[0]
    t_rel_days = t_mjd - t0
    t_even = np.arange(0, t_rel_days[-1], target_dt_days)
    resid_even = np.interp(t_even, t_rel_days, residual_us)

    t_sec = t_even * 86400.0
    fs = 1.0 / (target_dt_days * 86400.0)
    return t_sec, resid_even, fs

def load_nanograv_residual_stub(path_to_ascii_table):
    """
    Stub: load an ASCII residual table (columns typically MJD, residual, ...).
    User must adapt column indices to the specific NANOGrav residual file format
    (epoch-averaged or full, whitened or un-whitened) downloaded from Zenodo
    or nanograv.org, then call nanograv_residual_to_even.
    """
    raise NotImplementedError(
        "Download residual tables from Zenodo (15-yr DOI 10.5281/zenodo.16051178) "
        "or nanograv.org, parse MJD + residual columns, then call "
        "nanograv_residual_to_even(t_mjd, residual_us)."
    )

# ------------------------------------------------------------------
# EHT / M87* light-curve proxy construction notes
# ------------------------------------------------------------------

def eht_proxy_from_epochs(epochs_mjd, values, target_dt_days=30.0):
    """
    Construct a simple evenly sampled proxy light curve from sparse EHT epochs
    (e.g. polarisation fraction or EVPA measurements published for 2017/2018/2021).

    This is a coarse proxy only. Continuous 1 Hz series do not exist.
    Label any subsequent R-FFT result as a proxy analysis.
    """
    epochs_mjd = np.asarray(epochs_mjd, dtype=float)
    values = np.asarray(values, dtype=float)
    order = np.argsort(epochs_mjd)
    epochs_mjd = epochs_mjd[order]
    values = values[order]

    t0 = epochs_mjd[0]
    t_rel = epochs_mjd - t0
    t_even = np.arange(0, t_rel[-1] + target_dt_days, target_dt_days)
    proxy = np.interp(t_even, t_rel, values)

    t_sec = t_even * 86400.0
    fs = 1.0 / (target_dt_days * 86400.0)
    return t_sec, proxy, fs

# ------------------------------------------------------------------
# Demo
# ------------------------------------------------------------------

if __name__ == "__main__":
    syn = load_synthetic_dir()
    print("Staged synthetic series:", list(syn.keys()))
    for k, v in syn.items():
        print(f"  {k}: N={len(v['signal'])}, fs={v['fs']}")
    print("\nPublic loaders ready (require local network + gwpy for LIGO/Virgo/KAGRA).")
    print("NANOGrav: convert residuals with nanograv_residual_to_even after download.")
    print("EHT: construct proxy with eht_proxy_from_epochs from published epoch values.")
