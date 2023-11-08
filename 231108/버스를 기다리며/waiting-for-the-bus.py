#제출 통과 못함 (테케 2)
def is_possible(num):
    i = 0 #사람 번호
    bus = m #아직 도착하지 않은 버스
    max_wait = 0
    while i < n:
        first_arrived = arr[i]
        ready = []
        while len(ready) < c and i < n and arr[i] - first_arrived <= num: #i가 마지막일 때 경우 처리해줘야!!!
            ready.append(arr[i])
            curr_time = arr[i]
            i += 1
        bus -= 1
        max_wait = max(max_wait, curr_time - first_arrived)

    if bus >= 0 and max_wait <= num:
        return True
    else:
        return False

        

            

#통과 못하는 테스트케이스
#7 4 2
#1 1 1 14 15 3 2
# mid : 2



n, m, c = tuple(map(int, input().split()))

arr = [int(a) for a in input().split()]
arr.sort()

left = 0
right = arr[-1] - arr[0]
result = right

while left <= right:
    mid = (left + right) // 2

    if is_possible(mid):
        result = min(result, mid)
        right = mid - 1
    else:
        left = mid +1 

print(result)