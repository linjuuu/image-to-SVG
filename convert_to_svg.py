from PIL import Image
import numpy as np

class ConvertToSVG :
    def __init__(self):
        self.image_path = "sample.png"
        self.output_path = "output.svg"
        
    def convert(self):
        img = Image.open(self.image_path)
        width, height = img.size
        block_size = 1
        svg_code = f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">'
        
        for y in range(0, height, block_size):
            for x in range(0, width, block_size):
                block = img.crop((x, y, x + block_size, y + block_size))
                block_array = np.array(block)
                median_color = tuple(np.median(block_array, axis=(0,1)).astype(int))
                svg_code += f'<rect x="{x}" y="{y}" width="{block_size}" height="{block_size}" fill="rgb{median_color}"/>'
        
        svg_code += '</svg>'
        
        with open(self.output_path, 'w') as f:
            f.write(svg_code)
        

convert_to_svg = ConvertToSVG()
convert_to_svg.convert()