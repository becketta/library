# The median of M numbers is defined as the middle number after sorting them in order
# if M is odd. Or it is the average of the middle two numbers if M is even. You start
# with an empty number list. Then, you can add numbers to the list, or remove existing
# numbers from it. After each add or remove operation, output the median.

# Input Format

# The first line is an integer, N, that indicates the number of operations. Each of the
# next N lines is either a x or r x. a x indicates that x is added to the set, and r x
# indicates that x is removed from the set.

# Constraints: 0

# Output Format

# For each operation: If the operation is add, output the median after adding x in a
# single line. If the operation is remove and the number x is not in the list, output
# Wrong! in a single line. If the operation is remove and the number x is in the list,
# output the median after deleting x in a single line. (If the result is an integer
# DO NOT output decimal point. And if the result is a real number, DO NOT output
# trailing 0s.)

# NOTE: If your median is 3.0, print only 3. And if your median is 3.50, print only 3.5.
# Whenever you need to print the median and the list is empty, print Wrong!


from bisect import bisect_left, insort

left = []
right = []
med = float('inf')

N = int(input().strip())
for _ in range(N):
    op,val = input().strip().split()
    val = int(val)
    
    ok = True
    if op == 'r':
        if val <= med:
            i = bisect_left(left, val)
            if i != len(left) and left[i] == val:
                del left[i]
            else:
                ok = False
        else:
            i = bisect_left(right, val)
            if i != len(right) and right[i] == val:
                del right[i]
            else:
                ok = False
        if not left and not right:
            med = float('inf')
            ok = False
    elif op == 'a':
        if val <= med:
            insort(left, val)
        else:
            insort(right, val)
    
    # Rebalance lists
    if len(left) - len(right) == 2:
        val = left.pop()
        right.insert(0, val)
    elif len(right) - len(left) == 1:
        left.append(right[0])
        right = right[1:]
    
    # Calculate and print median
    if not ok:
        print("Wrong!")
    else:
        if len(left) > len(right):
            med = left[-1]
        else:
            med = (left[-1] + right[0]) / 2
            if med % 1 == 0:
                med = int(med)
        print(med)