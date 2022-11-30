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

#FUNCTIONS
def printMenu():
  print("[1] Enter airport details\n[2] Enter flight details\n[3] Enter price plan and calculate profit\n[4] Clear data\n[5] Quit")
  choice = 0
  while choice > 5 or choice < 1:
    choice = int(input("\nEnter a number from 1 to 5 representing your choice"))
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
    aircraftType = input("Enter type of aircraft")
    if aircraftType != details[0][0] and aircraftType != details[1][0] and aircraftType != details[2][0]:
        print("\nError: invalid aircraft type\n")
        time.sleep(1)
        print("Returning to main menu...\n")
        time.sleep(1)
        repeat = True
        return repeat
    elif aircraftType == details[0][0]:
      for i in range(4):
        print("Name: " + details[0][i] + "\n")
    elif aircraftType == details[1][0]:
      for i in range(4):
        print("Running cost per seat per 100km" + details[1][i] + "\n")
    elif aircraftType == details[2][0]:
      for i in range(4):
        print("Maximum number of economy seats" + details[2][i] + "\n")
  if choice == 5:
    print("Quitting...")
    quit()

#MAIN
while repeat == True:
  choice = printMenu()
  repeat = executeChoice(choice)
