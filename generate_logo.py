#!/usr/bin/env python3
"""
Daily Challenge Logo Generator

This script generates a simple logo for the Daily Challenge repository.
The logo includes:
- Text "Daily Challenge"
- Gradient background
- Optional simple icon (a star)

Requirements:
- Python 3.x
- Pillow library (install with: pip install Pillow)

Usage:
    python3 generate_logo.py

Output:
    Creates a file named 'daily_challenge_logo.png' in the current directory.
"""

from PIL import Image, ImageDraw, ImageFont
import sys


def create_gradient(width, height, color1, color2):
    """
    Create a vertical gradient from color1 to color2.
    
    Args:
        width: Width of the gradient
        height: Height of the gradient
        color1: Starting color (R, G, B)
        color2: Ending color (R, G, B)
    
    Returns:
        PIL Image object with gradient
    """
    base = Image.new('RGB', (width, height), color1)
    top = Image.new('RGB', (width, height), color2)
    mask = Image.new('L', (width, height))
    mask_data = []
    
    for y in range(height):
        # Linear gradient from top to bottom
        alpha = int(255 * (y / height))
        mask_data.extend([alpha] * width)
    
    mask.putdata(mask_data)
    base.paste(top, (0, 0), mask)
    return base


def draw_star(draw, center_x, center_y, size, color):
    """
    Draw a simple 5-pointed star.
    
    Args:
        draw: ImageDraw object
        center_x: X coordinate of star center
        center_y: Y coordinate of star center
        size: Size of the star
        color: Color of the star (R, G, B)
    """
    import math
    
    points = []
    for i in range(10):
        angle = (i * 36 - 90) * math.pi / 180
        if i % 2 == 0:
            # Outer points
            x = center_x + size * math.cos(angle)
            y = center_y + size * math.sin(angle)
        else:
            # Inner points
            x = center_x + (size * 0.4) * math.cos(angle)
            y = center_y + (size * 0.4) * math.sin(angle)
        points.append((x, y))
    
    draw.polygon(points, fill=color)


def generate_logo(output_file='daily_challenge_logo.png', width=800, height=400):
    """
    Generate the Daily Challenge logo.
    
    Args:
        output_file: Path where the logo will be saved
        width: Width of the logo in pixels
        height: Height of the logo in pixels
    """
    # Define colors
    color_start = (41, 128, 185)  # Blue
    color_end = (142, 68, 173)    # Purple
    text_color = (255, 255, 255)  # White
    star_color = (241, 196, 15)   # Gold
    
    # Create gradient background
    print(f"Creating logo with dimensions {width}x{height}...")
    img = create_gradient(width, height, color_start, color_end)
    draw = ImageDraw.Draw(img)
    
    # Draw decorative stars
    star_size = 30
    star_positions = [
        (100, 80),
        (700, 100),
        (120, 320),
        (680, 340)
    ]
    
    for x, y in star_positions:
        draw_star(draw, x, y, star_size, star_color)
    
    # Add text
    try:
        # Try to use a nice font if available
        font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 80)
        font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 40)
    except:
        # Fallback to default font
        print("Using default font (TrueType font not found)")
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    # Calculate text position (centered)
    text1 = "Daily"
    text2 = "Challenge"
    
    # Get text bounding boxes for centering
    bbox1 = draw.textbbox((0, 0), text1, font=font_large)
    bbox2 = draw.textbbox((0, 0), text2, font=font_large)
    
    text1_width = bbox1[2] - bbox1[0]
    text2_width = bbox2[2] - bbox2[0]
    
    # Draw text with shadow for better visibility
    shadow_offset = 3
    shadow_color = (0, 0, 0, 128)
    
    # "Daily" text
    x1 = (width - text1_width) // 2
    y1 = height // 2 - 80
    draw.text((x1 + shadow_offset, y1 + shadow_offset), text1, fill=shadow_color, font=font_large)
    draw.text((x1, y1), text1, fill=text_color, font=font_large)
    
    # "Challenge" text
    x2 = (width - text2_width) // 2
    y2 = height // 2 + 10
    draw.text((x2 + shadow_offset, y2 + shadow_offset), text2, fill=shadow_color, font=font_large)
    draw.text((x2, y2), text2, fill=text_color, font=font_large)
    
    # Save the image
    img.save(output_file)
    print(f"✓ Logo saved successfully to: {output_file}")
    print(f"  Dimensions: {width}x{height} pixels")
    print(f"  You can now use this logo in your repository!")


def main():
    """Main function to run the logo generator."""
    print("=" * 60)
    print("Daily Challenge Logo Generator")
    print("=" * 60)
    print()
    
    try:
        generate_logo()
        print()
        print("Instructions:")
        print("1. The logo has been generated as 'daily_challenge_logo.png'")
        print("2. You can add it to your README.md with:")
        print("   ![Daily Challenge Logo](daily_challenge_logo.png)")
        print("3. Feel free to modify the script to customize:")
        print("   - Colors (color_start, color_end)")
        print("   - Dimensions (width, height)")
        print("   - Text content")
        print("   - Star positions and colors")
        print()
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
