from PIL import Image

img1 = Image.open("D:/Python Code/Best-on-Python/assignment5.png")
img2 = Image.open("D:/Python Code/Best-on-Python/linechart.png")
img3 = Image.open("D:/Python Code/Best-on-Python/task.png")
img4 = Image.open("D:/Python Code/Best-on-Python/assignment6.png")

# img1.show()
# img2.show()
# img3.show()
# img4.show()

# Join two image
width, height = img1.size
# imageSize = Image.new('RGB', (1280, 480))
# imageSize.paste(img1, (0, 0))
# imageSize.paste(img2, (width, 0))
# imageSize.save("two_image.png")
#
# print('Two Image Joined')
#
# img = Image.open('D:/Python Code/Best-on-Python/two_image.png')
# img.show()

# Join 4 images
# imageSize = Image.new('RGB', (1280, 960))
# imageSize.paste(img1, (0, 0))
# imageSize.paste(img2, (width, 0))
# imageSize.paste(img3, (0, height))
# imageSize.paste(img4, (width, height))
# imageSize.save("four_image.png")
# print('Four Image Joined ')
