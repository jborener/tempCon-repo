#!/usr/bin/env python3
import sys
sys.path.append('./modules')
import temperature as temp

def main():
	again = 'y'
	while again.lower()=='y':
        	print("\n\nMENU\n1. Fahrenheit to Celsius\n2. Celsius to Fahreheit\n")
        	sel = int(input("Enter a menu option: "))

        	if sel == 1:
                	fah = float(input('Enter degrees Fahrenheit: '))
                	print('Degrees Celsius: ',temp.toCelsius(fah))
        	elif sel == 2:
                	cel = float(input('Enter degrees Celsius: '))
                	print('Degrees Fahrenheit: ',temp.toFahrenheit(cel))
        	else:
                	print('Invalid Menu Selection! ')
        	again=input('\nConvert another temperature? (y/n): ')

if __name__ == "__main__":
	main()

