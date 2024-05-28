import asyncio


async def set_timeout(callback_func,time_in_ss):
    print("hello world")
    await asyncio.sleep(time_in_ss)
    callback_func()


def test_print():
    print("test")


asyncio.run(set_timeout(test_print, 2))


