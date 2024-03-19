import csv

x = dict()
header=["name","number","email","address"]

# Load the CSV data into the dictionary
with open('test.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for i, row in enumerate(csv_reader):
        if i == 0:
            header = row
        else:
            x[row[0]] = row[1:]

print(header)

# Write the dictionary back to the CSV file
def write_to_csv():
    with open('test.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)  # Write the header
        for key, value in x.items():
            writer.writerow([key] + value)  # Write the rest of the data

while True:
    try: 
        print("1. Add")
        print("2. Update")
        print("3. Search")
        print("4. Delete")
        print("5. Exit")
        ch = int(input("Enter your input: "))
        if ch == 1:
            name = input("Enter your name: ")
            if name.isalpha():
                if name not in x:
                    number1 = input("Enter your number: ")
                    email1 = input("Enter your email: ")
                    address1 = input("Enter your address: ")
                    x[name] = [number1, email1, address1]
                    write_to_csv()
                    print("Added successfully.")
                else:
                    print("This name already used, please choose a new name")
            else:
                print("Please enter a correct string")
        elif ch == 2:
            name = input("Enter the name to update: ")
            if name in x:
                number1 = input("Enter your number: ")
                email1 = input("Enter your email: ")
                address1 = input("Enter your address: ")
                x[name] = [number1, email1, address1]
                write_to_csv()
                print("Updated successfully.")
            else:
                print("Name not found.")
        elif ch == 3:
            name = input("Enter the name to search: ")
            if name in x:
                print("Found:", [name] + x[name])
            else:
                print("Name not found.")
        elif ch == 4:
            name = input("Enter the name to delete: ")
            if name in x:
                del x[name]
                write_to_csv()
                print("Deleted successfully.")
            else:
                print("Name not found.")
        elif ch == 5:
            print("Exiting.")
            break
        else:
            print("Invalid input, please try again.")
    except ValueError:
        print("Please enter a number.")
