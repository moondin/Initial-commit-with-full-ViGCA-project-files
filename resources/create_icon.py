"""
Icon Generator for ViGCA

Creates a simple icon file for the ViGCA application.
"""
import os
try:
    from PIL import Image, ImageDraw, ImageFont
    has_pil = True
except ImportError:
    has_pil = False
    print("PIL not installed. Please install Pillow with: pip install Pillow")

def create_icon():
    """Create a simple icon for ViGCA."""
    if not has_pil:
        return False
    
    # Create a blank image with a blue background
    icon_size = 256
    img = Image.new('RGBA', (icon_size, icon_size), color=(0, 120, 212, 255))
    draw = ImageDraw.Draw(img)
    
    # Draw a white circular background
    padding = 20
    draw.ellipse(
        (padding, padding, icon_size - padding, icon_size - padding), 
        fill=(255, 255, 255, 255)
    )
    
    # Draw inner elements
    # - Circle for "eye"
    eye_size = 100
    eye_pos = (icon_size // 2 - eye_size // 2, icon_size // 2 - eye_size // 2 - 20)
    draw.ellipse(
        (eye_pos[0], eye_pos[1], eye_pos[0] + eye_size, eye_pos[1] + eye_size),
        fill=(0, 120, 212, 255),
        outline=(0, 80, 160, 255),
        width=3
    )
    
    # - Pupil
    pupil_size = 40
    pupil_pos = (icon_size // 2 - pupil_size // 2, icon_size // 2 - pupil_size // 2 - 20)
    draw.ellipse(
        (pupil_pos[0], pupil_pos[1], pupil_pos[0] + pupil_size, pupil_pos[1] + pupil_size),
        fill=(0, 0, 0, 255)
    )
    
    # - Mouse cursor
    cursor_size = 50
    cursor_start = (icon_size // 2 - 30, icon_size // 2 + 40)
    # Arrow shape
    points = [
        cursor_start,
        (cursor_start[0] + cursor_size, cursor_start[1] + cursor_size // 2),
        (cursor_start[0] + cursor_size // 2, cursor_start[1] + cursor_size // 2),
        (cursor_start[0] + cursor_size, cursor_start[1] + cursor_size),
        (cursor_start[0] + cursor_size // 2, cursor_start[1] + cursor_size // 1.5),
        (cursor_start[0] + cursor_size // 3, cursor_start[1] + cursor_size),
        cursor_start
    ]
    draw.polygon(points, fill=(0, 0, 0, 255))
    
    # Save as PNG first (ICO support might be limited)
    png_path = os.path.join(os.path.dirname(__file__), "vigca_icon.png")
    img.save(png_path)
    
    # Try to save as ICO if possible
    try:
        ico_path = os.path.join(os.path.dirname(__file__), "vigca_icon.ico")
        # Convert to sizes commonly used in ICO files
        img.save(ico_path, format="ICO", sizes=[(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])
        print(f"Icon created successfully: {ico_path}")
        print(f"PNG version also available: {png_path}")
        return True
    except Exception as e:
        print(f"Could not create ICO file: {e}")
        print(f"PNG version is available: {png_path}")
        return False

if __name__ == "__main__":
    create_icon()