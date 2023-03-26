import os
from pathlib import Path
from PIL import Image

def convert_pdf(source: Path, destiny: Path):
    """Convert a directory of images to a PDF file."""
    source = Path(source).resolve().absolute()
    destiny = Path(destiny).resolve().absolute()

    # Create a list of images in the directory
    images_paths = []
    for file in os.listdir(source):
        if file.endswith(".jpg") or file.endswith(".png"):
            images_paths.append(Path(source / file).resolve())

    # Sort the list of images in alphabetical order
    images_paths.sort()
    images = [Image.open(image) for image in images_paths]

    # Create the PDF file
    pdf_path = Path(destiny / (os.path.basename(source) + '.pdf'))
    images[0].save(
        pdf_path, 'PDF', resolution=100.0, save_all=True, append_images=images[1:]
    )

if __name__ == '__main__':
    # Convert the images to PDF
    pass