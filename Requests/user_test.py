import requests, json,pytest

from Data.conftest import base_url, end_point_user,validate_url

@pytest.fixture
def test_valid_url(base_url):
    validate_url(base_url)



# @pytest.fixture
def test_post(base_url,test_valid_url):
    global user_name
    with open('..\\Data\\Post_user.json', 'r') as file:
        data = json.load(file)

    response=requests.post(f'{base_url}{end_point_user}', json=data)
    user_name = response.json().get("name")
    print(response.json())
    print(response.status_code)
    return user_name


# @pytest.fixture
def test_user_get(base_url):
    global user_name
    resp = requests.get(f"{base_url}{end_point_user}/{user_name}")
    print(resp.json())


# @pytest.fixture
def test_put_user(base_url):
    # global user_name
    with open ('..\\Data\\Put_user', 'r') as file:
        data = json.load(file)

    resp = requests.put(f'{base_url}{end_point_user}/{user_name}', json=data)

    print(resp.json())


# @pytest.fixture
def test_delete(base_url):
    global user_name

    resp=requests.delete(f"{base_url}{end_point_user}/{user_name}")


