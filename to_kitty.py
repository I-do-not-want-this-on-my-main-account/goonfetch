from io import BytesIO
from typing import Tuple
from PIL import Image as pillow_image
from rich.console import Console
from textual_image.renderable.tgp import Image

def print_kitty(img: BytesIO, sizes: Tuple[int | None] = (None, None)) -> None:
    console = Console()
    console.print(Image(pillow_image.open(img), sizes[0], sizes[1]))
