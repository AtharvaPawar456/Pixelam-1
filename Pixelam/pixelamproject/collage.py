# from PIL import Image

# def create_2x2_grid(img_path_list):
#     # Open images
#     images = [Image.open(img_path) for img_path in img_path_list]

#     # Calculate the dimensions of the grid
#     max_width = max(img.size[0] for img in images)
#     max_height = max(img.size[1] for img in images)
#     grid_width = 2 * max_width
#     grid_height = 2 * max_height

#     # Create a blank image for the grid
#     grid = Image.new('RGB', (grid_width, grid_height), color=(255, 255, 255))

#     # Paste images onto the grid
#     for i in range(2):
#         for j in range(2):
#             idx = i * 2 + j
#             if idx < len(images):
#                 img = images[idx]
#                 img_width, img_height = img.size

#                 # Calculate maximum scale factor to fit the image within the grid cell
#                 scale_factor = min(max_width / img_width, max_height / img_height)

#                 # Resize the image
#                 new_width = int(img_width * scale_factor)
#                 new_height = int(img_height * scale_factor)
#                 resized_img = img.resize((new_width, new_height), Image.ANTIALIAS)

#                 # Calculate offsets to center the image
#                 x_offset = max_width * j + (max_width - new_width) // 2
#                 y_offset = max_height * i + (max_height - new_height) // 2

#                 grid.paste(resized_img, (x_offset, y_offset))

#     return grid

# # Example usage:
# imgPath = ['cat.png', 'data.jpeg', 'hmp----.jpeg', 'upscaled_image.jpg']  # Replace with your image paths
# grid = create_2x2_grid(imgPath)
# # grid.show()  # Show the grid
# grid.save('2x2_grid.jpg')  # Save the grid


from PIL import Image
import io
import base64

def create_2x2_grid_from_base64(image_data_list):
    # Open images from base64 data
    images = [Image.open(io.BytesIO(base64.b64decode(img_data))) for img_data in image_data_list]

    # Calculate the dimensions of the grid
    max_width = max(img.size[0] for img in images)
    max_height = max(img.size[1] for img in images)
    grid_width = 2 * max_width
    grid_height = 2 * max_height

    # Create a blank image for the grid
    grid = Image.new('RGB', (grid_width, grid_height), color=(255, 255, 255))

    # Paste images onto the grid
    for i in range(2):
        for j in range(2):
            idx = i * 2 + j
            if idx < len(images):
                img = images[idx]
                img_width, img_height = img.size

                # Calculate maximum scale factor to fit the image within the grid cell
                scale_factor = min(max_width / img_width, max_height / img_height)

                # Resize the image
                new_width = int(img_width * scale_factor)
                new_height = int(img_height * scale_factor)
                resized_img = img.resize((new_width, new_height), Image.ANTIALIAS)

                # Calculate offsets to center the image
                x_offset = max_width * j + (max_width - new_width) // 2
                y_offset = max_height * i + (max_height - new_height) // 2

                grid.paste(resized_img, (x_offset, y_offset))

    return grid

# # Example usage:
# img_base64_list = ['base64_encoded_img1', 'base64_encoded_img2', 'base64_encoded_img3', 'base64_encoded_img4']
# grid = create_2x2_grid_from_base64(img_base64_list)

# # Save the grid image to a BytesIO object
# img_byte_array = io.BytesIO()
# grid.save(img_byte_array, format='JPEG')

# # Encode the BytesIO object to base64
# base64_img = base64.b64encode(img_byte_array.getvalue()).decode()

# print(base64_img)  # Print the base64 encoded collage image
