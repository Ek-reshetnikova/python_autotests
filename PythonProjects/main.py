import requests
import json

token = '65bf9bfd3a31bc0ea37fdf32b49ff114'

response = requests.post('https://pokemonbattle.me:5000/pokemons', headers = {'Content-type' : 'application/json', 'trainer_token': token}, 
json = {
    "name": "Делавер",
    "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"
})

print(response.json)
pokemon_id = response.json()['id']

response_change = requests.put('https://pokemonbattle.me:5000/pokemons', headers = {'Content-type' : 'application/json', 'trainer_token': token}, 
json = {
    "pokemon_id": pokemon_id,
    "name": "Катя",
    "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"
})


response_catch = requests.post('https://pokemonbattle.me:5000/trainers/add_pokeball', headers = {'Content-type' : 'application/json', 'trainer_token': token}, 
json = {
    "pokemon_id": pokemon_id
})

print(response_catch.text)
