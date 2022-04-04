import pandas as pd
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer


    
def get_data(pth):

    df = pd.read_csv(pth)
    df['sex']= df['sex'].apply({'male':0, 'female':1}.get)
    df['smoker'] =  df['smoker'].apply({'yes':1, 'no':0}.get)
    df['region'] = df['region'].apply({'southwest':1, 'southeast':2, 'northwest':3, 'northeast':4}.get)

    X_train, X_test, y_train, y_test = train_test_split(df.values[:,:-1], df.values[:,-1], test_size=0.2, random_state = 42)

    # ct = ColumnTransformer( [('ordinal', OrdinalEncoder(handle_unknown= 'use_encoded_value', unknown_value = -1), [1,4,5] )] )

    # x_train = ct.fit_transform(x_train)
    # x_test = ct.transform(x_test)

    return X_train, X_test, y_train, y_test


