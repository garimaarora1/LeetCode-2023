class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = [i for i in range(len(accounts))]
        
        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent_x = find(x)
            parent_y = find(y)
            if parent_x != parent_y:
                if parent_x < parent_y:
                    parent[parent_y] = parent_x
                else:
                    parent[parent_x] = parent_y
                return True
            return False
        
        email_groups = defaultdict(int)
        for i, account in enumerate(accounts):
            name = account[0]
            for email in account[1:]:
                if email not in email_groups:
                    email_groups[email] = i
                else:
                    union(email_groups[email], i)
        print(email_groups)
        print(parent)
        merged_accounts_dict = defaultdict(list)
        
        for key, value in email_groups.items():
            parent_idx = find(value)
            merged_accounts_dict[parent_idx].append(key)
        
        merged_accounts_list = []
        
        for key, value in merged_accounts_dict.items():
            account = []
            value = sorted(value)
            parent_name = accounts[key][0]
            account.append(parent_name)
            account.extend(value)
            merged_accounts_list.append(account)
        
        return merged_accounts_list
                