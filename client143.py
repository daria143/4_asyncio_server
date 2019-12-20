import asyncio


HOST = 'localhost'
while True:
    PORT = int(input('Enter port number from  1024 to 65525: '))
    if 1024 <= int(PORT) <= 65525:
        break
    else:
        print('Error in port value')


async def tcp_echo_client(HOST, PORT):
    reader, writer = await asyncio.open_connection(HOST, PORT)
    message = input('Enter your message: ')

    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(100)
    print(data.decode())
    writer.close()


loop = asyncio.get_event_loop()
task = loop.create_task(tcp_echo_client(HOST, PORT))
loop.run_until_complete(task)

