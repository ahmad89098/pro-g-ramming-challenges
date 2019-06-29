# Pro/g/ramming Challenges
# 93: Wind Chill Calculator
# by ahmad89098
import math

v = int(input(("Enter wind velocity: )))
t = int(input("Enter the temperature: "))

wind_chill = 35.74 + (0.6215*t) - (35.75*math.pow(v,0.16)) + 0.4275*t*math.pow(v,0.16)
print(wind_chill)
