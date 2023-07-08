from main import Add

def Add_test():
    assert Add(2,3) == 5
    print("Add function work correctly")

if __name__ == "__main__":
    Add_test()