import random

# 선택 정렬
def selcetion(list):
    # 리스트 만큼 반복
    for i in range(len(list)):
        # 첫번째 인덱스
        min = i
        # i+1 부터 리스트 크기전까지 반복
        for j in range(i+1, len(list)):
            #만약 min 인덱스 다음에 있는 수가 min 인덱스 에 있는 값보다 작은게 있으면 
            if list[j] < list[min]:
                # min은 작은 값의 인덱스
                min = j
        # 첫번째 인덱스의 값과 가장 작은 값을 교체
        list[i], list[min] = list[min], list[i]
    # 리턴
    return list

def insertion(list):
    print("insertion")

def bubble(list):
    print("bubble")
    
def quick(list):
    print("quick")

def merge(list):
    print("merge")

def heap(list):
    print("heap")


def main():
    num = [1,2,3,4,5,6,7]
    while(1):
        list = []
        a = int(input("여러가지 정렬 프로그램 구현\n 1. 선택 정렬\n 2. 삽입 정력\n 3. 버블 정렬\n 4. 퀵 정력\n 5. 합병 정렬\n 6. 힙 정력\n 7. 종료\n"))
        for i in range(25):
            list.append(random.randrange(0, 101))
        if a in num:
            match a:
                case 1:
                    print("선택 정렬")
                    print("정렬 전", list)
                    print("정렬 후", selcetion(list))                      
                case 2:
                    print("삽입 정렬")
                    print("정렬 전", list)
                    print("정렬 후", insertion(list))                  
                case 3:
                    print("버블 정렬")
                    print("정렬 전", list)
                    print("정렬 후", bubble(list))
                case 4:
                    print("퀵 정렬")
                    print("정렬 전", list)
                    print("정렬 후", quick(list))
                case 5:
                    print("합병 정렬")
                    print("정렬 전", list)
                    print("정렬 후", merge(list))
                case 6:
                    print("힙 정렬")
                    print("정렬 전", list)
                    print("정렬 후", heap(list))
                case 7:
                    print("종료")
                    break
        else:
            print("번호 오류")

main()