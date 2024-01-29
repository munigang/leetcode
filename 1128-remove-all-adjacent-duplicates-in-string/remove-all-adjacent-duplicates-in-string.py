class Solution:
    def removeDuplicates(self, s: str) -> str:
        lst=[]
        for char in s:
            if lst:
                if lst[-1]==char:
                    lst.pop()
                else:
                    lst.append(char)
            else:
                lst.append(char)
        lst=''.join(lst)
        return lst


        

        