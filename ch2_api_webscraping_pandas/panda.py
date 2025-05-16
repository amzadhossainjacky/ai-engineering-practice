import pandas as pd

#step 1: create data list
data = [
    {
        "name": "Malek", "age": 29, "salary": 23000
    },
    {
        "name": None, "age": 26, "salary": 15000
    },
    {
        "name": "Jahid", "age": None, "salary": 21000
    },
    {
        "name": "Khalid", "age": 27, "salary": 42000
    }
]

#step 2: create a data frame

# df = pd.DataFrame(data)
# print(df)

#save csv

# save_csv = df.to_csv('people_data.csv', index=False)
# print("csv file save")

#read csv
df = pd.read_csv('people_data.csv')
# print(df)

#is null check

# print(df.isnull())
# print(df.isnull().sum())

#duplicate value remove

# df = df.drop_duplicates(inplace=True)
# print(df)

#remove row of any missing value
# df.dropna(inplace=True)
# print(df)


#NaN replace with 0
df.fillna(0, inplace=True)
print(df) 


