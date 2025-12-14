def bill_amount(bill, tip_percent ):
    total = bill *(1 + 0.01 * tip_percent)
    total = round(total, 2)
    print('Please pay: ' , total)
bill_amount(100, 30)