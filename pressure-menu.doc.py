#pressure calculator program

#this variable tells the loop whether it should loop or not.
# 1 means loop. anything else means don't loop.

loop = 1

#this variable holds the user's choice in the menu:

choice = 0

while loop == 1:
    #print what options you have
    print "Welcome to pressure calculator.py"
    print "14.7 PSI = 760 mmHg/Torr = 101.3 kPa = 1 atm"
    print "your options are:"
    print " "
    print "1) Enter PSI"
    print "2) Enter mmHg/Torr"

    print "3) Enter kPa"

    print "4) Enter atm (atmospheres)"
    print "5) Quit pressure calculator.py"
    print " "

    choice = input("Choose your option: ")
    if choice == 1:
        psi = input("Pressure in pounds per square inch  PSI: ")
 	print "Pressure in atmospheres"
	print psi/14.7     
        print "Pressure in mmHG or Torr"
	print (psi/14.7)*760
	print "Pressure in kPa"
	print (psi/14.7)*101.3
	print ""
    elif choice == 2:
        mmhg = input("Pressure in mmHg or Torr: ")
        print "Pressure in atmospheres"
	print mmhg/760.
	print "Pressure in PSI"
	print (mmhg/760.)*14.7
	print "Pressure in kPa"
	print (mmhg/760.)*101.3
        print ""
    elif choice == 3:
        kpa = input("Enter the pressure in kPa: ")
        print "Pressure in PSI"
	print (kpa/101.3)*14.7
	print "Pressure in atmospheres"
	print (kpa/101.3)
	print "Pressure in mmHg"
	print (kpa/101.3)*760
	print ""
    elif choice == 4:
        atm = input("Pressure in atmospheres: ")
        print "Pressure in PSI"
	print atm*14.7
	print "Pressure in mmHg"
	print atm*760.0
	print "Pressure in kPa"
	print atm*101.3
        print ""
    elif choice == 5:
        loop = 0
