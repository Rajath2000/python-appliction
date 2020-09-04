from tkinter import *
import requests
import json
#in command prompt
#pip install reqests
#how to connect API on an internet
wether = Tk()
wether.title("Weather report")
wether.geometry("400x50")
#http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=5160FBC5-20B0-49D1-B81E-4C11A4FAC794
linl="http://www.airnowapi.org/aq/observation/zipCode/current/?format=text/csv&zipCode=~zipCode~&distance=25&API_KEY=5160FBC5-20B0-49D1-B81E-4C11A4FAC794"

try:
	api_requests = requests.get(link)
	api = json.loads(api_requests.content)
	city = api[0]['ReportingArea']
	Qulity=api[0]['AQI']
	catgory=api[0]['Category']['Name']
	if catgory =='Good':
		color="#00e400"
	elif catgory=='Moderate':
		color = "#ffff00"
	elif catgory == 'Unhealthy for Sensitive Groups':
		color="#ff7e00"
	elif catgory == 'Unhealthy':
		color="#ff0000"
	elif catgory=='Very Unhealthy':
		color="#8f3f97"
	elif catgory=='Hazardous':
		color="#7e0023"
	mylabel=Label(wether,text=city+" Air Qulity "+str(Qulity)+" "+catgory,font=("Helvectica",20),background=color).pack()
	wether.configure(background=color)
except Execption as e:
	api = "Error..."
	ab = Label(wether,text=api).pack()
    
wether.mainloop()