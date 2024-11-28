import pandas as pd
from sklearn.preprocessing import OneHotEncoder


def bin_to_num(data):
    binnedinc = []
    for i in data["binnedInc"]:
        # remove the paranthesis and brackets
        i = i.strip("()[]")
        # Split the string by comma into the list
        i = i.split(",")
        # Convert the list to a tuple
        i = tuple(i)
        # Convert individual elements to float
        i = tuple(map(float, i))
        # Convert the tuple to a list
        i = list(i)
        # Append the list to a binnedinc list
        binnedinc.append(i)
    data["binnedInc"] = binnedinc
    #make new column lower and upper bounnd
    data["Lower_bound"] = [i[0] for i in data["binnedInc"]]
    data["Upper_bound"] = [i[1] for i in data["binnedInc"]]
    #and also median point
    data["Median"] = (data["Lower_bound"] + data["Upper_bound"])/2
    #drop the binnedinc column
    data.drop("binnedInc", axis= 1, inplace = True)
    return data

def cat_to_column(data):
    #make new column by splitting geographical column
    data['County'] = [i.split(',')[0] for i in data['Geography']]
    data['State'] = [i.split(',')[1] for i in data['Geography']]
    #drop the geographical column
    data.drop("Geography", axis = 1, inplace = True)
    return data

def one_hot_encoding(X):
    #Select categorical column
    categorical_columns = X.select_dtypes(include = ["object"]).columns
    #One Hot Encode categorical columns
    one_hot_encoder = OneHotEncoder(sparse_output=False, handle_unknown="ignore")
    one_hot_encoded = one_hot_encoder.fit_transform(X[categorical_columns])
    #Convert the one hot encoded array into dataframe
    one_hot_encoded = pd.DataFrame(
        one_hot_encoded, columns=one_hot_encoder.get_feature_names_out(categorical_columns)
    )
    #drop the categorical columns from the original dataframe
    X= X.drop(categorical_columns, axis = 1)
    #Contatenting one hot encoded dataframe to orignal dataframe
    X = pd.concat([X, one_hot_encoded], axis=1)
    return X