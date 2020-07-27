import csv
import sys
from read_csv import read_csv
from read_csv import read_and_transform_csv
from function_to_apply import foo
from decimal import Decimal, ROUND_HALF_UP
import time

start = time.process_time()
input_filepath = '../insight_testsuite/tests/test_1/input/complaints.csv'
output_filepath = '../insight_testsuite/tests/test_1/output/generated_report.csv'

#print(input_filepath)

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

end = time.process_time()


test_1_actual_report = []
with open('../insight_testsuite/tests/test_1/output/report.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for i,row in enumerate(reader):
        test_1_actual_report.append(row)

test_1_generated_report = []
with open('../insight_testsuite/tests/test_1/output/generated_report.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for i,row in enumerate(reader):
        test_1_generated_report.append(row)


if test_1_actual_report == test_1_generated_report:
    print("Insight's test passed")
else:
    print("Insight's test failed")

start = time.process_time()
input_filepath = '../insight_testsuite/tests/my_test/input/complaints.csv'
output_filepath = '../insight_testsuite/tests/my_test/output/generated_report.csv'

#print(input_filepath)

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

end = time.process_time()

import pandas as pd
import numpy as np

input_filepath = '../insight_testsuite/tests/my_test/input/complaints.csv'
output_filepath = '../insight_testsuite/tests/my_test/output/report.csv'

start_pandas = time.process_time()
df = pd.read_csv(input_filepath)
df['Product'] = df['Product'].str.lower()
try:
    df['Year'] = pd.to_datetime(df['Date received'], format='%Y-%m-%d').dt.year
except:
    print("Error parsing date")

df1 = df.groupby(['Product','Year']).agg({'Company':'count'}).reset_index()
df2 = df[['Product','Year','Company']].drop_duplicates().groupby(['Product','Year']).size().reset_index(name='Total Companies')
df3 = df[['Product','Year','Company']].groupby(['Product','Year','Company']).size().reset_index().groupby(['Product','Year']).agg({0:'max'}).reset_index()

result = df1.merge(df2).merge(df3)

result[0] = (((result[0]/result['Company'])*100)+0.5).apply(np.floor).astype(int)

result.to_csv(output_filepath, header=False, index=False)
end_pandas = time.process_time()


my_test_actual_report = []
with open('../insight_testsuite/tests/my_test/output/report.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for i,row in enumerate(reader):
        my_test_actual_report.append(row)

my_test_generated_report = []
with open('../insight_testsuite/tests/my_test/output/generated_report.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for i,row in enumerate(reader):
        my_test_generated_report.append(row)

if my_test_actual_report == my_test_generated_report:
    print("My test passed")
else:
    print("My test failed")
