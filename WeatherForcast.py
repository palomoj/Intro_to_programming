# Weather Forcast Application
# Author: Jason Palomo
# Creation Date: 07/23/2020
# API source: http://openweathermap.org/
# The program will prompt the user for their city or zipcode and request the weather forecast

import requests
import string

#Function will take the search value and determin if the user has entered in a zipcode or city name. The input 
#will determin what api url is called and returned.
def getWeather(weather_Search_Value):
	if weather_Search_Value == str(weather_Search_Value):
		city = weather_Search_Value
		url_City = (f'http://api.openweathermap.org/data/2.5/weather?q={city},&appid=450427af87eccda0b72928eae7befaac&units=Imperial')
		resC = requests.get(url_City)
		dataC = resC.json()
		#print(dataC)
		return dataC
	elif weather_Search_Value == int(weather_Search_Value):
		zipCode = weather_Search_Value
		url_Zip = (f'http://api.openweathermap.org/data/2.5/weather?zip={zipCode},&appid=450427af87eccda0b72928eae7befaac&units=Imperial')
		resZ = requests.get(url_Zip)
		dataZ = resZ.json()
		#print(dataZ)
		return dataZ

#Takes the weahter forcast json output and formats into a readable format. Can add additional weather elements as needed.
def formatOutput(output):
	temp = output['main']['temp']
	wind_speed = output['wind']['speed']
	description = output['weather'][0]['description']

	print(f'\nTemperature : {temp} degree fahrenheit')
	print(f'Wind Speed : {wind_speed} m/s')
	print(f'Description : {description}')


#Displays the welcome message and gives a little information about the program
def displayWelcome():
	print('''\nThank you for using the Weather Forcast Application where
you can access current weather data for any location including over
200,000 cities by searching the city name or zip code. .\n''')

#This function requests the choice from the user. I want to seperate the city choice from zipcode
#this way it will be easier to validate the data. Also the api url is different for city search and zipcode search
def searchCoice():
	choice = ''
	while choice != '1' and choice != '2':
		choice = input("To search by City, enter 1. To search by Zipcode, enter 2: ")
		return choice
		
#This function takes in the choice and asks the user for the city or zipcode based on search method chosen.
#Funtion will also validate the search entry by only allowing charactors for city search and numbers for zipcode.
def searchLocation(choiceNumber):
	searchLoc = ''
	if choiceNumber == '1':
		searchLoc = str(input('Please enter city name: '))
	elif choiceNumber == '2':
		searchLoc = int(input('Please enter city zip code: '))
	else: 
		print('Incorrect entry, please enter 1 for city or 2 for zip code')	
	return searchLoc

#Main part of program that will keep the program running and call the different functions 
continueSearch = 'yes'

while continueSearch == 'yes' or continueSearch == 'y':
	displayWelcome()
	choiceNumber = searchCoice()
	weather_Search_Value = searchLocation(choiceNumber)
	getWeather(weather_Search_Value)
	output = getWeather(weather_Search_Value)
	formatOutput(output)
	
	continueSearch = input('Would you like to search again? (yes or no): ')
	if continueSearch == 'no' or 'n':
		print('Program has closed!')
