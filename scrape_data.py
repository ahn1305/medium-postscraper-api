from PIL import Image, ImageDraw, ImageFont
import random

def generate_gradient_placeholder(title, output="placeholder.png", size=(800, 400)):
    # Predefined gradient pairs (start → end)
    gradients = [
        ((236, 72, 153), (139, 92, 246)),    # pink → purple
        ((34, 211, 238), (59, 130, 246)),    # teal → blue
        ((251, 191, 36), (244, 114, 182)),   # yellow → pink
        ((16, 185, 129), (132, 204, 22)),    # green gradient
        ((79, 70, 229), (124, 58, 237)),     # indigo → violet
    ]

    color1, color2 = random.choice(gradients)
    img = Image.new("RGB", size, color=color1)
    draw = ImageDraw.Draw(img)

    # Create vertical gradient
    for y in range(size[1]):
        ratio = y / size[1]
        r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
        g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
        b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
        draw.line([(0, y), (size[0], y)], fill=(r, g, b))

    # Load font
    try:
        font = ImageFont.truetype("arial.ttf", 36)
    except:
        font = ImageFont.load_default()

    # Text wrapping
    max_width = size[0] - 100
    words = title.split()
    lines = []
    line = ""
    for word in words:
        test_line = f"{line} {word}".strip()
        bbox = draw.textbbox((0, 0), test_line, font=font)
        if bbox[2] - bbox[0] < max_width:
            line = test_line
        else:
            lines.append(line)
            line = word
    lines.append(line)

    # Total height calculation
    total_height = sum([draw.textbbox((0, 0), l, font=font)[3] for l in lines])
    y = (size[1] - total_height) // 2

    # Draw lines centered
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        x = (size[0] - text_width) // 2
        draw.text((x, y), line, font=font, fill="white")
        y += text_height

    img.save(output)
    print(f"✅ Image saved as {output}")

generate_gradient_placeholder("Understanding Large Language Models and its use cases", "placeholder.png")
