def time_to_loc(loc): #최소인 위치가 가능한지, 가능하다면 얼마나 걸리는지
    max_time = 0
    max_loc = 0
    for i in range(n):
        curr_dist = abs(loc - arr[i][0]) / arr[i][1]
        if curr_dist > max_time: #크거나 같으면??: 
            max_time = curr_dist
            max_loc = arr[i][0]
#print(loc, location[i], velocity[i])
    return max_time, max_loc

n = int(input())
location = [int(a) for a in input().split()]
velocity = [int(a) for a in input().split()]

arr = [(l,v) for l, v in zip(location, velocity)]

arr.sort()



#최소인 위치
left = arr[0][0] 
right = arr[-1][0]
result = right

while left <= right:
    mid = (left + right) // 2
    time, furthest_loc = time_to_loc(mid)

    if time <= result:
        result = min(result, time)
    if mid < furthest_loc:
        left = mid + 1 
    else:
        right = mid - 1



print(f'{result:.4f}')