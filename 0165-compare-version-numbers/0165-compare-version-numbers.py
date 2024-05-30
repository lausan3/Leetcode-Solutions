class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # O(n) where n = max(len(version1, version2)) O(2n) space
        
        ver1Arr, ver2Arr = version1.split('.'), version2.split('.')
        ver1Len, ver2Len = len(ver1Arr), len(ver2Arr)
        i = 0

        # make sure the arrays are the same length
        if ver1Len != ver2Len:
            if ver1Len > ver2Len:
                ver2Arr.extend(["0" for i in range(ver1Len - ver2Len)])
            else:
                ver1Arr.extend(["0" for i in range(ver2Len - ver1Len)])

        # compare the version revisions
        for i in range(len(ver1Arr)):
            one, two = int(ver1Arr[i]), int(ver2Arr[i])

            if one < two:
                return -1
            elif one > two:
                return 1
        
        return 0