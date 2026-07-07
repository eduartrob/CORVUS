from PIL import Image, ImageDraw, ImageFont
import sys

def create_image(filename, text, outname):
    lines = text.split('\n')
    width = 900
    height = 40 + len(lines) * 20
    img = Image.new('RGB', (width, height), color = (30, 30, 30))
    d = ImageDraw.Draw(img)
    y = 20
    for line in lines:
        d.text((20, y), line, fill=(200, 200, 200))
        y += 20
    img.save(outname)

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        text = f.read()
    create_image(sys.argv[1], text, sys.argv[2])
