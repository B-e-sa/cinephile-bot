import discord
import os

"""
manages bot init
"""


class Bot():
    def __init__(self):
        self.__token = os.getenv("TOKEN")
        self.__intents = discord.Intents.default()
        self.__intents.message_content = True
        self.__intents.guilds = True

    def get_intents(self):
        return self.__intents

    def get_token(self):
        return self.__token
