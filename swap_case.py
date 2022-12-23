def swap_case(s):
    word = ""
    for i in s:
        
        if ord(i) <ord('A')<ord('B'):
            word += i
        elif i.isupper():
            word += i.lower()
        elif i.islower():
            word += i.upper()
    return word

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
