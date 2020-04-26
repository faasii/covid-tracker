#!/bin/python3

import datetime
import json
import requests
import sys

#Coded by faasi
#https://github.com/faasii/

now = datetime.datetime.now()
day = now.day
month = now.month

if month == 4:
        m = 21
elif month == 5:
        m = 51
elif month == 6:
        m = 82
elif month == 7:
        m = 112
elif month == 8:
        m = 143

c = day + m

len = len(sys.argv)
if len == 2:
	info = sys.argv[1]
	info = info.lower()
elif len == 3:
	n = sys.argv[2]
	c = "_"
	info = info + c + n
	info = info.lower()
elif len == 1:
	print("99.India")
	print("0.Andaman Nicobar Island")
	print("1.AndhraP Pradesh")
	print("2.Arunachal Pradesh")
	print("3.Assam")
	print("4.Bihar")
	print("5.Chandigarh")
	print("6.Chhattisgarh")
	print("7.Delhi")
	print("8.Goa")
	print("9.Gujarat")
	print("10.Haryana")
	print("11.Himachal pradesh")
	print("12.Jammu_kashmir")
	print("13.Jharkhand")
	print("14.Karnataka")
	print("15.Kerala")
	print("16.Ladakh")
	print("17.Madhya_pradesh")
	print("18.Maharashtra")
	print("19.Manipur")
	print("20.Meghalaya")
	print("21.Mizoram")
	print("22.Nagaland")
	print("23.Odisha")
	print("24.Puducherry")
	print("25.Punjab")
	print("26.Rajasthan")
	print("27.Tamil nadu")
	print("28.Telengana")
	print("29.Tripura")
	print("30.Uttarakhand")
	print("31.Up")
	print("32.West bengal")
	print("")
	st = input("Select State : ")
	sta = int(st)
	if sta == 0:
		info = "andaman_nicobar"
	elif sta == 1:
		info = "andhra_pradesh"
	elif sta == 2:
		info = "arunachal_pradesh"
	elif sta == 3:
		info = "assam"
	elif sta == 4:
		info = "bihar"
	elif sta == 5:
		info = "chandigarh"
	elif sta == 6:
		info = "chhattisgarh"
	elif sta == 7:
		info = "delhi"
	elif sta == 8:
		info = "goa"
	elif sta == 9:
		info = "gujarat"
	elif sta == 10:
		info = "haryana"
	elif sta == 11:
		info = "himachal_pradesh"
	elif sta == 12:
		info = "jammu_kashmir"
	elif sta == 13:
		info = "jharkhand"
	elif sta == 14:
		info = "karnataka"
	elif sta == 15:
		info = "kerala"
	elif sta == 16:
		info = "ladakh"
	elif sta == 17:
		info = "madhya_pradesh"
	elif sta == 18:
		info = "maharashtra"
	elif sta == 19:
		info = "manipur"
	elif sta == 20:
		info = "meghalaya"
	elif sta == 21:
		info = "mizoram"
	elif sta == 22:
		info = "nagaland"
	elif sta == 23:
		info = "odisha"
	elif sta == 24:
		info = "puducherry"
	elif sta == 25:
		info = "punjab"
	elif sta == 26:
		info = "rajasthan"
	elif sta == 27:
		info = "tamil_nadu"
	elif sta == 28:
		info = "telengana"
	elif sta == 29:
		info = "tripura"
	elif sta == 30:
		info = "uttarakhand"
	elif sta == 31:
		info = "up"
	elif sta == 32:
		info = "west_bengal"
	elif sta == 99:
		info = "india"
	else:
		print("")
		print("Your input is wrong")
		exit()

