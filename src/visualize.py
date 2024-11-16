import matplotlib.pyplot as plt
import pandas as pd

def plot_predictions_for_year(y_test, y_pred, dates, stock_ticker, year):
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