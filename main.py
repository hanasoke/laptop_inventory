# Simple CRUD Inventory Laptop using Python (CLI Based)

laptops = []

def create_laptop():
    print("\n=== CREATE A LAPTOP DATA ===")
    code = input("Laptop Code: ")
    name = input("Laptop Name: ")
    stock = int(input("Stock: "))
    price = float(input("Price: "))
    
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
        print(f"{i}. Code: {laptop['code']} | Name: {laptop['name']} | {laptop['stock']} | Price: {laptop['price']} ")
    print()
    
def update_laptop(): 
    print("\n=== DELETE LAPTOP DATA ===")
    read_laptops()
    code = input("Input the updated laptop code: ")
    
    for laptop in laptops: 
        if laptop['code'] == code:
            print("Data has been found! Please Update.")
            laptop['name'] = input("New Name: ")
            laptop['stock'] = int(input("New Stock: "))
            laptop['price'] = float(input("New Price: "))
            print("New Data has been updated!\n")
            return 

    print("No New Data found!\n")
    
def delete_laptop():
    print("\n=== DELETE LAPTOP DATA ===")
    read_laptops()
    code = input("Enter the laptop code that will be removed: ")
    
    for laptop in laptops:
        if laptop['code'] == code: 
            laptops.remove(laptop)
            print("Data has been deleted!\n")
            return 
        
    print("No data found.\n")
    
def main_menu(): 
    while True: 
        print("=== LAPTOP INVENTORY MENU ===")
        print("1. Add New Laptop")
        print("2. Look The Data")
        print("3. Update Data")
        print("4. Delete Data")
        print("5. Exit")
        
        choice = input("Choice A Menu: ")
        
        if choice == '1':
            create_laptop()
        elif choice == '2':
            read_laptops()
        elif choice == '3':
            update_laptop()
        elif choice == '4':
            delete_laptop()
        elif choice == '5':
            print("Exit from Program...")
            break 
        else: 
            print("No Valid Choice!\n")
        
if __name__ == '__main__':
    main_menu()