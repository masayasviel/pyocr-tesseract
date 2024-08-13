import pyocr
from PIL import Image

tools = pyocr.get_available_tools()
tool = tools[0]

txt = tool.image_to_string(
    Image.open('./assets/kurohitsugi.png'),
    lang='jpn+eng',
    builder=pyocr.builders.TextBuilder(tesseract_layout=6)
)

with open('./out/o.txt', 'w') as f:
    f.write(txt)
