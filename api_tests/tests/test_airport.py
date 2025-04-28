from api_tests.api_test_data import expected_airports, airports_distance, EXPECTED_DISTANCE


def test_verify_airport_count(get_airports_data):
    assert len(get_airports_data) == 30, f"Expected 30 airports but got {len(get_airports_data)}"

def test_specific_airport(get_airports_data):
    airports = get_airports_data
    airport_names = [airport["attributes"]["name"] for airport in airports]
    for expected in expected_airports:
        assert expected in airport_names, f"Expected airport '{expected}' not found."

def test_distance_between_two_airports(post_distance_between_airports):
    response_json = post_distance_between_airports(airports_distance)
    kilometers = response_json["data"]["attributes"]["kilometers"]
    assert kilometers > EXPECTED_DISTANCE, f"Distance should be greater than 400 km, but got {kilometers} km"
