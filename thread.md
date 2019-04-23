# OS

1. job scheduling
2. Concurrency programming
   multithreading | Asynchronoous I/O

# program과 process

- program
  -> 하드디스크에 저장되어 있는 "하나"의 이미지(code), data)

- process
  -> 메인 메모리에 올라와서 실행을 시작한 프로그램

# 스케쥴링

1. 선점형 스케쥴링 preemptive scheduling
   -> 새치기가 가능

2. 비 선점형 스케쥴링 nonpreemtive scheduling

# 동작

## 동작 순서

                                                Terminated
                                                    |

create(process생성, 메모리에 적재) -> waiting -> running(cpu할당, 실행) -> blocked(I/O작업)
| |

---

## wating

Queue에 저장
priority(우선순위)에 따라 OS 스케줄러가 현재 실행 중인 우선순위와 비교하여 작으면 대기 크면 runnig중인 프로세스를 queue로 내리고 cpu 할당(preemption)
pre-emptive로 multitasking이 가능

## 우선순위

1. priority algorithm
2. priority가 같을 때 -> Round-robin algorithm : 정해진 시간동안 Process를 실행(time slice, Quantum)
3. aging -> 기아상태 해결을 위함

## I/O작업

느리고 CPU가 필요없음
I/O 가 끝날 때 까지 기다린 후 다시 waiting으로

## Terminated

running이 끝나면 종료

# Context Switching
