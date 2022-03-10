import data_handler as dh
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor

X_train, X_test, y_train, y_test = dh.get_data("insurance.csv")

def train_model(X_train, y_train):
    dt = DecisionTreeRegressor(random_state=42, max_depth=3)
    dt = dt.fit(X_train, y_train)

    rf = RandomForestRegressor(n_estimators =5, max_depth=4,random_state = 42)
    rf = rf.fit(X_train, y_train)    

    gbr =  GradientBoostingRegressor(random_state=42)  
    gbr = gbr.fit(X_train, y_train)

    return dt,rf,gbr