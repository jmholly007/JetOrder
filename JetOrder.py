import smtplib
import xlrd  # allows us to read from an excel file

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)  # set up email application
server.login("joshuahollytest@gmail.com", "password placeholder - not valid")  # python projects email address

supplierspath = 'C:\Python38\PythonSpreadsheets\CS5374_Project_Suppliers.xlsx'  # set up path to pull suppliers stock count

inputWorkbookSuppliers = xlrd.open_workbook(supplierspath)  # Pulls supplier's stock count
inputWorksheetSuppliers = inputWorkbookSuppliers.sheet_by_index(0)

supplierPricing = 'C:\Python38\PythonSpreadsheets\CS5374_Project_Pricing.xlsx'  # set up path to pull pricng of parts
inputWorkbookPricing = xlrd.open_workbook(supplierPricing)  # Pulls supplier's stock count
inputWorksheetPricing = inputWorkbookPricing.sheet_by_index(0)


def askForUserID():
    count = 0
    triesleft = 3
    while triesleft != 0:
        userID = input("Please enter your user ID to authenticate: ")
        userID = int(userID)
        if userID == 123456:
            print("Correct User ID: ", userID)
            askForPartNumber()
            break
        elif userID == 123457:
            print("Correct User ID: ", userID)
            askForPartNumber()
            break
        elif userID == 123458:
            print("Correct User ID: ", userID)
            askForPartNumber()
            break
        else:
            count = count + 1
            triesleft = triesleft - 1
            print("Incorrect. Tries left: ", triesleft)
            if triesleft == 0:
                print("End of Tries.")
                break


def askForPartNumber():
    global partNumber
    partNumber = int(input("Please enter the part number you would like to order."))
    stockdecision(partNumber)


def stockdecision(partNumber):
    if partNumber == 1111 or 2222 or 3333 or 4444 or 5555:
        if partNumber == 1111:
            oneoneoneone()
        elif partNumber == 2222:
            twotwotwotwo()
        elif partNumber == 3333:
            threethreethreethree()
        elif partNumber == 4444:
            fourfourfourfour()
        elif partNumber == 5555:
            fivefivefivefive()
        else:
            print("Please enter a valid PN.")
            askForPartNumber()
    else:
        askForPartNumber()



def oneoneoneone():
    vendor = []  # creates list
    qty = []  # creates list
    for i in range(1, 7):
        vendor.append(str(inputWorksheetSuppliers.cell(0, i).value))  # first digit is row, second is column
    for i in range(1, 7):
        qty.append(int(inputWorksheetSuppliers.cell(1, i).value))

    pn = 1111
    askForQtyNeeded(qty, vendor, pn)  # pass vendor and qty list


def twotwotwotwo():
    vendor = []  # creates list
    qty = []  # creates list
    for i in range(1, 7):
        vendor.append(str(inputWorksheetSuppliers.cell(0, i).value))  # first digit is row, second is column
    for i in range(1, 7):
        qty.append(int(inputWorksheetSuppliers.cell(2, i).value))

    pn = 2222
    askForQtyNeeded(qty, vendor, pn)  # pass vendor and qty list


def threethreethreethree():
    vendor = []  # creates list
    qty = []  # creates list
    for i in range(1, 7):
        vendor.append(str(inputWorksheetSuppliers.cell(0, i).value))  # first digit is row, second is column
    for i in range(1, 7):
        qty.append(int(inputWorksheetSuppliers.cell(3, i).value))

    pn = 3333

    askForQtyNeeded(qty, vendor, pn)  # pass vendor and qty list


def fourfourfourfour():
    vendor = []  # creates list
    qty = []  # creates list
    for i in range(1, 7):
        vendor.append(str(inputWorksheetSuppliers.cell(0, i).value))  # first digit is row, second is column
    for i in range(1, 7):
        qty.append(int(inputWorksheetSuppliers.cell(4, i).value))

    pn = 4444

    askForQtyNeeded(qty, vendor, pn)  # pass vendor and qty list


def fivefivefivefive():
    vendor = []  # creates list
    qty = []  # creates list
    for i in range(1, 7):
        vendor.append(str(inputWorksheetSuppliers.cell(0, i).value))  # first digit is row, second is column
    for i in range(1, 7):
        qty.append(int(inputWorksheetSuppliers.cell(5, i).value))

    pn = 5555

    askForQtyNeeded(qty, vendor, pn)  # pass qtylist, vendor list, part number


