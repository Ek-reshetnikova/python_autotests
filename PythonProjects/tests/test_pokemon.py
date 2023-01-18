import requests
import pytest

def test_status_code():
    response = requests.get('https://pokemonbattle.me:5000/pokemons')
    assert response.status_code == 200

@pytest.mark.parametrize('key, value', [('trainer_name', 'Del'), ('city', 'Moscow')])

def test_fragment_of_response(key, value):
    response = requests.get('https://pokemonbattle.me:5000/trainers', params = {'trainer_id' : '1810' })
    assert response.json()[key] == value

