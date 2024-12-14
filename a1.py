#surface gravity factor
n_Mercury = 0.38
n_Venus = 0.91
n_Moon = 0.165
n_Mars = 0.38
n_Jupiter = 2.34
n_Saturn = 0.93
n_Uranus = 0.92
n_Neptune = 1.12
n_Pluto = 0.066

#user: alex
#earth weight: 170

#name input
s_name = input("What is your name? ")
#earth weight input, with str to float conversion
n_earth_weight = float(input("What is your earth weight? "))
#formatted print statement outputting name and earth weight
print(f"Hello {s_name} your weight is {n_earth_weight:.2f} lbs.")
#formatted print state outputting name and following string
print(f"{s_name} here are your weights on our Solar Systems planet's:")
#multiple formatted print statements documenting the planet's surface gravity factor + your earth weight = weight on specified planet
print(f"Weight on Mercury: {n_Mercury * n_earth_weight:10.2f} lbs.")
print(f"Weight on Venus:   {n_Venus * n_earth_weight:10.2f} lbs.")
print(f"Weight on Moon:    {n_Moon * n_earth_weight:10.2f} lbs.")
print(f"Weight on Mars:    {n_Mars * n_earth_weight:10.2f} lbs.")
print(f"Weight on Jupiter: {n_Jupiter * n_earth_weight:10.2f} lbs.")
print(f"Weight on Saturn:  {n_Saturn * n_earth_weight:10.2f} lbs.")
print(f"Weight on Uranus:  {n_Uranus * n_earth_weight:10.2f} lbs.")
print(f"Weight on Neptune: {n_Neptune * n_earth_weight:10.2f} lbs.")
print(f"Weight on Pluto:   {n_Pluto * n_earth_weight:10.2f} lbs.")