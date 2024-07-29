from bot import Bot
from discord_instance import DiscordInstance
from dotenv import load_dotenv

load_dotenv()
BOT = Bot()
DISCORD = DiscordInstance(intents=BOT.get_intents())
DISCORD.run(BOT.get_token())