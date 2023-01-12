import discord
import responses
import roll
from pymongo_get_database import get_database

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
TOKEN = "MTA2MTYyNjg0NzQ0OTg0OTg5Ng.GNWj6y.QjMHkan78U0r6yctVDvLl-lpsm-Cnbk9eCY420"

#Reads the gifs and links values in the db and returns an output string
def read_db(db):
  mycol = db["Chat"]
  gifs = mycol.find_one()["gifs"]
  links = mycol.find_one()["links"]
  out = "Es wurden schon " + str(gifs) + " gifs und " + str(links) + " links gepostet"
  return out

#Increments the key value in the db collection chat with 1
def update_db(db, key):
  mycol = db["Chat"]
  new_value = mycol.find_one()[key] + 1
  updating_value = { "$set": {key: new_value} }
  mycol.update_one({key: new_value-1}, updating_value)
  
def run_bot():
  
  db = get_database() 

  allowed_mentions = discord.AllowedMentions(everyone=True)

  @client.event
  async def ready():
    print(f'{client.user} is now running')

  @client.event
  async def on_message(message):
    if message.author != client.user:     #Prevents the bot from answering to itself
      answers = responses.get_response(message.content)  #Returns an array of possible Messages and Numbers

      #Adds the right messages or reactions
      for i in answers:
        if (type(i) is str):
          if "Wer will" in i:             
            sent = await message.channel.send(
              content="@everyone " + i, allowed_mentions=allowed_mentions)
            await sent.add_reaction("☑️")
            await sent.add_reaction("❌")
          else:
            await message.channel.send(i)
        elif (i == 1):
          for x in client.emojis:
            if x.name == "AliSchwarzenegger":
              await message.add_reaction(x)
        elif (i == 2):
          for x in client.emojis:
            if x.name == "HansiWeasley":
              await message.add_reaction(x)
        elif (i == 3):
          for x in client.emojis:
            if x.name == "hhhh":
              await message.add_reaction(x)
        elif (i == 4):
          for x in client.emojis:
            if x.name == "Emote2":
              await message.add_reaction(x)
        elif (i == 5):
          out = roll.roll_100(message)
          await message.channel.send(out)
        elif (i == 6):
          out = roll.roll_numbers(message)
          await message.channel.send(out)
        elif (i == 7):
          out = roll.throw_coin()
          await message.channel.send(out)
        elif (i == 8):
          await message.channel.send("Mögliche Kommandos sind: !coin !roll !stats")
        elif (i == 9):
          await message.add_reaction("♿")
        elif (i == 10):
          out = update_db(db, "gifs")
        elif (i == 11):
          out = update_db(db, "links")
        elif (i == 12):
          out = read_db(db)
          await message.channel.send(out)
                       
  client.run(TOKEN)
