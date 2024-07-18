class Solution {
    public String minWindow(String s, String t) {
        int i = 0;
        int j = 0;
        int freq;
        int[] res = new int[] {-1,-1};
        int uniqueCharactersCount = t.length();
        int minWindowSize = Integer.MAX_VALUE;
        char ch;
        char charAtI;
        Map<Character, Integer> tFreqMap = new HashMap<>();
        for (char chT : t.toCharArray()) {
            tFreqMap.put(chT, tFreqMap.getOrDefault(chT, 0) + 1);
        }
        while(j < s.length()) {
            ch = s.charAt(j);
            if(tFreqMap.containsKey(ch)) {
                 tFreqMap.put(ch, tFreqMap.get(ch) - 1);
                if(tFreqMap.get(ch) >= 0) {uniqueCharactersCount--;}
            }
            while(uniqueCharactersCount == 0) {
                if ((j-i+1) < minWindowSize) {
                    minWindowSize = j-i+1;
                    res[0] = i;
                    res[1] = j;
                }
                charAtI = s.charAt(i);
                if (tFreqMap.containsKey(charAtI)) {
                    tFreqMap.put(charAtI, tFreqMap.get(charAtI) + 1);
                    if (tFreqMap.get(charAtI) == 1) ++uniqueCharactersCount;
                }
                ++i;
            }
            ++j;
        }
        
        if (res[0] == -1) {
            return "";
        }
        
        return s.substring(res[0], res[1] + 1);
    }
}