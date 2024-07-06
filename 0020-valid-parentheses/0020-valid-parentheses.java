class Solution {
    private static final HashMap<Character, Character> MAPPINGS;
    
    static {
        MAPPINGS = new HashMap<>();
        MAPPINGS.put(']', '[');
        MAPPINGS.put('}', '{');
        MAPPINGS.put(')', '(');
    }
    
    
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        
        for (char ch : s.toCharArray()) {
            
            if (MAPPINGS.containsKey(ch)) {
                char topElement = stack.isEmpty() ? '#' : stack.pop();

                if (topElement != MAPPINGS.get(ch))
                    return false;
            } else {
                stack.push(ch);
            }
            
        } 
        
        return stack.isEmpty();
        
        
    }
}