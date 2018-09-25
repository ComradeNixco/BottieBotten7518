from dotenv import load_dotenv

import os

load_dotenv(verbose=True)

DISCORD_APP_SECRET = os.getenv('DISCORD_APP_SECRET')