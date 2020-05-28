SQFT_PER_ACRE = 43560

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

acres = length * width / SQFT_PER_ACRE

print("The area of the field is", acres, "acres")
