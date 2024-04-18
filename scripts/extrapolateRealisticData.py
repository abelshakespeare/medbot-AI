import pandas as pd
from datetime import timedelta, date
import random

def random_date(start, end):
    """
    This function will return a random date between two date objects.
    """
    delta = end - start
    random_days = random.randrange(delta.days)
    return start + timedelta(days=random_days)

def assign_dates(file_path, start_year, end_year, min_occurrences):
    """
    Assign each date within the given range to entries in the CSV file
    ensuring each date appears at least a specified minimum number of times.
    """
    # Load the data
    df = pd.read_csv(file_path)
    
    # Generate a date list from start_year to end_year
    start_date = date(start_year, 1, 1)
    end_date = date(end_year, 12, 31)
    date_list = [start_date + timedelta(days=x) for x in range((end_date-start_date).days + 1)]

    # Make sure we have enough dates to meet the min_occurrences requirement
    extended_date_list = date_list * min_occurrences
    random.shuffle(extended_date_list)
    extended_date_list = extended_date_list[:len(df)]
    
    # If there are still more rows than extended dates, fill the rest with random dates
    while len(extended_date_list) < len(df):
        extended_date_list.append(random_date(start_date, end_date))

    # Shuffle the list to avoid any pattern
    random.shuffle(extended_date_list)

    # Assign dates to the DataFrame
    df['Appointment Date'] = [date.strftime('%d/%m/%Y %H:%M') for date in extended_date_list]

    # Save the DataFrame back to a new CSV file
    df.to_csv('/Users/abelshakespeare/Documents/GitHub/medbot-AI/data/extrapolated/extrapolated_data.csv', index=False)

# Adjust 'min_occurrences' to ensure each date appears at least that many times
assign_dates('/Users/abelshakespeare/Documents/GitHub/medbot-AI/data/cleaned/cleaned_data.csv', 2018, 2019, min_occurrences=3)
