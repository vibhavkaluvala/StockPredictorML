def add_features(data):
    data['MA10'] = data['Close'].rolling(window=10).mean()
    data['MA50'] = data['Close'].rolling(window=50).mean()
    data['Close_Next_Day'] = data['Close'].shift(-1)
    return data.dropna()