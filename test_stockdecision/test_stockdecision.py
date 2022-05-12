from pytest import mark

#run this test with the following in terminal "pytest -m water -v"'
@mark.water
def test_stockdecision():
    partNumber = 2222
    if partNumber == 1111 or 2222 or 3333 or 4444 or 5555:
        if partNumber == 1111:
            assert True
        elif partNumber == 2222:
            assert True
        elif partNumber == 3333:
            assert True
        elif partNumber == 4444:
            assert True
        elif partNumber == 5555:
            assert True
        else:
            assert False
    else:
        assert False
