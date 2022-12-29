import textwrap

def wrap(string, max_width):
    length = len(string)
    ans = ""
    # for i in range(length):
    #     ans += string[i]
    #     if i!= 0 and (i+1) % max_width == 0:
    #         ans += "\n"
    wrapper = textwrap.TextWrapper(width = max_width)
    word_list = wrapper.wrap(text = string)
    for i in word_list:
        ans += i
        ans += "\n"   
    return ans

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
