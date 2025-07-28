#operations module
#importing required functions from other modules

from datetime import datetime
from read import read_furniture_data

#function for processing selling of furniture 
def selling_furniture():

    """
    stores return value from read_furniture_data in furniture_data
    try except is implemented in user input code
    reads the file furniture_data_file as read and prints the data
    loops for continuation of selling is implemented with product id validation and also quantity validation using while loop
    operations in the quantity of products is carried out to updated the data
    the updated data is written back to the original file and thus updated data is displayed in another transaction
    
    """
    furniture_data = read_furniture_data() #storing the return value from read_furniture_data
    
    print("-------------------------------------------------------------------------------------------------------------------------")
    print("Please Enter your details for bill generation. ")
    

    name = input("Please enter the name of the Customer: ")
    while name == "":
        print("Empty field found, please try again")
        name = input("Please enter the name of the Customer: ")
    

    try:
        phone_number = input("Please enter the phone number of the Customer: ")
        while phone_number == "":
            print("Field cannot be empty!")
            phone_number = input("Please enter the phone number of the Customer: ")
        phone_number = int(phone_number)
    except:
        print("Invalid Input")

        
    print("\n")
    print("-------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("S.N.   Company Name                  Item Name       Quantity    Price")
    print("\n")
    print("-------------------------------------------------------------------------------------------------------------------------")

    try:
        file = open("furniture_data_file.txt", "r")
        for line in file:
            data = line.strip().split(",")
            
            sn = data[0]
            company_name = data[1]
            product_name = data[2]
            quantity = data[3]
            price = data[4]
            
            #Calculating spaces needed for alignment of items
            spaces_for_sn = 5 - len(sn)
            spaces_for_company_name = 30 - len(company_name)
            spaces_for_product_name = 20 - len(product_name)
            spaces_for_quantity = 10 - len(quantity)
            spaces_for_price = 10 - len(price)
            
            #Formatting and printing each line with calculated spaces
            print(sn + " " * spaces_for_sn +
                  company_name + " " * spaces_for_company_name +
                  product_name + " " * spaces_for_product_name +
                  quantity + " " * spaces_for_quantity +
                  price + " " * spaces_for_price)
            
        print("-------------------------------------------------------------------------------------------------------------------------")
        file.close()
    except Exception as e:
        print("Error!", e)


        
    sell_items_user = [] #creating list for storing purchased items
    total_amount = 0.0 

    while True:
        #try except for every user input
        try:
            input_product_id = input("Enter the product id: ")
        except ValueError:
            print("Please enter numeric value.")
        

        while input_product_id not in furniture_data: #checks the input_product_id  with key in dictionary  
            print("Please Enter Valid Id!")
            try:
                input_product_id = input("Enter the product id: ")
            except ValueError:
                print("Please enter numeric value.")
        try:
            input_quantity = int(input("Enter the quantity of product: "))
            while input_quantity == "":
                print("Please Enter the quantity.")
                input_quantity = int(input("Enter the quantity of product: "))
        except ValueError:
            print("Please enter numeric value.")

        quantity_of_product = furniture_data[input_product_id][2]
        
        while input_quantity <= 0 or input_quantity > int(quantity_of_product) or input_quantity=="":
            print("The quantity you wish to sell is not available. Please enter the quantity again.")
            try:
                input_quantity = int(input("Please Provide the number of quantity of the item you want to sell: "))
            except ValueError:
                print("Please enter numeric value")
                

        new_quantity = int(furniture_data[input_product_id][2]) - int(input_quantity) #processing the quantity
        
        furniture_data[input_product_id][2] = new_quantity #assigning new value of quantity to update the data in updated_furniture_data.txt
  
        name_of_company = furniture_data[input_product_id][0] #assigning value to variable
        
        name_of_product = furniture_data[input_product_id][1] #assigning value to variable
        
        price_of_selected_item = furniture_data[input_product_id][3].replace("$", '') #replacing the $ sign with space so that we can operate on price
        
        total_price = float(price_of_selected_item) * int(input_quantity)#calculating price
        
        sell_items_user.append([input_product_id, name_of_company, name_of_product, input_quantity, price_of_selected_item]) #appending the data to the list

        #Updating totals
        total_amount += total_price

        #Checking if the user wants to add more items
        try:
            sell_more = input("Do you want to sell more items? (Y/N): ").upper()
        except ValueError:
            print("Invalid Input!")
        if sell_more != 'Y':
            break

    #checking if user wants the products to be shipped or not
    try:
        shipping_cost = input("Dear user do you want your furniture to be shipped? (Y/N): ").upper()
    except ValueError:
        print("Please enter 'Y' if you wish to ship and 'N' if you don't want shipping.")
        
    if shipping_cost == "Y":
        shipping_cost = 50
    else:
        shipping_cost = 0


    #different operations for calculating prices
    vat_amount = total_amount * 0.13 #vat
    total_with_vat = total_amount + vat_amount #total with vat
    grand_total = total_with_vat + shipping_cost #grand total
 
    date_and_time_present = datetime.now() #extracting the real time date and time
    

    print("--------------------------------------------------------")
    print("\n")
    print("Name of the Customer: " + str(name))
    print("\n")
    print("Contact number: " + str(phone_number))
    print("\n")
    print("Date and time of sale: " + str(date_and_time_present))
    print("\n")
    print("Sale Details are:")
    print("\n")

    #iterating over items in the list to print them accordingly
    for item in sell_items_user:
        #assigning data to variables
        input_product_id = str(item[0])
        name_of_company = str(item[1])
        name_of_product = str(item[2])
        input_quantity = str(item[3])
        price_of_selected_item = "$" + str(item[4])
        #calculating each spaces 
        detail = (input_product_id + " " * (4 - len(input_product_id)) + 
                  name_of_company + " " * (30 - len(name_of_company)) + 
                  name_of_product + " " * (15 - len(name_of_product)) +
                  input_quantity + " " * (10 - len(input_quantity)) + 
                  price_of_selected_item + " " * (10 - len(price_of_selected_item)) + 
                  "\n")
        print(detail)

    print("\n")
    print("Total Amount: $" + str(total_amount))
    print("\n")
    print("13% VAT: $" + str(vat_amount))
    print("\n")
    print("Total with 13% VAT: $" + str(total_with_vat))
    print("\n")
    print("Your Shipping Cost is: $" + str(shipping_cost))
    print("\n")
    print("Grand Total: $" + str(grand_total))
    print("\n")
    print("--------------------------------------------------------")


    #updating the data in furniture_data_file.txt
   
    file = open("furniture_data_file.txt", "w")
    for key, values in furniture_data.items():
        line = str(key) + "," + str(values[0]) + "," + str(values[1]) + "," + str(values[2]) + "," + str(values[3]) + "\n"
        file.write(line)
    file.close()

    
    return name, phone_number, date_and_time_present, sell_items_user, total_amount, vat_amount, total_with_vat, shipping_cost, grand_total, new_quantity 

#function for purchasing furniture
def purchasing_furniture():
    """
    stores return value from read_furniture_data in furniture_data
    try except is implemented in user input code
    reads the file furniture_data_file as read and prints the data
    loops for continuation of purchasing is implemented with product id validation and also quantity validation using while loop
    operations in the quantity of products is carried out to updated the data
    the updated data is written back to the original file and thus updated data is displayed in another transaction
    
    """

    furniture_data = read_furniture_data() #storing the return value from read_furniture_data
    
    print("-------------------------------------------------------------------------------------------------------------------------")
    print("Please Enter your details for bill generation. ")

    
    name = input("Please enter the name of the Employee: ")
    while name == "": #checking for empty input
        print("Empty field found, please try again")
        name = input("Please enter the name of the Employee: ")
    

    
    try:
        phone_number = input("Please enter the phone number of the Employee: ")
        while phone_number == "": #chekcing for empty input
            print("Field cannot be empty!")
            phone_number = input("Please enter the phone number of the Employee: ")
        phone_number = int(phone_number)
    except:
        print("Invalid Input")
    
    

    print("\n")
    print("-------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("S.N.   Company Name                  Item Name       Quantity    Price")
    print("\n")
    print("-------------------------------------------------------------------------------------------------------------------------")

    try:
        file = open("furniture_data_file.txt", "r")
        for line in file:
            data = line.strip().split(",")
            
            sn = data[0]
            company_name = data[1]
            product_name = data[2]
            quantity = data[3]
            price = data[4]
            
            #Calculating spaces needed for alignment of items
            spaces_for_sn = 5 - len(sn)
            spaces_for_company_name = 30 - len(company_name)
            spaces_for_product_name = 20 - len(product_name)
            spaces_for_quantity = 10 - len(quantity)
            spaces_for_price = 10 - len(price)
            
            #Formatting and printing each line with calculated spaces
            print(sn + " " * spaces_for_sn +
                  company_name + " " * spaces_for_company_name +
                  product_name + " " * spaces_for_product_name +
                  quantity + " " * spaces_for_quantity +
                  price + " " * spaces_for_price)
            
        print("-------------------------------------------------------------------------------------------------------------------------")
        file.close()
    except Exception as e:
        print("Error!", e)
        
    purchased_items_user = [] #creating an empty list
    
    total_amount = 0.0

    while True:
        #try except for every user input 
        try:
            input_product_id = input("Enter the product id: ") 
        except ValueError:
            print("Please enter numeric value.")
        

        while input_product_id not in furniture_data: #checks the input_product_id  with key in dictionary
            print("Please Enter Valid Id!")
            try:
                input_product_id = input("Enter the product id: ")
            except ValueError:
                print("Please enter numeric value.")
        try:
            input_quantity = int(input("Enter the quantity of product: "))
            while input_quantity == "":
                print("Please Enter the quantity.")
                input_quantity = int(input("Enter the quantity of product: "))
        except ValueError:
            print("Please enter numeric value.")
            
        quantity_of_product = furniture_data[input_product_id][2]
        
        while input_quantity <= 0 or input_quantity == "":
            try:
                input_quantity = int(input("Please Provide the number of quantity of the item you want to purchase: "))
            except ValueError:
                print("Please enter numeric value.")

        new_quantity = int(furniture_data[input_product_id][2]) + int(input_quantity) #processing the quantity

        furniture_data[input_product_id][2] = new_quantity #assigning new value of quantity to update the data in updated_furniture_data.txt
        
        name_of_company = furniture_data[input_product_id][0] #assigning value to variable

        name_of_product = furniture_data[input_product_id][1] #assigning value to variable

        price_of_selected_item = furniture_data[input_product_id][3].replace("$", '') #replacing the $ sign with space so that we can operate on price
        
        total_price = float(price_of_selected_item) * int(input_quantity) #calculating price
        
        purchased_items_user.append([input_product_id, name_of_company, name_of_product, input_quantity, price_of_selected_item]) #appending the data to the list

        # Update totals
        total_amount += total_price

        # Check if the user wants to add more items
        try:
            purchase_more = input("Do you want to add more items? (Y/N): ").upper()
        except ValueError:
            print("Invalid Input!")
        if purchase_more != 'Y':
            break

    
    #different operations for calculating prices
    vat_amount = total_amount * 0.13
    total_with_vat = total_amount + vat_amount

    #no shipping cost in case of purchase from manufacture
    grand_total = total_with_vat

    date_and_time_present = datetime.now() #extracting realtime date and time

    print("--------------------------------------------------------")
    print("\n")
    print("Name of the Employee: " + str(name))
    print("\n")
    print("Contact number: " + str(phone_number))
    print("\n")
    print("Date and time of purchase: " + str(date_and_time_present))
    print("\n")
    print("Purchase Details are:")
    print("\n")

    #iterating over each items to print them accordingly
    for item in purchased_items_user:
        #assigning values to variables
        input_product_id = str(item[0])
        name_of_company = str(item[1])
        name_of_product = str(item[2])
        input_quantity = str(item[3])
        price_of_selected_item = "$" + str(item[4])

        #calculating each spaces for alignment
        detail = (input_product_id + " " * (5 - len(input_product_id)) + 
                  name_of_company + " " * (30 - len(name_of_company)) + 
                  name_of_product + " " * (15 - len(name_of_product)) +
                  input_quantity + " " * (10 - len(input_quantity)) + 
                  price_of_selected_item + " " * (10 - len(price_of_selected_item)) + 
                  "\n")
        print(detail)
        

    print("\n")

    print("Total Amount: $" + str(total_amount))
    print("\n")
    print("13% VAT: $" + str(vat_amount))
    print("\n")
    print("Total with 13% VAT: $" + str(total_with_vat))
    print("\n")
    print("Grand Total: $" + str(grand_total))
    print("\n")
    print("--------------------------------------------------------")
    print("\n")

    #updating the data in furniture_data_file.txt
    
    file = open("furniture_data_file.txt", "w")
    for key, values in furniture_data.items():
        line = str(key) + "," + str(values[0]) + "," + str(values[1]) + "," + str(values[2]) + "," + str(values[3]) + "\n"

        file.write(line)
    file.close()

    return name, phone_number, date_and_time_present, purchased_items_user, total_amount, vat_amount, total_with_vat, grand_total, new_quantity
