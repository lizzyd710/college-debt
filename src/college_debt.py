import wbdata as wb
import pandas as p

# Temporary way of keeping track of the debt amount.
DEBT = 1.5 * 10 ** 12

if __name__ == '__main__':
    id = input("Enter ID for an indicator using current US dollars: ")
    indicator = wb.get_indicator(id)
    if "current US$" in str(indicator[0].get("name")):
        df = wb.get_dataframe(indicator)
        df.head()
    else:
        print("Indicator is not in proper units of current US dollars.")
