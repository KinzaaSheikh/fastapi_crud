import asyncio

async def greet(name: str):
    print(f"Hello {name}")
    await asyncio.sleep(1)
    print("Goodbye {name}")


async def main():
    await asyncio.gather(
        greet("Kinza"),
        greet("Sheikh")
    )

asyncio.run(main())
