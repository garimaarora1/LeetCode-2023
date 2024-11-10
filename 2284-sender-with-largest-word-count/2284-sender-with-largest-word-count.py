class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        counter = Counter()
        maxi = 0  
        max_sender = '' 
        
        for sender, message in zip(senders, messages):            
            counter[sender] += len(message.split())
            
            # Important: use counter[sender] to check for updated count.
            if counter[sender] > maxi or (counter[sender] == maxi and sender > max_sender):
                maxi = counter[sender]
                max_sender = sender

        return max_sender
