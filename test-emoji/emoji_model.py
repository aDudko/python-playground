class Emoji:

    def __init__(self, emoji):
        self.emoji = emoji
        self.emoji_len = len(emoji.encode('ascii', 'replace'))
