class Solution(object):
  def lengthOfLongestSubstring(self, s):
    i = 0
    j = 0
    d = {}
    ans = 0
    while j < len(s):
        if s[j] not in d or i > d[s[j]]:
            ans = max(ans, (j - i + 1))
            d[s[j]] = j
        else:
            i = d[s[j]] + 1
            ans = max(ans, (j - i + 1))
            j -= 1
        # print(ans)
        j += 1
    return ans


# ob1 = Solution()
# print(ob1.lengthOfLongestSubstring("ABCADECCDCCD"))


def multiply(x,y):
    product = x * y
    return product
num = multiply(2,4)
print(num)


def multiply(x, y):
"""Return the product of two numbers x and y."""
product = x * y
return product

