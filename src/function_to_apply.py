from datetime import datetime
def foo(row_num,row,dict_,result):
#     year = int(row[dict_['Date received']][0:4])
    try:
        year = datetime.strptime(row[dict_['Date received']], '%Y-%m-%d').year
    except:
        print("An exception occurred while parsing year from date in row %d" %(row_num))
    product = row[dict_['Product']].lower()
    company = row[dict_['Company']]
    
    if (product,year) in result.keys():
        result[(product,year)][0]+=1
        if company in result[(product,year)][1].keys():
            result[(product,year)][1][company]+=1
        else:
            result[(product,year)][1][company]=1
    else:
        result[(product,year)]=[1,{company:1}]
    
    return result
