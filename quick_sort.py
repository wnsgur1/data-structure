import random

def quick_sort(A, left, right) :  
    # 왼쪽이 오른쪽 보다 작을때
    if left < right :
        # i는 left에서 한칸 오른쪽
        i = left + 1
        # j는 right
        j = right
        # pivot은 첫번째 값
        pivot = A[left]
        # i가 j보다 작을때
        while i <= j :
            # i가 right보다 작고 i인덱스 값이 pivot보다 작거나 같으면 i를 오른쪽으로(i+=1) 이동
            while i <= right and A[i] <= pivot : i += 1
            # j가 left보다 크고 j인덱스 값이 pivot보다 크면 i를 왼쪽으로(j-=1) 이동
            while j >= left and A[j] > pivot : j -= 1
            # 만약 i가 j보다 작으면 i와 j인덱스 값 교체
            if i < j : A[i], A[j] = A[j], A[i]
        # left와 j인덱스 값 교체
        A[left], A[j] = A[j], A[left]
        # 처음부터 j-1까지 quick_sort, j+1부터 right까지 quick_sort
        quick_sort(A, left, j-1)
        quick_sort(A, j+1, right)
    #리턴 
    return A



def main():
    list = []
    for i in range(25):
        list.append(random.randrange(0, 101))

    print(quick_sort(list, 0, 24))

main()