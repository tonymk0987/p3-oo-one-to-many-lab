class Pet:
    all = []  # Define a class variable all that stores all instances of the Pet class.
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]  # class variable 
    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception("Invalid pet type")
        self.name = name
        self.pet_type = pet_type
        self._owner = owner
        if owner:
            owner.add_pet(self)  # Add the pet to the owner's list of pets
        Pet.all.append(self)

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        if not isinstance(value, Owner):
            raise TypeError("Owner must be an instance of Owner class")
        self._owner = value

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):  # method called pets(self) that returns a full list of the owner's pets.
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("Pet must be an instance of Pet class")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda x: x.name)
