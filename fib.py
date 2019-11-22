# fibonacci.py

def fib():
    fibs = [1,2]

    for i in range(1,9):

        '''
        implement Fibonacci sequence to calculate the
        first 10 Fibonacci numbers, note Fn = Fn-1 + Fn-2
        '''

        fibn = fibs[i] + fibs[i-1]
        fibs.append(fibn)

        return fibs

def main():
    print('OUTPUT', fib())

if __name__ == "__main__":
    main()
