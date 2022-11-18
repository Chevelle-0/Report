#LISTS
airportCodes = ["JFK", "ORY", "MAD", "AMS", "CAI"]
airportNames = ["John F Kennedy International", "Paris-Orly", "Adolfo Suarez MAdrid-Bajaras", "Amsterdam Schipol", "Cairo International"]
distanceFromLPL = [5326, 629, 1428, 526, 3779]
distanceFromBOH = [5486, 379, 1151, 489, 3584]

#VARIABLES
choice = 0
UKairportCode = ""
nonUKairportCode = ""
complete1 = 0

#FUNCTIONS
def printMenu():
  print("[1] Enter airport details\n[2] Enter flight detauils\n[3] Enter price plan and calculate profit\n[4] Clear data\n[5] Quit")
  choice = 0
  while choice > 5 or choice < 1:
    choice = int(input("\nEnter a number from 1 to 5 representing your choice\n"))
  return choice

def executeChoice(choice):
  #AIRPORT DETAILS
  if choice == 1:
    #UK CODE
    UKairportCode = input("Enter three letter code of UK airport\n")
    while UKairportCode != "LPL" and UKairportCode != "BOH":
      UKairportCode = input("Enter three letter code of UK airport\n")
      if UKairportCode != "LPL" and UKairportCode != "BOH":
        print('Error: UK airport code must be "LPL" or "BOH"\n')
    #OVERSEAS CODE
    nonUKairportCode = input("Enter three letter code of overseas airport\n")
    while nonUKairportCode == "LPL" and nonUKairportCode == "BOH":
      nonUKairportCode = input("Enter three letter code of overseas airport\n")
      if nonUKairportCode == "LPL" and nonUKairportCode == "BOH":
        print('Error: UK airport code must not be "LPL" or "BOH"\n')
    for i in range(len(airportCodes)):
      if nonUKairportCode == airportCodes[i]:
        print(airportNames[i])
        complete1 = 1
    if complete1 == 0:
      print("Overseas airport code does not match any in database")
  printMenu()
  if choice == 5:
    print("Quitting...")
    quit()

#MAIN
choice = printMenu()
executeChoice(choice)
