import data_handler as dh
import train as tm
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import r2_score
X_train, X_test, y_train, y_test = dh.get_data("insurance.csv")

dt,rf,gbr = tm.train_model(X_train, y_train)

def test_model(X_test, y_test):
    dt_pred = dt.predict(X_test)

    rf_pred = rf.predict(X_test)

    gbr_pred = gbr.predict(X_test)

    dt_score = r2_score(y_test, dt_pred)

    rf_score = r2_score(y_test, rf_pred)

    gbr_score = r2_score(y_test, gbr_pred)

    return dt_score, rf_score, gbr_score

dt_score, rf_score, gbr_score = test_model(X_test, y_test)

print(dt_score, rf_score, gbr_score)



