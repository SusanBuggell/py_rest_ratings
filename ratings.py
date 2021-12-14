"""Restaurant rating lister."""

# put your code here
rest_dict={}
sorted_rest_dict={}
user_rest=None
user_rate=0
option=0

def process_rest_ratings():
    global rest_dict
    """open and read scores.txt, strip out trailing whitespace, assign to dict"""

    str_rest_rate = open("scores.txt")
    for rest in str_rest_rate:
            rest = rest.rstrip() 
            rest = rest.split(":")
            # print(f'rest: {rest}')
            rest_dict[rest[0]]=rest[1]    
    # print(f'rest_dict: {rest_dict}')
    str_rest_rate.close()


def user_rate_valid():
    """is user restaurant rating entry valid?"""
    global user_rate
    global user_rest
    while not isinstance(user_rate, int) or user_rate < 1 or user_rate > 5:
        try:
            user_rate=int(user_rate)
            while user_rate<1 or user_rate>5:
                user_rate=input(f'Please enter a rating from 1-5 for {user_rest}: ')
                user_rate_valid()
        except:
            user_rate=input(f'Please enter a rating betweein 1-5 for {user_rest}')
            user_rate_valid()

def option_valid():
    """is user option from user_choices() valid?"""
    global option
    while not isinstance(option, int) or option < 1 or option > 3:
        try:
            option=int(option)
            while option<1 or option>3:
                option=input(f'Please enter a choice between 1-3: ')
                option_valid()        
        except:
            option=input(f'Please enter a choice between 1-3: ')
            option_valid()
    if option >=1 and option <=3:
        if option == 1:
            display_sorted_dict()
            user_choices()
        elif option == 2:
            new_user_rest()
            user_choices()
        else:
            quit()

def user_choices():
    """display user choices for actions"""
    global option
    option=input('Please select from the following options:\n1. See an alphabetical list of all of the restaurants with ratings\n2. Add a new restaurant with rating\n3. Quit the restaurant listings\n')
    option_valid()


def new_user_rest(): 
    """does user want to enter a new restaurant with rating?"""
    is_new_rest = input("Would you like to add a new restaurant (y/n) ? ")
    if is_new_rest == 'y':
        global user_rest
        global user_rate
        global rest_dict
        user_rest=input("Please enter a new restaurant to add to the list: ")
        user_rate=input(f"Please enter a rating from 1-5 for {user_rest}: ")
        user_rate_valid()
        print(f'Thank you for adding {user_rest} with a rating of {user_rate}')
        rest_dict[user_rest]=user_rate
        user_choices()
        option_valid()
    else:
        user_choices()
        option_valid()

    
def display_sorted_dict():
    """display sorted dictionary to user"""
    global rest_dict
    global sorted_rest_dict
    sorted_rest_dict = {key: value for key, value in sorted(rest_dict.items())}
    for key, value in sorted_rest_dict.items():
        print(f'{key} is rated at {value}')



process_rest_ratings()
user_choices()







