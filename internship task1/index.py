

cart = []


while True:
    
    print(" SHOPPING CART SYSTEM ")
    
    print("1. Add Product\n2. View All Products\n3. Search Product by Id\n4. Update Product\n5. Delete Product\n6. Place Order\n7. Exit")
    
    
    choice = input("\nEnter your choice (1-7): ")

#   Adding Products
    if choice == '1':
        try:
            product_id = int(input("Enter Product ID: "))
            
            # Checking if id already exists in the cart
            duplicate = False
            for item in cart:
                if item['id'] == product_id:
                    duplicate = True
                    break
            
            if duplicate:
                print("Error : A product with this ID already exists ")
            else:
                # Collecting product details
                product_name = input("Enter Product Name : ")
                product_price = float(input("Enter Product Price : "))
                product_quantity = int(input("Enter Product Quantity : "))
                
                # Creating dictionary and storing in list
                product = {
                    "id": product_id,
                    "name": product_name,
                    "price": product_price,
                    "quantity": product_quantity
                }
                cart.append(product)

                print(f"Successfully : '{product_name}' added to cart")
                
        except ValueError:
            print("Invalid input!   ID, Price, and Quantity must be numbers")

    # Viewing all products and calculating bills
    elif choice == '2':
        if not cart:
            print("\nYour cart is currently empty.")
        else:
            total_bill = 0
            print("Current Cart")
            for item in cart:
                # Calculate individual bill for each item

                individual_bill = item["price"] * item["quantity"]

                # calculating total bill
                total_bill = total_bill + individual_bill

                print(f"ID : {item['id']} | Name : {item['name']} | Price : {item['price']} | Quantity : {item['quantity']} | Individual bill : {individual_bill}")
            
            
            print(f"Total Bill : {total_bill}")

    # Searching by product ID
    elif choice == '3':
        if not cart:
            print("\nCart is empty. Nothing to search.")
        else:
            while True:
                try:
                    search_id = int(input("Enter ID to search : "))
                    found = False
                    for item in cart:
                        if item['id'] == search_id:
                            print(f"\nProduct Found : {item}")
                            found = True
                            break
                    
                    
                    if found:        # Exiting inner loop if found
                        break
                    else:           # retrying
                        print("ID not found.")
                        retry = input("Press 1 to try again | 2 for Main Menu : ")
                        if retry == '2':
                            break
                except ValueError:
                    print("Please enter a valid Id")

    
    elif choice == '4':  #updating a product
        if not cart:
            print("\nCart is empty , Nothing to update.")
        else:
            while True:
                try:
                    target_id = int(input("Enter product ID to update : "))
                    found = False
                    for item in cart:

                        if item['id'] == target_id:

                            print(f"Updating : {item['name']}")

                            # now overwrite existing dictionary values
                            item["price"] = float(input("Enter new price : "))

                            item["quantity"] = int(input("Enter new quantity : "))

                            print("Update successful!")
                            found = True
                            break
                    
                    if found:
                        break
                    else:
                        print("ID not found")
                        retry = input("Press 1 to try again | 2 for Main Menu : ")
                        if retry == '2':
                            break
                except ValueError:
                    print("Invalid input  Use numbers for ID, Price, and Quantity")

    
    elif choice == '5':    # deleting product
        if not cart:
            print("\nCart is empty. Nothing to delete")
        else:
            while True:
                try:
                    # Displaying Ids and names to help the user to choose
                    print("\nItems available to delete")
                    for item in cart:
                        print(f"ID : {item['id']} | Name : {item['name']}")
                        
                    target_id = int(input("Enter Product ID to delete : "))
                    found = False
                    
                    
                    for i in range(len(cart)):    # Searching by index 
                        if cart[i]["id"] == target_id:
                            removed_item = cart.pop(i)
                            print(f"Removed : {removed_item['name']}")
                            found = True
                            break
                    
                    if found:
                        break
                    else:
                        print("ID not found.")
                        retry = input("Press 1 to try again | 2 for Main Menu : ")
                        if retry == '2':
                            break
                except ValueError:
                    print("Please enter a valid Id")

    
    elif choice == '6':    # placing order
        
            

            print("THANK YOU FOR SHOPPING ")
            

            
            break

    
    elif choice == '7':  # exiting program
        print("Program finish")
        break

    
    else:                # handling invalid values
        print("Invalid choice Please enter a number between 1 and 7")