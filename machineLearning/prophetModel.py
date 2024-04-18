# prophet_model.py
import pandas as pd
from prophet import Prophet
import pickle


def load_data(file_path):
    """
    Load and preprocess data from a CSV file.
    Args:
        file_path (str): The path to the CSV file containing the data.
    
    Returns:
        pd.DataFrame: A DataFrame with 'ds' and 'y' columns ready for Prophet.
    """
    df = pd.read_csv(file_path)
    df['ds'] = pd.to_datetime(df['Appointment Date'], dayfirst=True)
    df['y'] = df['Attend'].groupby(df['ds']).sum().reset_index(drop=True)
    return df[['ds', 'y']]

def train_model(df):
    """
    Train the Prophet model on the prepared data.
    Args:
        df (pd.DataFrame): DataFrame with columns 'ds' (date) and 'y' (target variable).
    
    Returns:
        Prophet model: The trained Prophet model.
    """
    model = Prophet()
    print(f"Starting model training with {len(df)} records...")
    model.fit(df)
    print("Model training complete.")
    return model

def create_forecast(model, periods=365):
    """
    Use the trained model to make future predictions.
    Args:
        model (Prophet model): The trained Prophet model.
        periods (int): Number of days to forecast into the future.
    
    Returns:
        pd.DataFrame: A DataFrame containing the forecast.
    """
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)
    return forecast

def save_model(model, filename='model.pkl'):
    """
    Save the trained Prophet model to a pickle file.
    Args:
        model (Prophet model): The trained Prophet model.
        filename (str): Filename for the saved model.
    """
    with open(filename, 'wb') as file:
        pickle.dump(model, file)

def save_forecast(forecast, filename='forecast.csv'):
    """
    Save the forecast data to a CSV file.
    Args:
        forecast (pd.DataFrame): The forecasted data.
        filename (str): Filename for the saved forecast data.
    """
    forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_csv(filename, index=False)

if __name__ == '__main__':
    # Specify the path to your CSV file
    data_path = '/Users/abelshakespeare/Documents/GitHub/medbot-AI/data/extrapolated/extrapolated_data.csv'
    
    # Load and prepare data
    data = load_data(data_path)
    
    # Train the Prophet model
    model = train_model(data)
    
    # Create forecast
    forecast = create_forecast(model)
    
    # Save the model and forecast
    save_model(model)
    save_forecast(forecast)
