INCOMPLETE

def review(d):
    for k in sorted(d.keys()):
        print(d[k], k)


def main():
    grocery_list = { }
    while True:
        try:
            item = input().strip().lower()
            
            if item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1

        except EOFError:
            break
            
    review(grocery_list)

main()