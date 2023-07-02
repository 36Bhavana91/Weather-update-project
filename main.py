# Weather-update-project
import tkinter as tk   #import python libraries
import requests
def get_weather():                           #creating a function to get info about weather
    api_key = "a356be8ce30422ed329984a9bf0d51ff"  # Insert API key
    city = entry.get()                                                                       #Get input from the user - city name
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"         #Provide link to open weather map
    response = requests.get(url)
    weather_data = response.json()
    if weather_data.get("cod") != "404":
        try:                                                              #Get required information to display
            main_info = weather_data["weather"][0]["main"]                #Information about the weather in the given city
            description = weather_data["weather"][0]["description"]             #Small description about the weather in the given city
            temperature = weather_data["main"]["temp"] - 273.15  # Convert to Celsius           #temperature in the given city

            result = f"Weather: {main_info}\nDescription: {description}\nTemperature: {temperature:.2f}°C"
            label['text'] = result
        except KeyError:
            label['text'] = "Data format error!"
    else:
        label['text'] = "City not found!"
root = tk.Tk()
frame = tk.Frame(root)
frame.pack(pady=20)
label = tk.Label(frame, font=('Arial', 14), anchor="center", justify="center")                  #Label in the output interface
label.pack()
entry = tk.Entry(root, font=('Arial', 14))
entry.pack(pady=10)
button = tk.Button(root, text="Get Weather", font=('Arial', 14), command=get_weather)            #button in the output interface
button.pack()
root.mainloop()