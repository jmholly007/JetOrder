from pytest import mark

#run this test with the following in terminal "pytest -m wind -v"'
@mark.wind
def test_PN():
    # w = PN
    # x = qtyneeded
    # y = cleanlist of available suppliers
    # z = maxNum

    x = 55
    w = 4444

    pricing =[] # sets up string to pull pricing from CS5374_Project_Pricing.xlsx
    if w == 1111:
        assert True
    elif w == 2222:
        assert True
    elif w == 3333:
        assert True
    elif w == 4444:
        assert True
    elif w == 5555:
        assert True

@mark.wind
def test_Cost():
    x = 55
    w = 4444
    pricing = [5.00]
   # pricing.append(int(inputWorksheetPricing.cell_value(row, 1)))  # (row, column) inserts stat from excel spreadsheet
    cost = pricing[0] # pulls pricing out of list
    totalcost = cost * x # pricing *  qty
    total = ("$"+str(totalcost) + ".00") # concatenates the pricing with a $ and .00
    print("Your total will be:", total)

    print("Would you like to order? Y/N")
    response = 'Y'
    #response = response.upper()
    #while response != 'Y' or response != 'N':
        #response = response.upper()
    if response == 'Y':
            #sendOrder(x, stockaboveNeeded, w, total)
            #break
            assert True
    elif response == 'N':
            #print("Program ending. Thank you.")
            #break
            assert False
    else:
            #response = (input("Invalid. Please select Y or N"))
            assert False

