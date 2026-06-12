class Solution(object):
    def isValid(self, s):
        n = len(s)
        se = []
        for i in s:
            if len(se) != 0:
                if ord(i) == ord(se[(len(se)) - 1]) + 1 or ord(i) == ord(se[(len(se)) - 1]) + 2:
                    se.pop()
                else:
                    se.append(i)
            else:
                se.append(i)
        if not se:
            return True
        return False

        