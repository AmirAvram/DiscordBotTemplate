import json
from typing import Optional, Union, Dict, Callable
from commands import commands_map

import discord

with open('config.json') as config_file:
    config = json.load(config_file)


class MyClient(discord.Client):
    def __init__(self, commands: Optional[Dict[str, Callable]] = None):
        discord.Client.__init__(self)
        if commands:
            self.commands = commands
        else:
            self.commands = commands_map

    async def on_ready(self) -> None:
        print(f'Logged on as {self.user}')
        await self.send_message("Hey I've just joined", self.get_channel_by_name_or_id('general'))

    async def on_message(self, message: discord.message) -> None:
        user_command = message.content.split(' ')[0]
        if user_command[0] == '.':
            user_command = user_command[1:]
            if user_command in self.commands.keys():
                await self.commands[user_command](message)
        print(f'Message from {message.author}: {message.content}')

    def get_channel_by_name_or_id(self, channel_name: Optional[str] = None, channel_id: Optional[int] = None) -> Optional[Union[discord.channel.VoiceChannel, discord.channel.TextChannel]]:
        channels = self.get_all_channels()
        for channel in channels:
            if channel.id == channel_id or channel.name == channel_name:
                return channel
        return None

    async def send_message(self, message: str, channel: discord.channel.TextChannel) -> None:
        await channel.send(message)


def run():
    client = MyClient()
    client.run(config['token'])


run()
