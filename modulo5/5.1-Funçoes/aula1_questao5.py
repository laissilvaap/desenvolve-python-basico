import emoji
emojis = {
    ":red_heart:": "❤️",
    ":thumbs_up:": "👍",
    ":thinking_face:": "🤔",
    ":partying_face:": "🥳"
}

print("Emojis:")
for emoji_char, emoji_code in emojis.items():
    print(f"{emoji_char} - {emoji_code}")

frase = input("Digite uma frase e ela será emojizada: ")

frase_emoji = emoji.emojize(frase)

print("Frase emojizada: ",frase_emoji)
