import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor,GradientBoostingRegressor
import pickle
import time
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA

def lr_non_supervised():
    pickle.dump(model, open"../Models/Trained_models.pkl/LRnoSupervisado.pkl", "wb")

def lr():
    pickle.dump(model, open('../Models/Trained_models.pkl/modeloRL.pkl', 'wb'))


train = pd.read_csv("../Data/train/train.csv", parse_dates = ['DateTime'])
train1 = pd.read_csv("../Data/train/train1.csv", parse_dates = ['DateTime'])
test = pd.read_csv("../Data/test/test.csv", parse_dates = ['DateTime'])
test1 = pd.read_csv("../Data/test/test1.csv", parse_dates = ['DateTime'])


X = train.values.reshape(-1, 1)
y = test


