from src.data_loader import load_data
from src.features import add_features
from src.train import train_model, evaluate_model, save_model
from src.predict import load_model, make_prediction
from src.visualize import plot_predictions_for_year
from sklearn.model_selection import train_test_split
from datetime import datetime

def run_pipeline(ticker, specific_year):
    try:
        start_date = '1900-01-01'
        end_date = datetime.today().strftime('%Y-%m-%d')
        model_path = 'models/stock_model.pkl'

        data = load_data(ticker, start_date, end_date)
        data = add_features(data)

        X = data[['Close', 'MA10', 'MA50']]
        y = data['Close_Next_Day']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = train_model(X_train, y_train)
        save_model(model, model_path)

        mae, mse = evaluate_model(model, X_test, y_test)
        print(f"Mean Absolute Error: {mae}")
        print(f"Mean Squared Error: {mse}")

        loaded_model = load_model(model_path)
        y_pred = make_prediction(loaded_model, X_test)

        dates = data.index[-len(y_test):].strftime('%Y-%m-%d')  # Format dates as strings

        plot_predictions_for_year(y_test, y_pred, dates, ticker, specific_year)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Welcome to the Stock Prediction Visualization Program!")
    
    ticker = input("Enter the stock ticker (e.g., AAPL, MSFT): ").upper()

    while True:
        specific_year = input("Enter the year to visualize (e.g., 2023): ")
        if specific_year.isdigit():
            specific_year = int(specific_year)
            break
        else:
            print("Invalid input. Please enter a numeric year.")

    run_pipeline(ticker, specific_year)
    