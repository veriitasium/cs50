def main():
    text = input("Input: ")
    print(shorten(text))

def shorten(text):
    text = text.strip()
    for c in text:
        match c.upper():
            case "A" | "E" | "I" | "O" | "U" :
                text = text.replace(c, "")

    return text

if __name__ == "__main__":
    main()