inport math
# Input the diameter of the circle
diameter = float(input("Enter the diameter of the circle: "))

# Calculate the radius (r) from the diameter
radius = diameter / 2

# Calculate the area
area = math.pi * (radius ** 2)

# Calculate the circumference
circumference = math.pi * diameter

# Print the results
print(f"Area of the circle: {area:.2f}")
print(f"Circumference of the circle: {circumference:.2f}")
