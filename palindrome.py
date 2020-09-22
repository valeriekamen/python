import math

"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]

Input: "aabaa"
Output: [["a","a","b","a","a"],["a","a","b","aa"],["a","aba","a"],["aa","b","a","a"],["aa","b","aa"],["aabaa"]]
"""


class Palindrome:
    def __init__(self, s):
        self.s = s
        self.res = []
        self.pals = {}

    def check_if_pal(self, s):
        r = math.floor(len(s) / 2)
        for i in range(r):
            if s[i] != s[-(i + 1)]:
                return False
        return True

    def make_into_str_list_and_append(self, alist):
        output = []
        for item in alist:
            astr = self.s[item[0] : item[1]]
            output.append(astr)

        self.res.append(output)

    def recur(self, thislist, start, end):
        thislist.append((start, end))
        ends = self.pals.get(end)

        if not ends:
            print(thislist)
            self.make_into_str_list_and_append(thislist)
            return

        else:
            for e in ends:
                newlist = thislist.copy()
                self.recur(newlist, end, e)

    def get_all_pals(self):
        s_len = len(self.s)

        # create hashtable for all pals
        for i in range(s_len):
            for j in range(s_len):
                this_str = self.s[i : j + 1]
                if this_str and self.check_if_pal(this_str):
                    if i in self.pals:
                        self.pals[i].append(j + 1)
                    else:
                        self.pals[i] = [j + 1]

        print(self.pals)

        for end in self.pals.get(0):
            l = []
            self.recur(l, 0, end)

        print(self.res)


p = Palindrome("aabaa")
p.get_all_pals()


# def recur(res, newlist, end, start, pals):
#     newlist.append((start, end))
#     ends = pals.get(end)

#     print("START AND ENDS ", start, ends)
#     print("NEWLIST", newlist)
#     if not ends:
#         print("APPENDING")
#         res.append(newlist)

#     else:

#         for e in ends:
#             thislist = newlist
#             print("NEXT", thislist)
#             recur(res, thislist, e, end, pals)

#     newlist = []
#     return res


# def palindrome(s):
#     output = []
#     pals = {}
#     s_len = len(s)

#     # create hashtable for all pals
#     for i in range(s_len):
#         for j in range(s_len):
#             this_str = s[i : j + 1]
#             if this_str and check_if_pal(this_str):
#                 if i in pals:
#                     pals[i].append(j + 1)
#                 else:
#                     pals[i] = [j + 1]

#     print(pals)

#     for end in pals.get(0):
#         bigr = []
#         r = []
#         res = recur(bigr, r, end, 0, pals)
#         output.extend(res)

#     print(output)


# def check_if_pal(s):
#     r = math.floor(len(s) / 2)
#     for i in range(r):
#         if s[i] != s[-(i + 1)]:
#             return False
#     return True


# def recur(res, newlist, end, start, pals):
#     newlist.append((start, end))
#     ends = pals.get(end)

#     print("START AND ENDS ", start, ends)
#     print("NEWLIST", newlist)
#     if not ends:
#         print("APPENDING")
#         res.append(newlist)

#     else:

#         for e in ends:
#             thislist = newlist
#             print("NEXT", thislist)
#             recur(res, thislist, e, end, pals)

#     newlist = []
#     return res


# def palindrome(s):
#     output = []
#     pals = {}
#     s_len = len(s)

#     # create hashtable for all pals
#     for i in range(s_len):
#         for j in range(s_len):
#             this_str = s[i : j + 1]
#             if this_str and check_if_pal(this_str):
#                 if i in pals:
#                     pals[i].append(j + 1)
#                 else:
#                     pals[i] = [j + 1]

#     print(pals)

#     for end in pals.get(0):
#         bigr = []
#         r = []
#         res = recur(bigr, r, end, 0, pals)
#         output.extend(res)

#     print(output)


# palindrome("aabaa")


# # from someone else

# class Solution:
#     # @param s, a string
#     # @return a list of lists of string
#     def partition(self, s):
#         self.res = []
#         self.findPalindrome(s, [])
#         return self.res

#     def findPalindrome(self, s, plist):
#         if len(s) == 0:
#             self.res.append(plist)
#         for i in range(1, len(s) + 1):
#             if self.isPalindrome(s[:i]):
#                 self.findPalindrome(s[i:], plist + [s[:i]])

#     def isPalindrome(self, s):
#         if s == s[::-1]:
#             return True
#         else:
#             return False


# a = Solution()
# print(a.partition("aabaa"))
