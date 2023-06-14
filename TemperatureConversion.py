#!/usr/bin/env python3
import sys
sys.path.append('./modules')
import temperature as temp

def main():
        again = 'y'
        while again.lower()=='y':
                print("\n\nMENU\n1. Fahrenheit to Celsius and Kelvin\n2. Celsius to Fahreheit and Kelvin\n")
                sel = int(input("Enter a menu option: "))

                if sel == 1:
                        fah = float(input('Enter degrees Fahrenheit: '))
                        cel,kel = temp.toCelsius(fah)
                        print('Degrees Celsius: ',cel)
                        print('Degrees Kelvin: ',kel)
                elif sel == 2:
                        cel = float(input('Enter degrees Celsius: '))
                        fah,kel = temp.toFahrenheit(cel)
                        print('Degrees Fahrenheit: ',fah)
                        print('Degrees Kelvin: ',kel)
                else:
                        print('Invalid Menu Selection! ')
                again=input('\nConvert another temperature? (y/n): ')

if __name__ == "__main__":
        main()

