# Suppose there is a circle. There are N petrol pumps on that circle. Petrol pumps are
# numbered 0 to (N-1) (both inclusive). You have two pieces of information corresponding
# to each of the petrol pump: (1) the amount of petrol that particular petrol pump will
# give, and (2) the distance from that petrol pump to the next petrol pump.

# Initially, you have a tank of infinite capacity carrying no petrol. You can start the
# tour at any of the petrol pumps. Calculate the first point from where the truck will
# be able to complete the circle. Consider that the truck will stop at each of the petrol
# pumps. The truck will move one kilometer for each litre of the petrol.

N = int(input().strip())

queue = []
negative = 0
for i in range(N):
    gas,dist = [int(v) for v in input().strip().split()]
    # Add gas station to processing queue
    if not queue or queue[-1][1] < 0:
        if gas - dist < 0:
            negative += 1
        queue.append( [i, gas - dist] )
    else:
        queue[-1][1] += (gas - dist)

while queue and queue[0][1] < 0:
    # Remove the next item
    queue.pop(0)
    
print(queue[0][0])