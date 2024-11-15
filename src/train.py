import pickle
from sklearn.linear_model import LinearRegression

def train_model(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def save_model(model, file_path):
    with open(file_path, 'wb') as f:
        pickle.dump(model, f)