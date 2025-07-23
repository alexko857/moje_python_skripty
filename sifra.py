
rot = int(input("zadaj rotaciu:"))
action = input("[s]ifrovat alebo [d]esifrovat:")
data = input("zadaj text:")
if action == "s" or action == "sifrovat":
    text = ""
    for char in data:
        char_ord = ord(char)
        if 32 <= char_ord <= 126:
            char_ord -=32
            char_ord += rot
            char_ord = char_ord%94
            char_ord +=32
            text += chr(char_ord)
    print("tvoj text:{}".format(text))
elif action == "d" or action == "desifrovat":
    text = ""
    for char in data:
        char_ord = ord(char)
        if 32 <= char_ord <= 126:
            char_ord -=32
            char_ord -= rot
            char_ord = char_ord%94
            char_ord +=32
            text += chr(char_ord)
    print("tvoj text :{}".format(text))
