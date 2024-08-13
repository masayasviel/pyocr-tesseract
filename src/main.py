import pyocr
from PIL import Image

tools = pyocr.get_available_tools()
tool = tools[0]

image = Image.open('./assets/qruppo.png').convert("L")
image.point(lambda x: 0 if x < 128 else x)

txt = tool.image_to_string(
    image,
    lang='jpn',
    builder=pyocr.builders.TextBuilder(tesseract_layout=6)
)

with open('./out/o.txt', 'w') as f:
    f.write(txt)
