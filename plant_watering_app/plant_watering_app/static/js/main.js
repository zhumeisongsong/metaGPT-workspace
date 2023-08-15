// static/js/main.js

// Function to get plants from the server
function getPlants() {
  return fetch("/plants")
    .then((response) => response.json())
    .then((data) => data);
}

// Function to get a specific plant from the server
function getPlant(plantId) {
  return fetch(`/plants/${plantId}`)
    .then((response) => response.json())
    .then((data) => data);
}

// Function to add a new plant to the server
function addPlant(plant) {
  return fetch("/plants", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(plant),
  })
    .then((response) => response.json())
    .then((data) => data);
}

// Function to update an existing plant on the server
function updatePlant(plantId, plant) {
  return fetch(`/plants/${plantId}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(plant),
  })
    .then((response) => response.json())
    .then((data) => data);
}

// Function to delete a plant from the server
function deletePlant(plantId) {
  return fetch(`/plants/${plantId}`, {
    method: "DELETE",
  })
    .then((response) => response.json())
    .then((data) => data);
}

// Function to water a plant
function waterPlant(plantId) {
  return fetch(`/plants/${plantId}/water`, {
    method: "POST",
  })
    .then((response) => response.json())
    .then((data) => data);
}

// Function to complete a watering schedule
function completeWateringSchedule(wateringScheduleId) {
  return fetch(`/watering-schedules/${wateringScheduleId}/complete`, {
    method: "POST",
  })
    .then((response) => response.json())
    .then((data) => data);
}

// Function to get notifications from the server
function getNotifications() {
  return fetch("/notifications")
    .then((response) => response.json())
    .then((data) => data);
}

// Function to send a notification to the server
function sendNotification(message) {
  return fetch("/notifications", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ message }),
  })
    .then((response) => response.json())
    .then((data) => data);
}

// Function to get weather data from the server
function getWeather() {
  return fetch("/weather")
    .then((response) => response.json())
    .then((data) => data);
}
