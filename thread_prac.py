import threading
import time
# target = 쓰레드가 실행할 함수
# args = 함수 실행 인자
# join() -> main Thread가 sub Thread의 종료를 대기하도록 함.


def run(n):
    for i in range(10):
        time.sleep(0.1)
    print(f"* [{n} done]")
def add(a,b):
    print(a+b)

players = ['rabbit', 'turtle', 'horse']
for player in players:
    t = threading.Thread(target=run, args = (player,))
    t.start()
    t.join()

t2 = threading.Thread(target=add, args = (1,2,))
t2.start()
