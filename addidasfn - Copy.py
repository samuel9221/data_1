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
    print("*. Quit")
    
    return input("Enter Numeric choice: ")

def graph():# i stopped here trying to begin graphs function
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
            plt.plot(df[x], df[y])
            plt.show()
        elif chart_type=="bar":
            plt.bar(df[x],df[y])
            plt.show()
        pass

    
    

while True:
    operation_input = operation()
    if operation_input =="*":
        break
    elif operation_input in ("1","2","3","4","6","7"):
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
            pass
        elif operation_input =="6":
            print(df.info())
        elif operation_input=="7":
            pass
            


    
