import discord
from discord.ext import commands
from discord import app_commands
import aiohttp
import io
import random
import time

TOKEN = 'token'
appID = 'appIDhere'

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='-', intents=intents, application_id=appID)
tree = bot.tree

capybara_facts = [
    "Capybaras are the largest rodents in the world.",
    "An adult capybara can weigh up to 150 pounds.",
    "Capybaras are native to South America.",
    "Capybaras are highly social animals and often live in groups of 10 to 20 individuals.",
    "Capybaras are excellent swimmers and can hold their breath underwater for up to 5 minutes.",
    "Capybaras' scientific name is Hydrochoerus hydrochaeris.",
    "Capybaras have partially webbed feet, which help them swim efficiently.",
    "Capybaras can run as fast as a horse on land for short distances.",
    "Capybaras are herbivores and primarily eat grasses and aquatic plants.",
    "Capybaras have a special digestive system that allows them to digest tough plant materials efficiently.",
    "Capybaras are often found near bodies of water such as rivers, lakes, and marshes.",
    "Capybaras have a high tolerance for different temperatures and can adapt to various climates.",
    "Capybaras are known for their calm and gentle nature, making them popular in wildlife parks.",
    "Capybaras are often seen lying on the grass, basking in the sun.",
    "Capybaras have orange-brown fur that helps them blend into their natural habitat.",
    "Capybaras can sleep in the water with just their noses poking out to breathe.",
    "Capybaras have a unique way of communicating using a variety of vocalizations, including barks and whistles.",
    "Capybaras' teeth grow continuously, so they need to chew on tough vegetation to keep them worn down.",
    "Capybaras have been domesticated in some areas and kept as pets.",
    "Capybaras are often seen in the wild with other animal species, such as birds, which clean parasites off their fur.",
    "Capybaras' eyes, ears, and nostrils are positioned high on their heads to help them keep watch for predators while swimming.",
    "Capybaras can live up to 8-10 years in the wild and up to 12 years in captivity.",
    "Capybaras' social groups are usually led by a dominant male, with other males often being subordinate.",
    "Capybaras engage in mutual grooming, which helps to strengthen social bonds within the group.",
    "Capybaras have been known to form close relationships with other animal species, including monkeys and birds.",
    "Capybaras are highly adaptable and can thrive in various habitats, including tropical rainforests and savannas.",
    "Capybaras have a keen sense of hearing and can detect predators from a distance.",
    "Capybaras' webbed feet make them exceptional swimmers and allow them to navigate through aquatic vegetation.",
    "Capybaras have a specialized cecum, an organ in their digestive system that helps break down plant material.",
    "Capybaras' fur is dense and water-resistant, which helps keep them warm and buoyant in the water.",
    "Capybaras are known to be quite vocal, and their vocalizations can vary depending on their mood and situation.",
    "Capybaras often use their sharp claws to dig and create burrows or to help them find food.",
    "Capybaras' large size and gentle demeanor have earned them the nickname 'giant guinea pig.'",
    "Capybaras are sometimes hunted for their meat and hides, but they are also protected in many areas.",
    "Capybaras are excellent foragers and can consume large quantities of vegetation each day.",
    "Capybaras' groups usually have a structured social hierarchy, with each member having a specific role.",
    "Capybaras are known to be quite intelligent and can learn to recognize and respond to human commands.",
    "Capybaras' diet consists mainly of grasses, but they also eat fruits, vegetables, and aquatic plants.",
    "Capybaras have a unique way of expressing affection, including nuzzling and gentle touches.",
    "Capybaras' large size and strong limbs help them to move quickly through water and across land.",
    "Capybaras are often seen in the wild grooming each other, which helps to maintain social bonds and hygiene.",
    "Capybaras have been observed engaging in playful behaviors, such as chasing and splashing in the water.",
    "Capybaras' ability to adapt to different environments has allowed them to thrive in both wild and captive settings.",
    "Capybaras' gentle nature and social behavior make them fascinating animals to study and observe.",
    "Capybaras have a unique combination of physical and behavioral traits that make them well-suited to their aquatic lifestyle.",
    "Capybaras' large size and friendly demeanor often make them a favorite among wildlife enthusiasts and animal lovers.",
    "Capybaras' social structure and group dynamics are complex and can vary depending on their environment and circumstances.",
    "Capybaras' ability to form strong bonds with other animals and with humans highlights their social and adaptable nature.",
    "Capybaras are often featured in wildlife documentaries and conservation programs due to their interesting behavior and habitat.",
    "Capybaras' presence in their natural habitat plays a crucial role in maintaining the balance of their ecosystem.",
    "Capybaras' diet and feeding habits contribute to the health and diversity of the plant life in their environment.",
    "Capybaras' unique physical characteristics and behaviors make them an important subject of study in the field of animal science."
]

