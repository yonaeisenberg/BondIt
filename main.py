import pandas as pd


# parse time to get number of minutes
def parse_time(time):
    hours, minutes = time.split(':')
    return int(hours) * 60 + int(minutes)


# main function to add values to the success column
def populate_success():
    # Read the CSV file
    flights_df = pd.read_csv('flights.csv')

    # Sort values by Arrival time
    flights_df.columns = flights_df.columns.str.strip()
    flights_df = flights_df.sort_values(by='Arrival', axis='index')

    # Use a counter to make sure not to have more than 20 flights success per day
    counter = 0

    # Iterate through the dataframe to check the value
    for index, row in flights_df.iterrows():
        if parse_time(row['Departure']) - parse_time(row['Arrival']) >= 180 and counter < 20:
            row['success'] = 'success'
            counter += 1
        else:
            row['success'] = 'fail'

    flights_df.to_csv('flights_with_success.csv', index=False)


if __name__ == '__main__':
    populate_success()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
