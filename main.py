import requests
from datetime import datetime
import time
import smtplib

MY_LAT = 51.507351  # Your latitude
MY_LONG = -0.127758  # Your longitude
counter = 5
# Your position is within +5 or -5 degrees of the ISS position.
MY_LAT_MIN = MY_LAT - 5
MY_LAT_MAX = MY_LAT + 5
MY_LONG_MIN = MY_LONG - 5
MY_LONG_MAX = MY_LONG + 5

MY_EMAIL = "metodiganev207@gmail.com"
MY_PASSWORD = "qxde kbuo jogg gvjp"


# MY_PASSWORD ="qxde kbuo jogg gvjp"


def is_iss_close(MY_LAT_MIN, MY_LAT_MAX, MY_LONG_MIN, MY_LONG_MAX):
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    iss_position = False
    if MY_LAT_MIN < iss_latitude < MY_LAT_MAX:
        if MY_LONG_MIN < iss_longitude < MY_LONG_MAX:
            iss_position = True
    return iss_position


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    hour_now = datetime.now().hour
    if hour_now > sunset or hour_now < sunrise:
        dark = True
    else:
        dark = False

    return dark


while counter > 0:
    time.sleep(3)
    if is_dark() and is_iss_close(MY_LAT_MIN, MY_LAT_MAX, MY_LONG_MIN, MY_LONG_MAX):
        print("OK")
    else:
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up\n\nThe ISS is Not above you in the sky."
        )
        connection.quit()
    counter -= 1

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
