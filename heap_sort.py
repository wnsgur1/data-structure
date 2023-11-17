import random

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
    p = 1; i = 2 # p는 부모인덱스, i는 자식인덱스
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
    list = []
    for i in range(25):
        list.append(random.randrange(0, 101))
    print(heap_sort(list))

main()