# import it
import discord

# get a bot
bot = discord.Client()

# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
# ^ tbh idk
@bot.event
# ^ what's this?
async def on_ready():
	# CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
	guild_count = 0
	# yeah ill stop

	# LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
	for guild in bot.guilds:
		# PRINT THE SERVER'S ID AND NAME.
		print(f"- {guild.id} (name: {guild.name})")

		# INCREMENTS THE GUILD COUNTER.
		guild_count = guild_count + 1

	# PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
	print("SampleDiscordBot is in " + str(guild_count) + " guilds.")

# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
@bot.event
async def on_message(message):
	# CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".
	if message.content == "hello":
		# SENDS BACK A MESSAGE TO THE CHANNEL.
		await message.channel.send("hey dirtbag")

# Import the os module.
import os
# Import load_dotenv function from dotenv module.
from dotenv import load_dotenv
# Loads the .env file that resides on the same level as the script.
load_dotenv()
# Grab the API token from the .env file.
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")


# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot.run(DISCORD_TOKEN)