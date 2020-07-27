import csv
from decimal import Decimal, ROUND_HALF_UP

# function to read the whole csv file as a dict of arrays with column names as keys and column values as arrays
def read_csv(filepath):
    with open(filepath) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        fields = reader.__next__()
        dict_ = {}
        for field in fields:
            dict_[field] = []
        for i,row in enumerate(reader):
#             if i%10000==0:
#                 print(i)

            for j,element in enumerate(row):
                dict_[fields[j]].append(element)
    return dict_


"""
function to apply a custom function foo row by row and store the result in a global variable
filepath gives the path of the file to read, foo is the custom function
result is used to specify the type of varible result is expected to be, in this case result is just an empty dict
result can also be used to check whether a condition is met or not (for e.g. checking if a column contains a value greater than 10)

the intention behind applying a custom function row by row and storing just the result is that we would not need to load the whole csv into memory
which can be helpful if the file is very large
"""
def read_and_transform_csv(filepath, foo, result):
    with open(filepath) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')

        # getting column names and creating a dictionary with column names as keys and their indexes as values
        fields = reader.__next__()
        dict_ = {}
        for i,field in enumerate(fields):
            dict_[field] = i

        # reading the file row by row
        for i,row in enumerate(reader):
            # applying the custom function and storing the result
            result = foo(i,row,dict_,result)

#             if i%10000==0:
#                 print(i)

    # sorting the result
    result = sorted(result.items())
    return result
