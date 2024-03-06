class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        answer = 0
        for account in accounts:
            if answer <= sum(account):
                answer = sum(account)
        return answer
        