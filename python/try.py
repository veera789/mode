print("stmt1")
try:
    print(10/0)
    expect zeroDivisionError:
        print(10/2)
        print("stmt3")
