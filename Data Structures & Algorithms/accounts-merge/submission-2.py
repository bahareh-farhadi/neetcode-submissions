class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emails_dict = dict()
        users_dict = dict()
        last_user_id = 0
        for account in accounts:
            username = account[0]
            dup_user = set()
            for i in range(1, len(account)):
                if account[i] in emails_dict:
                    dup_user.add(emails_dict[account[i]])
            if not dup_user:
                # create new user
                last_user_id+=1
                users_dict[last_user_id] = dict()
                users_dict[last_user_id]['name'] = username
                users_dict[last_user_id]['emails'] = set()
                for i in range(1, len(account)):
                    users_dict[last_user_id]['emails'].add(account[i])
                    emails_dict[account[i]] = last_user_id
            else:
                # merge duplicate users
                # use any user 
                staying_user = dup_user.pop()
                for other_user in dup_user:
                    for email in users_dict[other_user]['emails']:
                        users_dict[staying_user]['emails'].add(email)
                        emails_dict[email] = staying_user
                    del users_dict[other_user]
                for i in range(1, len(account)):
                    users_dict[staying_user]['emails'].add(account[i])
                    if account[i] not in emails_dict:
                        emails_dict[account[i]] = staying_user

        res = list()
        for key, val in users_dict.items():
            temp = list()
            temp.append(val['name'])
            temp.extend(sorted(val['emails']))
            res.append(temp)
        return res

                

                

            
        