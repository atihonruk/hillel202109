import asyncio


def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


async def fib_handler(reader, writer):
    while True:
        data = await reader.read(256)  # recv, BLOCKING
        if not data:
            break
        arg = int(data)
        # res = fib(arg)  # CPU bound
        # conn.execute()  # blocking
        writer.write(data)
        await writer.drain()
        
    writer.close()




async def echo_handler(reader, writer):
    while True:
        data = await reader.read(256)  # recv, BLOCKING
        if not data:
            break
        writer.write(data)
        await writer.drain()
    writer.close()
    await writer.wait_closed()


async def main():
    server = await asyncio.start_server(echo_handler, host='127.0.0.1', port=5555)

    async with server:
        await server.serve_forever()


asyncio.run(main())
