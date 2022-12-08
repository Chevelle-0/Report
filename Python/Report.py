import time
#LISTS
airportCodes = ["JFK", "ORY", "MAD", "AMS", "CAI"]
airportNames = ["John F Kennedy International", "Paris-Orly", "Adolfo Suarez Madrid-Bajaras", "Amsterdam Schipol", "Cairo International"]
distanceFromLPL = [5326, 629, 1428, 526, 3779]
distanceFromBOH = [5486, 379, 1151, 489, 3584]
details = [["Boeing 737", 8, 2650, "180", "8"], ["Airbus 321", 7, 5600, "220", "10"], ["Boeing 787", 5, 4050, "406", "14"]]

#VARIABLES
choice = 0
UKairportCode = ""
nonUKairportCode = ""
complete1 = 0
repeat = True
firstClass = 0
aircraftID = 0
aircraftType = ""
airportCodeNumber = 5
firstClassPrice = 0
economyClassPrice = 0
flightCostperSeat = 0
flightCost = 0
flightIncome = 0
flightProfit = 0
detail1 = 0
detail2 = 0
detail3 = 0
detail4 = 0
LPLdistance = 0
BOHdistance = 0

#FUNCTIONS
def printMenu():
	print("[1] Enter airport details\n[2] Enter flight details\n[3] Enter price plan and calculate profit\n[4] Clear data\n[5] Quit")
	choice = 0
	while choice > 5 or choice < 1:
		choice = int(input("\nEnter a number from 1 to 5 representing your choice\n"))
		print("\n")
	return choice

#AIRPORT DETAILS
def airportDetails():
	global repeat
	global UKairportCode
	global nonUKairportCode
	global airportCodeNumber
	complete = 0
	complete1 = 0
	#UK CODE
	UKairportCode = input("Enter three letter code of UK airport\n")
	print("\n")
	while UKairportCode != "LPL" and UKairportCode != "BOH":
		if UKairportCode != "LPL" and UKairportCode != "BOH":
			print('Error: UK airport code must be "LPL" or "BOH"!\n')
		UKairportCode = input("Enter three letter code of UK airport\n")
		print("\n")
	#OVERSEAS CODE
	while complete1 == 0:
		nonUKairportCode = input("Enter three letter code of overseas airport\n")
		print("\n")
		while nonUKairportCode == "LPL" and nonUKairportCode == "BOH":
			nonUKairportCode = input("Enter three letter code of overseas airport\n")
			while nonUKairportCode == "LPL" or nonUKairportCode == "BOH":
				print('Error: overseas airport code must not be "LPL" or "BOH"\n')
				nonUKairportCode = input("Enter three letter code of overseas airport\n") 
		for i in range(len(airportCodes)):
			if nonUKairportCode == airportCodes[i]:
				print("\nName of airport with given code:\n" + airportNames[i] + "\n")
				complete1 = 1
		if complete1 == 0:
			print("Error: Overseas airport code did not match any in database!\n")
	time.sleep(2)
	print("Operation complete, returning to main menu... \n")
	time.sleep(1)
	for i in range(5):
		if airportCodes[i] == nonUKairportCode:
			airportCodeNumber = i
	repeat = True
	return repeat

def flightDetails():
	global aircraftType
	global firstClass
	aircraftType = input("Enter type of aircraft\n")
	print("\n")
	if aircraftType != details[0][0] and aircraftType != details[1][0] and aircraftType != details[2][0]:
			print("Error: invalid aircraft type\n")
			time.sleep(1)
			print("Returning to main menu...\n")
			time.sleep(1)
			repeat = True
			return repeat
	elif aircraftType == details[0][0]:
		aircraftID = 0
		time.sleep(0.5)
		print("Name: " + details[0][0])
		time.sleep(0.5)
		print(f"Running cost per seat per 100km: £{details[0][1]}")
		time.sleep(0.5)
		print(f"Maximum flight range (km): {details[0][2]}")
		time.sleep(0.5)
		print("Maximum number of economy seats: " + details[0][3])
		time.sleep(0.5)
		print("Maximum number of first-class seats: " + details[0][4])
		print("\n")
		time.sleep(1)
		firstClass = int(input("Enter number of first class seats\n"))
		if firstClass > 0:
			if firstClass > int(details[aircraftID][4]):
				print("\nError: number of first-class seats too large\n")
				time.sleep(0.5)
				print("Operation complete, returning to main menu...\n")
				time.sleep(1)
				repeat = True
				return repeat
			else:
				time.sleep(0.5)
				print(f"\nNumber of economy seats: {int(details[aircraftID][3]) - (firstClass*2)}")
				time.sleep(1)
		else:
			print("Error: Number of first class seats too small, returing to main menu...")
		print("\nOperation complete, returning to main menu... \n")
		time.sleep(1)
		repeat = True
		return repeat
	elif aircraftType == details[1][0]:
		aircraftID = 1
		time.sleep(0.5)
		print("Name: " + details[1][0])
		time.sleep(0.5)
		print("Running cost per seat per 100km: " + details[1][1])
		time.sleep(0.5)
		print("Maximum flight range (km): " + details[1][2])
		time.sleep(0.5)
		print("Maximum number of economy seats:" + details[1][3])
		time.sleep(0.5)
		print("Maximum number of first-class seats 5: " + details[1][4])
		print("\n")
		time.sleep(1)
		firstClass = int(input("Enter number of first class seats\n"))
		if firstClass != 0:
			if firstClass > details[aircraftID][4]:
				print("Error: number of first-class seats too large")
				repeat = True
				return repeat
			else:
				print(f"Number of economy seats: {details[aircraftID][3] - (firstClass*2)}")
		print("\nOperation complete, returning to main menu... \n")
		time.sleep(1)
		repeat = True
		return repeat
	elif aircraftType == details[2][0]:
		aircraftID = 2
		time.sleep(0.5)
		print("Name: " + details[2][0])
		time.sleep(0.5)
		print("Running cost per seat per 100km: " + details[2][1])
		time.sleep(0.5)
		print("Maximum flight range (km): " + details[2][2])
		time.sleep(0.5)
		print("Maximum number of economy seats: " + details[2][3])
		time.sleep(0.5)
		print("Maximum number of first-class seats: " + details[2][4])
		print("\n")
		time.sleep(1)
		firstClass = int(input("Enter number of first class seats\n"))
		if firstClass != 0:
			if firstClass > details[aircraftID][4]:
				print("Error: number of first-class seats too large")
				repeat = True
				return repeat
			else:
				print(f"Number of economy seats: {details[aircraftID][3] - (firstClass*2)}")
		print("\nOperation complete, returning to main menu... \n")
		time.sleep(1)
		repeat = True
		return repeat

