import asyncio
import time


async def countdown(n):
    while n > 0:
        print(f'pr down {n}')
        await asyncio.sleep(1)
        n -= 1

async def countup(stop):
    n = 0
    while n < stop:
        print(f'pr up {n}')
        await asyncio.sleep(1)
        n += 1

def hello():
    print('Hello')


async def main():
    await asyncio.gather(countdown(5), countup(5))




# asyncio.run(countdown(10))
# asyncio.run(countdown(10))