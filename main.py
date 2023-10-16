import os
from PIL import ImageGrab, Image

clipboard_content = ImageGrab.grabclipboard()

if isinstance(clipboard_content, Image.Image):
    desktop_dir = os.path.join(os.path.expanduser('~'), 'Desktop')
    clipboard_content.save(os.path.join(desktop_dir, 'clipboard_image.png'))