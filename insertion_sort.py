import random

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

def main():
    list = []
    for i in range(25):
        list.append(random.randrange(0, 101))
    print(insertion_sort(list))

main()