from collections import deque

def solution(priorities, location):
    answer = 0
    dd = deque([(j,i) for i,j in enumerate(priorities)])
    
    while len(dd):
        item = dd.popleft()
        if item[0] < max(dd)[0] and dd:
            dd.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
    return answer

# def solution(priorities, location):
#     answer = 0
    
#     d = deque([(v,i) for i,v in enumerate(priorities)])

#     while len(d):
#         item = d.popleft()
#         if d and max(d)[0] > item[0]:
#             d.append(item)
#         else:
#             answer += 1
#             if item[1] == location:
#                 break
#     return answer