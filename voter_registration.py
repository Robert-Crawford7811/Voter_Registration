"""Program to register eligible users to vote"""
def voter_registration():
    """Main function of the program interface of Voter Registration"""
    print("##############################")
    print("Welcome to the Python Voter Registration Application.")

    while True:
        # Cancels Registration and stops the program running
        choice = input("Do you want to continue with Voter Registration? (Yes/No): ").lower()

        if choice != "yes":
            print("Your registration process has been canceled.")
        # Establishes personal information of User
        first_name, last_name, age = personal_info()

        if eligible_to_vote(age):
            # Establishes personal information of User
            citizen, state, zipcode = residency_info()
            if citizen and not citizenship(citizen): # Stops registration if user is not a citizen
                print("Sorry, you are not eligible to register to vote.")
            else:
                # Calls Print Functions
                print_personal_registration(first_name, last_name, age)
                print_residency_registration(citizen, state, zipcode)
                break
        else:
            print("Sorry, you are not eligible to register to vote.")

def personal_info():
    '''Requests personal information about the user'''
    # Requests user identification information
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    age = user_age()
    return first_name, last_name, age

def user_age():
    ''' Requests the user to enter their age'''
    while True:
        try:
            #Verifies the Users age is a valid entry
            age = int(input("What is your age? "))
            #Ensures user doesn't enter an age above 120
            if 0 < age <= 120:
                return age
            print("Please enter a valid age.")
        except ValueError:
            print("Please enter a valid age as a number.")

def eligible_to_vote(age):
    """Requests the users age and validates the information inputted"""
    # Enforces the lowest age requirement to vote
    return age >= 18

def citizenship(citizen):
    """Defines citizenship status that can vote"""
    # Enforces U.S. Citizenship to Register
    return citizen.lower() == "yes"

def residency_info():
    """Collect the citizenship and residency information of the user"""
    # Requests citizenship requirement
    citizen = input("Are you a U.S. Citizen? (Yes/No): ")
    # Only continues if US Citizen
    if citizenship(citizen):
        state = input("What state do you live? (2-letter code): ").upper()
        zipcode = input("What is your zipcode? ")
        return citizen, state, zipcode
    return citizen, None, None
def print_personal_registration(first_name, last_name, age):
    '''Prints the personal information of the user'''
    print("\nThanks for registering to vote. Here is the information we received:")
    print(f"Name (first last) : {first_name} {last_name}")
    print(f"Age: {age}")

def print_residency_registration(citizen, state, zipcode):
    '''Prints the residency information of the user'''
    #Seperates the print statements to reduce argument count
    print(f"U.S. Citizen: {'Yes' if citizenship(citizen) else 'No'}")
    if citizenship(citizen):
        print(f"State: {state}")
        print(f"Zipcode: {zipcode}")

    print(
        "\nThank you, your voter registration card should be shipped within 3 weeks.\n")
    print("##############################")


if __name__ == "__main__":
    voter_registration()
