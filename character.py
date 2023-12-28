class Character:
    def __init__(self, name, gender, species, origin, status, image, number_of_episodes):
        self.name = name
        self.gender = gender
        self.species = species
        self.origin = origin
        self.status = status
        self.image_url = image
        self.number_of_episodes = number_of_episodes
    
    def show_character(self):
        print(self.name, self.gender)