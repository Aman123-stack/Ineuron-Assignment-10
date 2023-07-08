q1>def isPowerOfThree(n):
    while n > 1:
        if n % 3 != 0:
            return False
        n /= 3
    return n == 1

q2>def lastRemaining(n):
    left_to_right = True
    remaining = n
    step = 1
    head = 1

    while remaining > 1:
        if left_to_right or remaining % 2 == 1:
            head += step

        remaining //= 2
        step *= 2
        left_to_right = not left_to_right

    return head
q3>def printSubsets(s, curr="", index=0):
    if index == len(s):
        print(curr)
        return

    # Exclude current element
    printSubsets(s, curr, index + 1)

    # Include current element
    printSubsets(s, curr + s[index], index + 1)

# Test the function
printSubsets("abc")

q4>def calculateLength(s):
    if s == "":
        return 0
    else:
        return 1 + calculateLength(s[1:])

# Test the function
print(calculateLength("Hello, World!"))  # Output: 13

q5>def countSubstrings(s):
    count = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[i] == s[j]:
                count += 1
    return count

# Test the function
print(countSubstrings("abc"))  # Output: 3
q6>def towerOfHanoi(n, source, target, auxiliary):
    if n == 1:
        print("Move disk 1 from rod", source, "to rod", target)
        return 1

    moves = 0
    moves += towerOfHanoi(n - 1, source, auxiliary, target)  # Move n-1 disks from source to auxiliary
    print("Move disk", n, "from rod", source, "to rod", target)
    moves += 1
    moves += towerOfHanoi(n - 1, auxiliary, target, source)  # Move n-1 disks from auxiliary to target

    return moves

# Test the function
n = 3
total_moves = towerOfHanoi(n, 1, 3, 2)
print("Total moves:", total_moves)
q7>def permute(s, left, right):
    if left == right:
        print("".join(s))
    else:
        for i in range(left, right + 1):
            s[left], s[i] = s[i], s[left]  # Swap characters
            permute(s, left + 1, right)  # Recursively find permutations of remaining characters
            s[left], s[i] = s[i], s[left]  # Backtrack (restore the original order)

# Test the function
s = "abc"
permute(list(s), 0, len(s) - 1)
q8>def countConsonants(s):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count = 0
    for char in s:
        if char in consonants:
            count += 1
    return count

# Test the function
print(countConsonants("Hello, World!"))  # Output: 7
