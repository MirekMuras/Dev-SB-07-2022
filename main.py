import pandas as pd

import test1
#from playground1 import d1

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    # Use a breakpoint in the code line below to debug your script.
    # df = test1.dummy_data()
    # df.to_csv('./playground1/data/data_1.csv', index=False)

    new_df = pd.read_csv('./playground1/data/data_1.csv')
    #test = d1.handling_missing_data(new_df)
    print(new_df)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
