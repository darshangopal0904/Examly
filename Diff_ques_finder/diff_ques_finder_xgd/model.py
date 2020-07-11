# import pandas
import pandas as pd

# read the dataset
df = pd.read_csv('C:/Users/DARSHAN.G/Downloads/dataset_examly_2.csv', error_bad_lines=False)

df.head()

#print(df.shape)

num_of_classes = len(df.Difficulty.unique())
#print(num_of_classes)

df.describe()

# split train input and output data
X = df.drop(axis=0, columns=['Difficulty'])
Y = df.Difficulty

#Print the shape of X and Y
#print(X.shape)
#print(Y.shape)

from sklearn.model_selection import train_test_split

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

from xgboost import XGBClassifier

# Create a classifier
xgb = XGBClassifier(booster='gbtree', objective='multi:softprob', random_state=42, eval_metric="auc", num_class=num_of_classes)

# Fit the classifier with the training data
xgb.fit(X_train,y_train)


# Save your model
from sklearn.externals import joblib
joblib.dump(xgb, 'model.pkl')
print("Model dumped!")

# Load the model that you just saved
model = joblib.load('model.pkl')

# Saving the data columns from training
model_columns = list(X.columns)
joblib.dump(model_columns, 'model_columns.pkl')
print("Models columns dumped!")