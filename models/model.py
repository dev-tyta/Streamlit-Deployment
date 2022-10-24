# importing python libraries
import pandas as pd
import pickle as pkl
from lightgbm.sklearn import LGBMClassifier
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.preprocessing import RobustScaler, OrdinalEncoder

import warnings
warnings.filterwarnings("ignore")

# loading diabetes data into variable data
data = pd.read_csv("./dataset/diabetes.csv")

# wrangling and feature extraction.
data.chol_hdl_ratio = round(data.cholesterol / data.hdl_chol, 2)
data.waist_hip_ratio = round(data.waist / data.hip, 2)

# renaming wrongly named columns
data.rename(columns={"weight": "height", "height": "weight"}, inplace=True)
data.height_weight = round(data.height / data.weight)
