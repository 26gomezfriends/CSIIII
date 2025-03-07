import csv

# Set up variables for the best seller
max_sales = 0.0
best_book = None

# Open the CSV file and read the data
with open('Bestseller - Sheet1.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)  # get the header row
    title_index = header.index('Title')
    sales_index = header.index('Sales in millions')
    
    # Find the book with the highest sales
    for row in reader:
        try:
            sales = float(row[sales_index])
        except ValueError:
            continue
        if sales > max_sales:
            max_sales = sales
            best_book = row

# Write the best seller's info to a new CSV file
with open('bestseller_info.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Sales in millions'])
    writer.writerow([best_book[title_index], best_book[sales_index]])

print("Best-selling book:", best_book[title_index])
print("Sales (in millions):", best_book[sales_index])
