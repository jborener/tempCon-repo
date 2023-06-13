
def toCelsius(fah):
        cel = (fah - 32) * 5/9
        return cel

def toFahrenheit(cel):
        fah = cel * 9/5 + 32
        return fah

def main():
        for temp in range(32,212+30,30):
                print(temp,'degrees Fahrenheit =',
                      round(toCelsius(temp)),'Celsius')

        for temp in range(0,100+20,20):
                print(temp,'degrees Celsius =',
                      round(toFahrenheit(temp)),'Fahrenheit')

if __name__ == '__main__':
	main()
