import discord
import openai
import config

COMPLETIONS_MODEL = "text-davinci-002"
COMPLETIONS_API_PARAMS = {
    # We use temperature of 0.0 because it gives the most predictable, factual answer.
    "temperature": 0.0,
    "max_tokens": 300,
    "model": COMPLETIONS_MODEL,
}
END_PROMPT = "Answer the question as truthfully as possible, if you don't know the answer, say I don't know"


class Client(discord.Client):

    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

    async def on_message(self, message: discord.Message):
        print(message.content)
        print(message.author.name)
        is_thread = message.channel.type == discord.ChannelType.public_thread
        # await message.channel.send("plop")
        """if not is_thread:
            prompt = f"{END_PROMPT}\n{message.content}"
            response = openai.Completion.create(
                prompt=prompt,
                **COMPLETIONS_API_PARAMS,
            )
            answer = response["choices"][0]["text"].strip(" \n")
            print(prompt)
            print(answer)
            if "I don't know" in answer:
                return
            thread = await message.create_thread(name=f"Answer to {message.content}")
            await thread.send(answer)
        """


intents = discord.Intents.default()
intents.message_content = True
client = Client(intents=intents)
client.run(config.discord_token)
