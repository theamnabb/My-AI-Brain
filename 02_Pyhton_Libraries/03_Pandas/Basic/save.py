import pandas as pd

#  Data from dataFrame

data = {
    'Name:': ['Ali', 'Sara', 'Amna'],
    'Age:': [22, 21, 23],
    'Marks:': [85, 90, 88],
    'City:': ['Karachi', 'Lahore', 'Islamabad'],
    'Country:': ['Pakistan', 'Pakistan', 'Pakistan'],
    'Gender:':['Male', 'Female', "female"]
}

df = pd.DataFrame(data)
print(df)

# Save this in cvs 

# df.to_csv('output.csv', index=False) 
# df.to_excel('output.xlsx', index=False) 
df.to_json('output.json', index=False) 
