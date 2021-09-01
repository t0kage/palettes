from PIL import Image, ImageDraw


def draw_image_from_palette(palette, height):
    paletteout = Image.new('HSV', (len(palette)*height, height),
                         color=255)
    palettedraw = ImageDraw.Draw(paletteout)

    for i in range(len(palette)):
        shape = (height * i, height, height * (i + 1), 0)
        palettedraw.rectangle(shape, fill=palette[i])

    paletteout.show()
