class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        res = [0] * len(deck)
        queue = deque(range(len(deck)))
        for card in deck:
            i = queue.popleft()
            res[i] = card
            if queue:
                queue.append(queue.popleft())
        return res