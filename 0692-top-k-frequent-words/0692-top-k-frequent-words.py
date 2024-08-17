class Pair:
    
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
        
    def __lt__(self, pair):
        return self.freq < pair.freq or self.freq == pair.freq and self.word > pair.word

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        min_heap = []
        
        for word, freq in counter.items():
            pair = Pair(word, freq)
            
            heapq.heappush(min_heap, pair)
            
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        top_k_freq_words = []
        while min_heap:
            pair = heapq.heappop(min_heap)
            top_k_freq_words.append(pair.word)
        return top_k_freq_words[::-1]
        
        