@bot.event
async def on_ready():
    await tree.sync()
    print(f"{bot.user.name} connected.")

@tree.command(name="helloworld", description="Just a testing command. Says \"Hello, world!\"")
async def hello(interaction: discord.Interaction):
    embed = discord.Embed(
        description="**Hello, world!**",
        color=discord.Color.blurple()
    )
    await interaction.response.send_message(embed=embed)

@bot.command(name="ping", help="| Ping Pong, tells you the bot's latency :)")
async def ping(ctx):
    await ctx.reply(f"Pong! {round(bot.latency * 1000)}ms")

@tree.command(name="ping", description="Pong!")
async def pingslash(interaction: discord.Interaction):
    await interaction.response.send_message(f"Pong! {round(bot.latency * 1000)}ms")

@tree.command(name="capybara", description="Cute capy picture!")
async def capyslash(interaction: discord.Interaction):
    url = "https://api.capy.lol/v1/capybara"

    start_time = time.monotonic()

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                image_data = await response.read()
                file = discord.File(io.BytesIO(image_data), filename="capybara.jpg")
                await interaction.response.send_message(file=file)

                elapsed_time = time.monotonic() - start_time
                print(f"Time taken to send capybara image: {elapsed_time:.2f} seconds")
            else:
                await interaction.response.send_message(f"❌ Unable to fetch a capybara image. Please try again later.")

@tree.command(name="fact", description="Get a random fact about capybaras!")
async def factslash(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Capybara Fact",
        description=random.choice(capybara_facts),
        color=discord.Color.blurple()
    )
    embed.set_footer(text="Did you know? These facts are homemade! Suggest a new one in the support server.")
    await interaction.response.send_message(embed=embed)

@tree.command(name="about", description="Learn about CapyPic!")
async def aboutslash(interaction: discord.Interaction):
    embed = discord.Embed(
        title="About CapyPic",
        description=f"I am a Discord bot who will serve you a picture of a capybara or capybara fact any time you want it!",
        color=discord.Color.blurple()
    )
    embed.add_field(name="Version", value="2.0", inline=True)
    embed.add_field(name="Source", value="Coming Soon! CapyPic's source code will be available in the future.", inline=True)
    embed.add_field(name="Add Bot", value="[Invite!](https://rdr.lol/go/invitecapypic)", inline=True)
    embed.add_field(name="Support Server", value="Join for help, suggestions, community and more! [Join!](https://discord.gg/3TbqBBEZCC)", inline=True)
    embed.add_field(name="Website", value="[Go!](https://jabin.is-a.dev/capypic)", inline=True)
    embed.add_field(name="Server Count", value=f"I am in {len(bot.guilds)} servers.")
    embed.set_footer(text="We get capybaras from capy.lol's api.")
    await interaction.response.send_message(embed=embed)

@bot.command(name="about")
async def about(ctx):
    embed = discord.Embed(
        title="About CapyPic",
        description=f"I am a Discord bot who will serve you a picture of a capybara or capybara fact any time you want it!",
        color=discord.Color.blurple()
    )
    embed.add_field(name="Version", value="2.0", inline=True)
    embed.add_field(name="Source", value="Coming Soon! CapyPic's source code will be available in the future.", inline=True)
    embed.add_field(name="Add Bot", value="[Invite!](https://rdr.lol/go/invitecapypic)", inline=True)
    embed.add_field(name="Support Server", value="Join for help, suggestions, community and more! [Join!](https://discord.gg/3TbqBBEZCC)", inline=True)
    embed.add_field(name="Website", value="[Go!](https://jabin.is-a.dev/capypic)", inline=True)
    embed.add_field(name="Server Count", value=f"I am in {len(bot.guilds)} servers.")
    embed.set_footer(text="We get capybaras from capy.lol's api.")
    await ctx.reply(embed=embed)

@bot.command(name='capy')
async def get_capybara(ctx):
    url = "https://api.capy.lol/v1/capybara"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                image_data = await response.read()
                file = discord.File(io.BytesIO(image_data), filename="capybara.jpg")
                await ctx.send(file=file)
            else:
                await ctx.send(f"❌ Unable to fetch a capybara image. Please try again later.")

@bot.command(name='capybara')
async def get_capybara(ctx):
    url = "https://api.capy.lol/v1/capybara"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                image_data = await response.read()
                file = discord.File(io.BytesIO(image_data), filename="capybara.jpg")
                await ctx.send(file=file)
            else:
                await ctx.send(f"❌ Unable to fetch a capybara image. Please try again later.")

@bot.command(name='capyfact')
async def capyfact(ctx):
    embed = discord.Embed(
        title="Capybara Fact",
        description=random.choice(capybara_facts),
        color=discord.Color.blurple()
    )
    embed.set_footer(text="Did you know? These facts are homemade! Suggest a new one in the support server.")
    await ctx.reply(embed=embed)

bot.run(TOKEN)