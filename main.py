amt=int(input('Enter the amount: '))
tip=int(input('Enter the tip in percentage: '))

def totalCal(a,t):
    total=a+a/100*t
    print('Total bill=',total)
totalCal(amt,tip)