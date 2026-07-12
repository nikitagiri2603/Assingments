import multiprocessing
import os

def CountPrime(no):
    count = 0

    for i in range(2, no + 1):
        flag = True

        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                flag = False
                break

        if flag:
            count += 1

    print("Process ID:", os.getpid(), " Number:", no, " Prime Count:", count)
    return count


def main():
    Data = [10000, 20000, 30000, 40000]

    pobj = multiprocessing.Pool()

    Result = pobj.map(CountPrime, Data)

    pobj.close()
    pobj.join()

    print("\nPrime Count for each number:")
    for no, primecount in zip(Data, Result):
        print(no, "->", primecount)


if __name__ == "__main__":
    main()