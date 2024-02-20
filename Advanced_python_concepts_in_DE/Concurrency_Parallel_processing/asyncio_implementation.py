import asyncio

# Define an asynchronous function
async def main():
    """
    A simple example of asynchronous programming with asyncio.

    This function prints 'Hello', waits for 1 second using asyncio.sleep(),
    and then prints 'World'.
    """
    print("Hello")

    # Wait for 1 second without blocking the event loop
    await asyncio.sleep(1)

    print("World")

# Run the asynchronous function
asyncio.run(main())


""" asyncio_implementation.py
--------------------------

This script explores asynchronous programming with asyncio.

Functions:
- main(): An asynchronous function that prints 'Hello', waits for 1 second using asyncio.sleep(), and then prints 'World'.

Usage:
- Run the script to see the output."""
