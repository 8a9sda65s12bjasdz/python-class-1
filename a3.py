#forgot comments
import sys
print("Alex's Temperature Converter:\n")

fT = float(input("What is the temperature? "))
sCF = input("Was the temperature that was entered F or f for Fahrenheit or C or c for Celcius? ")
if sCF == "F" or sCF == "f":
    if fT > 212:
         print("Temp can not be > 212")
    else:
        fCelsius = (5.0/9)*(fT-32)
        print(f"The temperature in Celcius is {fCelsius:.1f}") 
elif sCF == "C" or sCF == "c":
    if fT > 100:
        print("Temp can not be > 100")
    else:
        fFahrenheit = ((9.0/5.0)*fT)+32
        print(f"The temperature in Fahrenheit is {fFahrenheit:.1f}")
else:
    print("Enter a F or C")
    sys.exit()
