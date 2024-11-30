import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit, OptimizeWarning
import math
from typing import Tuple, List

def readfile(filename: str) -> Tuple[np.ndarray, np.ndarray]:
    """Reads and returns the data in the file as two numpy arrays.

    Parameters:
    filename (str): The name of the file to read.

    Returns:
    Tuple[np.ndarray, np.ndarray]: Two numpy arrays containing the x and y data.
    """
    with open(filename, "r") as filehandle:
        lines = filehandle.readlines()
    
    xarr = np.array([])
    yarr = np.array([])
    
    for line in lines:
        temp = line.split(",")
        xarr = np.append(xarr, float(temp[0]))
        yarr = np.append(yarr, float(temp[1]))
    
    return xarr, yarr

def plot(x: np.ndarray, y: np.ndarray, title: str) -> None:
    """Plots two columns of values and displays them.

    Parameters:
    x (np.ndarray): X-axis values.
    y (np.ndarray): Y-axis values.
    title (str): Title of the plot.
    """
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel("Wavelength")
    plt.ylabel("Spectral radiance")
    plt.show()

def plankspec(lamda: np.ndarray, h: float, c: float, k: float, T: float) -> np.ndarray:
    """The true Planck spectrum equation.

    Parameters:
    lamda (np.ndarray): Wavelengths.
    h (float): Planck's constant.
    c (float): Speed of light.
    k (float): Boltzmann's constant.
    T (float): Temperature.

    Returns:
    np.ndarray: Spectral radiance.
    """
    return (2 * h * c ** 2) / (lamda ** 5) * (1 / (np.expm1(h * c / (lamda * k * T))))

def fit1(lamda: np.ndarray, hc2: float, hcbykbt: float) -> np.ndarray:
    """First fitting function with combined parameters.

    Parameters:
    lamda (np.ndarray): Wavelengths.
    hc2 (float): Combined parameter.
    hcbykbt (float): Combined parameter.

    Returns:
    np.ndarray: Fitted values.
    """
    return (2 * hc2) / (lamda ** 5) * (1 / (np.expm1(hcbykbt / lamda)))

def fitT(lamda: np.ndarray, T: float) -> np.ndarray:
    """Fit function to estimate temperature.

    Parameters:
    lamda (np.ndarray): Wavelengths.
    T (float): Temperature.

    Returns:
    np.ndarray: Fitted values.
    """
    return plankspec(lamda, 6.626e-34, 3e8, 1.38e-23, T)

def fith(lamda: np.ndarray, h: float) -> np.ndarray:
    """Fit function to estimate Planck's constant.

    Parameters:
    lamda (np.ndarray): Wavelengths.
    h (float): Planck's constant.

    Returns:
    np.ndarray: Fitted values.
    """
    return plankspec(lamda, h, 3e8, 1.38e-23, T)

def fitc(lamda: np.ndarray, c: float) -> np.ndarray:
    """Fit function to estimate the speed of light.

    Parameters:
    lamda (np.ndarray): Wavelengths.
    c (float): Speed of light.

    Returns:
    np.ndarray: Fitted values.
    """
    return plankspec(lamda, 6.626e-34, c, 1.38e-23, T)

def fitk(lamda: np.ndarray, k: float) -> np.ndarray:
    """Fit function to estimate Boltzmann's constant.

    Parameters:
    lamda (np.ndarray): Wavelengths.
    k (float): Boltzmann's constant.

    Returns:
    np.ndarray: Fitted values.
    """
    return plankspec(lamda, 6.626e-34, 3e8, k, T)

def metrics_and_plot(fitfunction, params: np.ndarray, covars: np.ndarray, yarr: np.ndarray, xarr: np.ndarray, title: str) -> None:
    """Evaluates and plots the fit results.

    Parameters:
    fitfunction: The fitting function.
    params (np.ndarray): Fitted parameters.
    covars (np.ndarray): Covariance matrix of the parameters.
    yarr (np.ndarray): Y-axis values.
    xarr (np.ndarray): X-axis values.
    title (str): Title of the plot.
    """
    predicts = fitfunction(xarr, *params)
    
    residuals = yarr - predicts
    residualssquaresum = np.sum(residuals ** 2)
    ysquaresum = np.sum((yarr - np.mean(yarr)) ** 2)
    R2 = 1 - (residualssquaresum / ysquaresum)
    
    standarddevparams = np.sqrt(np.diag(covars))
    
    params_str = ", ".join([f"Param {i+1}: {param:.3e} ± {std:.3e}" for i, (param, std) in enumerate(zip(params, standarddevparams))])
    
    plt.plot(xarr, yarr, label="Original dataset")
    plt.plot(xarr, predicts, label="Fit curve")
    plt.xlabel("Wavelength (in m)")
    plt.ylabel("Spectral radiance")
    plt.title(f"Comparison of the original dataset and the best fit\n{title}, R2 score: {R2:.3f}\n{params_str}")
    plt.legend()
    plt.show()

def estimate_params(fitfunction, xarr: np.ndarray, yarr: np.ndarray, initial_guesses: List[float]) -> Tuple[np.ndarray, np.ndarray]:
    """Estimates the parameters of the fitting function using curve fitting.

    Parameters:
    fitfunction: The fitting function.
    xarr (np.ndarray): X-axis values.
    yarr (np.ndarray): Y-axis values.
    initial_guesses (List[float]): Initial guesses for the parameters.

    Returns:
    Tuple[np.ndarray, np.ndarray]: Estimated parameters and covariance matrix.
    """
    try:
        return curve_fit(fitfunction, xarr, yarr, p0=initial_guesses)
    except OptimizeWarning:
        new_guesses = [(1 + 0.001) * i for i in initial_guesses]
        return estimate_params(fitfunction, xarr, yarr, initial_guesses=new_guesses)

FILENAME = "d4.txt"

xarr, yarr = readfile(FILENAME)
plot(xarr, yarr, f"Given dataset - {FILENAME}")

parameters, covariances = estimate_params(fit1, xarr, yarr, initial_guesses=[1e-17, 4.695 * xarr[np.argmax(yarr)]])
metrics_and_plot(fit1, parameters, covariances, yarr, xarr, "hc2 and hcbykbt (determined by finding wavelength at max radiance)")

parameters, covariances = estimate_params(fitT, xarr, yarr, initial_guesses=[4000])
T = parameters[0]
metrics_and_plot(fitT, parameters, covariances, yarr, xarr, "T (with a random guess)")

parameters, covariances = estimate_params(fith, xarr, yarr, initial_guesses=[1e-34])
metrics_and_plot(fith, parameters, covariances, yarr, xarr, "h (with an arbitrary guess of the same order)")

parameters, covariances = estimate_params(fitc, xarr, yarr, initial_guesses=[2.5e8])
metrics_and_plot(fitc, parameters, covariances, yarr, xarr, "c (with an arbitrary guess of the same order)")

parameters, covariances = estimate_params(fitk, xarr, yarr, initial_guesses=[1e-23])
metrics_and_plot(fitk, parameters, covariances, yarr, xarr, "k (with an arbitrary guess of the same order)")

