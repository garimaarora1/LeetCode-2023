class Solution {
    public int passThePillow(int n, int time) {
        int direction = time / (n-1);
        int additionalPeople = time % (n-1);
        
        if (direction % 2 == 0)
            return 1 + additionalPeople;
        return n - additionalPeople;
    }
}