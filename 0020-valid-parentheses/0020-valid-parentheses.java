class Solution {
    public boolean isValid(String s) {
        HashMap<Character, Character> mappings = new HashMap<Character, Character>();
        mappings.put(']', '[');
        mappings.put('}', '{');
        mappings.put(')', '(');
        Stack<Character> stack = new Stack<Character>();
        for (int i = 0 ; i < s.length() ; i++) {
            Character ch = s.charAt(i);
            
            if(mappings.containsKey(ch)) {
                if(stack.isEmpty()) {
                    return false;
                }
                char topElement = stack.pop();
                if (topElement != mappings.get(ch)) {
                    return false;
                }
            } else {
                stack.push(ch);
            }
        }
        return stack.isEmpty();
        
    }
}