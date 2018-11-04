from dotenv import load_dotenv

import os

load_dotenv(verbose=True)

DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')