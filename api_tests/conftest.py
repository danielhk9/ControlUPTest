import pytest
import requests

from api_tests.config import BASE_URL


@pytest.fixture(scope="session")
def base_url():
    return f'{BASE_URL}/api'

@pytest.fixture(scope="session")
def api_session():
    session = requests.Session()
    return session


@pytest.fixture
def get_airports_data(api_session, base_url):
    response = api_session.get(f"{base_url}/airports")
    assert response.status_code == 200, f"Expected 200 but got {response.status_code}"
    return response.json()['data']


@pytest.fixture
def post_distance_between_airports(api_session, base_url):
    def _post(data):
        response = api_session.post(f"{base_url}/airports/distance", data=data)
        assert response.status_code == 200, f"Expected 200 but got {response.status_code}"
        return response.json()
    return _post