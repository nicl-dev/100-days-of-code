import colorgram

random_colors = colorgram.extract('image.jpg', 10)
my_colors = []

for color in random_colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb = (r, g, b)
    my_colors.append(rgb)

print(my_colors)