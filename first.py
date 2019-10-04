#!/usr/bin/env python3

if __name__ == "__main__":
    n: bool
    for n in range(50, 151):
        m5: bool = n % 5 == 0
        m7: bool = n % 7 == 0

        if m5 and m7:
            print("FooBar")
        elif m7:
            print("Bar")
        elif m5:
            print("Foo")
        else:
            print(n)