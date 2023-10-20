def identify_shapes(shelf_layout):
    brand_shapes = {}  # Dictionary to store brand shapes and locations

    # Define functions to check if a given region is a specific shape
    def is_horizontal_rectangle(region):
        return all(all(cell == 'B' for cell in row) for row in region)

    def is_vertical_rectangle(region):
        return all(all(cell == 'G' for cell in column) for column in region)

    def is_square(region):
        return is_horizontal_rectangle(region) and is_vertical_rectangle(region)

    def is_polygon(region):
        return not is_horizontal_rectangle(region) and not is_vertical_rectangle(region)

    # Iterate through the shelf layout
    for row in range(len(shelf_layout)):
        for col in range(len(shelf_layout[0])):
            brand = shelf_layout[row][col]

            # Check if the brand is not already identified
            if brand not in brand_shapes:
                # Find the region around the brand
                region = []

                for i in range(row, len(shelf_layout)):
                    if all(cell == brand for cell in shelf_layout[i][col:]):
                        region.append(shelf_layout[i][col:])
                    else:
                        break

                # Determine the shape of the brand and its location
                if is_horizontal_rectangle(region):
                    shape = 'horizontal rectangle'
                    location = ['bottom left'] if brand == 'B' else ['middle right']
                elif is_vertical_rectangle(region):
                    shape = 'vertical rectangle'
                    location = ['left'] if brand == 'G' else ['right']
                elif is_square(region):
                    shape = 'square'
                    location = ['bottom left'] if brand == 'B' else ['top left']
                elif is_polygon(region):
                    shape = 'polygon'
                    location = ['top left'] if brand == 'G' else ['right']

                # Store the result in the dictionary
                brand_shapes[brand] = {'shape': shape, 'location': location}

    return brand_shapes

# Test cases
shelf_layout1 = [
    ['G', 'M', 'N', 'B'],
    ['G', 'M', 'N', 'B'],
    ['G', 'M', 'N', 'B'],
    ['G', 'M', 'N', 'B']
]

shelf_layout2 = [
    ['G', 'G', 'M', 'M'],
    ['G', 'G', 'M', 'M'],
    ['B', 'B', 'N', 'N'],
    ['B', 'B', 'N', 'N']
]

shelf_layout3 = [
    ['G', 'G', 'G', 'M', 'M', 'M', 'M'],
    ['G', 'B', 'G', 'M', 'N', 'N', 'M'],
    ['G', 'G', 'G', 'M', 'N', 'N', 'M'],
    ['B', 'B', 'B', 'B', 'B', 'N', 'N']
]

output1 = identify_shapes(shelf_layout1)
output2 = identify_shapes(shelf_layout2)
output3 = identify_shapes(shelf_layout3)

print(output1)
print(output2)
print(output3)

print('adding the new features')
