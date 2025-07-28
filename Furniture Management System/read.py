#read module
#reads the information from the text file

def read_furniture_data():
    """
    Reads the data from the file and stores it in a dictionary
    data is iterated by using for loop and any new line characters are replaced
    data is split based on commas and it is stored in a list product_data
    """
    furniture_data ={} #for storing the data
    
    try:
        file = open("furniture_data_file.txt", "r") #reading the text file 


        #iterating along each line and appending the data to a list
        for data in file:
            data = data.replace("\n"," ")
            data = data.split(",")
            product_data = []
            for i in range(1,len(data)):
                product_data.append(data[i].strip())# .strip() to remove new line characters
            furniture_data[data[0]] = product_data

        file.close() #closing the file after it has been read

    except FileNotFoundError:
        print("ERROR! The File 'furniture_data_file.txt' was not Found.") #error message incase of filenotfounderror

    except Exception as e:
        print("ERROR!",e) #error message for any other error

    return furniture_data #returning the dictionary

                

