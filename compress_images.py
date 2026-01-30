import os
from PIL import Image

def compress_images(directory):
    valid_extensions = ('.png', '.jpg', '.jpeg')
    for filename in os.listdir(directory):
        if filename.lower().endswith(valid_extensions):
            filepath = os.path.join(directory, filename)
            with Image.open(filepath) as img:
                # Resize if the image is wider than 800px
                if img.width > 800:
                    scale = 800 / img.width
                    new_size = (800, int(img.height * scale))
                    img = img.resize(new_size, Image.Resampling.LANCZOS)
                
                # Save as optimized PNG with higher compression
                img.save(filepath, optimize=True)
                print(f"Compressed {filename} to {os.path.getsize(filepath) / 1024:.2f} KB")

if __name__ == "__main__":
    # Point to the relative path within the repo for GitHub Actions
    compress_images("docs/assets/")