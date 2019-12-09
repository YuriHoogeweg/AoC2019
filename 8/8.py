input_file = open('input.txt', 'r')
pixels = [int(pixel) for pixel in input_file.read()]

# Part 1
layer_width = 25
layer_height = 6
pixels_per_layer = layer_width * layer_height

layers = []
layer_fewest_zeroes = (float('inf'), None)

def count_char_in_layer(layer, character):
    return sum([row.count(character) for row in layer])

for i in range(0, int(len(pixels) / pixels_per_layer)):
    layer_pixels = pixels[i * pixels_per_layer:i * pixels_per_layer + pixels_per_layer]
    layer = [layer_pixels[x:x+layer_width] for x in range(0, len(layer_pixels), layer_width)]
    layers.append(layer)

    zero_count = count_char_in_layer(layer, 0)
    if zero_count < layer_fewest_zeroes[0]:
        layer_fewest_zeroes = (zero_count, layer)

print('Part 1: ' + str(count_char_in_layer(layer_fewest_zeroes[1], 1) * count_char_in_layer(layer_fewest_zeroes[1], 2)))

# Part 2
image = [[] for y in range(0, layer_height)]
for y in range(0, layer_height):
    for x in range(0, layer_width):
        pixel_value = 2
        for layer in layers: 
            pixel_value = layer[y][x]

            if pixel_value != 2:
                break

        image[y].append(pixel_value)

print('Part 2:')
for row in image:
    print(''.join(['█' if pixel == 1 else ' ' for pixel in row]))