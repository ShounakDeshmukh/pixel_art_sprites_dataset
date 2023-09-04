# from PIL import Image

# background = Image.open("spritesheets/body/bodies/male/fur_grey.png")
# overlay1 = Image.open("spritesheets/head/heads/human_male/universal/fur_black.png")
# overlay2 = Image.open("spritesheets/eyes/male_gray.png")
# overlay3= Image.open("spritesheets/torso/jacket/trench/male/dark_gray.png")
# overlay4= Image.open("spritesheets/weapon/polearm/scythe/scythe.png")

# # ... Add more overlay images as needed


# result = Image.new("RGBA", background.size)

# result.paste(background, (0, 0))

# # Overlay the first image
# result = Image.alpha_composite(result, overlay1)

# # Overlay the second image
# result = Image.alpha_composite(result, overlay2)
# result = Image.alpha_composite(result, overlay3)
# # result = Image.alpha_composite(result, overlay4)

# result=result.crop(box=(0,640,64,640+64))

# result.show()  # Display the final result


# STRUCTURE = (gender,cape,head,eyes,neck,hair,hat,facial,body,arms,legs,wrists,gloves,dress,feet,shoulders,beards,bauldrons,shield)  # noqa: E501
import os


# For Pure male 
# Cape 
cape = os.listdir('spritesheets/1.cape/male/')
# Head color
head = os.listdir('spritesheets/2.head/human_male/universal/')
# eye color
eye = os.listdir('spritesheets/3.eyes/male/')
# ear color and type
ear  = os.listdir('spritesheets/4.ears/')
# nose type and color
nose = os.listdir('spritesheets/5.nose/')
# facial ornaments (glasses etc)
facial = os.listdir('spritesheets/6.facial/')     
# body color
body = os.listdir('spritesheets/7.body/bodies/male/')
# hair
hair = os.listdir('spritesheets/8.hair/male/')


print((len(cape)+1)*len(head)*len(eye)*len(ear)*len(nose)*(len(facial)+1)*len(body)*len(hair))