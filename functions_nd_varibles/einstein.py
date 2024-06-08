def square(n):
    return n * n

mass = int(input("m: "))
# c - speed of light
speed = 300000000

# E = mc^2
energy = mass * pow(speed, 2)
print(f"E: {energy}")