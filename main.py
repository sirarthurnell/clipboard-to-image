import uuid
import os
from PIL import ImageGrab, Image

clipboard_content = ImageGrab.grabclipboard()

if isinstance(clipboard_content, Image.Image):
    desktop_dir = os.path.join(os.path.expanduser('~'), 'Desktop')
    unique_filename = str(uuid.uuid4())
    clipboard_content.save(os.path.join(desktop_dir, f'img-{unique_filename}.png'))