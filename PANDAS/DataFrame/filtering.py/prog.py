import pandas as pd
data = {
    'htno': list(range(101, 121)),  # Roll numbers from 101 to 120
    'name': ['Aniket', 'John', 'Sara', 'Rahul', 'Priya', 'Vivek', 'Rani', 'Amit', 'Rohit', 'Pooja',
             'Kiran', 'Neha', 'Arjun', 'Sneha', 'Vikas', 'Raj', 'Meena', 'Harish', 'Nisha', 'Vijay'],
    'telugu': [50, 90, 78, 88, 92, 79, 65, 80, 91, 76, 88, 92, 81, 90, 75, 87, 93, 78, 89, 86],
    'english': [82, 92, 80, 85, 91, 67, 76, 83, 88, 79, 90, 95, 82, 93, 76, 89, 87, 84, 90, 88],
    'hindi': [78, 89, 82, 84, 93, 67, 80, 45, 90, 81, 91, 86, 83, 88, 78, 92, 89, 82, 87, 85],
    'maths': [95, 98, 80, 70, 97, 80, 92, 91, 89, 77, 95, 96, 82, 94, 83, 99, 93, 89, 85, 92],
    'science': [92, 85, 90, 87, 96, 81, 63, 86, 91, 78, 92, 88, 89, 95, 80, 90, 94, 83, 88, 91],
    'social': [91, 86, 84, 90, 79, 82, 47, 85, 93, 81, 86, 91, 84, 92, 79, 88, 90, 86, 85, 87],
}
df = pd.DataFrame(data)

df['total']=df['telugu']+df['english']+df['hindi']+df['maths']+df['science']+df['social']
print(df)
print("-------------------------------------")
#add and cal percentage 
df['percentage']=round((df['total']/600)*100,2)
print(df)
print("-------------------------------------")
print(df['percentage'].max())
print("-------------------------------------")

#filtering

print(df[df['english']>90])
print("-------------------------------------")

print(df.loc[df['maths']>=90])
print("-------------------------------------")

print(df[(df["maths"]>=80) & (df['maths']<=90)][["name","maths"]])
print("-------------------------------------")

print(df.loc[(df["maths"]>=80) & (df['maths']<=90)][["name","maths"]])
print("-------------------------------------")

print(df[(df["total"]>=510) & (df['total']<=550)][['name','total']])
print("-------------------------------------")

print(df[(df["total"]>=510) & (df['total']<=550)][['name','total']].size)
print("-------------------------------------")

print(df.loc[df["percentage"]>=84])
print("-------------------------------------")

a=df.loc[df["percentage"]>=84,["grade"]]="distinction"
print(a)
print(df["grade"])
print("-------------------------------------")
df.loc[((df["percentage"]>=65)& (df["percentage"]<84)),["grade"]]="first"

print(df["grade"])
print("-------------------------------------")
# print(df[df["grade"]=="distinction".upper()].shape[0])
df.loc[((df["percentage"]>=60)&(df['percentage']<65)),["grade"]]="SECOND"
print(df[["grade","percentage"]])
print("-------------------------------------")

print(df.loc[df["percentage"].max()==df["percentage"]])

print(df.loc[df["percentage"].max()==df["percentage"],["name"]])