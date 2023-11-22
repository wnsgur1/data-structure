import random

def selection_sort(A) :
    n = len(A)

    # list 길이 -1 만큼 반복
    for i in range(n-1) :
        # least = i
        least = i
        for j in range(i+1, n) : # 최소값 탐색
            # least 앞쪽 list값이 least인덱스 값보다 작으면
            if A[j] < A[least] :
                # least는 작은 값의 인덱스
                least = j
        # 처음위치와 제일 작은 위치 교체
        A[i], A[least] = A[least], A[i]

    # 리턴
    return A

def main():
    list = []
    for i in range(25):
        list.append(random.randrange(0, 101))
    print(selection_sort(list))

main()