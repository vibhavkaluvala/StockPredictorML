import matplotlib.pyplot as plt

def plot_predictions(y_test, y_pred):
    plt.plot(y_test.values, label="Actual Prices")
    plt.plot(y_pred, label="Predicted Prices")
    plt.title("Predicted vs Actual Prices")
    plt.xlabel("Days")
    plt.ylabel("Price")
    plt.legend()
    plt.show()