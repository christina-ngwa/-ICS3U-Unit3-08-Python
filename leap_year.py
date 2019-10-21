#!/usr/bin/env python3

# Created by: Christina Ngwa
# Created on: October 2019
# This program uses a nested if statement


def main():
    # this function uses a nested if statement

    # output
    print("Is the year a leap year? Find out.")
    print("")

    # input
    year = int(input("Enter a year: "))
    print("")

    # process
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("It is a leap year.")
            else:
                print("It is not a leap year.")
        else:
            print("It is not a leap year.")
    else:
        print("It is not a leap year.")


if __name__ == "__main__":
    main()
