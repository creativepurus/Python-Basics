high_income = True
good_credit = True
criminal_record = True

'''
if high_income and good_credit:
    print("You are eligible for Loan...")
elif high_income or good_credit:
    print("You are eligible for a Loan upto 10 Lacs...")
    '''
if good_credit and not criminal_record:
    print("You are eligible for Loan because you didn't have any criminal record...")
else:
    print("Sorry, You are not eligible for the Loan...")