from pytest import mark


#run this test with the following in terminal "pytest -m smoke -v"'
@mark.smoke
def test_userID(): #testing the user ID input
    userID = 123459
    if userID == 123456:
        assert True
    elif userID == 123457:
        assert True
    elif userID == 123458:
        assert True
    else:
        assert False

#run this test with the following in terminal "pytest -m fire -v"'
@mark.fire
def test_userIDsecond():
    count = 0
    triesleft = 3
    while triesleft != 0:
        print("Please enter your user ID to authenticate: ")
        userID = 12357
        userID = int(userID)
        if userID == 123456:
            print("Correct User ID: ", userID)
            assert True
            break
        elif userID == 123457:
            print("Correct User ID: ", userID)
            assert True
            break
        elif userID == 123458:
            print("Correct User ID: ", userID)
            assert True
            break
        else:
            count = count + 1
            triesleft = triesleft - 1
            print("Incorrect. Tries left: ", triesleft)
            if triesleft == 0:
                assert False

