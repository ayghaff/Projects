from typing import Final
import os
from discord import Intents, Client, Message
from responses import get_response
import aiohttp

aiohttp.TCPConnector(ssl=False)


TOKEN: Final[str] = "MTIxMTAzMTIyMzQ0MzM5ODc4Nw.GXa427.i9J-SSAa64Xb3C7j5d9fNz97ZJP639XxCO-CnY"

intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print("No message content. Possible intent failure...")
        return

    if is_private := user_message[0] == "?":
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


@client.event
async def on_ready() -> None:
    print(f"{client.user} is up and running...")



@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f"[{channel}] {username}:'{user_message}'")
    await send_message(message, user_message)


def main() -> None:
    client.run(token=TOKEN)


if __name__ == "__main__":
    main()
