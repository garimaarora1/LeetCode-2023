class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res_set = set()
        for email in emails:
            local_name, domain_name = email.split("@")
            local_name = local_name.split("+")[0]
            local_name = local_name.split('.')
            local_name = ''.join(local_name)
            new_email = local_name + "@" + domain_name
            res_set.add(new_email)
        print(res_set)
        return len(res_set)