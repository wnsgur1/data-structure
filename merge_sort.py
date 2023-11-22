import random

sorted = []

s = 1
def merge(A, left, mid, right) :
    global s
    global sorted
    i = left # 왼쪽 리스트의 첫 번째 인덱스
    j = mid + 1 # 오른쪽 리스트의 첫 번째 인덱스
    k = left # 정렬될 리스트의 첫 번째 인덱스
    # 분할된 리스트의 합병
    while i <= mid and j <= right :
        if A[i] <= A[j] :
            sorted[k] = A[i]; i, k = i+1, k+1
        else :
            sorted[k] = A[j]; j, k = j+1, k+1
        # 리스트 복사
    
    if i > mid :
        sorted[k : k+right-j+1] = A[j : right+1]
    else :
        sorted[k : k+mid-i+1] = A[i : mid+1]
    # 임시 리스트에 값 삽입
    A[left : right+1] = sorted[left : right+1]
    s += 1

def merge_sort(A, left, right) :

    if left < right :
        mid = (left + right) // 2 # 분할
        
        merge_sort(A, left, mid) # 분할
        merge_sort(A, mid+1, right) # 분할

        merge(A, left, mid, right) # 합병
    
    return A

def main():
    list = []
    global sorted
    for i in range(25):
        list.append(random.randrange(0, 101))
        sorted.append(list)
    print(merge_sort(list, 0, 24))

main()