#ENTER PRICE PLAN
def pricePlan():
	global flightCostperSeat
	global flightCost
	global flightIncome
	global flightProfit
	global UKairportCode
	global aircraftType
	global nonUKairportCode
	if UKairportCode == "" or nonUKairportCode == "":
		print("Error: codes for UK and non UK airports not entered")
		print("\n")
		time.sleep(1)
		repeat = True
		return repeat
	if aircraftType == "":
		print("Error: aircraft type not entered")
		print("\n")
		time.sleep(1)
		repeat = True
		return repeat
	if firstClass == 0:
		print("Error: number of first class seats not entered")
		print("\n")
		time.sleep(1)
		repeat = True
		return repeat
	if UKairportCode == "LPL" and distanceFromLPL[airportCodeNumber] > details[aircraftID][2]:
		print("Error: maximum flight range less than distance between airports")
		print("\n")
		time.sleep(1)
		repeat = True
		return repeat
	if UKairportCode == "BOH" and distanceFromBOH[airportCodeNumber] > details[aircraftID][2]:
		print("Error: maximum flight range less than distance between airports")
		print("c")
		time.sleep(1)
		repeat = True
		return repeat
	firstClassPrice = int(input("Enter the price of a first class seat\n"))
	print("\n")
	economyClassPrice = int(input("Enter the price of an economy seat\n"))
	print("\n")
	detail1 = int(details[aircraftID][1])
	detail2 = int(details[aircraftID][2])
	detail3 = int(details[aircraftID][3])
	detail4 = int(details[aircraftID][4])
	if UKairportCode == "LPL":
		LPLdistance = int(distanceFromLPL[airportCodeNumber])
	if	UKairportCode == "BOH":	
		BOHdistance = int(distanceFromBOH[airportCodeNumber])
	if UKairportCode == "B0H":
		flightCostperSeat = detail1 * BOHdistance / 100
	if UKairportCode == "LPL":
		flightCostperSeat = detail1 * LPLdistance / 100
	flightCost =  flightCostperSeat * (detail4 + detail3)
	flightIncome = detail4 * firstClassPrice + detail3 * economyClassPrice
	flightProfit = flightIncome - flightCost
	time.sleep(0.5)
	print(f"Flight cost per seat: {flightCostperSeat}")
	print("\n")
	time.sleep(0.5)
	print(f"Flight cost: {flightCost}")
	print("\n")
	time.sleep(0.5)
	print(f"Flight income: {flightIncome}")
	print("\n")
	time.sleep(0.5)
	print(f"flight profit: {flightProfit}")
	print("\n")
	time.sleep(2)
	print("Operation complete, returning to main menu... \n")
	time.sleep(1)
	repeat = True
	return repeat

def clearData():
	global choice
	global UKairportCode 
	global nonUKairportCode 
	global complete1 
	global repeat 
	global firstClass 
	global aircraftID 
	global aircraftType 
	global airportCodeNumber
	global firstClassPrice 
	global economyClassPrice 
	global flightCostperSeat 
	global flightCost 
	global flightIncome
	global flightProfit 
	global detail1 
	global detail2 
	global detail3 
	global detail4
	global LPLdistance
	global BOHdistance 
	choice = 0
	UKairportCode = ""
	nonUKairportCode = ""
	complete1 = 0
	repeat = True
	firstClass = 0
	aircraftID = 0
	aircraftType = ""
	airportCodeNumber = 5
	firstClassPrice = 0
	economyClassPrice = 0
	flightCostperSeat = 0
	flightCost = 0
	flightIncome = 0
	flightProfit = 0
	detail1 = 0
	detail2 = 0
	detail3 = 0
	detail4 = 0
	LPLdistance = 0
	BOHdistance = 0
	print("Data cleared, returning to main menu...
	")
	repeat = True 
	return repeat
	

def executeChoice(choice):
	#VARIABLES
	global repeat
	complete1 = 0
	repeat = True
	firstClass = 0
	#AIRPORT DETAILS
	if choice == 1:
		repeat = airportDetails()
		return repeat
	#FLIGHT DETAILS
	if choice == 2:
		repeat = flightDetails()
		return repeat
	if choice == 3:
		repeat = pricePlan()
		return repeat
	if choice == 4:
		repeat = clearData()
		return repeat
	if choice == 5:
		print("Quitting...")
		quit()

#MAIN
while repeat == True:
	choice = printMenu()
	repeat = executeChoice(choice)
