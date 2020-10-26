from typing import Dict, Callable
from datetime import datetime
import discord


async def hello_func(message: discord.message) -> None:
    await message.channel.send(f'Hello to you: {message.author.name} :smile:')


async def ping_func(message: discord.message) -> None:
    await message.channel.send(f'Pong: {(datetime.utcnow() - message.created_at).total_seconds()} seconds')


commands_map: Dict[str, Callable] = {
    'hey': hello_func,
    'hello': hello_func,
    'ping': ping_func
}
