import pytest
import requests
import json

from Data.conftest import base_url, end_point_pet, validate_url



pet_id = 0

@pytest.fixture
def test_valid_url(base_url):
    validate_url(base_url)


# @pytest.fixture
def test_post(base_url,test_valid_url):
    global pet_id
    with open ('..\\Data\\Post_pet.json', 'r') as file:
        data = json.load(file)

    response = requests.post(f'{base_url}{end_point_pet}', json=data)
    print(response.json())
    pet_id = response.json().get("id")
    print(response.status_code)

    return pet_id

    # print("Status :" , response.json().get("status"))

#
# def test_get_details(base_url):
#     global pet_id
#
#     response = requests.get(f"{base_url}{end_point_pet}/{pet_id}")
#
#     print(response.json())
#     print("Status Code: ", response.json().get("status"))

# @pytest.fixture
def test_put(base_url):
    global pet_id
    with open ('..\\Data\\Put_pet.json', 'r') as file:
        data = json.load(file)
    resp = requests.put(f'{base_url}{end_point_pet}', json=data)
    print(resp.status_code)
    pet_id = resp.json().get("id")
    print(resp.json())
    return pet_id
#
# def compare_data():
#     with open('..\\Data\\Post_pet.json', 'r') as file:
#         data = json.load(file)
#     with open('..\\Data\\Put_pet.json', 'r') as file:
#         put_data = json.load(file)
#     for key in data:
#         if data[key] != put_data[key]:
#             print(f"{key} is not equal to {data[key]}")

def test_get_details(base_url):
    global pet_id
    response = requests.get(f"{base_url}{end_point_pet}/{pet_id}")

    print(response.json())
    print("Status Code: ", response.json().get("status"))

def test_delete(base_url):
    global pet_id
    resp = requests.delete(f"{base_url}{end_point_pet}/{pet_id}")
    # assert resp.status_code == 200, "Pet deletion failed"
