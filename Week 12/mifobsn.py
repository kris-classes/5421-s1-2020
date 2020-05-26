import time
import asyncio
import collections


class Scheduler:
    def __init__(self):
        self.ready = collections.deque()

    def call_soon(self, func):
        self.ready.append(func)

    def run(self):
        while self.ready:
            func = self.ready.popleft()
            func()

def hello(name):
    time.sleep(2)
    print(f'hello{name}')

def somethingelse():
    time.sleep(3)
    print(b'hell')

def countdown(n):
    while n > 0:
        print(f'pr down {n}')
        time.sleep(1)
        n -= 1

def countup(stop):
    n = 0
    while n < stop:
        print(f'pr up {n}')
        time.sleep(1)
        n += 1


sched = Scheduler()
sched.call_soon(lambda: hello('Bob'))
sched.call_soon(somethingelse)
sched.call_soon(lambda: countdown(5))
sched.call_soon(lambda: countup(5))
sched.run()










'''threading.Thread(target=countdown, args=(5,)).start()
threading.Thread(target=countup, args=(5,)).start()'''
'''countdown(5)
countup(5)'''