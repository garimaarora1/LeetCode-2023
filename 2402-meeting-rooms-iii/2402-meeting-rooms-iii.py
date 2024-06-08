class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        meeting_count = [0]*(n)
        unused_rooms = list(range(n))
        heapq.heapify(unused_rooms)
        used_rooms = []
        meetings.sort()
        for meeting in meetings:
            while used_rooms and used_rooms[0][0] <= meeting[0]:
                _, room = heapq.heappop(used_rooms)
                heapq.heappush(unused_rooms, room)
            if unused_rooms:
                room = heapq.heappop(unused_rooms)
                heapq.heappush(used_rooms, (meeting[1], room))
            else:
                room_availability_time, room = heapq.heappop(used_rooms)
                heapq.heappush(used_rooms, (room_availability_time+meeting[1]-meeting[0], room))
            meeting_count[room] += 1
        return  meeting_count.index(max(meeting_count))