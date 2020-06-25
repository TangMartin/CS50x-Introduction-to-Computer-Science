from cs50 import get_float


def main():
    print(f"{numberofcoins()}")

def numberofcoins():
    
    money = -1
    while money < 0:
        money = get_float("Change owed: ")
        
    totalcents = money * 100

    numberofcoins = 0

    tempnumber = 0

    remainder  = 0

    quarter = 25
    dime = 10
    nickel = 5
    penny = 1

    if quarter <= totalcents:
        remainder = totalcents % quarter
        numberofcoins = numberofcoins + (totalcents - remainder) / quarter
        totalcents = remainder

    if dime <= totalcents:
        remainder = totalcents % dime
        numberofcoins = numberofcoins + (totalcents - remainder) / dime
        totalcents = remainder

    if nickel <= totalcents:
        remainder = totalcents % nickel
        numberofcoins = numberofcoins + (totalcents - remainder) / nickel
        totalcents = remainder

    if penny <= totalcents:
        remainder = totalcents % penny
        numberofcoins = numberofcoins + (totalcents - remainder) / penny
        totalcents = remainder

    return numberofcoins

main()