# fibonacci.py

def fib():
    fibs = [1, 2]

    for i in range(1,9):
        #Some sort of code kinda like this but not this: fibs += fibs[i] + fibs[i-1]

    return fibs

def main():
    print('OUTPUT', fib())

'''if __name__ == "__main__":
    main()'''

print(fib())
