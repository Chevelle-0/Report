import time
#LISTS
airportCodes = ["JFK", "ORY", "MAD", "AMS", "CAI"]
airportNames = ["John F Kennedy International", "Paris-Orly", "Adolfo Suarez MAdrid-Bajaras", "Amsterdam Schipol", "Cairo International"]
distanceFromLPL = [5326, 629, 1428, 526, 3779]
distanceFromBOH = [5486, 379, 1151, 489, 3584]
details = [["Boeing 737", "£8", "2650", "180", "8"], ["Airbus 321", "£7", "5600", "220", "10"], ["Boeing 787", "£5", "4050", "406", "14"]]

#VARIABLES
choice = 0
UKairportCode = ""
nonUKairportCode = ""
complete1 = 0
repeat = True
firstClass = 0
aircraftID = 0

#FUNCTIONS
def printMenu():
  print("[1] Enter airport details\n[2] Enter flight details\n[3] Enter price plan and calculate profit\n[4] Clear data\n[5] Quit")
  choice = 0
  while choice > 5 or choice < 1:
    choice = int(input("\nEnter a number from 1 to 5 representing your choice\n"))
    print("\n")
  return choice

def executeChoice(choice):
  #VARIABLES
  complete1 = 0
  repeat = True
  #AIRPORT DETAILS
  if choice == 1:
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
    return repeat
  #FLIGHT DETAILS
  if choice == 2:
    aircraftType = input("Enter type of aircraft\n")
    print("\n")
    if aircraftType != details[0][0] and aircraftType != details[1][0] and aircraftType != details[2][0]:
        print("\nError: invalid aircraft type\n")
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
      print("Running cost per seat per 100km: " + details[0][1])
      time.sleep(0.5)
      print("Maximum number of economy seats: " + details[0][2])
      time.sleep(0.5)
      print("Details 4: " + details[0][3])
      time.sleep(0.5)
      print("Details 5: " + details[0][4])
      time.sleep(1)
      if firstClass != 0:
        if firstClass > details[aircraftID][4]:
          print("Error: number of first-class seats too large")
          repeat = True
          return repeat
        else:
          print(f"Number of economy seats: {details[aircraftID][3] - (firstClass*2)}")
      print("Operation complete, returning to main menu... \n")
      print("\nOperation complete, returning to main menu... \n")
      time.sleep(1)
    elif aircraftType == details[1][0]:
      aircraftID = 1
      time.sleep(0.5)
      print("Name: " + details[1][0])
      time.sleep(0.5)
      print("Running cost per seat per 100km: " + details[1][1])
      time.sleep(0.5)
      print("Maximum number of economy seats: " + details[1][2])
      time.sleep(0.5)
      print("Details 4: " + details[1][3])
      time.sleep(0.5)
      print("Details 5: " + details[1][4])
      time.sleep(1)
      if firstClass != 0:
        if firstClass > details[aircraftID][4]:
          print("Error: number of first-class seats too large")
          repeat = True
          return repeat
        else:
          print(f"Number of economy seats: {details[aircraftID][3] - (firstClass*2)}")
      print("Operation complete, returning to main menu... \n")
      print("Operation complete, returning to main menu... \n")
      time.sleep(1)
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
      time.sleep(1)
      firstClass = int(input("Enter number o first class seats"))
      if firstClass != 0:
        if firstClass > details[aircraftID][4]:
          print("Error: number of first-class seats too large")
          repeat = True
          return repeat
        else:
          print(f"Number of economy seats: {details[aircraftID][3] - (firstClass*2)}")
      print("Operation complete, returning to main menu... \n")
      time.sleep(1)
  if choice == 5:
    print("Quitting...")
    quit()

#MAIN
while repeat == True:
  choice = printMenu()
  repeat = executeChoice(choice)
