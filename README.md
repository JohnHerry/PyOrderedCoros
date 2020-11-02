# PyOrderedCoros

## Introduction

EN: *PyOrderedCoros* sited as POC is a coroutine-list-wrapper that the concurrency of coroutines are limited, while the outputs of coroutines are in the same order with the coroutine list.

CN: *PyOrderedCoros* 是一个对协程序列的封装，用于控制协程并发度，并同时确保协程执行结果的输出顺序。

## Requirements & Installation

### Requirement

python3.6 +

### Install

You should first download this project and then execute the follows:

```
python setup.py install
```

## Usage

EN: after installation of this project, you can specify the coroutines and their concurrency you want. 
Here is the example:

```
from POC import ordered_concurrency

# The coroutine function

async async_func(arg):
    ...
    return result

# The coroutine list
def gen_coroutines(arg_list):
    ...
    return [async_func(arg) for arg in arg_list]

# Run coroutines with specified concurrency and return results with order.
async def streamout_coroutines():
    task_args = [...]
    task_coros = gen_coroutines(task_args)
    for task in ordered_concurrency(task_coros, concurrent_cnt=5)
        result = await task
        if result:
            yield result

```

You can also view the *example* codes as demo.

CN: POC有一个核心函数用于实现项目功能，ordered_concurrency 向它传递两个参数，第一个参数是协程列表，第二个参数是并发度。
经上述封装即可支持结果有序的，协程并发度可控的流式计算任务。
