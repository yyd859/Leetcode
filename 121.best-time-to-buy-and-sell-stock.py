#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # first try, passed most tests but if the prices list is too long, O(N2)will TLE
        # result = 0
        # for i in range(0,len(prices)):
        #     buy=prices[i]
        #     for j in range(i,len(prices)):
        #         sell = prices[j]
        #         if buy<sell and (sell-buy)>result:
        #             result=(sell-buy)
        # return result
        # second try, still TLE because min(buy_list) is still scanning the whole list
        # max_profit=0
        # buy_list=[]
        # for i in range(0,len(prices)):
        #     sell = prices[i]
        #     buy_list.append(sell)
        #     buy_lowest = min(buy_list)
        #     profit=sell - buy_lowest
        #     if profit>max_profit:
        #         max_profit=profit
        # return max_profit
        # third try, have buy_lowest to be very big intially and update it everytime finding a lower price
        max_profit=0
        buy_lowest=float('inf')
        for i in range(0,len(prices)):
            sell = prices[i]
            if buy_lowest>sell:
                buy_lowest = sell
            profit=sell - buy_lowest
            if profit>max_profit:
                max_profit=profit
        return max_profit
        # time complexity O(N); space complexity O(1)
# @lc code=end

