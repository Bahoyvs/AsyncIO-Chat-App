import asyncio
from concurrent.futures import ThreadPoolExecutor

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    async def send_message(self, writer, message):
        writer.write(message.encode() + b'\n')
        await writer.drain()

    async def run(self):
        reader, writer = await asyncio.open_connection(self.host, self.port)
        try:
            loop = asyncio.get_event_loop()
            executor = ThreadPoolExecutor()
            while True:
                message = await loop.run_in_executor(executor, input, "Enter message to send (/quit to exit): ")
                await self.send_message(writer, message)
                if message.strip() == "/quit":
                    break
        finally:
            writer.close()

if __name__ == "__main__":
    client = Client("[Enter server IP address]", 5001)
    asyncio.run(client.run())

