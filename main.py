from PIL import Image

background = Image.open("spritesheets/body/bodies/male/fur_grey.png")
overlay1 = Image.open("spritesheets/head/heads/human_male/universal/fur_black.png")
overlay2 = Image.open("spritesheets/eyes/male_gray.png")
overlay3= Image.open("spritesheets/torso/jacket/trench/male/dark_gray.png")
overlay4= Image.open("spritesheets/weapon/polearm/scythe/scythe.png")

# ... Add more overlay images as needed


result = Image.new("RGBA", background.size)

result.paste(background, (0, 0))

# Overlay the first image
result = Image.alpha_composite(result, overlay1)

# Overlay the second image
result = Image.alpha_composite(result, overlay2)
result = Image.alpha_composite(result, overlay3)
# result = Image.alpha_composite(result, overlay4)

result=result.crop(box=(0,640,64,640+64))

result.show()  # Display the final result
