from datetime import datetime
def foo(row_num,row,dict_,result):
#     year = int(row[dict_['Date received']][0:4])
    # trying to get the year from the date
    try:
        year = datetime.strptime(row[dict_['Date received']], '%Y-%m-%d').year
    except:
        print("An exception occurred while parsing year from date in row %d" %(row_num))
    # getting the product name and converting it to lowercase
    product = row[dict_['Product']].lower()
    company = row[dict_['Company']]

    # cheking if the (product,year) combination already exists in the result dictionary
    # if it does incrementing its count by 1
    if (product,year) in result.keys():
        result[(product,year)][0]+=1
        # checking if we have already encountered this company for this particular (product,year) combination
        # if it does incrementing its count by 1
        if company in result[(product,year)][1].keys():
            result[(product,year)][1][company]+=1
        # else adding this company for this particular (product,year) combination
        else:
            result[(product,year)][1][company]=1
    # else adding this particular (product,year) combination to the result
    else:
        result[(product,year)]=[1,{company:1}]

    return result
