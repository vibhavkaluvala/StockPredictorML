from src.data_loader import load_data
from src.features import add_features
from src.train import train_model, save_model
from src.predict import load_model, make_prediction
from src.visualize import plot_predictions

# Load and preprocess data
data = load_data('AAPL', '2015-01-01', '2023-01-01')
data = add_features(data)

# Split data
X = data[['Close', 'MA10', 'MA50']]
y = data['Close_Next_Day']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train and save model
model = train_model(X_train, y_train)
save_model(model, 'models/stock_model.pkl')

# Load model and predict
model = load_model('models/stock_model.pkl')
y_pred = make_prediction(model, X_test)

# Visualize results
plot_predictions(y_test, y_pred)