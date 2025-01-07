import pytest
from src import main

def test_api_call():
    response = main.api_call('Phoenix')
    assert response.status_code == 200
    assert 'Phoenix' in response.json()['name']
    assert isinstance(response.json()['main']['temp'], (int, float))

def main():
    pass



""" TODO
API Call Tests
1. assert API_call status code
2. assert response JSON keys

S3 Bucket Tests
1. Check for S3_bucket
2. if not S3_bucket Create S3 bucket 
3. assert S3_bucket
4. if not JSON_file put JSON_file object
5. assert get JSON_file object
"""