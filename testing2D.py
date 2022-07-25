
try:
    from PIL import Image
except ImportError:
    import Image

background = Image.open("testimage.png")
overlay = Image.open("rotatedimage.png")

background = background.convert("RGBA")
overlay = overlay.convert("RGBA")

new_img = Image.blend(background, overlay, 0.5)
new_img.save("new.png","PNG")
