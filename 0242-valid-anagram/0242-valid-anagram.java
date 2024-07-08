class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length())
            return false;
            
        int[] freqArray = new int[26];
        
        for (int i = 0 ; i < s.length() ; i++) { 
            freqArray[s.charAt(i) - 'a']++;
            freqArray[t.charAt(i) - 'a']--;
        }

        for (int freq: freqArray) {
            if (freq != 0)
                return false;
        }
        return true;
    }
}