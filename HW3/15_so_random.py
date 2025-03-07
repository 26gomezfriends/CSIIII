import random
from functools import reduce

# Name parts
prefixes = ['Mystic', 'Golden', 'Dark', 'Shadow', 'Silver']
suffixes = ['storm', 'song', 'fire', 'blade', 'whisper']

def create_fantasy_name(list_1, list_2):
    return random.choice(list_1) + ' ' + random.choice(list_2)

def capitalize_suffix(name):
    return name.capitalize()

capitalized_suffixes = list(map(capitalize_suffix, suffixes))

# Set seed so the output is reproducible
random.seed(1)

# Generate 10 fantasy names
random_names = [create_fantasy_name(prefixes, capitalized_suffixes) for _ in range(10)]

def fire_in_name(name):
    return 'Fire' in name

def concatenate_names(name1, name2):
    return name1 + ", " + name2

# Filter names with 'Fire'
filtered_names = list(filter(fire_in_name, random_names))

# Combine the filtered names into one string
reduced_names = reduce(concatenate_names, filtered_names) if filtered_names else ""

def display_name_info():
    print("Fantasy Names:")
    for name in random_names:
        print(name)
    
    print("\nFiltered names with 'Fire':", filtered_names)
    print("Concatenated names:", reduced_names)

display_name_info()
