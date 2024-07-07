class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int len = temperatures.length;
        Stack<int[]> stack = new Stack<>();
        int arr[] = new int[len];
        
        for(int i = len-1 ; i>=0 ; i -- ) {
   
            while(!stack.isEmpty() && stack.peek()[0] <= temperatures[i]) {
                stack.pop();
            }
            
            if (!stack.isEmpty())
                arr[i] = stack.peek()[1] - i;
                
            stack.push(new int[] {temperatures[i], i});
            }
        
        return arr;
    }
}