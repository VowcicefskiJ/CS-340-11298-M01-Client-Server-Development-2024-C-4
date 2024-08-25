# CS-340-11298-M01-Client-Server-Development-2024-C-4

Reflection
How do you write programs that are maintainable, readable, and adaptable?

When writing code, it's important to keep things simple and organized. For this project, I created a Python class called AnimalShelter that handles all the database operations in one place. This makes the code easier to understand and update. If I need to make changes or use this code in another project, I only have to adjust a few things.

This approach had some big benefits:

    Modularity: All the database operations are in one class, so it’s easy to manage.
    Reusability: The class can be used in other projects with just a few changes.
    Clarity: The code is straightforward, with clear names for each function, so it's easy to follow.

How do you approach a problem as a computer scientist?

When faced with a problem, I start by understanding what needs to be done. For this project, that meant figuring out how Grazioso Salvare needed to manage their animal data. I then built the AnimalShelter class to handle the database tasks, and I connected it to the dashboard.

This approach was different from other assignments where I might have focused on just one part of the project. Here, I needed to make sure everything worked together smoothly—from the database to the user interface.

In the future, I’ll continue to:

    Define the Requirements: Understand what the project needs.
    Design Modular Code: Keep code organized and reusable.
    Test and Iterate: Build and test each part step-by-step.

What do computer scientists do, and why does it matter?

As a computer scientist, my job is to solve problems using software. In this project, I helped Grazioso Salvare manage their animal data more efficiently. This is important because it allows them to focus on what really matters—rescuing and caring for animals.


Getting Started
Prerequisites

    MongoDB
    Python 3.x
    PyMongo Library

Installation

To install the necessary Python packages, run: pip install pymongo dash jupyter-dash dash-leaflet

Usage

The AnimalShelter class is your gateway to interacting with the MongoDB database:
from animal_shelter import AnimalShelter

# Set up the connection to the database
shelter = AnimalShelter('username', 'password', 'nv-desktop-services.apporto.com', 32558, 'AAC', 'animals')

# Example: Add a new animal record
result = shelter.create({
    'age_upon_outcome': '2 years',
    'animal_id': 'A123456',
    'animal_type': 'Dog',
    'breed': 'Labrador Retriever',
    'color': 'Yellow',
    'outcome_type': 'Adoption'
})

# Example: Retrieve records of all Labrador Retrievers
results = shelter.read({'breed': 'Labrador Retriever'})
print(results)

