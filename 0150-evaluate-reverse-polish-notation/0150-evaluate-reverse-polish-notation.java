class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        
        for (String token : tokens) {
            if ("+-/*".contains(token)) {
                int first = stack.pop();
                int second = stack.pop();
                int result = 0;
                switch(token) {
                    case "+":
                        result = second + first;
                        break;
                    case "-":
                        result = second - first;
                        break;
                    case "*":
                        result = second * first;
                        break;
                    case "/":
                        result = second / first;
                        break;
                
                } 
                stack.push(result);
            } else
                stack.push(Integer.valueOf(token));
        }
        
        return stack.peek();
    }
}