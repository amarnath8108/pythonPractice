
def c_to_f():
    for i in range(0,21):
        Fahrenheit = ((9/5)*i) + 32
        print("{0}\t\t\t{1}".format(i,Fahrenheit))

if __name__ == '__main__':
    print("{0}\t\t{1}".format("Celsius","Fahrenheit"))
    c_to_f()