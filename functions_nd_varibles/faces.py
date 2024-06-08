def main():
    emoji_text = convert(input())
    print(emoji_text)


def convert(emoticon):
    emoticon = emoticon.replace(":)", "🙂")
    emoticon = emoticon.replace(":(", "🙁")
    return emoticon

main()