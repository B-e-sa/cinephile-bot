import discord
"""
manages the bot interactions with discord
"""


class DiscordInstance(discord.Client):
    def __init__(self, *args, **kwargs):
        super(DiscordInstance, self).__init__(*args, **kwargs)