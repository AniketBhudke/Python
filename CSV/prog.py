# Writing: Use csv.writer() or csv.DictWriter() to write data to a CSV file.
#----------------------------------------------------------------------------------------
#csv.writer() 
# import csv 

# # Sample data
# data = [
#     ['Name', 'Age', 'City'],
#     ['Alice', 25, 'New York'],
#     ['Bob', 30, 'Los Angeles'],
#     ['Charlie', 35, 'Chicago']
# ]

# # Writing to CSV file
# with open('D:\\PYTHON BACKEND\\NUMPY\\CSV\\example.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(data)

# print("CSV file created successfully!")

#----------------------------------------------------------------------------------------
#csv.DictWriter()

# import csv

# # Sample data as dictionaries
# data = [
#     {'Name': 'Alice', 'Age': 25, 'City': 'New York'},
#     {'Name': 'Bob', 'Age': 30, 'City': 'Los Angeles'},
#     {'Name': 'Charlie', 'Age': 35, 'City': 'Chicago'}
# ]
# with open("D:\\PYTHON BACKEND\\NUMPY\\CSV\\dictwriter.csv","w",newline="")as fp:
#     filnames=["Name","Age","City"]
#     writer=csv.DictWriter(fp,fieldnames=filnames)
#     writer.writeheader()
#     writer.writerows(data)

    


# Reading: Use csv.reader() or csv.DictReader() to read data from a CSV file.
#----------------------------------------------------------------------------------------
#csv.reader()
# import csv

# # Reading from CSV file
# with open('D:\\PYTHON BACKEND\\NUMPY\\CSV\\dictwriter.csv', 'r') as file:
#     reader = csv.reader(file)
    
#     for row in reader:
#         print(row)
#----------------------------------------------------------------------------------------
#csv.DictReader()
# import csv

# # Reading from CSV file
# with open('D:\\PYTHON BACKEND\\NUMPY\\CSV\\dictwriter.csv', 'r') as file:
#     reader = csv.DictReader(file)
    
#     for row in reader:
#         print(row)
#----------------------------------------------------------------------------------------


# Writing to a CSV file: Use numpy.savetxt() to write a NumPy array to a CSV file.
import numpy as np

data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
np.savetxt('example111111.csv', data, delimiter=',', fmt='%d')
print("CSV file created successfully!")


# Reading from a CSV file: Use numpy.loadtxt() for simple CSV files or numpy.genfromtxt() for more complex CSV files with headers or missing data.

# import numpy as np

# # Reading the CSV file into a NumPy array
# data = np.loadtxt('example.csv', delimiter=',')

# print("Data read from the CSV file:")
# print(data)
#----------------------------------------------------------------------------------------
# Reading from a CSV file with headers: Use numpy.genfromtxt() with the delimiter and names
# import numpy as np
# import csv
# # Reading the CSV file with missing values (or headers)
# data = np.genfromtxt('D:\\PYTHON BACKEND\\NUMPY\\CSV\\dictwriter.csv', delimiter=',', skip_header=1,dtype=str)


# print("Data read from the CSV file with headers:")
# print(data)
