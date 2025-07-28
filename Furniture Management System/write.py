
#write module

#importing required functions from different modules

from read import read_furniture_data
from datetime import datetime
from operations import selling_furniture, purchasing_furniture


#for bill while selling
def generate_bill_sell():
    """
       stores the return value from read_furniture_data in furniture_data
       catches the return value from selling_furnitures
       stores the real date and time in date
       creates a unique file for billing purposes
       iterates over each item in sell_items_user and prints them in a formatted way using spaces and opeartions while writing in unique file
    
    """
    #storing return value from read module in furniture_data
    furniture_data = read_furniture_data()

    #catching return values from selling furniture function and storing in variables
    name, phone_number, date, sell_items_user, total_amount, vat_amount, total_with_vat, shipping_cost, grand_total, new_quantity = selling_furniture()

    #extracting the current date and time for billing purposes
    date = str(datetime.now().year) + "-" + str(datetime.now().month) + "-" + str(datetime.now().day) + "-" + str(datetime.now().hour) + "-" + str(datetime.now().minute) + "-" + str(datetime.now().second)
    
    unique_file = name +  str(date) + ".txt"  #create a unique file for bills
    
    try:
        file = open(unique_file, "w")
        file.write("---------------------------------------------------------------------------------")
        file.write("\n")
        file.write("Name of the Customer: " + str(name) + "\n")
        file.write("\n")
        file.write("Contact number: " + str(phone_number) + "\n")
        file.write("\n")
        file.write("Date and time of purchase: " + str(date) + "\n")
        file.write("\n")
        file.write("Sale Details:\n")
        file.write("\n")
        
        #iterating over each item and assigning values and computing the spaces to align the items in bill
        for i in sell_items_user:
            input_product_id = str(i[0])
            name_of_company = str(i[1])
            name_of_product = str(i[2])
            input_quantity = str(i[3])
            price_of_selected_item = "$" + str(i[4])
            
            detail = (input_product_id + " " * (5 - len(input_product_id))
                      + name_of_company + " " * (30 - len(name_of_company))
                      + name_of_product + " " * (15 - len(name_of_product))
                      + input_quantity + " " * (10 - len(input_quantity))
                      + price_of_selected_item + " " * (10 - len(price_of_selected_item)) + "\n")
                      
            
            file.write(detail) #writing the file after calculation of spaces
            
           
        file.write("\n")
        file.write("\n")
        file.write("Total Amount: $" + str(total_amount) + "\n")
        file.write("\n")
        file.write("13% VAT: $" + str(vat_amount) + "\n")
        file.write("\n")
        file.write("Total with 13% VAT: $" + str(total_with_vat) + "\n")
        file.write("\n")
        file.write("Shipping Cost: $" + str(shipping_cost) + "\n")
        file.write("\n")
        file.write("Grand Total: $" + str(grand_total) + "\n")
        file.write("---------------------------------------------------------------------------------")
        file.close()
    except Exception as e:
        print("ERROR!", e)
        
#for bill while purchasing
def generate_bill_purchase():

    """
       stores the return value from read_furniture_data in furniture_data
       catches the return value from purchasing_furniture
       stores the real date and time in date
       creates a unique file for billing purposes
       iterates over each item in sell_items_user and prints them in a formatted way using spaces and opeartions while writing in unique file
    
    """
    #storing return value from read module
    furniture_data = read_furniture_data()
    
    #catching return values from selling furniture function and storing in variables
    name, phone_number, date, purchased_items_user, total_amount, vat_amount, total_with_vat, grand_total, new_quantity = purchasing_furniture()
    
    #extracting the current date and time for billing purposes
    date = str(datetime.now().year) + "-" + str(datetime.now().month) + "-" + str(datetime.now().day) + "-" + str(datetime.now().hour) + "-" + str(datetime.now().minute) + "-" + str(datetime.now().second)
    
    unique_file = name +  str(date) + ".txt"  #Create a unique file for bills
    
    try:
        file = open(unique_file, "w")
        file.write("---------------------------------------------------------------------------------")
        file.write("\n")
        file.write("Name of the Employee: " + str(name) + "\n")
        file.write("\n")
        file.write("Contact number: " + str(phone_number) + "\n")
        file.write("\n")
        file.write("Date and time of purchase: " + str(date) + "\n")
        file.write("\n")
        file.write("Purchase Details:\n")
        file.write("\n")
        file.write("\n")

        #iterating over each item and assigning values and computing the spaces to align the items in bill
        for i in purchased_items_user:
            
            input_product_id = str(i[0])
            name_of_company = str(i[1])
            name_of_product = str(i[2])
            input_quantity = str(i[3])
            price_of_selected_item = "$" + str(i[4])
            
            detail = (input_product_id + " " * (5 - len(input_product_id))
                      + name_of_company + " " * (30 - len(name_of_company))
                      + name_of_product + " " * (15 - len(name_of_product))
                      + input_quantity + " " * (10 - len(input_quantity))
                      + price_of_selected_item + " " * (10 - len(price_of_selected_item)) + "\n")
                
            file.write(detail) #writing the file after calculation of spaces 
 
            
        file.write("\n")
        file.write("\n")
        file.write("Total Amount: $" + str(total_amount) + "\n")
        file.write("\n")
        file.write("13% VAT: $" + str(vat_amount) + "\n")
        file.write("\n")
        file.write("Total with 13% VAT: $" + str(total_with_vat) + "\n")
        file.write("\n")
        file.write("Grand Total: $" + str(grand_total) + "\n")
        file.write("---------------------------------------------------------------------------------")
        file.close()
    except Exception as e:
        print("ERROR!", e)
