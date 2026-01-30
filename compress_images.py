import os
from PIL import Image

def compress_images(directory):
    valid_extensions = ('.png', '.jpg', '.jpeg')
    
    for filename in os.listdir(directory):
        if filename.lower().endswith(valid_extensions):
            filepath = os.path.join(directory, filename)
            
            with Image.open(filepath) as img:
                print(f"Original size of {filename}: {os.path.getsize(filepath) / 1024:.2f} KB")
                
                img.save(filepath, optimize=True, quality=85)
                
                print(f"New size of {filename}: {os.path.getsize(filepath) / 1024: .2f} KB")
                
if __name__ == "__main__":
    assets_path = os.path.expanduser("~/rootcausesystems/website/docs/assets/")
    compress_images(assets_path)