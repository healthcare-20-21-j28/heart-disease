
import pandas as pd
import numpy as np
import random as rnd
import warnings

from operator import add

MEDIUM_SIZE = 10
SMALL_SIZE = 8
MEDIUM_SIZE = 10
BIGGER_SIZE = 12

# %matplotlib inline
warnings.filterwarnings('ignore')

#import Dataset
df = pd.read_csv('data/heart.csv')
df.head()

#import model
import pickle
filename = 'models/finalized_model.sav'
svm_model = pickle.load(open(filename, 'rb'))


def predict_prob(age,	sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak,	slope, ca, thal):
    df.loc[0] = [age,	sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak,	slope, ca,thal, 1]
    df.head()
    nominal_features = ['cp', 'slope', 'thal', 'restecg']
    x = pd.get_dummies(df.drop(['target'], axis=1), columns=nominal_features, drop_first=True).values
    y = df.target.values

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, shuffle=False)

    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    x_train = sc.fit_transform(x_train)

    #Dimensionality Reduction
    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
    lda = LDA()
    x_train = lda.fit_transform(x_train, y_train)
    predicted_probability = svm_model.predict_proba(x_train)
    print(predicted_probability[0])
    return (predicted_probability[0][1] * 100)

a = predict_prob(56, 1, 1, 120, 236, 0, 1, 178, 0, 0.8, 2, 0, 2)






