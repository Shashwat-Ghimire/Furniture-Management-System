"""
the module which is the main face of the program
user inputs and loops
calling of different functions from different modules
"""

#importing necessary functions from modules
from read import read_furniture_data
from write import generate_bill_sell, generate_bill_purchase

#defining the main function
def main():
    """
    This is the main function that calls other functions to operate the system
    data is read from read module when user selects to sell or purchase products
    the functions from write are call which write the to the bill
    the functions from operations are called in write module to write the data
    """
    #UI with welcome here
    print("---------------------------------------------------------------------------------")
    print("\n")
    print("----------------------","WELCOME TO BRJ FURNITURE STORE SYSTEM","---------------------")
    print("\n")
    print("---------------------------------------------------------------------------------")
    print("\n")

    
    

    while True:
        #UI / options that are given to the user
        
        print("Please Select one of the options below to use our System.")
        print("\n")
        print("Type 1 to Sell the products to customer.")
        print("Type 2 to Purchase from Manufacturer.")
        print("Type 3 to Exit from the system.")
        print("\n")
        print("---------------------------------------------------------------------------------")
        print("\n")
        #taking user input for sell/purchase/exit
        #input error exception
        try:
            user_input = int(input("Enter your choice: "))

            if user_input == 1:
                read_furniture_data()
                generate_bill_sell()
                print("Sale Successful.")
                
            elif user_input == 2:
                read_furniture_data()
                generate_bill_purchase()
                print("Purchase Successful.")

            elif user_input == 3:
                print("Thank you for using the system. Exiting....")
                break

            else:
                print("Invalid choice. Please try again.")

        
        except Exception as e:
            print("ERROR!",e)

main()  #calling the main function to run the module
