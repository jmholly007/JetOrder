from pytest import mark

# run this test with the following in terminal "pytest -m wave -v"'
@mark.wave
def test_sendOrder():
    # qty = quantity
    # x = stockaboveNeeded
    # PN = part Number
    # total = total cost

    # print("Purchase Order complete for ", x[0][1], "pc(s) from", x[0][0])
    SUBJECT = 'HOT ORDER'
    '''message1 = """
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
    '''

    x = ['Home Goods']
    if x[0] == 'Home Depot':
        # server.sendmail("joshuahollytest@gmail.com", "jm.holly007@gmail.com", EMAILMESSAGE)
        # print("Email was sent to: jm.holly007@gmail.com. This program is complete.")
        assert True
    elif x[0] == 'Lowes':
        # server.sendmail("joshuahollytest@gmail.com", "jm.holly007@gmail.com", EMAILMESSAGE)
        # print("Email was sent to: jm.holly007@gmail.com. This program is complete.")
        assert True
    elif x[0] == 'Ace Hardware':
        # server.sendmail("joshuahollytest@gmail.com", "jm.holly007@gmail.com", EMAILMESSAGE)
        # print("Email was sent to: jm.holly007@gmail.com. This program is complete.")
        assert True
    elif x[0] == 'Walmart':
        # server.sendmail("joshuahollytest@gmail.com", "jm.holly007@gmail.com", EMAILMESSAGE)
        # print("Email was sent to: jm.holly007@gmail.com. This program is complete.")
        assert True
    elif x[0] == 'Target':
        # server.sendmail("joshuahollytest@gmail.com", "jm.holly007@gmail.com", EMAILMESSAGE)
        # print("Email was sent to: jm.holly007@gmail.com. This program is complete.")
        assert True
    elif x[0] == 'Academy':
        # server.sendmail("joshuahollytest@gmail.com", "jm.holly007@gmail.com", message1)
        # print("Email was sent to: jm.holly007@gmail.com. This program is complete.")
        assert True
    else:
        assert False
