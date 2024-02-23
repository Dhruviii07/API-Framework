import pytest
import requests
import sys

end_point_pet = '/v2/pet'
end_point_user = '/v2/user'
end_point_store = '/v2/store/order'


@pytest.fixture
def base_url():
    return 'https://petstore.swagger.io'



def validate_url(base_url):
    try:
        response = requests.head(base_url)
        response.raise_for_status()
        print(f"URL '{base_url}' is valid")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error validating URL '{base_url}':{e}")
        return False

# sys.exit()
def test_valid_url(base_url):
    validate_url(base_url)









