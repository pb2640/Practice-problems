class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ans = set()
        for email in emails:
            #first read left part
            left = ""
            right = ""
            for letter in email:
                if(letter=="+" or letter=="@"):
                    break
                elif(letter=="."):
                    continue
                else:
                    left+=letter
            for i in range(len(email)-1,-1,-1):
                if(email[i]=="@"):
                    right = email[i]+right
                    break
                else:
                    right = email[i]+right
            
            ans.add(left+right)
        return(len(ans))