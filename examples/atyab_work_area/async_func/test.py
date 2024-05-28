import asyncio
import aiohttp
import requests


async def send_request(url):
    async with aiohttp.ClientSession() as session_from_pool:
        try:
            async with session_from_pool.get(url) as response:
                return await response.json()
        except Exception as ex:
            print(ex)


async def send_request_using_requests(url):
    res = await asyncio.get_event_loop().run_in_executor(None, requests.get, url)
    return f"From requests: {res.json()}"


async def main():
    try:
        t1 = asyncio.create_task(send_request_using_requests("https://api.github.com/users/codelineatyab"))
        return await asyncio.gather(
            t1,
            send_request("https://api.github.com/users/codelineatyab"),
            send_request("https://api.github.com/users/HaithamAlMaamari")
        )
    except Exception as ex:
        print(ex)

print(asyncio.run(main()))
