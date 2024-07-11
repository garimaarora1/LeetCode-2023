class Solution {
    public boolean isAnagram(String s, String t) {
        int n = s.length();
        if (n != t.length())
            return false;
        
        int[] freqArray = new int[26];
        
        for(int i = 0 ; i < n ; ++i) {
            int s_idx = s.charAt(i) - 'a';
            freqArray[s_idx] ++;
            
            int t_idx = t.charAt(i) - 'a';
            freqArray[t_idx] --;
        }
    
        for(int i = 0 ; i < 26 ; ++i) {
            if(freqArray[i] != 0)
                return false;
        }
    return true;
    }
}