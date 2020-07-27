import csv
from decimal import Decimal, ROUND_HALF_UP

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

def read_and_transform_csv(filepath, foo, result):
    with open(filepath) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        fields = reader.__next__()
        dict_ = {}
        for i,field in enumerate(fields):
            dict_[field] = i
        for i,row in enumerate(reader):
            result = foo(i,row,dict_,result)
            
#             if i%10000==0:
#                 print(i)

    # result = dict(sorted(result.items()))
    result = sorted(result.items())
    return result
