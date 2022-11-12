#!/usr/bin/env python3
import json
import time, EA_RESTAPI
import urllib.request
from bs4 import BeautifulSoup as soup


print("Well Hello There!")

#use the structured time function to grab the time
Local_time = time.strftime("%m/%d/%Y %I:%M:%S %p")
print("The current time is ", Local_time)

#Create a string variable for your user name("Enter your name:")
user_name = str(input("Enter your name: \n"))

#Print user_name
print("Username is:", user_name)

#Create an integer for user_age
user_age = int(input("Enter your age: \n"))

#Print user_age
print("Your age is: ", user_age)

print("Retrieving current weather forecast... Please be patient!")
EA_RESTAPI.WeatherData()
