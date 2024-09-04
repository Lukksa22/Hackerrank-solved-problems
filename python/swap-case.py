def swap_case(s):
    string1 = ''
    for c in s:
        if c.islower():
            string1 += c.upper()
        else:
            string1 += c.lower()
    return string1

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)