# result=result.crop(box=(0,640,64,640+64))

# result.show()  # Display the final result


# STRUCTURE = (gender,cape,head,eyes,neck,hair,hat,facial,body,arms,legs,wrists,gloves,dress,feet,shoulders,beards,bauldrons,shield)  # noqa: E501
import os
from PIL import Image
from numpy.random import choice 
import numpy as np

# Male Warrior assets



# Head color
head = os.listdir('spritesheets/2.head/human_male/universal/')
head_color=choice(head)

# eye color
eye = os.listdir('spritesheets/3.eyes/male/')
eye = choice(eye)
# ear color and type
ear  = os.listdir('spritesheets/4.ears/')
ear = choice(ear)
# nose type and color
nose = os.listdir('spritesheets/5.nose/')
# facial ornaments (glasses etc)
facial = os.listdir('spritesheets/6.facial/')
facial = choice(facial)
facial = [facial,None]
facial = choice(facial)

# body color
body_color = head_color
# hair
hair = os.listdir('spritesheets/8.hair/male/')
hair.append(None)
# arms
arms = os.listdir('spritesheets/9.arms/armour/male/')
arms.append(None)
arms=choice(arms)
# bauldron
bauldron = os.listdir('spritesheets/10.bauldron/male/')
bauldron.append(None)
bauldron = choice(bauldron)
# leg wear
legs = os.listdir('spritesheets/11.legs/male/')
legs = choice(legs)
# beards (facial hair in general)
beards = os.listdir('spritesheets/12.beards/')
beards.append(None)
#footwear 
feet = os.listdir('spritesheets/13.feet/armour/male/')
feet.append(None)
# helmet 
helmet = os.listdir('spritesheets/14.hat/helmet/')
helmet.append(None)

# helmet accessory 
helmet_accs = os.listdir('spritesheets/14.hat/accessory/male/')
helmet_accs.append(None)

# Cape color
cape = os.listdir('spritesheets/1.cape/male/')
cape.append(None)
cape = choice(cape)




body_overlay = Image.open('spritesheets/7.body/bodies/male/'+head_color)
resultant = Image.new("RGBA",body_overlay.size)
resultant.paste(body_overlay, (0, 0))

head_overlay = Image.open('spritesheets/2.head/human_male/universal/'+head_color)
resultant = Image.alpha_composite(resultant,head_overlay)

eye_overlay = Image.open('spritesheets/3.eyes/male/'+eye)
resultant = Image.alpha_composite(resultant,eye_overlay)

ear_overlay = Image.open('spritesheets/4.ears/'+ear)
resultant = Image.alpha_composite(resultant,ear_overlay)

if facial is not None:
    facial_overlay = Image.open('spritesheets/6.facial/'+facial)
    resultant = Image.alpha_composite(resultant,facial_overlay)

if arms is not None:
    arms_overlay = Image.open('spritesheets/9.arms/armour/male/'+arms)
    resultant = Image.alpha_composite(resultant,arms_overlay)

legs_overlay = Image.open('spritesheets/11.legs/male/'+legs)
resultant = Image.alpha_composite(resultant,legs_overlay)




resultant.show()