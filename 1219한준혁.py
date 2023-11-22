import random

sorted = []

s = 1

# 선택 정렬
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

# 선택 정렬
def insertion_sort(A) :
    # n은 리스트 길이
    n = len(A)
    # 1부터 리스트 끝까지
    for i in range(1, n) :
        # key는 현재(i 인덱스에 있는) 리스트 값
        key = A[i]
        # j는 i 한칸 왼쪽
        j = i-1
        # j가 0보다 크고 key가 j인덱스에 있는 리스트 값보다 작으면 반복
        while j >= 0 and A[j] > key :
            # 오른쪽으로 이동
            A[j+1] = A[j]
            j -= 1
        # 정렬된 위치에 key 삽입
        A[j+1] = key
    # 리턴
    return A

# 버블 정렬
def bubble_sort(A) :
    # n은 리스트 길이
    n = len(A)
    # 리스트 끝엥서 부터 처음 까지
    for i in range(n-1, 0, -1) :
        # i번만큼 반복
        for j in range(i) :
            # 만약 뒤에 값이 앞에값보다 크면
            if A[j] > A[j+1] :
                # 위치 변경
                A[j], A[j+1] = A[j+1], A[j]

    # 리턴
    return A
# 퀵 정렬
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


sorted = []

s = 1
def merge(A, left, mid, right) :
    global s
    global sorted
    i = left # 왼쪽 첫 번째 인덱스
    j = mid + 1 # 오른쪽 첫 번째 인덱스
    k = left # 정렬될 리스트의 첫 번째 인덱스
    # 리스트 합병
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

# 합병 정렬
def merge_sort(A, left, right) :

    if left < right :
        mid = (left + right) // 2 # 분할
        
        merge_sort(A, left, mid) # 분할
        merge_sort(A, mid+1, right) # 분할

        merge(A, left, mid, right) # 합병
    
    # 리턴
    return A




def heappush(heap, n) :
    heap.append(n)
    i = len(heap) - 1 # n이 삽입된 위치
    while i != 1 and n > heap[i//2]:
        heap[i] = heap[i//2]
        i//=2
    heap[i] = n

def heappop(heap) :
    size = len(heap) - 1
    if size == 0 : return None # 공백트리
    p = 1; i = 2 # p는 부모, i는 자식
    root = heap[1] # 삭제할 노드
    last = heap[size] # 마지막 노드
    while i <= size :
        if i < size and heap[i] < heap[i+1] :
            i += 1 # 자식 중 더 큰값 선택
        if last >= heap[i] : break
        heap[p] = heap[i] # 자식을 부모위치로
        p = i # 부모위치가 자식위치로
        i *= 2 # 자식위치 이동
    heap[p] = last
    heap.pop()
    return root

def heap_sort(data) :
    heap = [0]
    #모든 데이터를 최대힙에 삽입
    for e in data :
        heappush(heap, e)
    # 모든 데이터를 힙에서 꺼내 역순으로 저장
    for i in range(1, len(data) + 1) :
        data[-i] = heappop(heap)
    return data


def main():
    num = [1,2,3,4,5,6,7]
    global sorted
    while(1):
        list = []
        a = int(input("여러가지 정렬 프로그램 구현\n 1. 선택 정렬\n 2. 삽입 정력\n 3. 버블 정렬\n 4. 퀵 정력\n 5. 합병 정렬\n 6. 힙 정력\n 7. 종료\n"))
        for i in range(25):
            list.append(random.randrange(0, 101))
            sorted.append(list)
        if a in num:
            match a:
                case 1:
                    print("선택 정렬")
                    print("정렬 전", list)
                    print("정렬 후", selection_sort(list))                      
                case 2:
                    print("삽입 정렬")
                    print("정렬 전", list)
                    print("정렬 후", insertion_sort(list))                  
                case 3:
                    print("버블 정렬")
                    print("정렬 전", list)
                    print("정렬 후", bubble_sort(list))
                case 4:
                    print("퀵 정렬")
                    print("정렬 전", list)
                    print("정렬 후", quick_sort(list, 0, 24))
                case 5:
                    print("합병 정렬")
                    print("정렬 전", list)
                    print("정렬 후", merge_sort(list, 0, 24))
                case 6:
                    print("힙 정렬")
                    print("정렬 전", list)
                    print("정렬 후", heap_sort(list))
                case 7:
                    print("종료")
                    break
        else:
            print("번호 오류")

main()