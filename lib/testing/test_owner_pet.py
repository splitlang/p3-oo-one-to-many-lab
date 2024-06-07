import pytest
from owner_pet import Pet, Owner

def test_owner_init():
    """Test Owner class initialization"""
    owner = Owner("John")
    assert owner.name == "John"

def test_pet_init():
    """Test Pet class initialization"""
    pet = Pet("Fido", "dog")
    assert pet.name == "Fido"
    assert pet.pet_type == "dog"

    owner = Owner("Jim")
    pet = Pet("Clifford", "dog", owner)
    assert pet.owner == owner

    Pet.all = []

def test_has_pet_types():
    """Test Pet class has variable PET_TYPES"""
    assert Pet.PET_TYPES == ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']

    Pet.all = []

def test_checks_pet_type():
    """Test Pet class validates pet_type"""
    with pytest.raises(Exception):
        Pet("Jim Jr.", "panda")

    Pet.all = []

def test_pet_has_all():
    """Test Pet class has variable all, storing all instances of Pet"""
    pet1 = Pet("Whiskers", "cat")
    pet2 = Pet("Jerry", "reptile")

    assert pet1 in Pet.all
    assert pet2 in Pet.all
    assert len(Pet.all) == 2

    Pet.all = []

def test_owner_has_pets():
    """Test Owner class has method pets(), returning all related pets"""
    owner = Owner("Ben")
    pet1 = Pet("Fido", "dog", owner)
    pet2 = Pet("Clifford", "dog", owner)
    owner.add_pet(pet1)
    owner.add_pet(pet2)

    assert [repr(pet) for pet in owner.pets] == [repr(pet1), repr(pet2)]

def test_owner_adds_pets():
    """Test Owner class has method add_pet(), validating and adding a pet"""
    owner = Owner("Ben")
    pet = Pet("Whiskers", "cat")
    owner.add_pet(pet)

    assert pet.owner == owner
    assert [repr(pet) for pet in owner.pets] == [repr(pet)]

def test_add_pet_checks_isinstance():
    """Test Owner class instance method add_pet() validates Pet type"""
    owner = Owner("Jim")
    with pytest.raises(Exception):
        owner.add_pet("Lucky")

    Pet.all = []

def test_get_sorted_pets():
    """Test Owner class has method get_sorted_pets, sorting related pets by name"""
    owner = Owner("John")
    pet1 = Pet("Fido", "dog", owner)
    pet2 = Pet("Clifford", "dog", owner)
    pet3 = Pet("Whiskers", "cat", owner)
    pet4 = Pet("Jerry", "reptile", owner)
    owner.add_pet(pet1)
    owner.add_pet(pet2)
    owner.add_pet(pet3)
    owner.add_pet(pet4)

    expected_sorted_pets = [repr(pet2), repr(pet1), repr(pet4), repr(pet3)]
    assert [repr(pet) for pet in owner.get_sorted_pets()] == expected_sorted_pets