import string
import random

characters = string.ascii_letters + "_"

def generate(n=5):
    """
    Here n, represents the length of 
    randomly generated string. By def. you're gonna
    get a randomly generate 5character long id.
    """
    url = ""
    for i in range(n):
        url += characters[random.randint(0, len(characters) - 1)]
    return url

# print(generate(10), len(characters))