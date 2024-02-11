import asyncio

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    async def run(self):
        reader, writer = await asyncio.open_connection(self.host, self.port)
        while True:
            message = input("Enter message to send: ")
            if not message:
                break
            writer.write(message.encode())
            await writer.drain()

        writer.close()

if __name__ == "__main__":
    client = Client("139.179.235.60", 5001)
    asyncio.run(client.run())
