#!/usr/bin/env python3
def main():
    num = int(input("Enter a number:"))

    for i in range(10):
        print(f"{i} x {num} = {i * num}")

if __name__ == "__main__":
    main()