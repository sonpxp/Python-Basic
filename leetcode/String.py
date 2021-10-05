class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup = {")": "(", "}": "{", "]": "["}

        for i in s:
            if i in lookup.values():
                stack.append(i)
            elif stack and lookup[i] == stack[-1]:
                stack.pop()
            else:
                print("False")
                return False

        print("True")
        return stack == []


if __name__ == '__main__':
    Solution.isValid(self=Solution(), s="()")
