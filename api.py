from flask import Flask, request, jsonify
import pandas as pd

# create Flask app
app = Flask(__name__)


# define GET endpoint to return all flights
@app.route('/flights', methods=['GET'])
def get_flights():
    # read in the CSV file
    flights_df = pd.read_csv('flights_with_success.csv')

    return jsonify(flights_df.to_dict(orient='records'))


# define GET endpoint to return a specific flight by ID
@app.route('/flights/<flight_id>', methods=['GET'])
def get_flight(flight_id):
    # read in the CSV file
    flights_df = pd.read_csv('flights_with_success.csv')

    flight = flights_df.loc[flights_df['flight ID'] == flight_id]
    if flight.empty:
        return jsonify({'error': 'Flight not found'})
    return jsonify(flight.to_dict(orient='records'))


# define POST endpoint to write flights to CSV
@app.route('/flights', methods=['POST'])
def post_flights():
    # get array of flights from request body
    flights = request.json

    # create dataframe from flights
    new_flights_df = pd.DataFrame(flights, columns=['flight ID', 'Arrival', 'Departure', 'success'])

    # append new flights to CSV file
    new_flights_df.to_csv('flights_with_success.csv', index=False)

    return jsonify({'success': True})


# run app
if __name__ == '__main__':
    app.run()
