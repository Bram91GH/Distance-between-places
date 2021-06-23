import math
import pandas as pd

# RADIUS EARTH
re = 6371

# CSV FILE WITH COORDINATES LAT, LON
df = pd.read_csv('countries.csv')

# INPUT COUNTRY TO GET LATITUDE AND LONGITUDE
input_country_1 = input('select your country: ')

x1 = df[df['name'] == input_country_1]['longitude']
y1 = df[df['name'] == input_country_1]['latitude']

# INPUT SECOND COUNTRY TO GET LATITUDE AND LONGITUDE
input_country_2 = input('select another country: ')

x2 = df[df['name'] == input_country_2]['longitude']
y2 = df[df['name'] == input_country_2]['latitude']

# Check coordinates and calculate the longitude difference between x1 and x2,
# implement in the haversine formula (longitude_difference)

if (float(x1) > 0 and float(x2) > 0):
    if(float(x1) > float(x2)):
        longitude_difference = float(x1) - float(x2)
    else:
        longitude_difference = float(x2) - float(x1)

elif (float(x1) < 0 and float(x2) < 0):
    if(float(x1) > float(x2)):
        longitude_difference = math.fabs(x1) - math.fabs(x2)
    else:
        longitude_difference = math.fabs(x2) - math.fabs(x1)

elif (float(x1) < 0 and float(x2) > 0):
    longitude_difference = math.fabs(x1) + float(x2)

else:
    longitude_difference = float(x1) + math.fabs(x2)


# x and y coordinates place 1 (radians)
x1 = math.radians(x1)
y1 = math.radians(y1)

# x and y coordinates place 2 (radians)
x2 = math.radians(x2)
y2 = math.radians(y2)

# LONGITUDE DIFFERENCE BETWEEN X1 X2
long_rad = math.radians(longitude_difference)

# FORMULA CENTRAL SUBTENDED ANGLE (HAVERSINE FORMULA)
haversine = math.acos(math.sin(y1)*math.sin(y2)+math.cos(y1)
                      * math.cos(y2)*math.cos(long_rad))

# HAVERSINE(RADIANS) TO DEGREES
deg = math.degrees(haversine)

# PI SQUARED X RE(RADIUS EARTH) X DEG(HAVERSINE DEGREES) : 360
outcome = math.tau * re * deg / 360

# OUTCOME IN DISTANCE BETWEEN TWO PLACES
print('The distance between ', input_country_1,
      ' and', input_country_2, ' is: ', outcome)
