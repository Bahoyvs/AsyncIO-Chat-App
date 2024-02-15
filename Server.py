import asyncio

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.clients = []

    async def handle_client(self, reader, writer):
        self.clients.append(writer)
        while True:
            data = await reader.readline()
            if not data:
                break
            message = data.decode().strip()
            print(f"Received message: {message}")
            for client in self.clients:
                client.write(data)
                await client.drain()

        self.clients.remove(writer)

    async def run(self):
        server = await asyncio.start_server(self.handle_client, self.host, self.port)
        async with server:
            await server.serve_forever()

if __name__ == "__main__":
    server = Server("[Enter a device IP address]", 5001)
    asyncio.run(server.run())
