import matplotlib.pyplot as plt
import pandas as pd

def plot_predictions(y_test, y_pred, dates, stock_ticker):
    """Plots the predicted vs. actual stock prices."""
    # plt.figure(figsize=(10, 6))
    # plt.plot(y_test.values[:100], label="Actual Prices")
    # plt.plot(y_pred[:100], label="Predicted Prices")
    # plt.title("Predicted vs Actual Prices")
    # plt.xlabel("Days")
    # plt.ylabel("Price")
    # plt.legend()
    # plt.show()

    plt.figure(figsize=(12, 6))
    
    # Plot actual and predicted prices
    plt.plot(dates[:100], y_test.values[:100], label="Actual Prices", marker='o')
    plt.plot(dates[:100], y_pred[:100], label="Predicted Prices", marker='x')

    # Add title and labels
    plt.title(f"{stock_ticker} Stock: Predicted vs Actual Prices")
    plt.xlabel("Date")
    plt.ylabel("Price")
    
    # Add legend
    plt.legend()

    # Rotate date labels for better readability
    monthly_ticks = pd.to_datetime(dates).to_series().dt.to_period("M").drop_duplicates().index
    plt.xticks(ticks=[i for i, date in enumerate(dates) if pd.to_datetime(date) in monthly_ticks], 
               labels=[date.strftime('%Y-%m') for date in monthly_ticks], 
               rotation=45)

    # Adjust layout to prevent overlapping elements
    plt.tight_layout()
    
    # Show the plot
    plt.show()

def plot_predictions_for_year(y_test, y_pred, dates, stock_ticker, year):
    """
    Plots the predicted vs. actual stock prices for a specific year with monthly increments.

    Parameters:
    - y_test: Actual prices
    - y_pred: Predicted prices
    - dates: Dates corresponding to y_test values
    - stock_ticker: The stock ticker symbol to display in the title
    - year: The specific year to filter and display
    """
    # Convert dates to pandas DateTime for filtering and formatting
    dates = pd.to_datetime(dates)

    # Filter data for the specific year
    mask = dates.year == year
    filtered_dates = dates[mask]
    filtered_y_test = y_test[mask]
    filtered_y_pred = y_pred[mask]

    # Ensure monthly ticks
    monthly_ticks = filtered_dates.to_series().dt.to_period("M").drop_duplicates().index

    # Plot data
    plt.figure(figsize=(12, 6))
    plt.plot(filtered_dates, filtered_y_test, label="Actual Prices", marker='o')
    plt.plot(filtered_dates, filtered_y_pred, label="Predicted Prices", marker='x')

    # Add title and labels
    plt.title(f"{stock_ticker} Stock: Predicted vs Actual Prices for {year}")
    plt.xlabel("Date")
    plt.ylabel("Price")
    
    # Set x-axis ticks for each month
    plt.xticks(ticks=[date for date in filtered_dates if date in monthly_ticks], 
               labels=[date.strftime('%Y-%m') for date in monthly_ticks], 
               rotation=45)

    # Add legend and adjust layout
    plt.legend()
    plt.tight_layout()
    plt.show()