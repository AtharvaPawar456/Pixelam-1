from PIL import Image, ImageFilter

def apply_filters(img_path):
    # Open the image
    img = Image.open(img_path)

    # List of filter names
    filter_names = [
        "BLUR",
        "CONTOUR",
        "DETAIL",
        "EDGE_ENHANCE",
        "EDGE_ENHANCE_MORE",
        "EMBOSS",
        "FIND_EDGES",
        "SHARPEN",
        "SMOOTH",
        "SMOOTH_MORE",
        # "GAUSSIAN_BLUR",  # Corrected name
        # "UNSHARP_MASK",
        # "BoxBlur",
        "GaussianBlur",
        "MedianFilter",
        "MinFilter",
        "MaxFilter",
        "ModeFilter",
        # "Kernel",
        # "RankFilter"
    ]

    # Apply each filter and save the result
    for filter_name in filter_names:
        if hasattr(ImageFilter, filter_name):
            # Apply the filter
            filtered_img = img.filter(getattr(ImageFilter, filter_name))

            # Save the filtered image
            filtered_img_path = f"filteredImg/{img_path.split('.')[0]}_{filter_name.lower()}.jpg"
            filtered_img.save(filtered_img_path)
        else:
            print(f"Filter '{filter_name}' not found.")

# Example usage:
img_path = "data.jpeg"  # Replace with your image path
apply_filters(img_path)
