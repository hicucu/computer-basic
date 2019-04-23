import threading
# 공유 자원
# 모든 쓰레드에서 접근 가능한
# 전역 변수

g_num = 0

# lock 객체
lock = threading.Lock()


def thread_main():
    global g_num

    # critical section
    # 임계 영역
    # 어떤 스레드에서 공유 자원에 접근한 후 수정 변경하려는 코드
    lock.acquire()
    for i in range(100000):
        g_num += 1
    lock.release()


threads = []

for i in range(50):
    th = threading.Thread(target=thread_main)
    threads.append(th)

for th in threads:
    th.start()

for th in threads:
    th.join()

print('g_num : {:,}'.format(g_num))
