import pytest
from src.main import main, api_call

def test_api_call():
    response = api_call('Phoenix')
    assert response.status_code == 200
    assert 'Phoenix' in response.json()['name']
    assert isinstance(response.json()['main']['temp'], (int, float))

def test_main():
    main()