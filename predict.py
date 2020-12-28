
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
    df.loc[0] = [int(age),	int(sex), int(cp), int(trestbps), int(chol), int(fbs), int(restecg), int(thalach), int(exang), float(oldpeak),	int(slope), int(ca), int(thal), 1]
    print(df.head())

    nominal_features = ['cp', 'slope', 'thal', 'restecg']
    x = pd.get_dummies(df.drop(['target'], axis=1), columns=nominal_features, drop_first=True).values
    y = df.target.values
    print('from predict.py')

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, shuffle=False)
    print(x_train[0])

    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    x_train = sc.fit_transform(x_train)
    print('after standard scaled\n', x_train)


    #Dimensionality Reduction
    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
    lda = LDA()
    x_train = lda.fit_transform(x_train, y_train)
    print('after standard scaled\n', x_train[0])

    predicted_probability = svm_model.predict_proba(x_train)
    print('predicted probability\n', predicted_probability[0])
    return (predicted_probability[0][1] * 100)






