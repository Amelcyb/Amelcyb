##############################################################
## This Python program is to calculate a holiday total cost ##
## written by: Amel Al-Bazi
## Date: Tuesday 08 October 2024
## CoGrammer Hyperiondev cohort Sep 2024
## Lesson 6 - task 6 - Fucntions
## Resubmission following review feedback: 
##      1) create separate function for holiday_cost 
##      2) ensure snake_format variable naming format
##############################################################


# step 1 - Descibe what will this programe do:
print("This program will calculate the total cost of holiday taking into account flights, accomodation and car rental costs.")


# Step 2 - set the flight prices per destination
toronto_flight = 1000 # flight ticket to Toronoto in £
valencia_flight = 800 # flight ticket to Valencia in £
marmaris_flight = 600 # flight ticket to Marmaris in £


# Step 3 - Ask user the city flight options, and hotel number of nights and number of car hire days required.
city_flight = input("""Available city flight options: 
t = Toronto - Canada £1000 or 
v = Valencia - Spain £800 or 
m = Marmaris - Turkey £600 or
other = flight cost excluded
Please select your city: """)

num_night = int(input("Enter number of required hotel nights (hotel night rate £50) : "))

rental_days = int(input("Enter number of required car hire days (car hire daily rate £10): "))

# Step 4 - create function to take in the user selected city flight and calculate the flight fare


def plane_cost(city_flight):
    
    if city_flight.lower() == "t":
        # Calculate Canada holiday cost
        city_flight = toronto_flight
        #print(f"The flight cost is: {flight_cost}")
        #break

    elif city_flight.lower() == "v":
        # Calculate Spain holiday cost
        city_flight = valencia_flight
        #print(f"The flight cost is: {flight_cost}")
        #break

    elif city_flight.lower() == "m":
        # Calculate Turkey holiday cost
        city_flight = marmaris_flight
        #print(f"The flight cost is: {flight_cost}")
        #break

    else:
    # Handle unrecognized input
        print("Unrecognized city flight option, flight cost excluded:")
        city_flight = 0
        #break
            
    return int(city_flight)


# Step 5 - create function to take num_nights as an argument and return a total cost for the hotel stay, night rate = £50
def hotel_cost(num_night):
    num_night = num_night * 50
    return num_night

# Step 6 - create function to take rental_days as an argument and return the total cost of the car rental, daily rate = £50
def car_rental(rental_days):
    rental_days = rental_days * 10
    return rental_days

# step 7 - lastly calculate the total holiday cost by calling the corresponding functions and adding them
total_cost = 0
def holiday_cost(total_cost):
    total_cost = plane_cost(city_flight) + hotel_cost(num_night) + car_rental(rental_days)
    return total_cost

print(f"Total holiday cost is: £ {holiday_cost(total_cost)}")

