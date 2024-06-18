import random
import sys

def main():
    level = get_level()

    score = 0

    for i in range(0, 10):
            x, y = generate_integer(level), generate_integer(level)
            answer = x + y
            attempts = 3
            while attempts != 0:
                try:
                    equation = f"{x} + {y} = "
                    trial = int(input(equation))
                    if trial == answer:
                        break
                    else:
                        attempts -= 1
                        print(attempts)
                        if attempts == 0:
                            print(equation, answer, sep="")
                            score -= 1
                            break
                        raise ValueError
                except ValueError:
                    print("EEE")
            
            score += 1

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))

            match level:
                case 1 | 2 | 3: return level
                case _: continue
        except ValueError:
            print("EEE")


def generate_integer(level):
    match level:
        case 1: return random.randint(0, 10)
        case 2: return random.randint(10, 99)
        case 3: return random.randint(100, 999)
        case _: sys.exit()

if __name__ == "__main__":
    main()