from PIL import Image, ImageDraw

def createImg(colors, single_color_width=115, scale_factor=10):
    overlap = 28 * scale_factor
    img_width = len(colors) * (single_color_width * scale_factor - overlap) + overlap
    img_height = 28 * scale_factor
    img = Image.new('RGB', (img_width, img_height))
    draw = ImageDraw.Draw(img)
    x_offset = 0
    radius = 14 * scale_factor
    for color in colors:
        draw.rounded_rectangle([x_offset, 0, x_offset + single_color_width * scale_factor, img_height], fill=color, radius=radius)
        x_offset += (single_color_width * scale_factor - overlap)
    return img

dark_list = [
    "#1A1515", "#2d2424", "#453636", "#725a5a", "#9c8181", "#DCC9BC", "#ffe9c7", "#CF223E",
    "#F07342", "#E39C45", "#959A6B", "#768F80", "#756D94", "#614F76", "#7B3D79", "#AE3F82"
]
light_list = [
    "#FFF7EB", "#E0CFC6", "#C1AEAE", "#A38A8A", "#9C8181", "#483939", "#2D2424", "#B54851",
    "#D0796D", "#C6846C", "#938579", "#878985", "#877B85", "#79657A", "#794F65", "#9F596C"
]

darkImg = createImg(dark_list)
darkImg.save("color-cycle-dark.png")

lightImg = createImg(light_list)
lightImg.save("color-cycle-light.png")
