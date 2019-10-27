

def string_len():
    name = input("What's your name? ")
    print("Nice to meet you " + name + "!")
    x = 0
    # string length without space
    for i in name:
       if i !=(' '):
         x+=1

    print (x)













if __name__ == '__main__':
  string_len()