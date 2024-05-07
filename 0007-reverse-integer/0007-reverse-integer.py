class Solution:
    def reverse(self, x: int) -> int:
        res = ""
        # save stringify'd int as positive integer
        stringedInt = str(x) if x >= 0 else str(x)[1:]

        for i in range(len(stringedInt) - 1, -1, -1):
            res += stringedInt[i]

        # get rid of leading 0s
        for i in range(len(res)):
            if res[i] != 0:
                break

            res = res[1:]

        # check for integer overflow:
        if int(res) > (1 << 31) - 1:
            return 0
            
        # check for negative
        return int(res) if x >= 0 else int("-" + res)