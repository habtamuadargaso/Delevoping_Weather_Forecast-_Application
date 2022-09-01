```# Delevoping_Weather_Forecast-_Application_project
Introducation about Weather Application projects main aims

Weather forcasting are made by the collecting as much data as possible about the current state of the weather such as tempture , humidity and wind and using meteorlogy to determine how the weather change or predict the future. How to create easily the this platform easily and clearly by using python library files.

For this project, we will import python library files and a Weather report API Key to get the weather conditions any user input location. For this project we need some few python librarys files

Install the required Python packages using the pip command. Make sure you have pip installed on your system.

step1 : Run the following command in your command prompt.
```
"pip3 install opencv-python qrcode numpy Image " step 2: or you can install them one by one as
``
1) "pip3 install opencv-python"
2) "pip3 install numpy"
3) " python -m pip install requests"
Developing Our Weather Telecast

step1 : we need import request from library import requests from pprint import pprint

step2: we need the API_key " " from a website that store the information about the weather and forecats them with accurate reslutes.

API_Key = "b3613ae4543eef03293d7f54d0b7e053"

step3 : one next step allow the usere to enter desired location for which they want to analyze or view the weather conditions.using input command

location = input ("Enter Your Desired Location : ")

step4 : we need variable that will store the default URL location weather access website

weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid="

step5 : combine the default path of the open weather map website with API_KEy variable

final_url = weather_url + API_Key

step6: Finally requests library to get the weather data

weather_data = requests.get(final_url).json() then to see the result pprint(weather_data
