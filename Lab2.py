WeightOnEarth = float(input("Enter an object's weight on Earth (in lbs):"))

# part 1-a
WeightOnTheMoon = (WeightOnEarth * 0.165)

# part 1-b
a = float(WeightOnTheMoon)
b = float(int(a))
UnderTheDecimalPoint = a - b
WeightOnTheMoon2 = float(int(UnderTheDecimalPoint * 16))

print("The object's weight on the moon is " + str(b) + " lbs " + str(WeightOnTheMoon2) + " oz")

# part 2-a
WeightOnTheMoon3 = round(WeightOnTheMoon / 2.2,3)

# part 2-b
d = float(int(WeightOnTheMoon3))
UnderTheDecimalPoint2 = WeightOnTheMoon3 - d
e = UnderTheDecimalPoint2 * 1000
WeightOnTheMoon4 = float(int(e))

print("The object's weight on the moon is " + str(d) + " kg " + str(WeightOnTheMoon4) + " g")

# part 3-a
import math

pythoid = 4 * math.sqrt(((WeightOnEarth) ** 2 - 13)/8 +22)

# part 3-b
f = float(pythoid)
g = float(int(f))
UnderTheDecimalPoint3 = f - g
WeightOnTheMoon5 = float(int(UnderTheDecimalPoint3 * 16))

print("The object's weight on planet Pythoid is " + str(g) + " lbs " + str(WeightOnTheMoon5) + " oz")
