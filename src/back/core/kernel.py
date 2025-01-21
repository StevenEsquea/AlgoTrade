from time import time
from abc import ABC, abstractmethod

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

import yfinance as yf

# Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
# Valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo

class Strategy(ABC):

    @abstractmethod
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_operations(self):
        pass

    @abstractmethod
    def ganancia(self):
        pass

    @abstractmethod
    def visualizar(self):
        pass

    def run(self):
        print(self.ganancia())
        self.visualizar()


class Operation:
    def __init__(self, entry_point, exit_point, is_closed = True):
        self.entry_point = entry_point
        self.exit_point = exit_point
        self.is_closed = is_closed