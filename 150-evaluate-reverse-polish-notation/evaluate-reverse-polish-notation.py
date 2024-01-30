class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        lst=[]
        for token in tokens:
            if token in "+-*/":
                num2=lst.pop()
                num1=lst.pop()
                if token=="+":
                    lst.append(num1+num2)
                elif token=="-":
                    lst.append(num1-num2)
                elif token=="*":
                    lst.append(num1*num2)
                elif token=="/":
                    lst.append(int(num1/num2))
            else:
                lst.append(int(token))
        return lst.pop()

        