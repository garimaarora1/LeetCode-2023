class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        int n = position.length;
        int[][] pairs = new int[n][2];
        for(int i = 0 ; i < n ; i++) {
            pairs[i][0] = position[i];
            pairs[i][1] = speed[i];
        }
        Arrays.sort(pairs, (a, b) -> Integer.compare(b[0], a[0]));
        
        Stack<Double> stack = new Stack<>();
        
        for(int[] pair : pairs) {
            int p = pair[0];
            int s = pair[1];
            
            double currTime = (double)(target-p)/s;
            
            if (stack.isEmpty() || currTime > stack.peek()) {
                stack.push(currTime);
            }
        }
        
        return stack.size();
    }
}