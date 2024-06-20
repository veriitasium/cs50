import sys

def main():
    fraction = input("Fraction: ")
    print(convert(fraction))

def convert(s):
    try:
        X, Y = list(map(int, s.split('/')))
        if X > Y:
            sys.exit("Incorrect sets of ")
        
        return gauge(X, Y)
    except (ValueError, ZeroDivisionError):
        sys.exit("Either value is not an integer or zero is in denominator")

def gauge(X, Y):
    return evaluate(int(float(X / Y) * 100))

def evaluate(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    return f"{percentage}%"

if __name__ == "__main__":
    main()