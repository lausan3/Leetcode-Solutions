class Solution:
    def decodeString(self, s: str) -> str:
        result = temp = mul = ""
        num = []
        st = []

        for i in range(len(s)):
            if "0" <= s[i] <= "9":
                mul += s[i]
            elif s[i] == "[":
                st.append(result)
                num.append(int(mul))
                mul = result = ""
            elif s[i] == "]":
                temp = result
                result += result * (num.pop() - 1)
                result = st.pop() + result
            else:
                result += s[i]

        return result

