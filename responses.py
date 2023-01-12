#Returns an array with reaction messages or a numbers that stand for a certain move based on the input message
def get_response(message):

    message_cleaned = str(message).lower()
    out = []

    if "pubg?" in message_cleaned:
        out.append("Wer will pubg?")
    if "civ?" in message_cleaned:
        out.append("Wer will civ?")
    if "league?" in message_cleaned:
        out.append("Wer will league?")
    if "dinner" in message_cleaned:
        out.append("Chicken Dinner :chicken:")
    if "main" in message_cleaned:
        out.append(1)
    if "hansi" in message_cleaned:
        out.append(2)
    if "lat" in message_cleaned:
        out.append(3)
    if "hallig" in message_cleaned:
        out.append(4)
    if "josser" in message_cleaned:
        out.append(9)
    if message_cleaned == "!stats":
        out.append(12)
    elif message_cleaned == "!würfeln" or message_cleaned == "!roll":
        out.append(5)
    elif "!würfeln" in message_cleaned and len(message_cleaned) > 9 or "!roll" in message_cleaned and len(message_cleaned) > 6:
        out.append(6)
    elif message_cleaned == "!münze" or message_cleaned == "!coin":
        out.append(7)
    elif message_cleaned == "!hilfe" or message_cleaned == "!help":
        out.append(8)
    elif "https://tenor.com" in message_cleaned:
        out.append(10)
    elif "https://" in message_cleaned or "http://" in message_cleaned or "www." in message_cleaned:
        out.append(11)
        
    return out
