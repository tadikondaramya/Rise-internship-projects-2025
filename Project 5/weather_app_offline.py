import tkinter as tk
from datetime import datetime

# Predefined mock weather data
mock_weather_data = {
    "chennai": {"temp": 34, "desc": "hot and sunny", "humidity": 60},
    "mumbai": {"temp": 30, "desc": "humid and cloudy", "humidity": 75},
    "delhi": {"temp": 36, "desc": "dry and sunny", "humidity": 40},
    "bangalore": {"temp": 28, "desc": "cool and rainy", "humidity": 80},
    "hyderabad": {"temp": 32, "desc": "sunny with clouds", "humidity": 55},
    "kolkata": {"temp": 31, "desc": "stormy", "humidity": 90},
}

def get_icon(description):
    if "sunny" in description:
        return "☀️"
    elif "cloud" in description:
        return "☁️"
    elif "rain" in description:
        return "🌧️"
    elif "storm" in description:
        return "⛈️"
    else:
        return "🌤️"

def get_weather():
    city = city_entry.get().lower()
    if not city:
        result_label.config(text="Please enter a city name.")
        return

    if city in mock_weather_data:
        data = mock_weather_data[city]
        icon = get_icon(data["desc"])
        now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        result = (
            f"{icon} Weather for {city.title()}:\n"
            f"Temp: {data['temp']}°C\n"
            f"Condition: {data['desc']}\n"
            f"Humidity: {data['humidity']}%\n"
            f"Checked at: {now}"
        )
    else:
        result = "Weather data not available for this city."
    
    result_label.config(text=result)

def clear_fields():
    city_entry.delete(0, tk.END)
    result_label.config(text="")

# Tkinter UI setup
app = tk.Tk()
app.title("Offline Weather App")

# Header
tk.Label(app, text="Offline Weather App", font=("Arial", 16, "bold")).pack(pady=10)

# City input
tk.Label(app, text="Enter City:", font=("Arial", 12)).pack()
city_entry = tk.Entry(app, font=("Arial", 12))
city_entry.pack(pady=5)

# Buttons
tk.Button(app, text="Get Weather", command=get_weather, width=20).pack(pady=5)
tk.Button(app, text="Clear", command=clear_fields, width=20).pack(pady=2)

# Output Label
result_label = tk.Label(app, text="", font=('Arial', 12), justify="left", padx=10, pady=10)
result_label.pack()

# Start GUI loop
app.mainloop()
