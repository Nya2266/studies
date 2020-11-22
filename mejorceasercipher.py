abc = ("abcdefghijklmnñopqrstuvwxyz")
cipher = ""
step = 0
post_cipher = ""

def InitData():
    global cipher, step
    cipher = input("Message to cipher")
    try:
        step = int(input("Choose the step to cipher 1-25 steps"))
    except ValueError: print("Please introduce an integer between 1 and 25"), InitData()
    except: print("Unknown error please try again"), InitData()
    if step > 0 and step < 26:
        pass
    else:
        print("Incorrect data please try again")
        InitData()


def cipher_now(cipher, step):
    for i in cipher:
        pos = abc.index(i)


abclist =
