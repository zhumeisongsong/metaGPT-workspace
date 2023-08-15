## models.py

from typing import List
import datetime

class Plant:
    def __init__(self, id: int, name: str, species: str, watering_frequency: int, watering_amount: int, season: str, image_url: str):
        self.id = id
        self.name = name
        self.species = species
        self.watering_frequency = watering_frequency
        self.watering_amount = watering_amount
        self.season = season
        self.image_url = image_url
        self.watering_schedules = []

class User:
    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email
        self.plants = []

class WateringSchedule:
    def __init__(self, id: int, date: datetime.datetime, is_completed: bool, plant: Plant):
        self.id = id
        self.date = date
        self.is_completed = is_completed
        self.plant = plant

class Weather:
    def __init__(self, id: int, temperature: float, humidity: float, description: str):
        self.id = id
        self.temperature = temperature
        self.humidity = humidity
        self.description = description

class Notification:
    def __init__(self, id: int, message: str, timestamp: datetime.datetime, user: User):
        self.id = id
        self.message = message
        self.timestamp = timestamp
        self.user = user
