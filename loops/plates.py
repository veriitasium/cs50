def main():
    plate = input("Plate: ")
    plate.__len__()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
    
def is_valid(s):

    # checks whether the length of a given input is between 2 and 6
    if 2 <= len(s) <= 6 and chars_check(s):

        # identfies first two characters of an input as letters
        if not s[0].isnumeric() and not s[1].isnumeric():

            """
                while enumerating (characters) through a given input (string), needless to say,
                to make sure first digit is not '0' we need to mechanically tell it to the computer.
            """
            first_not_zero = True

            # since we checked first two letters and don't need double iterate, simply start w/ index 2. 
            for i in s[2:]:
                if i.isnumeric():

                    # here, to prevent first digit in an input from number '0'
                    # we inserted a checkup in case '0' comes as a first number
                    if i == '0' and first_not_zero:
                        return False
                    
                    # in case first number is not zero we explicitly tell it to program by
                    # assigning first_non_zero a False value
                    # purposefully stating, because first number is not '0',
                    # there is no need to check whether '0' comes in the rest part
                    first_not_zero = False

                    # if all previous conditions are satisfied and first number isn't a '0'
                    # then last step (checking whether the rest of an input is digit) 
                    if not s[s.index(i):].isnumeric():
                        return False
                    continue
            return True
    return False
                      
def chars_check(s):
    """ 
        return (not s.__contains__(" ")) and (not s.__contains__(".")) and (not s.__contains__(","))
    """
    return " " not in s and "." not in s and "," not in s

if __name__ == "__main__":
    main()