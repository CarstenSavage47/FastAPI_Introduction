# In Terminal write: touch main.py

from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import hypercorn

app = FastAPI()

db = [] # In-memory database

# Define the structure for a city in the app
class City(BaseModel): # Inherits a basemodel
    name: str # Datatype of 'name' field
    timezone: str # Datatype of 'timezone' field

@app.get("/")
def index():
    return {'key':'value'}

# Run the server in Terminal with: uvicorn main:app --reload

''' http://127.0.0.1:8000 ''' ''' URL for the FastAPI server '''
''' For documentation, we can add /docs to the URL. '''
''' There is also /redoc '''

@app.get('/cities') # This is a Get request
def get_cities(): # Create function
        return db # Return database

@app.get('/cities/{city_id}')
def get_city(city_id: int):
    return db[city_id-1]

@app.post('/cities') # Allows us to create a city
def create_city(city:City): # By doing this, FastAPI expects something that resembles a city to be in the body of the request. We can create a city in the body of the request, send it, and then FastAPI will put it in the variable city.
                           db.append(city.dict())  # Appends the city to our in-memory database.
                           return db[-1] # We want to see the thing that we just inserted into the database.

# City_id represents the location in a list of the city. ID 1 will be the element at the 0 index, etc.
@app.delete('/cities/{city_id}') # Allows us to delete cities that we've added
def delete_city(city_id: int):
    db.pop(city_id-1) # Pop, or delete the city out of our database.
    return {} # Return nothing, or empty dictionary
