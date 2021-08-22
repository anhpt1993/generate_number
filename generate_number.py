# generate numbers according to the rules

def input_data():
    while True:
        try:
            num = int(input("Enter an integer greater than or equal to 0: "))
            if num >= 0:
                return num
                break
            else:
                print("Wrong input. Try again please")
                print()
        except ValueError:
            print("Input value shall be an integer, not decimal or string")
            print()

def generate(number):
    my_string = "0123456789"
    convert_number = str(number)
    result = ""
    for i in range(len(convert_number)):
        my_string = my_string.replace(convert_number[i],"")

    #print(my_string)
    for i in range(len(my_string)):
        if my_string[i] > convert_number:
            result = my_string[i] + my_string[0] * (len(convert_number) - 1)
            break
    else:
        if my_string[0] != "0":
            result = my_string[0] * (len(convert_number) + 1)
        else:
            result = my_string[1] + my_string[0] * len(convert_number)

    return result

def again():
    print()
    answer = input("Do you want to play again? (Y/N): ").upper().strip()
    if answer == "Y" or answer == "YES":
        return True
    else:
        print("Bye! See you next time!!!")
        exit()

if __name__ == '__main__':
    while True:
        print("Please enter the index of the number that you want to display")
        index = input_data()
        count = 0
        string = ""
        while True:
            print(f"{generate(string)}", end = " ")
            string = generate(string)
            if count == index:
                break
            else:
                count = count + 1
        print("\n----------------------------------\n")
        again()