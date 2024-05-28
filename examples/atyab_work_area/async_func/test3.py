import asyncio
import requests


async def fetch(url):
    event_loop = asyncio.get_event_loop()
    res = await event_loop.run_in_executor(None, requests.get, url)
    return res.json()


async def count_to_10():
    counter = 1
    while counter <= 10:
        print(counter)
        await asyncio.sleep(1)
        counter += 1


async def main():
    side_task = asyncio.create_task(count_to_10())
    results = await asyncio.gather(
        fetch("https://api.github.com/users/aaziz9"),
        fetch("https://api.github.com/users/codelineatyab"),
        fetch("https://api.github.com/users/HaithamAlMaamari")
    )

    for curr_result in results:
        print(curr_result)

    await side_task
    return results

if __name__ == "__main__":
    results = asyncio.run(main())
    print(results)
    pass
    pass
    pass
    pass

