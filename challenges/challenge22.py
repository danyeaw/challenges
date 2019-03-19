import re


def validate_phone_number(phone_number_list):
    valid = []
    for i in range(len(phone_number_list)):
        if re.match(r"^(313|248)\d{7}$", phone_number_list[i]):
            valid.append("YES")
        else:
            valid.append("NO")
    return valid


if __name__ == '__main__':
    n = int(input("Enter number of phone numbers: "))
    phone_number_list = []
    for number in range(n):
        entered_num = input("Phone number " + str(number + 1) + ": ")
        phone_number_list.append(entered_num)
    print(*validate_phone_number(phone_number_list), sep="\n")
