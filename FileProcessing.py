#Name: Jason Palomo
#Date: 07/28/2020
#Program Description: Get name, address, and phone# from user. Ask where to save data, verify location, save, and then read data back
#to user for verification

import os

#Function to gather demographic information from the end user(name, address, city, state, zip, phone number). 
def get_user_info():
    first_name =  input('Enter your First Name: ')
    last_name = input('Enter your Last Name: ')
    address = input('Enter your Address": ')
    city = input('Enter City: ')
    state = input('Enter State: ')
    zipcode = input('Enter Zipcode: ')
    phone_num = input('Please enter your phone number without dashes or spaces: ')

#Format the data into a comma delimited single line
    data = (f'{first_name},{last_name},{address},{city},{state},{zipcode},{phone_num}')
    return data

#Function will ask the user for a directory to save the data, check if directory is valid, if it's valid, change working directory,
#and save the file. If the directory is not valid, will prompt user for a valid directory
def save_file():
    active = True
    
    while active == True:
        directory = input('Please specify the direcroty you wish to save the file. Example: (C:\\Pyhon_Scripts): ')
        check_path = os.path.isdir(directory)
        os.chdir(directory)

        if check_path == False:
            print('Directory does not exist!')
        else:
            file_name = input('Save File AS Example:"filename.txt": ')
            with open(file_name, 'w') as file_object:
                file_object.write(user_data)
                file_loc = (f'{directory}\{file_name}')

            active = False
            return file_loc
    
#Function to read the saved file and print the location to the end user and show what data was saved to the file. 
def read_file():
    file_name = file_location

    with open(file_name, 'r') as file_read:
        lines = file_read.readlines()

    for line in lines:
        print(f'\nFile Save Location: {file_name}')
        print(f'\nHere is a review of the data you entered:\n{line.rstrip()}')    

    
#Main program to call the functions.
user_data = get_user_info()
file_location = save_file()
read_file()