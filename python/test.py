import asyncio
import aiohttp


async def fetch(host):
    print('fetch %s...' % host)
    reader, writer = await asyncio.open_connection(host, 80)
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    await writer.drain()
    while True:
        line = await reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    writer.close()


async def request():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.github.com/events') as resp:
            print(resp.status)
            print(await resp.text())


# loop = asyncio.get_event_loop()
# tasks = [fetch(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
# loop.run_until_complete(asyncio.wait(tasks))
# tasks = [request() for _ in range(5)]
# loop.run_until_complete(asyncio.wait(tasks))
# print('a')
# asyncio.run(request())
# print('b')
# asyncio.run(request())
# print('c')
# asyncio.run(request())
# print('d')
# asyncio.run(request())
# print('e')
# # loop.run_until_complete(request(loop))
# loop.close()

async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')

m = main()
# asyncio.run(m)
print('a')
