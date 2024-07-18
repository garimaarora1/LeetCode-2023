class Solution {
    public int characterReplacement(String s, int k) {
        int i = 0;
        int j = 0;
        int currFreq;
        int maxi = 0;
        Map<Character, Integer> freqMap = new HashMap<>();
        while(j < s.length()) {
            currFreq = freqMap.getOrDefault(s.charAt(j), 0);
            freqMap.put(s.charAt(j), ++currFreq);
            
            while((j-i+1)-Collections.max(freqMap.values())>k) {
                currFreq = freqMap.get(s.charAt(i));
                freqMap.put(s.charAt(i), --currFreq);
                ++i;
            }
            maxi = Math.max(maxi, j-i+1);
            ++j;
        }
        return maxi;
        
    }
}