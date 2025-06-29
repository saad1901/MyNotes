import time

def func1():
    print("Func 1")
    time.sleep(2)

def func2():
    print("Func 2")
    time.sleep(2)

def func3():
    print("Func 3")
    time.sleep(2)

def main():
    func1()
    func2()
    func3()

# main()


import asyncio

async def printfunc(name, time):
    print(f"Start {name}")
    await asyncio.sleep(time)
    print(f"End {name}")

async def main():
    # await asyncio.gather(
    #     printfunc('A', 2),
    #     printfunc('B', 1)
    # )

    await printfunc('A', 2)
    await printfunc('B', 1)
    

asyncio.run(main())