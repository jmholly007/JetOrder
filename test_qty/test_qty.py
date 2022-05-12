from pytest import mark


# run this test with the following in terminal "pytest -m dirt -v"'
@mark.dirt
def test_qty():
    x = [75, 34, 56, 78]
    global qtyNeeded
    # qtyNeeded = input("Please enter the qty you require: ")
    qtyNeeded = 56
    # qtyNeeded = int(qtyNeeded)
    maxNum = max(x)  # takes the largest number from list of Qty's available to procure
    print(maxNum)
    while qtyNeeded <= 0 or qtyNeeded >= maxNum:
        if qtyNeeded >= 1 and qtyNeeded <= maxNum:
            assert True
        else:
            assert False
            # print("Invalid. Please select a number great than 0 and less than or equal to", maxNum, ".")
            # qtyNeeded = input()
            # qtyNeeded = int(qtyNeeded)


@mark.dirt
def test_approval():
    # print("You have selected qty: ", qtyNeeded)
    # print("Is this correct? Y/N")
    response = 'Y'
    # response = response.upper()
    # while response != 'Y' or response != 'N':
    if response == 'Y':
        assert True
    elif response == 'N':
        # askForQtyNeeded(x, y)
        assert False
    else:
        # response = (input("Invalid. Please select Y or N"))
        assert False
