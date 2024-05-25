import argparse
import pandas as pd
from prophet import Prophet


def main(city, state, predict_time_length_in_day, zillow_csv_data_file):
    city_name = city.lower().title()
    # Load the dataset into a Pandas DataFrame
    print("To make sure the data is up to date, check the following link and look for 'HOME VALUES' section: https://www.zillow.com/research/data/")
    df = pd.read_csv(zillow_csv_data_file)

    # Create a new DataFrame with column 3 and columns from 6 until the end
    df = df.iloc[:, [2] + list(range(5, len(df.columns)))]

    # Transpose the original DataFrame to swap rows and columns
    df_transposed = df.transpose()

    # Set the first row as column headers
    new_header = df_transposed.iloc[0]
    df_transposed = df_transposed[1:]
    df_transposed.columns = new_header

    # Reset index to make the current index (which represents the months) a regular column
    df_transposed.reset_index(inplace=True)

    # Rename the columns to match the new structure
    df_transposed.columns = ['Date', "United States, US"] + list(df_transposed.columns[2:])

    # Convert 'Date' column to datetime
    df_transposed['Date'] = pd.to_datetime(df_transposed['Date'])

    # Save the modified DataFrame back to a CSV file
    df_transposed.to_csv('modified_house_prices.csv', index=False)
    # Select only 'Date' and the specified city columns
    try:
        df = df_transposed[['Date', city_name + ', ' + state]]
    except KeyError:
        print("Error in city name or state name abbreviation")
        print("Otherwise, there is no record of the housing price for that city")
        return

    # Rename columns to match Prophet's requirements
    df.columns = ['ds', 'y']

    # Initialize Prophet model
    m = Prophet()

    # Fit the model
    m.fit(df)

    # Create future dataframe for forecasting
    future = m.make_future_dataframe(periods=predict_time_length_in_day)

    # Make predictions
    forecast = m.predict(future)

    # Plot the forecast
    fig1 = m.plot(forecast)
    fig2 = m.plot_components(forecast)
    fig1.show()
    fig2.show()
    input("Press Enter to continue...")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process city and state.')
    parser.add_argument('city', type=str, help='City name')
    parser.add_argument('state', type=str, help='State abbreviation')
    parser.add_argument('predict_time_length_in_day', type=int, help='Time length in days')
    parser.add_argument('zillow_csv_data_file', type=str, help='Zillow home value csv data file')
    args = parser.parse_args()

    main(args.city, args.state.upper(), args.predict_time_length_in_day, args.zillow_csv_data_file)
