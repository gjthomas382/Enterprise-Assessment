#!/usr/bin/env python3
import requests, json
from bs4 import BeautifulSoup

#Grab the users IP Address
def WeatherData():
	ip = requests.get('https://api.ipify.org').content.decode('utf8')

	#Grab the users IP address and location data
	response = requests.get('http://ipwho.is/' + str(ip))
	json_response = response.json()

	#Search for the surrent weather via google.com using users postal code
	url = "https://www.google.com/search?q="+"weather"+json_response['postal']
	html = requests.get(url).content

	#Beautiful Soup html parser for retrieving usable data from the google search.
	soup = BeautifulSoup(html, 'html.parser')
	temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
	string = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
	data = string.split('\n')
	sky = data[1]

	#prints Temperature and weather condition.
	print("The temperature is", temp)
	print("The current weather is", sky)

	weatherurl = 'https://wttr.in/{}' .format(json_response['city'])
	requestedWeather = requests.get(weatherurl)
	print(requestedWeather.text)
