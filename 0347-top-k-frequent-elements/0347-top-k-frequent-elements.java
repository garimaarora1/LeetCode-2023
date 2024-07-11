class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // O(1) time
        if (k == nums.length) {
            return nums;
        }
        
        HashMap<Integer, Integer> freqMap = new HashMap<>();
        
        // 1. Build hash map: character and how often it appears
        // O(N) time
        for(int num : nums) {
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        }
        
        // init heap 'the less frequent element first'
        Queue<Integer> heap = new PriorityQueue<>((n1, n2) -> freqMap.get(n1) - freqMap.get(n2));
        
        // 2. Keep k top frequent elements in the heap
        // O(N log k) < O(N log N) time
        for (int n: freqMap.keySet()) {
          heap.add(n);
          if (heap.size() > k) heap.poll();    
        }
        
        // 3. Build an output array
        // O(k log k) time
        int[] top = new int[k];
        for(int i = k - 1; i >= 0; --i) {
            top[i] = heap.poll();
        }
        return top;
    }
}