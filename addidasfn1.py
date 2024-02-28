import matplotlib.pyplot as plt
import pandas as pd

print("1. Select file using the file location/file path or filename")
print("2. If file path is used, use single backslashes")
print('3. If its filename, drop your file in the folder that contains this script')
print('4. Ensure file name, file path and extension are properly written')

file1 = input()
while not file1:
    print("File path cannot be empty")
    print("\n")
    file1=input()

print("\n")
df = pd.read_excel(file1)


def operation():
    print("Please select operation to perform")
    print("1. Quick Summary")#this will have to include both default en customised percentiles
    print("2. Print whole Data")
    print("3. Finding Blanks")
    print("4. Plotting graph")
    print("5. Filtering Data")
    print('6. Data Structure')
    print('7. Grouping Data')
    print('8. Maximum Value')
    print('9. Minimum Value')
    print("*. Quit")
    
    return input("Enter Numeric choice: ")

def graph():# 
    print("Specify the \"x\" and \"y\" columns")
    print("Enter \"x\" axis column name")
    x = input()
    print("\n")
    print("Enter \"y\" axis column name")
    y = input()
    print("\n")
    print("Specify type of graph")
    chart_type = input()

    if x in df.columns and y in df.columns:
        if chart_type=="line":
            df[x] = df[x].astype(str)
            plt.plot(df[x], df[y])
            plt.show()
        elif chart_type=="bar":
            df[x] = df[x].astype(str)
            plt.bar(df[x],df[y])
            plt.show()
        else:
            print("Enter corect values")

def filter_data():
    print("Please specify column name for the data to be filtered")
    column_name = input("Please enter column name: ")
    print("Specify Data name in the column")
    data_name = input("Please enter specific item name: ")
    if column_name in df.columns:
        filtered_data = df[df[column_name]==data_name]
        print(filtered_data)
    else:
        print("Invalid Column name")
    

def max_value():
    print("Enter column name to consider")
    col_name = input()
    max_value_1 = df.loc[df[col_name].idxmax()]
    print(max_value_1)

def min_value():
    print("Enter column name to consider")
    col_name1 = input()
    min_value_2 = df.loc[df[col_name1].idxmin()]
    print(min_value_2)

#The Main loop
while True:
    operation_input = operation()
    if operation_input =="*":
        break
    elif operation_input in ("1","2","3","4","6","7","8"):
        if operation_input =="1":
            print("We are now getting a quick summary of the data")
            print(df.describe())
        elif operation_input =="2":
            print("This is your data")
            print(df)
        elif operation_input =="3":
            print("Summary of the blanks")
            print(df.isnull().sum())
        elif operation_input =="4":
            graph()
        elif operation_input =="5":
            filter_data()
        elif operation_input =="6":
            print(df.info())
        elif operation_input=="7":
            pass
        elif operation_input =="8":
            max_value()
        elif operation_input == "9":
            min_value()
        else:
            print("Enter correct values")


    
            


    
