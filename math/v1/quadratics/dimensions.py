#!/usr/bin/env python3
# dimensions.py

"""Maximum area of rectangle:

        l
  ###############
w ############### w
  ###############
        l

P = 2w + 2l
A = wl

# maximum_area_of_rectangle(P,r=100,unit="cm") -> str
# sort_ans(a, b) -> int

"""

from functools import cmp_to_key

def sort_ans(a, b):
    if a["area"] < b["area"]:
        return 1
    elif a["area"] == b["area"]:
        return 0
    else:
        return -1


def maximum_area_of_rectangle(P, r=100, unit="cm"):
    answers = []
    for l in range(-1*r, r):
        for w in range(-1*r, r):
            if (l+l+w+w) == P:
                answers.append({"area": l*w, "l":l,"w":w})

    answers.sort(key=cmp_to_key(sort_ans))
    max_area, l, w = answers[0].values()
    return f"dims= ({l}{unit} by {w}{unit}), area= {max_area}{unit}²"


if __name__ == "__main__":
    from util import get_vars

    print("P = Perimeter")
    vars = get_vars({ "P":float })

    print(maximum_area_of_rectangle(**vars))
