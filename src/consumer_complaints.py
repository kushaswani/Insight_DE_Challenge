import csv
import sys
from read_csv import read_csv
from read_csv import read_and_transform_csv
from function_to_apply import foo
from decimal import Decimal, ROUND_HALF_UP

input_filepath = sys.argv[1]
output_filepath = sys.argv[2]

print(input_filepath)
print(output_filepath)

result = read_and_transform_csv(filepath = input_filepath, foo = foo, result = {})

with open(output_filepath, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    for k,v in result:
#     for k,v in result.items():
        row = [k[0],k[1],v[0],len(v[1])]
        temp_v = 0
        for v_ in v[1].values():
            if v_>temp_v:
                temp_v = v_
        ratio = int(Decimal((temp_v/v[0])*100).to_integral_value(rounding=ROUND_HALF_UP))
        row.append(ratio)
        writer.writerow(row)
print('Completed')
