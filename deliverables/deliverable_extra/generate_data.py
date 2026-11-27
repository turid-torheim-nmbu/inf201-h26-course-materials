from collections.abc import Callable
import numpy as np


def simulate_sensor(
        x_exact_fn: Callable[[np.ndarray], np.ndarray],
) -> tuple[np.ndarray, np.ndarray, np.ndarray, float]:

    """Simulate 5 seconds of noisy position sensor readings sampled at 200 Hz.

    Evaluates the exact analytical displacement function on a uniform time grid
    and corrupts it with 60 Hz electrical interference (amplitude 0.8 m) and
    Gaussian white sensor noise (standard deviation 0.25 m) using a fixed random
    seed for reproducibility.

    Args:
        x_exact_fn (Callable[[np.ndarray], np.ndarray]): A vectorized numerical
            function (such as one created via ``sympy.lambdify``) that accepts a
            1D NumPy array of time values in seconds and returns the exact
            displacement values in meters.

    Returns:
        tuple[np.ndarray, np.ndarray, np.ndarray, float]: A 4-tuple containing:
            - t (np.ndarray): 1D array of timestamps in seconds, with shape (1000,).
            - raw_signal (np.ndarray): 1D array of corrupted sensor readings
              (clean signal + 60 Hz hum + Gaussian noise) in meters, with shape (1000,).
            - clean_signal (np.ndarray): 1D array of true, noise-free
              displacements in meters, with shape (1000,).
            - fs (float): Sampling rate of the sensor in Hz (200.0).
    """
    rng = np.random.default_rng(7)
    fs = 200.0
    t = np.arange(0, 5.0, 1.0 / fs)

    clean_signal = x_exact_fn(t)
    electrical_buzz = 0.8 * np.sin(2 * np.pi * 60.0 * t)
    sensor_noise = rng.normal(0, 0.25, size=t.shape)

    raw_signal = clean_signal + electrical_buzz + sensor_noise
    return t, raw_signal, clean_signal, fs
