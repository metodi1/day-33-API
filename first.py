import requests

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# #да показва ако има грешка каква е
# response.raise_for_status()
#
# data = response.json()
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# print(longitude, latitude)

MY_LAT = 42.483780
MY_LNG = 26.510771
MY_FORMATTED = 0
parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted":MY_FORMATTED,
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]




print(sunrise)
print(sunset)