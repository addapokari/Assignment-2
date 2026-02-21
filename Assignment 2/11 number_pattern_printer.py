# This program prints four different number patterns based on the height provided by the user.
def pattern1 (height):
    for i in range(1, height + 1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()     
def pattern2 (height):
    for i in range(1, height + 1):
        for j in range(i, 0, -1):
            print(j, end=' ')
        print()
def pattern3 (height):
    for i in range(1, height + 1):
        for j in range(1, i + 1):
            print('*', end=' ')
        print()
def pattern4 (height):
    for i in range(1, height + 1):
        for j in range(i, 0, -1):
            print('*', end=' ')
        print()
def main():
    height = int(input("Enter the height of the patterns: "))
    print("\nPattern 1:")
    pattern1(height)
    print("\nPattern 2:")
    pattern2(height)
    print("\nPattern 3:")
    pattern3(height)
    print("\nPattern 4:")
    pattern4(height)
if __name__ == "__main__":    main()
