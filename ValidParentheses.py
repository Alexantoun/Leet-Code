class Solution:
    def isValid(self, s: str) -> bool:
        parenth = 0
        brack = 0
        brace = 0
        for x in range(0,len(s)):
            print(x)
            
        for x in range(0, len(s)):
            if x == "(":
                parenth+=1
            elif x == ")":
                parenth-=1
            elif x=="[":
                brack+=1
            elif x=="]":
                brack-=1
            elif x=="{":
                brace+=1
            elif x=="}":
                brace-=1
            if brack < 0 or parenth < 0 or brace < 0:
                print("false")
                break

        if brack==0 and parenth==0 and brace==0:
            print("true")
        else:
            print("false")
        
            
        