import asyncio
import logging
from highrise import BaseBot, __main__
from highrise.__main__ import BotDefinition
from highrise.models import SessionMetadata, User

# Configure logging to see outputs in server logs
logging.basicConfig(level=logging.INFO)


class Bot(BaseBot):

    async def on_start(self, session_metadata: SessionMetadata):
        print("Bot successfully connected and online.")

    async def on_chat(self, user: User, message: str):
        print(f"{user.username}: {message}")


if __name__ == "__main__":
    room_id = "6ab061eeaba5e084307f6b50"
    token = "cfeae7e59e084ceef7c10f09424870c0b66b9b12b30cde66b5caf69517bd385a"

    definitions = [BotDefinition(Bot(), room_id, token)]
    asyncio.run(__main__.main(definitions))
