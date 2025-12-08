#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    #first try, failed
    def coinChange(self, coins: List[int], amount: int) -> int:
        # coins = sorted(coins,reverse=True)
        # count = 0
        # for value in coins:
        #     count = count + amount//value
        #     amount = amount - amount//value * value
        #     if amount % value == 0:
        #         return count
        # return -1
    #hint: use the dynamtic programming
        dp=[-1]*(amount+1)
        dp[0]=0
        for i in range(1,amount+1):
            cand_list=[]
            for coin in coins:
                j = i - coin
                if j>=0 and dp[j]!=-1:
                    cand_list.append(dp[j]+1)
            if len(cand_list)>0:
                dp[i]=min(cand_list)
        return dp[amount]
    # success, but can sort coins and if coin>i skip




# @lc code=end

