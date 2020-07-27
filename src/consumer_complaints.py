import csv
import sys
# from read_csv import read_csv

# importing read_and_transform_csv function which lets you apply custom functions to rows and get the transformed dataframe as dict of arrays
from read_csv import read_and_transform_csv

# importing the custom function which we need to apply to get intended results
from function_to_apply import foo

# importing Decimal and ROUND_HALF_UP to round [0.5,1] to 1 and [0,0.5) to 0
from decimal import Decimal, ROUND_HALF_UP

# getting the input and output filepaths from command line arguments
input_filepath = sys.argv[1]
output_filepath = sys.argv[2]

# print(input_filepath)
# print(output_filepath)

# getting the intended result through applying the custom function to every row
result = read_and_transform_csv(filepath = input_filepath, foo = foo, result = {})

# writing the result to a csv file
with open(output_filepath, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    # Used tuple of (product,year) as key
    for k,v in result:
        # k[0] represents products, k[1] represents year, v[0] represents total number of complaints received for that product and year
        # v[1] represents a dictionary with companies as keys and their number of instances as values
        # therefore len(v[1]) gives the total number of companies receiving at least one complaint for that product and year
        row = [k[0],k[1],v[0],len(v[1])]
        temp_v = 0
        # finding highest number of complaints filed against one company for that product and year.
        for v_ in v[1].values():
            if v_>temp_v:
                temp_v = v_
        # calculating highest percentage (rounded to the nearest whole number) of total complaints filed against one company for that product and year
        ratio = int(Decimal((temp_v/v[0])*100).to_integral_value(rounding=ROUND_HALF_UP))
        row.append(ratio)

        # writing to the csv file row by row
        writer.writerow(row)
print('Completed')
