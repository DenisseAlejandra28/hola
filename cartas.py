import random
cartas = ["jack", "queen", "king"]

def main():
    random.seed(0)
    print(random.choices(cartas, weights=[70, 20, 10] ,k=2))

main()