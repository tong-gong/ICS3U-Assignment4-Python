#!/usr/bin/env python3

# Created by Tong Gong
# Created time November 2020
# This is a program tells you number of days in a month.


def main():
    # This is the function tells you number of days in a month

    # Input
    user_input_month = input("Enter the month you want check in number 1-12:")
    print("")

    # Process & output
    try:
        user_input_month = int(user_input_month)
        if 0 < user_input_month <= 12:
            if user_input_month == 1:
                print("31 days in January")
            elif user_input_month == 2:
                input_year = input("Enter the year you want check:")
                print("")
                input_year = int(input_year)
                if input_year % 4 != 0:
                    print("28 days in {}'s February".format(input_year))
                else:
                    if input_year % 100 != 0:
                        print("29 days in {}'s February".format(input_year))
                    else:
                        if input_year % 400 != 0:
                            print("28 days in {}'s February"
                                  .format(input_year))
                        else:
                            print("29 days in {}'s February".
                                  format(input_year))
            elif user_input_month == 3:
                print("31 days in March")
            elif user_input_month == 4:
                print("30 days in April")
            elif user_input_month == 5:
                print("31 days in May")
            elif user_input_month == 6:
                print("30 days in June")
            elif user_input_month == 7:
                print("31 days in July")
            elif user_input_month == 8:
                print("31 days in August")
            elif user_input_month == 9:
                print("30 days in September")
            elif user_input_month == 10:
                print("31 days in october")
            elif user_input_month == 11:
                print("30 days in November")
            elif user_input_month == 12:
                print("31 days in December")
        elif user_input_month < 0:
            print("Sorry, you did not enter a positive integer")
        elif user_input_month > 12:
            print("Sorry, your input number is too big!")
    except Exception:
        print("You are not enter a number between 1-12")


if __name__ == "__main__":
    main()
