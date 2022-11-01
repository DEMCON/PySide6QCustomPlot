""" Python wrapper for QCustomPlot
"""

__version__ = '0.0.1'

# Trick to load Qt DLL's before PySide6QCustomPlot.
import PySide6.QtWidgets
import PySide6.QtCore
import PySide6.QtPrintSupport

# Now load PySide6QCustomPlot
from .PySide6QCustomPlot import *