def askForQtyNeeded(x, y, z):
    # x = qtys
    # y = vendors
    # z = PN
    PN = z
    c = [item for t in zip(y, x) for item in
         t]  # intertwines vendor and qty lists to make 1 new list ex. [Acehardware, 1, Homedepot, 3..etc]
    n = 2
    final = [c[i * n:(i + 1) * n] for i in range((len(
        c) + n - 1) // n)]  # seprates vendor and qty into new lists. ex. [['Home Depot', 1], ['Lowes', 55], ['Ace Hardware', 0]]
    cleanlist = [item for item in final if item[
        1] >= 1]  # removes vendor/qty if the qty is 0. Then creates new list with only vendor's with avialable qty
    print("Available quantities: ")
    for xp in cleanlist:
        print("Vendor:", xp[0], "Qty:", xp[1])

    global qtyNeeded
    qtyNeeded = input("Please enter the qty you require: ")
    qtyNeeded = int(qtyNeeded)
    maxNum = max(x)  # takes the largest number from list of Qty's available to procure
    while qtyNeeded <= 0 or qtyNeeded >= maxNum:
        if qtyNeeded >= 1 and qtyNeeded <= maxNum:
            break
        else:
            print("Invalid. Please select a number great than 0 and less than or equal to", maxNum, ".")
            qtyNeeded = input()
            qtyNeeded = int(qtyNeeded)
            break

    print("You have selected qty: ", qtyNeeded)
    print("Is this correct? Y/N")
    response = input()
    response = response.upper()
    while response != 'Y' or response != 'N':
        if response == 'Y':
            break
        elif response == 'N':
            askForQtyNeeded(x, y)
            break
        else:
            response = (input("Invalid. Please select Y or N"))
            break

    orderQty(PN, qtyNeeded, cleanlist, maxNum)


def orderQty(w, x, y, z):
    # w = PN
    # x = qtyneeded
    # y = cleanlist of available suppliers
    # z = maxNum

    stockaboveNeeded = [item for item in y if item[1] == z]  # removes any supplier who doesn't have enough of qtyNeeded
    print("Jet Order is able to  order qty:", x, "as it appears", stockaboveNeeded[0][0], "has", stockaboveNeeded[0][1],
          "pc(s) in stock available.")

    pricing = []  # sets up string to pull pricing from CS5374_Project_Pricing.xlsx
    if w == 1111:
        row = 1
    elif w == 2222:
        row = 2
    elif w == 3333:
        row = 3
    elif w == 4444:
        row = 4
    elif w == 5555:
        row = 5
    pricing.append(int(inputWorksheetPricing.cell_value(row, 1)))  # (row, column) inserts stat from excel spreadsheet
    cost = pricing[0]  # pulls pricing out of list
    totalcost = cost * x  # pricing *  qty
    total = ("$" + str(totalcost) + ".00")  # concatenates the pricing with a $ and .00
    print("Your total will be:", total)

    print("Would you like to order? Y/N")
    response = input()
    response = response.upper()
    while response != 'Y' or response != 'N':
        response = response.upper()
        if response == 'Y':
            sendOrder(x, stockaboveNeeded, w, total)
            break
        elif response == 'N':
            print("Program ending. Thank you.")
            break
        else:
            response = (input("Invalid. Please select Y or N"))


def sendOrder(qty, x, PN, total):
    # qty = quantity
    # x = stockaboveNeeded
    # PN = part Number
    # total = total cost

    print("Purchase Order complete for ", x[0][1], "pc(s) from", x[0][0])
    SUBJECT = 'HOT ORDER'
    message1 = """
    Good day,
    
    This is JetOrder from SpaceX with an order for """ + str(x[0][0]) + """.
    
    We have an urgent need for the following:
    
    """ + "Part Number: " + str(PN) + ' | Qty: ' + str(qty) + """
    """ + "Cost: " + str(total) + """

    Please overnight the product to the following address:
    
    Space Exploration Technologies Corp
    12259 Crenshaw Blvd, Hawthorne, CA 90250
    
    Please reply back with tracking when shipment is complete. 
    If you have any questions, please contact the following:
    
    Elon Musk 
    999-999-9999
    """
    print("Email sent to supplier: ", message1)  # shows the user the email that was sent to the supplier
    EMAILMESSAGE = 'Subject: {}\n\n{}'.format(SUBJECT, message1)  # creates the subject line of the email

    if x[0][0] == 'Home Depot':
        server.sendmail("joshuahollytest@gmail.com", "jm.holly007@gmail.com", EMAILMESSAGE)
        print("Email was sent to: jm.holly007@gmail.com. This program is complete.")
    elif x[0][0] == 'Lowes':
        server.sendmail("joshuahollytest@gmail.com", "jm.holly007@gmail.com", EMAILMESSAGE)
        print("Email was sent to: jm.holly007@gmail.com. This program is complete.")
    elif x[0][0] == 'Ace Hardware':
        server.sendmail("joshuahollytest@gmail.com", "jm.holly007@gmail.com", EMAILMESSAGE)
        print("Email was sent to: jm.holly007@gmail.com. This program is complete.")
    elif x[0][0] == 'Walmart':
        server.sendmail("joshuahollytest@gmail.com", "jm.holly007@gmail.com", EMAILMESSAGE)
        print("Email was sent to: jm.holly007@gmail.com. This program is complete.")
    elif x[0][0] == 'Target':
        server.sendmail("joshuahollytest@gmail.com", "jm.holly007@gmail.com", EMAILMESSAGE)
        print("Email was sent to: jm.holly007@gmail.com. This program is complete.")
    elif x[0][0] == 'Academy':
        server.sendmail("joshuahollytest@gmail.com", "jm.holly007@gmail.com", message1)
        print("Email was sent to: jm.holly007@gmail.com. This program is complete.")

    runAgain()


def runAgain():
    print("Would you like to run the program again again? Y/N")
    response = input()
    if response == "Y":
        askForPartNumber()
    else:
        print("Thank you for using JetOrder. This will complete the program.")


### START OF PROGRAM
print("Hello, welcome to Jet Order.")
askForUserID()  # begins program

server.quit()  # ends the email application
