import csv

data = [
  ['Item', 'Quantity'],
  ['Blender', 2],
  ['Posters', 30],
  ['Shoes', 2]
]

try:
    # Try to open the file and read its contents
    with open('packing_list.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
except FileNotFoundError:
    # If the file doesn't exist, create it with the data
    print("Packing list file not found. Creating a new one.")
    with open('packing_list.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

