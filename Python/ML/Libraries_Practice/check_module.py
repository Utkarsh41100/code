try:
    import pandas as pd
    print("Pandas is installed.")
except ImportError:
    print("Pandas is not installed.")

try:
    import numpy as np
    print("NumPy is installed.")
except ImportError:
    print("NumPy is not installed.")

try:
    import matplotlib.pyplot as plt
    print("Matplotlib is installed.")
except ImportError:
    print("Matplotlib is not installed.")

try:
    from sklearn.linear_model import LinearRegression
    print("scikit-learn is installed.")
except ImportError:
    print("scikit-learn is not installed.")
