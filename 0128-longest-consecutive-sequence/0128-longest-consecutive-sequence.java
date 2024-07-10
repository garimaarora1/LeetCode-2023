class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for(int num : nums) {
            set.add(num);
        }
        
        int maxConsecutiveSeqLength = 0;
        
        for(int num: nums) {
            if(!set.contains(num-1)) {
                int currLength = 1;
                while(set.contains(num + currLength)) {
                    currLength ++;
                }
                maxConsecutiveSeqLength = Math.max(currLength, maxConsecutiveSeqLength);
            }
        }
        return maxConsecutiveSeqLength;
    }
}