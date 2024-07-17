class Solution {
    public int maxProfit(int[] prices) {
        int buyPrice = prices[0];
        int maxProfit = 0;

        int n = prices.length;

        for (int i = 1; i < n; i++) {
            if(prices[i] < buyPrice) buyPrice = prices[i];
            else maxProfit = Math.max(maxProfit, prices[i]-buyPrice);
        }

        return maxProfit;
    }
}