vowel_text = input("Input: ")

for c in vowel_text:
    match c.upper():
        case "A" | "E" | "I" | "O" | "U" :
            vowel_text = vowel_text.replace(c, "")

print(vowel_text)