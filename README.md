# Distance-between-places

**Version 1.0.0**

this python script calculates the distance between two countries based on input

---

## Formula
This script creates a straigt line on the spherical surface of the earth from your two given inputs. 
We use the harvine formula to calculate this distance from point A to point B. The script takes the central latitude and longitude coordinates from a country and uses those to implement in the haversine formula. Since haversine implies the earth is a perfect sphere (which is not the case), the outcomes of this script have an accuracy of 98.5%.

After our inputs the script checks what the assigned coordinates are, calculates the longitude difference between the two given countries and uses longitude difference in the haversine formula.

after succesfully getting the outcome in radians from the haversine formula



## Notes:

since the python math operaters used in this script are calculated with radians we have to convert degrees to radians first and later convert them back to get the right outcome.

the outcome is in kilometers by default. if you want the outcome in miles simply multiply the amount of kilometers by 0.6214




---

## Sources used

with the help of this video about great circle distance I was able to learn how the math behind this project works:
https://www.youtube.com/watch?v=634GucAdzzA&ab_channel=SpaceflightScience

documentation python math operaters used in this project:
https://docs.python.org/3/library/math.html


