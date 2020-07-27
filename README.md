# Insight_DE_Challenge

Created a function to apply a custom function row by row while reading and storing the result.
The intention behind applying a custom function row by row and storing just the result is that we would not need to load the whole csv into memory
which can be helpful if the file is very large.

Created a test script to test both Insight's test data and my test data (got the dataset from http://files.consumerfinance.gov/ccdb/complaints.csv.zip and randomly selected 140658 rows to comply with github's file size limit).
