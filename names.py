def writenames():
    with open('text.txt', '+w') as file:
        names = ["Norton, Eduard", "Bonham, Helena", "Pitt, Brat", "Meatloaf"]
        for name in names:
            file.write(name + "\n")

def readnames():
    with open('text.txt', 'r') as file:
        names = file.readlines()
        return names

