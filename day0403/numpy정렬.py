import numpy as np

item = ['사과','바나나','수박','체리','복숭아','딸기']
dty = [200,1000,10,20,30,1000]


# 연습) 판매량이 높은 순으로 과일명을 출력
dty1 = np.array(dty)
arr_item = np.array(item)

# 기본적으로 argsort는 오름차순이기에
# 내림차순으로 바꿔줘야한다. 그 식이 [::-1] 이다. (stemp이 -1)
# index = np.argsort(dty1)[::-1]
# print(arr_item[index])

n = np.argmax(dty1)     #최대값이 2개이상일때는 첫번째 즉 인덱스 반환 X
print(arr_item[n])

n =np.argwhere(dty1 == np.max(dty1))
print(n)
r = arr_item[n]
r = r.reshape(r.size)
print(r)
# print(arr_item[4])

'''
바나나
[[1]
 [5]]
['바나나' '딸기']
'''





# a = [7,8,1,5,3]
# arr = np.array(a)
# # 정렬했을때 와아햘 데이터의 순서를 반환하는 함수
# # 몇번째 요소부터 먼저 와야하나?
# idx = np.argsort(arr)
# print(idx)
# '''
# [2 4 3 0 1]
# '''
# print(arr[idx])
# '''
# [1 3 5 7 8]
# '''
#
# arr.sort()
# # 정렬이 되어버린 arr배열이 된다.
# print(arr)
# '''
# [1 3 5 7 8]
# '''