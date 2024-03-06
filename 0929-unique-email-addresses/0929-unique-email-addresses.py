class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res_set = set()
        for email in emails:
            idx = email.index("@")
            print(idx)
            res = ''
            i = 0
            while i < len(email):
                if i< idx and email[i] == '+':
                    i = idx
                if i< idx and email[i] != '.':
                    res += email[i]
                elif i >= idx:
                    res += email[i]
                i += 1
            res_set.add(res)
        print(res_set)
        return len(res_set)
        