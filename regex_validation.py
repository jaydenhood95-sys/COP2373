import re


# Validate a phone number
def validate_phone(phone):
    pattern = r'^\d{3}-\d{3}-\d{4}$'
    return bool(re.match(pattern, phone))


# Validate a Social Security number
def validate_ssn(ssn):
    pattern = r'^\d{3}-\d{2}-\d{4}$'
    return bool(re.match(pattern, ssn))


# Validate a ZIP code
def validate_zip(zip_code):
    pattern = r'^\d{5}$'
    return bool(re.match(pattern, zip_code))


# Get user input and display the validation results
def main():
    phone = input("Enter your phone number (123-456-7890): ")
    ssn = input("Enter your Social Security number (123-45-6789): ")
    zip_code = input("Enter your ZIP code (12345): ")

    # Check the phone number
    if validate_phone(phone):
        print("Phone number is valid.")
    else:
        print("Phone number is invalid.")

    # Check the Social Security number
    if validate_ssn(ssn):
        print("Social Security number is valid.")
    else:
        print("Social Security number is invalid.")

    # Check the ZIP code
    if validate_zip(zip_code):
        print("ZIP code is valid.")
    else:
        print("ZIP code is invalid.")


# Call the main function
if __name__ == "__main__":
    main()
