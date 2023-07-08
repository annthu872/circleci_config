from main import Add

def Add_test():
    assert Add(2,3) == 5
    assert Add(4,6) == 100
    print("Test Add Function Success")

if __name__ =="__main__":
    Add_test()