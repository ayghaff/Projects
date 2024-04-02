

unit = input("What unit are you going to input? (F)ahrenheit, (C)elsius, (K)elvin: ").lower()

if unit == "f":
    conversion_unit = input("What would you like to convert it to? (C)elsius, (K)elvin: ").lower()
    if conversion_unit == "c":
        temperature_input = input("Insert the temperature in the unit you chose at the beginning of the script: ")
        converted_temperature = (float(temperature_input) - 32) * 5/9
        print(str(converted_temperature) + "°C")
    elif conversion_unit == "k":
        temperature_input = input("Insert the temperature in the unit you chose at the beginning of the script: ")
        converted_temperature = (float(temperature_input) - 32) * 5 / 9 + 273.15
        print(str(converted_temperature) + "°K")

elif unit == "c":
    conversion_unit = input("What would you like to convert it to? (F)ahrenheit, (K)elvin: ").lower()
    if conversion_unit == "f":
        temperature_input = input("Insert the temperature in the unit you chose at the beginning of the script: ")
        converted_temperature = (float(temperature_input) * 9/5) + 32
        print(str(converted_temperature) + "°F")
    elif conversion_unit == "k":
        temperature_input = input("Insert the temperature in the unit you chose at the beginning of the script: ")
        converted_temperature = (float(temperature_input) + 273.15)
        print(str(converted_temperature) + "°K")

elif unit == "k":
    conversion_unit = input("What would you like to convert it to? (F)ahrenheit, (C)elsius: ").lower()
    if conversion_unit == "f":
        temperature_input = input("Insert the temperature in the unit you chose at the beginning of the script: ")
        converted_temperature: float = (float(temperature_input) - 273.15) * 9 / 5 + 32
        print(converted_temperature, "°F")
    elif conversion_unit == "c":
        temperature_input = input("Insert the temperature in the unit you chose at the beginning of the script: ")
        converted_temperature = (float(temperature_input) - 273.15)
        print((converted_temperature, "°C"))
