class Solution:
    def reduce(self, email):
        email = email.split('@')
        email[0] = email[0].split('+')[0]
        email[0] = email[0].replace('.', '')
        # print(email)

        return '@'.join(email)
   
    def numUniqueEmails(self, emails: List[str]) -> int:
        return len(set([self.reduce(x) for x in emails]))