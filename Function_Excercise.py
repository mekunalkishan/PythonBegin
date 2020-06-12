ex_celcius = input("Enter the temprature to be convereted from Celcius to Farenhite")

ex_cel_int = int(ex_celcius)
def ConvertToFarenhite():
    return 1.8 * ex_cel_int + 32
print(ConvertToFarenhite())
print("The farenhite converted is " +str(ConvertToFarenhite()))

