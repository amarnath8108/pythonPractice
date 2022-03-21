def is_prime(number):
    count=0
    for i in range(1,number+1):
        if(number % i == 0):
           count=count+1
    print(count==2)

if __name__ == '__main__':
    num = int(input("Enter the input value to check prime or not : "))
    is_prime(num)