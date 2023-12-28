#Importing Moddules
import requests
from tkinter import *
from PIL import Image, ImageTk
from character import Character
from scrollable import ScrollableFrame
#Loading data from the API
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

characters = load_data()

char = characters[0]
#Creating UI
root = Tk()
root.title("Rick and Morty")
root.geometry("535x560")
root.update()
root.resizable(0,0)
scrollable = ScrollableFrame(root)
scrollable.pack(fill = BOTH, expand= True)

#Frame for each character
list_item_frame = Frame(scrollable.scrollable_frame, borderwidth=4, relief= GROOVE)
list_item_frame.pack(fill = X, padx = 7.5)

#Left frame
left_frame = Frame(list_item_frame)
left_frame.grid(row=0, column=0, padx = 7.5, pady = 15)

#Load the image

#Right frame
right_frame = Frame(list_item_frame)
right_frame.grid(row=0, column=1, sticky= "we")
Label(right_frame, text = "Name: " +char.name, font=("Helvetica", 12), padx = 7.5).pack(anchor = W, expand = True)

root.mainloop()


            