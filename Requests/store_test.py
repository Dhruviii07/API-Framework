import json

import pytest
import requests
from Data.conftest import base_url,end_point_store,validate_url

pet_id = 0

@pytest.fixture
def test_valid_url(base_url):
    validate_url(base_url)


# @pytest.fixture
def test_post(base_url,test_valid_url):
    global pet_id
    with open('..\\Data\\Post_store.json', 'r') as file:
        data = json.load(file)

    response = requests.post(f'{base_url}{end_point_store}', json=data)
    pet_id = response.json().get("id")
    print(response.status_code)
    print(response.json())
    return pet_id


    # print("Quantity :", resp.json().get("quantity"))



def test_get(base_url):
    global pet_id
    resp=requests.get(f"{base_url}{end_point_store}/{pet_id}")
    print(resp.status_code)

    print(resp.json())



def test_delete(base_url):
    global pet_id
    resp = requests.delete(f"{base_url}{end_point_store}/{pet_id}")
    print(resp.json())
    print(resp.status_code)
    assert resp.status_code == 200, "Pet deleted successfully"



