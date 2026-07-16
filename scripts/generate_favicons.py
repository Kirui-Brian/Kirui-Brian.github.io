import os
import base64
from PIL import Image, ImageDraw

def main():
    profile_path = 'images/profile.png'
    output_dir = 'images'
    
    if not os.path.exists(profile_path):
        print(f"Error: Profile picture not found at {profile_path}")
        return
        
    print(f"Loading profile picture from {profile_path}...")
    img = Image.open(profile_path)
    
    # Ensure it's square
    width, height = img.size
    if width != height:
        print(f"Profile image is not square ({width}x{height}). Cropping to square...")
        min_dim = min(width, height)
        left = (width - min_dim) / 2
        top = (height - min_dim) / 2
        right = (width + min_dim) / 2
        bottom = (height + min_dim) / 2
        img = img.crop((left, top, right, bottom))
        
    # Convert to RGBA and apply a circular mask
    img = img.convert("RGBA")
    mask = Image.new("L", img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, img.size[0], img.size[1]), fill=255)
    img.putalpha(mask)
        
    # 1. Save standard PNG sizes
    sizes = {
        'favicon-32x32.png': (32, 32),
        'favicon-192x192.png': (192, 192),
        'favicon-512x512.png': (512, 512),
        'apple-touch-icon-180x180.png': (180, 180)
    }
    
    for filename, size in sizes.items():
        out_path = os.path.join(output_dir, filename)
        resized_img = img.resize(size, Image.Resampling.LANCZOS)
        resized_img.save(out_path, format='PNG')
        print(f"Generated {out_path} ({size[0]}x{size[1]})")
        
    # 2. Save ICO file (contains multiple sizes: 16x16, 32x32, 48x48)
    ico_path = os.path.join(output_dir, 'favicon.ico')
    # Pillow allows saving ICO files with standard sizes
    # We can pass a list of sizes to save
    img.save(ico_path, format='ICO', sizes=[(16, 16), (32, 32), (48, 48)])
    print(f"Generated {ico_path} with 16x16, 32x32, 48x48 sizes")
    
    # 3. Save SVG file containing Base64 encoded PNG
    # Use the 192x192 size for embedding to keep it lightweight but sharp enough
    svg_path = os.path.join(output_dir, 'favicon.svg')
    resized_192 = img.resize((192, 192), Image.Resampling.LANCZOS)
    
    # Temporarily save to a byte buffer to get base64 bytes
    import io
    buffered = io.BytesIO()
    resized_192.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
    
    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 192 192" width="100%" height="100%">
  <image href="data:image/png;base64,{img_str}" x="0" y="0" width="192" height="192"/>
</svg>
'''
    with open(svg_path, 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print(f"Generated {svg_path} (Base64-embedded SVG)")
    
    print("All favicons successfully generated!")

if __name__ == '__main__':
    main()
