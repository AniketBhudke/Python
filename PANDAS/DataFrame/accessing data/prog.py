import pandas as pd

# Create a DataFrame with 20 rows of sample data
data = {
    'htno': list(range(101, 121)),  # Roll numbers from 101 to 120
    'name': ['Aniket', 'John', 'Sara', 'Rahul', 'Priya', 'Vivek', 'Rani', 'Amit', 'Rohit', 'Pooja',
             'Kiran', 'Neha', 'Arjun', 'Sneha', 'Vikas', 'Raj', 'Meena', 'Harish', 'Nisha', 'Vijay'],
    'telugu': [85, 90, 78, 88, 92, 79, 85, 80, 91, 76, 88, 92, 81, 90, 75, 87, 93, 78, 89, 86],
    'english': [88, 92, 80, 85, 91, 77, 86, 83, 88, 79, 90, 95, 82, 93, 76, 89, 87, 84, 90, 88],
    'hindi': [87, 89, 82, 84, 93, 75, 80, 85, 90, 81, 91, 86, 83, 88, 78, 92, 89, 82, 87, 85],
    'maths': [95, 98, 88, 93, 97, 80, 92, 91, 89, 77, 95, 96, 82, 94, 83, 99, 93, 89, 85, 92],
    'science': [92, 85, 90, 87, 96, 81, 83, 86, 91, 78, 92, 88, 89, 95, 80, 90, 94, 83, 88, 91],
    'social': [91, 86, 84, 90, 89, 82, 87, 85, 93, 81, 86, 91, 84, 92, 79, 88, 90, 86, 85, 87],
}
df = pd.DataFrame(data)
print(df)
print("-----------------------------------")

for rec in df.iterrows():
    print(rec)
print("-----------------------------------")
print(df[4:10])    
print("-----------------------------------")
print(df[::2])
print("-----------------------------------")
print(df[4:10:-1])
print("-----------------------------------")
print(df[["name","htno"]])