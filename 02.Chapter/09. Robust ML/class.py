from sklearn.svm import SVC
from sklearn.datasets import load_iris
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split


iris = load_iris()
X,y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)

# creating a pipeline
pipe = Pipeline([('scaling', StandardScaler())])
pipe2 = Pipeline([('scaling', StandardScaler()), ('imp', SimpleImputer())])
col_trans = ColumnTransformer([('01', pipe, [0,1]), ('23', pipe2, [2,3])])
pipe3 = Pipeline([('ct', col_trans), ('clf', SVC())])


pipe3.fit(X_train, y_train)
res = pipe3.score(X_test, y_test)
print(res)
