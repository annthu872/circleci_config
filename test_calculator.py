from calculator import Add

def Add_test():
    assert Add(2,3) == 5
    assert Add(-1,5) == 4
    assert Add(0,0) == 0
    assert Add(10,-5) == 5
    assert Add(3.14,1.86) ==5.0
    assert Add(1000000,1) ==1000001
    assert Add(100,200) == 300
    assert Add(-10,-20) ==-30
    assert Add(0.5,0.5) == 1.0
    assert Add(9999999999999999,1) == 10000000000000000

    print("Test successfully")

if __name__ =="__main__":
    Add_test()