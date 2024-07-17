class Solution {
    public int maxProfit(int k, int[] prices) {
        int[] buyPrice = new int[k];
        for (int i = 0; i < k; i++) {
            buyPrice[i] = Integer.MAX_VALUE;
        }
        int[] maxProfit = new int[k];
        for(int i = 0; i < prices.length; i++){
            for(int j = 0; j<k; j++) {
                if(j == 0) buyPrice[j] = Math.min(buyPrice[j], prices[i]);
                else buyPrice[j] = Math.min(buyPrice[j], prices[i]-maxProfit[j-1]);
                maxProfit[j] = Math.max(maxProfit[j], prices[i]-buyPrice[j]);
            }
        }
        return maxProfit[k-1];

        
    }
}