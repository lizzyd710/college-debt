import wbdata as wb
import pandas as p

# Temporary way of keeping track of the debt amount.
DEBT = 1.5 * 10 ** 12

if __name__ == '__main__':
    id = input("Enter indicator ID: ")
    indicator = wb.get_indicator(id)
