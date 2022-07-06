
# import asyncio

# async def function1():
#     print('Function - 1 is running')
#     await function2()
#     print('finished-----')
# async def function2():
#     print('Function - 2 is running')
#     await asyncio.sleep(10)


# asyncio.run(function1())
# ---------------------------------------------------------------------------
# import asyncio

# async def function1():
#     print('Function - 1 is running')
#     task1 = asyncio.create_task(function2())
#     # await task1 # wait till task1 complete and after print (finished)
#     print('finished-----')

# async def function2():
#     print('Function - 2 is running')
#     await asyncio.sleep(10)


# asyncio.run(function1())
    
# ---------------------------------------------------------------------------

import asyncio

async def function1():
    print('Start fatching API...')
    await asyncio.sleep(2)
    print('Finished fatching API...')
    return {'item1':1,'item2':2,'item3':3,'item4':4}

async def function2():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.3)


async def run_main():
    task1 = asyncio.create_task(function1())
    task2 = asyncio.create_task(function2())

    output = await task1
    print(output)
    await task2


asyncio.run(run_main())