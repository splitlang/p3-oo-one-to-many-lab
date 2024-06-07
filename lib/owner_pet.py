class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        if pet_type not in Pet.PET_TYPES:
            raise Exception("Invalid pet type.")
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

    def __repr__(self):
        return f"{self.name} ({self.pet_type})"

class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Input must be a Pet instance.")
        pet.owner = self
        self.pets.append(pet)

    def get_sorted_pets(self):
        self.pets.sort(key=lambda pet: pet.name)
        return self.pets