import requests
import json

def FindSlot(pin_code, date):
    URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=" + str(pin_code) + "&date=" + str(date)

    responce = requests.get(URL).text

    responce_info = json.loads(responce)
    FreeSlots = []

    for center in responce_info['centers']: # dict
        for key, value in center.items():
            if(key == 'sessions'):
                for val in value: # list
                    for key1, val1 in val.items(): # dict
                        if(key1 == 'available_capacity'):
                            if(val1 == 1):
                                FreeSlots.append(val)
    return FreeSlots


def start():
	pin_code = input("Enter the pin code ")
	date = input("Input date in format -> dd-mm-yyyy ")

	Final_Slot = []
	Final_Slot = AvailableSlot(pin_code, date)

	if(len(Final_Slot) > 1):
		print("Slot Avalaible")
		for slot in Final_Slot:
			print(slot)

	else:
		print("No slot found")

start()





