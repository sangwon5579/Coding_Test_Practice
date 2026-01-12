# def solution(k, score):
#     answer = []
#     k_list = []
#     if(k > len(score)):
#         for i in range(len(score)):
#             k_list.append(score[i])
#             k_list.sort()
#             answer.append(k_list[0])
#         return answer
#     else:        
#         for i in range(k):
#             k_list.append(score[i])
#             k_list.sort()
#             answer.append(k_list[0])
#         leng = len(score) - k
#         for i in range(leng):      
#             if(score[i+k] > k_list[0]):
#                 k_list.pop(0)
#                 k_list.append(score[i+k])
#                 k_list.sort()
#                 answer.append(k_list[0])
#             else:
#                 answer.append(k_list[0])
#         return answer
    
    
import heapq

def solution(k, score):
    answer = []
    heap = []

    for s in score:
        heapq.heappush(heap, s)

        if len(heap) > k:
            heapq.heappop(heap)

        answer.append(heap[0])

    return answer