if info != "india":
	if info == "andaman_nicobar":
		loc = 0
	elif info == "andhra_pradesh":
		loc = 1
	elif info == "arunachal_pradesh":
        	loc = 2
	elif info == "assam":
        	loc = 3
	elif info == "bihar":
        	loc = 4
	elif info == "chandigarh":
        	loc = 5
	elif info == "chhattisgarh":
        	loc = 6
	elif info == "delhi":
        	loc = 7
	elif info == "goa":
        	loc = 8
	elif info == "gujarat":
        	loc = 9
	elif info == "haryana":
        	loc = 10
	elif info == "himachal_pradesh":
        	loc = 11
	elif info == "jammu_kashmir":
        	loc = 12
	elif info == "jharkhand":
        	loc = 13
	elif info == "karnataka":
        	loc = 14
	elif info == "kerala":
        	loc = 15
	elif info == "ladakh":
        	loc = 16
	elif info == "madhya_pradesh":
        	loc = 17
	elif info == "maharashtra":
        	loc = 18
	elif info == "manipur":
        	loc = 19
	elif info == "meghalaya":
        	loc = 20
	elif info == "mizoram":
        	loc = 21
	elif info == "nagaland":
        	loc = 22
	elif info == "odisha":
        	loc = 23
	elif info == "puducherry":
        	loc = 24
	elif info == "punjab":
        	loc = 25
	elif info == "rajasthan":
        	loc = 26
	elif info == "tamil_nadu":
        	loc = 27
	elif info == "telengana":
        	loc = 28
	elif info == "tripura":
        	loc = 29
	elif info == "uttarakhand":
        	loc = 30
	elif info == "up":
        	loc = 31
	elif info == "west_bengal":
        	loc = 32
	else:
		print("State name is wrong .Try correct name ")
		print("or")
		print("Run script without argument (eg. python3 covid-tracker.py )")
		exit()

	def state():
		c = day + m
		url = "https://api.rootnet.in/covid19-in/stats/history"
		response = requests.get(url)
		l = response.json()
		a_state_loc = l['data'][c]['regional'][loc]['loc']
		a_state_total = l['data'][c]['regional'][loc]['totalConfirmed']
		a_state_dis = l['data'][c]['regional'][loc]['discharged']
		a_state_death = l['data'][c]['regional'][loc]['deaths']
		a_state_active = a_state_total - a_state_dis - a_state_death
		print("State : " + str(a_state_loc))


		c = c - 1
		b_state_total = l['data'][c]['regional'][loc]['totalConfirmed']
		b_state_dis = l['data'][c]['regional'][loc]['discharged']
		b_state_death = l['data'][c]['regional'][loc]['deaths']
		b_state_active = b_state_total - b_state_dis - b_state_death
		print(" ")
		print("Today Status ")

		t_state_total = a_state_total - b_state_total
		t_state_dis = a_state_dis - b_state_dis
		t_state_death = a_state_death - b_state_death
		t_state_active = a_state_active - b_state_active

		print(" ")
		print("Confirmed case " + str(t_state_total))
		#print("Active " + str(t_state_active))
		print("Discharged " + str( t_state_dis))
		print("Death " + str(t_state_death))

		print("")

		print("Total status")
		print("")
		print("Confirmed case " + str(a_state_total))
		print("Active " + str(a_state_active))
		print("Discharged " + str(a_state_dis))
		print("Death " + str(a_state_death))
	result = state()
elif info == "india":
	def india():
		c = day + m
		url = "https://api.rootnet.in/covid19-in/stats/history"	
		response = requests.get(url)
		b = response.json()
		a_india_total = b['data'][c]['summary']['total']
		a_india_dis = b['data'][c]['summary']['discharged']
		a_india_death = b['data'][c]['summary']['deaths']
		a_india_active = a_india_total - a_india_dis - a_india_death

		c = c - 1
		b_india_total = b['data'][c]['summary']['total']
		b_india_dis = b['data'][c]['summary']['discharged']
		b_india_death = b['data'][c]['summary']['deaths']
		b_india_active = b_india_total - b_india_dis - b_india_death
		print("India")
		print("")
		print("Today Status ")

		t_india_total = a_india_total - b_india_total
		t_india_dis = a_india_dis - b_india_dis
		t_india_death = a_india_death - b_india_death
		t_india_active = a_india_active - b_india_active
		print(" ")
		print("Today confirmed case " + str(t_india_total))
		print("Today Active " + str(t_india_active))
		print("Today Discharged " + str( t_india_dis))
		print("Today Death " + str(t_india_death))

		print("")

		print("Total status")

		print("Total confirmed case " + str(a_india_total))
		print("Total active " + str(a_india_active))
		print("Total discharged " + str(a_india_dis))
		print("Total Death " + str(a_india_death))
#	result = india()

url = "https://api.rootnet.in/covid19-in/stats/history"
response = requests.get(url)
hh = response.json()

t = hh['lastOriginUpdate']
print("")
print("last updated on "+ str(t))
