#!/usr/bin/env python3
import re
import sys
from typing import List

def die(msg: str):
    sys.stderr.write(f"{msg}\n");
    print("false")
    sys.exit(1)


# Cannot use str as variable because is a reserved word =/
def dots(text: str):
    if re.search(r'^([a-zA-Z\.]|(?<!\d)\d(?!\d))*$', text):
        numbers: List[int] = [int(d) for d in re.sub(r'\D', '', text)]

        step: int
        for step in range(0, len(numbers), 2):
            if 10 > sum(numbers[step:step + 2]):
                die("The pairs doesn't add up to 10.")

        if re.search(r'(\d.*?(\.\.\.).*?\d)', text):
            print("true")
        else:
            die(
                "Cannot match exactly 3 dots between every pair of two numbers "
                "that add up to 10."
            )
    else:
        die(
            "The parameter contain single digit numbers, letters, and dots "
            "and check if there are exactly 3 dots between every pair of two "
            "numbers that add up to 10"
        )


if __name__ == "__main__":
    dots(sys.argv[1])