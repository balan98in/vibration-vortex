import numpy as np
import scipy.linalg as la
import scipy.signal as signal
import matplotlib as mpl
M = np.array([[4, 0, 0], [0, 4, 0], [0, 0, 4]])
K = np.array([[8, -4, 0],[-4, 8, -4], [0, -4, 4]])
evalues, evectors = la.eig(K, M)