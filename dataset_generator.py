import os
from PIL import Image
from numpy.random import choice


def generate_dataset(numchars):
    train = []
    test = []
    ############# DIRS #############
    head_dir = os.listdir("spritesheets/2.head/human_male/universal/")
    eye_dir = os.listdir("spritesheets/3.eyes/male/")
    ear_dir = os.listdir("spritesheets/4.ears/")
    nose_dir = os.listdir("spritesheets/5.nose/")
    facial_dir = os.listdir("spritesheets/6.facial/")
    hair_dir = os.listdir("spritesheets/8.hair/male/")
    torso_dir = os.listdir("spritesheets/15.torso/male/")
    arms_dir = os.listdir("spritesheets/9.arms/armour/male/")
    bauldron_dir = os.listdir("spritesheets/10.bauldron/male/")
    legs_dir = os.listdir("spritesheets/11.legs/male/")
    feet_dir = os.listdir("spritesheets/13.feet/male/")
    helmet_dir = os.listdir("spritesheets/14.hat/helmet/male/")
    helmet_accs_dir = os.listdir("spritesheets/14.hat/accessory/male/")
    shoulder_dir = os.listdir("spritesheets/shoulders/male/")
    shield_dir = os.listdir("spritesheets/shield/male/")
    weapon_dir = os.listdir("spritesheets/weapon/")

    for i in range(numchars):
        # Head color
        head_color = choice(head_dir)

        # eye color
        eye = choice(eye_dir)

        # ear color and type
        ear = choice(ear_dir)

        # nose type and color
        nose = choice(nose_dir)

        # facial ornaments (glasses etc)
        facial = choice([choice(facial_dir), None], p=[0.3, 0.7])

        # body color
        body_color = head_color

        # hair
        hair = choice([choice(hair_dir), None], p=[0.6, 0.4])

        torso = choice(torso_dir)
        # arms
        arms = choice([choice(arms_dir), None], p=[0.8, 0.2])

        # bauldron
        bauldron = choice([choice(bauldron_dir), None])

        # leg wear
        legs = choice(legs_dir)

        # footwear
        feet = choice([choice(feet_dir), None], p=[0.9, 0.1])

        if hair is None:
            # helmet
            helmet = choice(helmet_dir)

            # helmet accessory
            helmet_accs = choice(helmet_accs_dir)

        shoulder = choice([choice(shoulder_dir), None], p=[0.4, 0.6])

        shield = choice([choice(shield_dir), None], p=[0.2, 0.8])

        weapon = choice([choice(weapon_dir), None], p=[0.4, 0.6])

        # OVERLAY
        # ##########################################################################################################3

        body_overlay = Image.open("spritesheets/7.body/bodies/male/" + head_color)
        resultant = Image.new("RGBA", body_overlay.size)
        resultant.paste(body_overlay, (0, 0))

        head_overlay = Image.open(
            "spritesheets/2.head/human_male/universal/" + head_color
        )
        resultant = Image.alpha_composite(resultant, head_overlay)

        eye_overlay = Image.open("spritesheets/3.eyes/male/" + eye)
        resultant = Image.alpha_composite(resultant, eye_overlay)

        ear_overlay = Image.open("spritesheets/4.ears/" + ear)
        resultant = Image.alpha_composite(resultant, ear_overlay)

        nose_overlay = Image.open("spritesheets/5.nose/" + nose)
        resultant = Image.alpha_composite(resultant, nose_overlay)

        if facial is not None:
            facial_overlay = Image.open("spritesheets/6.facial/" + facial)
            resultant = Image.alpha_composite(resultant, facial_overlay)

        torso_overlay = Image.open("spritesheets/15.torso//male/" + torso)
        resultant = Image.alpha_composite(resultant, torso_overlay)

        if arms is not None:
            arms_overlay = Image.open("spritesheets/9.arms/armour/male/" + arms)
            resultant = Image.alpha_composite(resultant, arms_overlay)

        if bauldron is not None:
            bauldron_overlay = Image.open("spritesheets/10.bauldron/male/" + bauldron)
            resultant = Image.alpha_composite(resultant, bauldron_overlay)

        legs_overlay = Image.open("spritesheets/11.legs/male/" + legs)
        resultant = Image.alpha_composite(resultant, legs_overlay)

        if feet is not None:
            feet_overlay = Image.open("spritesheets/13.feet/male/" + feet)
            resultant = Image.alpha_composite(resultant, feet_overlay)

        if hair is None:
            helmet_overlay = Image.open("spritesheets/14.hat/helmet/male/" + helmet)
            resultant = Image.alpha_composite(resultant, helmet_overlay)

            helmet_accs_overlay = Image.open(
                "spritesheets/14.hat/accessory/male/" + helmet_accs
            )
            resultant = Image.alpha_composite(resultant, helmet_accs_overlay)

        else:
            hair_overlay = Image.open("spritesheets/8.hair/male/" + hair)
            resultant = Image.alpha_composite(resultant, hair_overlay)

        if shoulder is not None:
            shoulder_overlay = Image.open("spritesheets/shoulders/male/" + shoulder)
            resultant = Image.alpha_composite(resultant, shoulder_overlay)

        if weapon is not None:
            weapon_overlay = Image.open("spritesheets/weapon/" + weapon)
            resultant = Image.alpha_composite(resultant, weapon_overlay)

        if shield is not None:
            try:
                shield_overlay = Image.open("spritesheets/shield/male/" + shield)
                resultant = Image.alpha_composite(resultant, shield_overlay)
            except:
                continue
        train_img = resultant.crop(box=(0, 640, 64, 640 + 64))
        train.append(train_img)
        test_img = resultant.crop(box=(0, 640 + 64, 64, 640 + 64 + 64))
        test.append(test_img)

    return train, test
