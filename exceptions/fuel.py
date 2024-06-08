def main():
    percentage = fuel_fraction("Fraction: ")

    print(evaluate(percentage))

def fuel_fraction(s):
    while True:
        try:
            X, Y = list(map(int, input(s).split("/")))

            if X > Y:
                continue
            
            return int(float(X / Y) * 100)
        except (ValueError, ZeroDivisionError):
            pass

def evaluate(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    return f"{percentage}%"

main()