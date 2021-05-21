from PIL import Image, ImageFilter

before = Image.open("D:\Code\python\Code\Capture.png")
after = before.filter(ImageFilter.BoxBlur(5))
after.save("out.png")