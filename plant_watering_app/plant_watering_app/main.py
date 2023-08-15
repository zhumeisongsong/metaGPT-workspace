from flask import Flask, render_template, request, jsonify
from models import Plant, User, WateringSchedule, Weather, Notification
import datetime

app = Flask(__name__)

class PlantWateringApp:
    def __init__(self, user, weather):
        self.user = user
        self.weather = weather
        self.notifications = []

    def get_plants(self):
        return self.user.plants

    def get_plant(self, plant_id):
        for plant in self.user.plants:
            if plant.id == plant_id:
                return plant
        return None

    def add_plant(self, plant):
        self.user.plants.append(plant)

    def update_plant(self, plant):
        for i, p in enumerate(self.user.plants):
            if p.id == plant.id:
                self.user.plants[i] = plant
                break

    def delete_plant(self, plant_id):
        for i, plant in enumerate(self.user.plants):
            if plant.id == plant_id:
                del self.user.plants[i]
                break

    def water_plant(self, plant_id):
        plant = self.get_plant(plant_id)
        if plant:
            watering_schedule = WateringSchedule(date=datetime.datetime.now(), is_completed=False, plant=plant)
            plant.watering_schedules.append(watering_schedule)

    def complete_watering_schedule(self, watering_schedule_id):
        for plant in self.user.plants:
            for watering_schedule in plant.watering_schedules:
                if watering_schedule.id == watering_schedule_id:
                    watering_schedule.is_completed = True
                    break

    def send_notification(self, message):
        notification = Notification(message=message, timestamp=datetime.datetime.now(), user=self.user)
        self.notifications.append(notification)

    def update_weather(self):
        # Fetch weather data from OpenWeatherMap API
        weather_data = {
            "temperature": 25.0,
            "humidity": 60.0,
            "description": "Sunny"
        }
        self.weather.temperature = weather_data["temperature"]
        self.weather.humidity = weather_data["humidity"]
        self.weather.description = weather_data["description"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/plants")
def get_plants():
    plants = app.plant_watering_app.get_plants()
    return jsonify(plants)

@app.route("/plants/<int:plant_id>")
def get_plant(plant_id):
    plant = app.plant_watering_app.get_plant(plant_id)
    if plant:
        return jsonify(plant)
    else:
        return jsonify({"error": "Plant not found"}), 404

@app.route("/plants", methods=["POST"])
def add_plant():
    data = request.get_json()
    plant = Plant(id=data["id"], name=data["name"], species=data["species"], watering_frequency=data["watering_frequency"], watering_amount=data["watering_amount"], season=data["season"], image_url=data["image_url"])
    app.plant_watering_app.add_plant(plant)
    return jsonify({"message": "Plant added successfully"})

@app.route("/plants/<int:plant_id>", methods=["PUT"])
def update_plant(plant_id):
    data = request.get_json()
    plant = Plant(id=plant_id, name=data["name"], species=data["species"], watering_frequency=data["watering_frequency"], watering_amount=data["watering_amount"], season=data["season"], image_url=data["image_url"])
    app.plant_watering_app.update_plant(plant)
    return jsonify({"message": "Plant updated successfully"})

@app.route("/plants/<int:plant_id>", methods=["DELETE"])
def delete_plant(plant_id):
    app.plant_watering_app.delete_plant(plant_id)
    return jsonify({"message": "Plant deleted successfully"})

@app.route("/plants/<int:plant_id>/water", methods=["POST"])
def water_plant(plant_id):
    app.plant_watering_app.water_plant(plant_id)
    return jsonify({"message": "Plant watered successfully"})

@app.route("/watering-schedules/<int:watering_schedule_id>/complete", methods=["POST"])
def complete_watering_schedule(watering_schedule_id):
    app.plant_watering_app.complete_watering_schedule(watering_schedule_id)
    return jsonify({"message": "Watering schedule completed successfully"})

@app.route("/notifications")
def get_notifications():
    notifications = app.plant_watering_app.notifications
    return jsonify(notifications)

@app.route("/notifications", methods=["POST"])
def send_notification():
    data = request.get_json()
    app.plant_watering_app.send_notification(data["message"])
    return jsonify({"message": "Notification sent successfully"})

@app.route("/weather")
def get_weather():
    weather = {
        "temperature": app.plant_watering_app.weather.temperature,
        "humidity": app.plant_watering_app.weather.humidity,
        "description": app.plant_watering_app.weather.description
    }
    return jsonify(weather)

if __name__ == "__main__":
    user = User(id=1, name="John Doe", email="john@example.com", plants=[])
    weather = Weather(id=1, temperature=0.0, humidity=0.0, description="")
    app.plant_watering_app = PlantWateringApp(user=user, weather=weather)
    app.run()
