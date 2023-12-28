#Importing Moddules
import requests
from tkinter import *
from PIL import Image, ImageTk
from character import Character

def load_data():
    url = "https://rickandmortyapi.com/api/character"
    response = requests.get(url)

    if response.status_code == 200:
        json_response = response.json()
        results = json_response['results']
        characters =[]
        for obj in results:
            name = obj['name']
            gender = obj['gender']
            species = obj['species']
            origin = obj['origin']['name']
            status = obj['status']
            image_url = obj['image']
            number_of_episodes = len(obj['episode'])
            
            character = Character(name, gender, species, origin, status, image_url, number_of_episodes)
            character.show_character()
            characters.append(character)
    return characters

load_data()
            