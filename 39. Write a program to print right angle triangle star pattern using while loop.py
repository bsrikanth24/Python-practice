"""
Description:
In this program nested loop concept is used.
"""

i = 1
while i <= 5:
    j = 1
    while j <= i:
        print('*', end=" ")
        j += 1
    print()
    i += 1