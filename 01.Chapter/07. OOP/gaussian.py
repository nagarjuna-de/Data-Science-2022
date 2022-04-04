import math
import matplotlib.pyplot as plt

class Gaussian():
    def __init__(self, mu=0, sigma=1):
        self.mean = mu
        self.stdev = sigma
        self.data_list = []

    # method for calculating mean.
    def calculate_mean(self, mu):
        mu = sum(self.data_list)/len(self.data_list)
        return mu

    def calculate_stdev(self, sample=True):