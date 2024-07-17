class Solution {
    public int maxProfit(int[] prices) {
        int buyPrice1 = Integer.MAX_VALUE;
        int buyPrice2 = Integer.MAX_VALUE;
        int maxPrice1 = 0;
        int maxPrice2 = 0;
        for (int i = 0; i < prices.length; i++) {
            buyPrice1 = Math.min(buyPrice1, prices[i]);
            maxPrice1 = Math.max(maxPrice1, prices[i]-buyPrice1);
            buyPrice2 = Math.min(buyPrice2, prices[i]-maxPrice1);
            maxPrice2 = Math.max(maxPrice2, prices[i]-buyPrice2);
        }
        return maxPrice2;
        
    }
}