# Simple CRUD Inventory Laptop using Python (CLI Based)

laptops = []

def create_laptop():
    print("\n=== CREATE A LAPTOP DATA ===")
    code = input("Laptop Code: ")
    name = input("Laptop Name: ")
    stock = int(input("Stock: "))
    price = float(input("Price"))
    
    laptop = {
        "code": code,
        "name": name,
        "stock": stock,
        "price": price
    }
    
    laptops.append(laptop)
    print("Data berhasil ditambahkan!\n")
    
def read_laptops():
    print("\n=== DATA LAPTOP ===")
    if not laptops: 
        print("No Laptop data.\n")
        return 
    
    for i, laptop in enumerate(laptops, start=1):
        print(f"{i}. Code: {laptop['code']} | Name: {laptop['name']} | {laptop['stock']} | Price: {laptop['harga']} ")
    print()
    
def update_laptop(): 
    print("\n=== DELETE LAPTOP DATA ===")