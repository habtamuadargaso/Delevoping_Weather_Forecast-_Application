
import requests
# requests module allows you to send HTTPrequests using Python.
# The HTTP request returns a Response Object with all the response data (content, encoding, status, etc).
from pprint import pprint
#The pprint module provides a capability to “pretty-print” arbitrary Python data structures in a well-formatted and more readable way!
API_Key = "b3613ae4543eef03293d7f54d0b7e053"
# An API key is a unique identifier used to connect to, or perform, an API call. you can can you sample free API address 
location = input ("Enter Your Desired Location : ")
#allow the usere to enter desired location for which they want to analyze or view the weather conditions.using input command 
weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid="
# we need variable that will store the default URL location weather access website
final_url = weather_url + API_Key
# combine the default path of the open weather map website with API_KEy variable
weather_data = requests.get(final_url).json()
#Finally requests library to get the weather data 

pprint(weather_data)