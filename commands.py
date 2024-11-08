import random
def emoji_maker():
    emoji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923", "\U0001F635"] #https://unicode.org/emoji/charts/full-emoji-list.html
    return random.choice(emoji)

def heads_tails():
    choice = random.randint(0,1)
    if choice < 1:
        return "YAZI"
    else:
        return "TURA"