class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded=""
        for i in range(len(strs)):
            encoded +=str(len(strs[i]))+"#"+strs[i]
        
        return encoded
    def decode(self, s: str) -> List[str]:
        res=[]
        j=0
        i=0
        while j<len(s):
            if s[j]=="#":
                length = int(s[i:j])
                res.append(s[j+1:j+length+1])
                j+= length +1
                i = j
                
            else:
                j+=1
        return res



