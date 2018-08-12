import pandas as pd
import random
from PSO import PSO
from utils import Configuration

#Some functions
def Sphere(x):
    total=0
    for i in range(len(x)):
        total+=x[i]**2
    return total

def Rosenbrock(x):
    total=0
    for i in range(len(x)):
        total += ((100 * (x[i] - x[i]**2)**2) + (x[i] - 1)**2)
    return total

def read_file_test():
    df = pd.read_csv('datasets/tests.csv')
    print(df.head())


PSO(Sphere)