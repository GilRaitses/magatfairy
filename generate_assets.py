
import re
from PIL import Image, ImageDraw
import os

def draw_braille_char(draw, x, y, char_code, color, dot_radius=2, spacing=6):
    # Unicode Braille Pattern: U+2800 to U+28FF
    # Offset from 0x2800 gives the bitmask
    if not (0x2800 <= char_code <= 0x28FF):
        return # Not a braille char
    
    mask = char_code - 0x2800
    
    # Dot positions (col, row) 0-indexed
    # 1: (0,0)  4: (1,0)
    # 2: (0,1)  5: (1,1)
    # 3: (0,2)  6: (1,2)
    # 7: (0,3)  8: (1,3)
    
    dots = {
        0: (0, 0), # Bit 0 -> Dot 1
        1: (0, 1), # Bit 1 -> Dot 2
        2: (0, 2), # Bit 2 -> Dot 3
        3: (1, 0), # Bit 3 -> Dot 4
        4: (1, 1), # Bit 4 -> Dot 5
        5: (1, 2), # Bit 5 -> Dot 6
        6: (0, 3), # Bit 6 -> Dot 7
        7: (1, 3)  # Bit 7 -> Dot 8
    }
    
    for bit, (col, row) in dots.items():
        if mask & (1 << bit):
            cx = x + col * spacing + dot_radius
            cy = y + row * spacing + dot_radius
            draw.ellipse((cx - dot_radius, cy - dot_radius, cx + dot_radius, cy + dot_radius), fill=color)

def render_ascii_to_image(lines, color, output_file, max_size=None, crop=True):
    # Settings for manual braille drawing
    dot_radius = 2
    # Spacing between dots in a char
    dot_spacing = 5 
    # Char dimensions
    # Width: 2 cols * spacing. Height: 4 rows * spacing.
    # Add some padding.
    char_width = dot_spacing * 2 + 4
    char_height = dot_spacing * 4 + 4
    
    img_width = int(max(len(line) for line in lines) * char_width) + 20
    img_height = int(len(lines) * char_height) + 20

    img = Image.new('RGBA', (img_width, img_height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    y = 10
    for line in lines:
        x = 10
        for char in line:
            draw_braille_char(draw, x, y, ord(char), color, dot_radius, dot_spacing)
            x += char_width
        y += char_height

    # Crop
    if crop:
        bbox = img.getbbox()
        if bbox:
            img = img.crop(bbox)
        
    if max_size:
        img.thumbnail(max_size, Image.Resampling.LANCZOS)
        
    img.save(output_file)
    print(f"Generated {output_file} at size {img.size}")

def main():
    print("Starting manual braille generation...")
    
    # 1. Favicon (Fairy)
    try:
        with open('docs/assets/fairy-frames.js', 'r', encoding='utf-8') as f:
            content = f.read()
        match = re.search(r'`(.*?)`', content, re.DOTALL)
        if match:
            text = match.group(1)
            lines = text.splitlines()
            while lines and not lines[0].strip(): lines.pop(0)
            while lines and not lines[-1].strip(): lines.pop()
            
            # Chartreuse
            render_ascii_to_image(lines, (127, 255, 0, 255), "favicon.png", max_size=(64, 64))
    except Exception as e:
        print(f"Error fairy: {e}")

    # 2. Cursor (Maggot)
    try:
        with open('docs/assets/maggot-frame.js', 'r', encoding='utf-8') as f:
            content = f.read()
        
        all_lines = content.splitlines()
        all_lines = [l for l in all_lines if l.strip() not in ['[', ']']]
        frame_lines = all_lines[:40]
        while frame_lines and not frame_lines[0].strip(): frame_lines.pop(0)
        while frame_lines and not frame_lines[-1].strip(): frame_lines.pop()

        # Black
        render_ascii_to_image(frame_lines, (0, 0, 0, 255), "cursor.png", max_size=(64, 64))

    except Exception as e:
        print(f"Error maggot: {e}")

if __name__ == "__main__":
    main()
