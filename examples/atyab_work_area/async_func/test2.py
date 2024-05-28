import asyncio


async def count_to_10():
    count = 1

    while count <= 10:
        print(count)
        await asyncio.sleep(1)
        count += 1


async def main():
    await asyncio.gather(count_to_10(), count_to_10())


asyncio.run(main())
