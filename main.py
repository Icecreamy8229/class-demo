from elements import ELEMENTS
from animals import ANIMALS
import random
import yaml
import requests

with open('config.yaml', "r") as file:
    config = yaml.safe_load(file)

def get_dino_password() -> str:
    random_password = requests.get("https://dinopass.com/password/strong").text
    return random_password
def create_passphrase() -> str:
    """
    creates a passphrase when called.
    :return: the passphrase as a string
    """
    passphrase = random.choice(ELEMENTS) + " " + random.choice(ANIMALS)
    return passphrase

def main():
    password = create_passphrase()
    print("Your new password is " + password)





if __name__ == "__main__":
    main()