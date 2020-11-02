# -*- coding:utf8 -*-
# Author: JohnHerry 
# Mail:  qhlonline@163.com
# Desc: ordered concurrency control of Python coroutines


import asyncio
from collections import OrderedDict


def ordered_concurrency(coroutines, concurrent_cnt):
    """
    Inputs:
        coroutines:      a list of python coroutines to be scheduled
        concurrent_cnt:  how many concurrent corouines can be scheduled
    """
    ordered_result = OrderedDict([coro, None] for coro in coroutines)
    task2coroutine = {}
    waiting_tasks = []
    
    def get_next_result():
        for cron in ordered_result.keys():
            if ordered_result[cron]:
                result = ordered_result[cron]
                del ordered_result[cron]
                return result
            else:
                break

    for coro in coroutines[: concurrent_cnt]:
        task = asyncio.ensure_future(coro)
        task2coroutine[task] = coro
        waiting_tasks.append(task)
    coroutines = coroutines[concurrent_cnt: ]

    async def do_concurrent_tasks():
        await asyncio.sleep(0)
        for task in waiting_tasks:
            coro = task2coroutine[task]
            if task.done():
                waiting_tasks.remove(task)
                try:
                    new_coro = coroutines.pop(0)
                    new_task = asyncio.ensure_future(new_coro)
                    task2coroutine[new_task] = new_coro 
                    waiting_tasks.append(
                        new_task
                    )
                except IndexError as e:
                    pass
                assert coro in ordered_result, "Error! cron not in result dict!"
                ordered_result[coro] = task.result()
                result = get_next_result()
                if result:
                    return result
                else:
                    return await do_concurrent_tasks()

        # wait and fanout coroutine-result after all coros are scheduled.
        if len(ordered_result) > 0:
            return get_next_result()

    while len(ordered_result) > 0:
        yield do_concurrent_tasks()
