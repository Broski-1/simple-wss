import asyncio
import websockets

wss = input('Websocket URI: ')

# set to false if you do not want to use secure sockets layer
ssl = True

# we wipe the file upon script execution
file = open('logfile.txt', 'w')
file.truncate()

async def websocket():
    async with websockets.connect(wss, ssl=ssl) as socket:
            # while we have a conntection to the socket
            while socket:
                x = input('> ')
                await socket.send(x)
                # we log output to a file, instead of the console.
                with open('logfile.txt', 'a') as file:
                    # if we receive output
                    if await socket.recv():
                        file.write(f'{await socket.recv()}\n\n')
                    else:
                        pass
        

if __name__ == "__main__":
    asyncio.run(websocket())
