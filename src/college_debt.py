import wbdata as wb
import pandas as p

# Temporary way of keeping track of the debt amount.
DEBT = 1.5 * 10 ** 12

if __name__ == '__main__':
    id = input("Enter ID for an indicator using current US dollars: ")
    indicator = wb.get_indicator(id)
    print("Checking unit compatibility...")
    if "current US$" in str(indicator[0].get("name")):
        print("Indicator is in proper units of current US dollars. Continuing.")
        series = p.Series()
        series = wb.get_data(id, pandas=True)
    else:
        print("Indicator is not in proper units of current US dollars.")