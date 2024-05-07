"""
Description: Converts inches input by user to feet.

Usage: A6E3.py (user inputs data)

Parameters: userinput1 = user inputs data in inches

"""

# Collect user data and preform conversions #
INCHES_PER_FEET = 12

try:
    INCHES = input("Enter a distance in inches: ")
    FEET = int(INCHES) // INCHES_PER_FEET
    REMAINDER = int(INCHES) % INCHES_PER_FEET

    # Print data #
    print(f"{INCHES}\" == {FEET}\'{REMAINDER}\"")

except:
    print("Error: Distance in inches must be an integer.")
