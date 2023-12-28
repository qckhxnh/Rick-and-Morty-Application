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
            characters.append(character)
    return characters

characters = load_data()

char = characters[0]
#Creating UI
root = Tk()
root.title("Rick and Morty")
root.geometry("500x560")
root.update()
scrollable = ScrollableFrame(root)
scrollable.pack(fill = BOTH, expand= True)

for char in characters:
    #Frame for each character
    list_item_frame = Frame(scrollable.scrollable_frame, borderwidth=6, relief= GROOVE)
    list_item_frame.pack(fill = X, padx = 7.5)

    #Left frame
    left_frame = Frame(master=list_item_frame)
    image = ImageTk.PhotoImage(char.get_image())
    image_lbl = Label(left_frame, image=image)
    image_lbl.image = image
    image_lbl.pack(fill=BOTH, expand=True)
    left_frame.grid(row=0, column=0, padx=7.5, pady=15) 

    #Right frame
    right_frame = Frame(list_item_frame)
    right_frame.grid(row=0, column=1, sticky= "we")
    Label(right_frame, text = "Name: " +char.name, font=("Helvetica", 12), padx = 7.5).pack(anchor = W, expand = True)
    Label(right_frame, text = "Gender: " +char.gender, font=("Helvetica", 12), padx = 7.5).pack(anchor = W, expand = True)
    Label(right_frame, text = "Species: " +char.species, font=("Helvetica", 12), padx = 7.5).pack(anchor = W, expand = True)
    Label(right_frame, text = "Origin: " +char.origin, font=("Helvetica", 12), padx = 7.5).pack(anchor = W, expand = True)
    Label(right_frame, text = "Status: " +char.status, font=("Helvetica", 12), padx = 7.5).pack(anchor = W, expand = True)
    Label(right_frame, text = "Number of episodes: " +str(char.number_of_episodes), font=("Helvetica", 12), padx = 7.5).pack(anchor = W, expand = True)

#Main loop
root.mainloop()


            