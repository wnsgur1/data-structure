import random

def selcetion():
    print("selcetion")

def insertion():
    print("insertion")

def bubble():
    print("bubble")
    
def quick():
    print("quick")

def merge():
    print("merge")

def heap():
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
                    selcetion()
                case 2:
                    insertion()
                case 3:
                    bubble()
                case 4:
                    quick()
                case 5:
                    merge()
                case 6:
                    heap()
                case 7:
                    print("종료")
                    break
        else:
            print("번호 오류")

main()