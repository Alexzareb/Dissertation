import numpy as np
from scipy.optimize import curve_fit
from sklearn.linear_model import LinearRegression


def N_i_j(i, j, data):
    count = 0
    ij = int('{}{}'.format(i, j))
    for tok in data:
        if tok == ij:
            count += 1
    return count

def N_i(i, data):
    count = 0
    for tok in data:
        if str(tok).startswith(str(i)):
            count += 1

    return count

def T_i_j(i, j, data):
    top = N_i_j(i, j, data)
    bottom = N_i(j, data)

    return top/bottom

def T_k(i, k, data):
    return T_i_j(i, i+k, data)


def z_k(k, omega, data):
    count = 0
    for i in range(omega - k):
        for l in range(N_i(i + 1, data)):
            count += 1

    return count

def f(k, a, c):
    return a * np.power(c, k - 1)

def horton_Rb(data, r):
    return horton_Nr(data, r)/horton_Nr(data, r + 1)

def horton_Nr(data, r):
    return data.count(r)

def horton_ri(strahler_data, length_data, r):
    lengths = []

    for s, l in zip(strahler_data, length_data):
        if s == r:
            lengths.append(l)

    return np.mean(lengths)

def horton_Rr(strahler_data, length_data, r):
    return horton_ri(strahler_data, length_data, r + 1) / horton_ri(strahler_data, length_data, r)

def D(Rb, Rr):
    return np.log(Rb) / np.log(Rr)

def read_toku_data(filename):

    with open(filename) as f_data:
        f_data.readline()
        data = f_data.readlines()

    toku = []
    strahler = []
    lengths = []

    for d in data:
        s = d.split(',')
        strahler.append(int(s[0]))
        toku.append(int(s[1]))
        lengths.append(float(s[2]))

    return toku, strahler, lengths


def fit_a_and_c(toku, strahler):

    x = []
    y = []
    omega = max(strahler)

    for k in range(1, omega + 1):
        for i in range(1, omega + 1):
            if ((i + k) <= omega) and ((i + k) >= 2):

                tk = T_k(i, k, toku)
                x.append(k)
                y.append(tk)

    weights = [z_k(k, omega, toku) for k in x]

    weights = np.sqrt(weights)
    norm_weights = []

    for w in weights:
        W = (w - np.min(weights)) / (np.max(weights) - np.min(weights))
        norm_weights.append((1 - W) + 0.01)

    p0 = 1.26, 2.4

    popt, pcov = curve_fit(f, x, y, p0)

    residuals = np.array(y) - f(np.array(x), popt[0], popt[1])
    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((y - np.mean(y))**2)
    r_squared = 1 - (ss_res / ss_tot)

    return r_squared, popt[0], popt[1]

def fit_a_and_c_x_y(toku, strahler):

    x = []
    y = []
    omega = max(strahler)

    for k in range(1, omega + 1):
        for i in range(1, omega + 1):
            if ((i + k) <= omega) and ((i + k) >= 2):

                tk = T_k(i, k, toku)
                x.append(k)
                y.append(tk)

    weights = [z_k(k, omega, toku) for k in x]

    weights = np.sqrt(weights)
    norm_weights = []

    for w in weights:
        W = (w - np.min(weights)) / (np.max(weights) - np.min(weights))
        norm_weights.append((1 - W) + 0.01)

    p0 = 1.26, 2.4

    popt, pcov = curve_fit(f, x, y, p0)

    residuals = np.array(y) - f(np.array(x), popt[0], popt[1])
    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((y - np.mean(y))**2)
    r_squared = 1 - (ss_res / ss_tot)

    return r_squared, popt[0], popt[1], x, y


def calc_Rb(strahler):

    omega = max(strahler)

    Rbs = np.zeros(omega - 1)

    for a, q in enumerate(range(1, omega)):
        Rbs[a] = horton_Rb(strahler, q)

    std = np.std(Rbs)
    avg = np.mean(Rbs)

    return avg, std


def calc_Rr(strahler, lengths):

    omega = max(strahler)

    Rbs = np.zeros(omega - 1)

    for a, q in enumerate(range(1, omega)):
        Rbs[a] = horton_Rr(strahler, lengths, q)

    std = np.std(Rbs)
    avg = np.mean(Rbs)

    return avg, std
