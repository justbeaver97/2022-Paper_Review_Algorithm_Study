"""
14225번 - https://www.acmicpc.net/problem/14225

부분수열의 합
수열 S가 주어졌을 때, 수열 S의 부분 수열의 합으로 나올 수 없는 가장 작은 자연수를 구하는 프로그램을 작성하시오.

예를 들어, S = [5, 1, 2]인 경우에 1, 2, 3(=1+2), 5, 6(=1+5), 7(=2+5), 8(=1+2+5)을 만들 수 있다. 
하지만, 4는 만들 수 없기 때문에 정답은 4이다.

refercence
itertools.combinations - https://stackoverflow.com/questions/464864/how-to-get-all-possible-combinations-of-a-list-s-elements 

오답 이유 - https://www.acmicpc.net/board/view/85746#comment-139115
"""

import itertools

n = int(input())
s = list(map(int, input().split()))

def sum_of_subsequence(array):
    combination = []
    for i in range(1, n+1):
        tmp = list(itertools.combinations(array, i))
        for j in tmp:
            combination.append(sum(j))
    return combination

def find_missing_num(array): #[1,2,3,5]
    i = 1
    for num in array: # 1-1 2-2 3-3 5-4
        if num > i:
            break
        i += 1    
    print(i)

subsequence_s = sum_of_subsequence(s)

# 틀린 풀이
# sorted_s = sorted(subsequence_s)
# find_missing_num(set(sorted_s))

# 맞는 풀이
sorted_s = sorted(set(subsequence_s))
find_missing_num(sorted_s)