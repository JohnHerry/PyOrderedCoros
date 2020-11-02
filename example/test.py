# -*- coding:utf8 -*-
# Author: JohnHerry
# Mail: qhlonline@163.com
# Desc: example code 


import asyncio
import random
import time
from POC import ordered_concurrency


async def coro_task(index):
    value = 0
    begin = time.time()
    for r in range(random.randint(10000, 10000000)):
        value += r
    print("coro index={} cost={}".format(index, time.time() - begin))
    return "index={}, random compute value={}".format(index, value)


async def test_ordered_corous(count=40, conncurrncy=5):
    conoutines = [
        coro_task(index) for index in range(count)
    ]

    results = []
    begin = time.time()
    for result in ordered_concurrency(conoutines, conncurrncy):
        data = await result
        if data:
            #print("data=", data)
            results.append(data)
    # print("cost = ", time.time() - begin)
    print("\n".join(results))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test_ordered_corous())
