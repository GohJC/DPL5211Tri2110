#student ID: 1201201564
#student Name: Goh Jia Chen

import math

radius = float(input("Enter the radius : "))
volume = ((4/3) * math.pi * math.pow(radius,3))
surface = (4 * math.pi * math.pow(radius,2))

print("\nVolume of the sphere is : {:.2f}".format(volume))
print("\nSurface of the sphere is : {:.2f}".format(surface))