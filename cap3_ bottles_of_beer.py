#criar uma função de uma canção que diminui uma garrafa de cerveja a cada verso

def bottle_verse(number):
    for i in range(number, 0 , -1):
        print(i, "bottles of beer on the wall")
        print(i, "bottles of beer")
        print("Take one down, pass it around")

bottle_verse(99)
