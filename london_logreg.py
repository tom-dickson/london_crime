import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler


df = pd.read_csv('full_data.csv').dropna(axis=0, subset=['Last outcome category'])
print(df['Last outcome category'].unique())
print(df.columns)

df2 = df[['Crime type','Longitude', 'Latitude', 'Last outcome category']].reset_index()
df2.drop(['index'], axis=1, inplace=True)

remove = ['Status update unavailable', 'Action to be taken by another organisation','Formal action is not in the public interest']

no_resolution = ['Investigation complete; no suspect identified', 'Under investigation', 'Unable to prosecute suspect']

df2 = df2[~ df2['Last outcome category'].isin(remove)]

df2['Resolution reached'] = ~ (df2['Last outcome category'].isin(no_resolution))
df2.dropna(axis=0, inplace=True)
df2.reset_index(inplace=True)
df2.drop(['index', 'Last outcome category'], axis=1, inplace=True)
df2['Resolution reached'] = df2['Resolution reached'].astype(int)

for val in df2['Crime type'].unique():
    df2[val] = df2['Crime type'] == val
    df2[val] = df2[val].astype(int)

df2.drop(['Crime type'], axis=1, inplace=True)

inputs = df2.drop(['Resolution reached'], axis=1).to_numpy()
output = df2['Resolution reached'].to_numpy()


X_train, X_test, y_train, y_test = train_test_split(inputs, output, test_size=.3, random_state=42)

min_max_scaler = MinMaxScaler()
X_train_scaled = min_max_scaler.fit_transform(X_train)
X_test_scaled = min_max_scaler.fit_transform(X_test)

model = LogisticRegression()
model.fit(X_train_scaled, y_train)

print(model.predict(X_test_scaled), model.predict_proba(X_test_scaled))
print(model.score(X_test_scaled, y_test))
print(confusion_matrix(y_test, model.predict(X_test_scaled)))
