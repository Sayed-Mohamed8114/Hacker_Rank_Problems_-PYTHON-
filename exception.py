#catch the error that will appear and show it to the user 

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        try:
            num1, num2 = input().split()
            num1 = int(num1)
            num2 = int(num2)
            print(num1 // num2)
        except ZeroDivisionError:
            print("Error Code: integer division or modulo by zero")
        except ValueError as e:
            print(f"Error Code: {e}")