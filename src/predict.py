import pickle

def load_model(file_path):
    with open(file_path, 'rb') as f:
        model = pickle.load(f)
    return model

def make_prediction(model, data):
    return model.predict(data)