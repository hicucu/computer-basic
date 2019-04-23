import threading


def thread_main(li, n):
    for i in range(offset * n, offset * (n + 1)):
        li[i] *= 2


n = 1000

offset = n // 4

# 쓰레드 생성
li = [i+1 for i in range(1, 1001)]
threads = []

# 멀티 쓰레드
for i in range(4):
    th = threading.Thread(target=thread_main, args=(li, i))
    threads.append(th)

for th in threads:
    th.start()

# 메인 쓰레드에서 나머지 쓰레드들에 모든 실행이 종료될 때 까지 기다린다.
for th in threads:
    th.join()

print(li)
