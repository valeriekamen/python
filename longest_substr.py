import argparse


def main():
    parser = argparse.ArgumentParser(description='Longest substr')
    parser.add_argument('--string', help='input str')

    args = parser.parse_args()

    if not args.string:
        return ''

    longest = longest_substr(args.string)
    print(longest)
    return longest

def longest_substr(string):
    
    longest_pair = (0,1)

    for u in set(string):
        #abca a = 0,3
        print('u is', u)
        all_i = [i for i, ltr in enumerate(string) if ltr == u or i == len(string)-1]
        print(all_i)
        
        strs = [string[all_i[i]:all_i[i+1]] for i in range(len(all_i)-1)]

        print('strs', strs)
        print('max', max(strs, key=len))

        # n is index of letters
        # i is position in all_i
    #     for i, n in enumerate(all_i):
    #         longest_len = longest_pair[1] - longest_pair[0]
    #         try:
    #             if all_i[i + 1] - n > longest_len:
    #                 longest_pair = (n, all_i[i+1])

    #         except Exception:
    #             if (len(string) - 1) - n > longest_len:
    #                 longest_pair = (n, len(string) - 1)

    # print(string[longest_pair[0]: longest_pair[1]])

# def longest_substr(string):

#     letters_with_longest = {}
    
#     for u in set(string):
#         #abca a = 0,3
#         all_i = [i for i, ltr in enumerate(string) if ltr == u]
#         return_strings = []
        
#         for i in all_i:

#             str_len = len(string) - 1
#             if i == str_len: #letter is already last in str
#                 return_strings.append(u)
#                 break

#             current = u
            
#             for n in range(i+1, len(string)):                
#                 if string[n] not in current:
#                     current += string[n]
#                     if n == str_len:
#                         return_strings.append(current) 
#                         break
#                     n += 1
#                 else:
#                     return_strings.append(current)
#                     break

#         letters_with_longest[u] = max(return_strings)
    
#     return max(letters_with_longest.values(), key=len)


if __name__ == '__main__':
    main()
