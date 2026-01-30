import os
from PIL import Image

def compress_images(directory):
    valid_extensions = ('.png', '.jpg', '.jpeg')
    for filename in os.listdir(directory):
        if filename.lower().endswith(valid_extensions):
            filepath = os.path.join(directory, filename)
            with Image.open(filepath) as img:
                if img.width > 800:
                    new_height = int((800 / img.width) * img.height)
                    img = img.resize((800, new_height), Image.Resampling.LANCZOS)
                img.save(filepath, optimize=True, quality=85)
                                
if __name__ == "__main__":
    assets_path = os.path.expanduser("~/rootcausesystems/website/docs/assets/")
    compress_images(assets_path)