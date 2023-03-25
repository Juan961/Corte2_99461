from func import matrix_custom, recursive_custom, recursive_fibo 

def main():
    try:
        print("==================== Start Matrix Function ====================")
        matrix_custom()
        print("==================== End Matrix Function ====================")

        print("==================== Start Recursive Function ====================")
        n = int(input("Insert n: "))
        p = int(input("Insert p: "))
        print(recursive_custom(n, p))
        print("==================== End Recursive Function ====================")

        print("==================== Start Recursive Fibonacci Function ====================")
        number_of_fibbo = int(input("Insert the number of fibonacci to see: "))
        recursive_fibo(number_of_fibbo)
        print("==================== End Recursive Fibonacci Function ====================")

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
