from blinkstick import blinkstick
bstick = blinkstick.find_first()
if not bstick:
    print("bstick not found.")
    exit()
bstick.set_color(red=0, green=255, blue=0)