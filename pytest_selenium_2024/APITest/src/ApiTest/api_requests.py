import requests
import random


# Cat API

base_url = 'https://catfact.ninja/breeds'


def get_all_cat_breeds():

    response = requests.request('GET', base_url)
    response_data = response.json()
    return response_data

def get_random_cat():
    
    all_cats = get_all_cat_breeds().get('data')
    return random.choice(all_cats)
    
# print(f"Random Cat: {get_random_cat()}")


