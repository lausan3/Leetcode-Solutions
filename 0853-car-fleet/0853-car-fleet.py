class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carsZip = [[p, s] for p, s in zip(position, speed)]
        fleetStack = []

        # going in reverse sorted order, we push the times that cars are going to take to get to the 
        # target from their position using their speed. Then, we push them onto the stack and compare them with
        # the last item that was pushed onto the stack, removing it if its time to reach target is less than
        # the previous car (remember that we are doing this in reverse so it's the car in front of it)
        # because it's going to change its speed to match that of the car in front of it.
        for p, s in sorted(carsZip)[::-1]:
            fleetStack.append((target - p) / s)
            if len(fleetStack) >= 2 and fleetStack[-1] <= fleetStack[-2]:
                fleetStack.pop()
        
        return len(fleetStack)