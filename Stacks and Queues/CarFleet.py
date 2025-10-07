def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = sorted(zip(position, speed), reverse=True)
        stack = []
        for pos, spd in cars:
            time = (target - pos) / spd
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)



# Time Complexity: O(n log n) due to sorting the cars by position; the single pass that follows is O(n).
# Space Complexity: O(n) in the worst case, where each car forms its own fleet and we store all their times on the stack.
#
# This function counts how many fleets reach the target by processing cars from closest to farthest relative to the finish line. 
# For each car, we compute how long it would take to arrive. If that time is greater than the time of the fleet directly ahead, 
# it can’t catch up and therefore starts a new fleet, so we push its time on the stack. Otherwise, it simply merges into the 
# fleet in front and we don’t store anything new. In the end, the number of fleets is just the size of the stack.
