import asyncio

async def greet(name: str):
    print(f"👋 Hello {name}")
    await asyncio.sleep(1)   # pretend slow operation
    print(f"👋 Goodbye {name}")

async def main():
    # TODO: Call greet("Kinza") and greet("Sheikh") sequentially
    await greet("Kinza")
    await greet("Sheikh")

asyncio.run(main())