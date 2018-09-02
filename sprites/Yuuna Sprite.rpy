########## ~ yuuna TEST SCRIPT ~ ##########

#$ yuuOut = renpy.random.choice([ 'sCasual', 'sCute', 'sFashion', 'sFlirty', 'sTennis', 'sUniform' ])
#$ yuuHairF = renpy.random.choice([ 'bun', 'braided', 'extensions', 'curled', 'pony' ])
#$ yuuHairB = renpy.random.choice([ 'bun', 'braided', 'extensions', 'curled', 'pony' ])



########## ~ yuunaCONDITIONSWITCHES ~ ##########
    
image yuuhairback = ConditionSwitch (
        "yuuHairB == 'default'", "i/sprites/yuuna/hairstyles/default/back.png",
        "yuuHairF == 'hotspring'", "i/sprites/yuuna/hairstyles/hotspring/back.png",
        "yuuHairB == 'pony'", "i/sprites/yuuna/hairstyles/pony/back.png",
        "yuuHairB == 'braided'", "i/sprites/yuuna/hairstyles/braided/back.png",
        "yuuHairB == 'bun'", "i/sprites/yuuna/hairstyles/bun/back.png",
        "yuuHairB == 'cooking'", "i/sprites/yuuna/hairstyles/cooking/back.png",
        "yuuHairB == 'curled'", "i/sprites/yuuna/hairstyles/curled/back.png",
        "yuuHairB == 'extensions'", "i/sprites/yuuna/hairstyles/extensions/back.png"
        )

image yuuoutfits = ConditionSwitch (
        "yuuOut == 'Camp Bag'", "i/sprites/yuuna/outfits/camping - bag.png",
        "yuuOut == 'Camp No Bag'", "i/sprites/yuuna/outfits/camping - no bag.png",
        "yuuOut == 'Cooking'", "i/sprites/yuuna/outfits/special - cooking.png",
        "yuuOut == 'Dog'", "i/sprites/yuuna/outfits/special - dog.png",
        "yuuOut == 'Halloween'", "i/sprites/yuuna/outfits/special - halloween.png",
        "yuuOut == 'hotspring'", "i/sprites/yuuna/outfits/special - hotspring.png",
        "yuuOut == 'sCasual'", "i/sprites/yuuna/outfits/summer - casual.png",
        "yuuOut == 'sCute'", "i/sprites/yuuna/outfits/summer - cute.png",
        "yuuOut == 'sFashion'", "i/sprites/yuuna/outfits/summer - fashion.png",
        "yuuOut == 'sFlirty'", "i/sprites/yuuna/outfits/summer - flirty.png",
        "yuuOut == 'sSwimsuit'", "i/sprites/yuuna/outfits/summer - swimsuit.png",
        "yuuOut == 'sTennis'", "i/sprites/yuuna/outfits/summer - tennis.png",
        "yuuOut == 'sUniform'", "i/sprites/yuuna/outfits/summer - uniform.png"
        )

image yuuhairfront = ConditionSwitch (
        "yuuHairF == 'default'", "i/sprites/yuuna/hairstyles/default/front.png",
        "yuuHairF == 'hotspring'", "i/sprites/yuuna/hairstyles/hotspring/front.png",
        "yuuHairF == 'pony'", "i/sprites/yuuna/hairstyles/pony/front.png",
        "yuuHairF == 'braided'", "i/sprites/yuuna/hairstyles/braided/front.png",
        "yuuHairF == 'bun'", "i/sprites/yuuna/hairstyles/bun/front.png",
        "yuuHairF == 'cooking'", "i/sprites/yuuna/hairstyles/cooking/front.png",
        "yuuHairF == 'curled'", "i/sprites/yuuna/hairstyles/curled/front.png",
        "yuuHairF == 'extensions'", "i/sprites/yuuna/hairstyles/extensions/front.png"
        )

image yuuHairA = ConditionSwitch (
        "yuuHairF == 'hotspring'", "i/sprites/empty.png",
        "yuuHairF == 'pony'", "i/sprites/yuuna/accessories/hair/tie.png",
        "yuuHairF == 'default'", "i/sprites/empty.png", # stuck behind "default" front, temp fix in AccessoryTop
        "yuuHairF == 'cooking'", "i/sprites/empty.png", # stuck behind "cooking" front, temp fix in AccessoryTop
        "yuuHairF == 'curled'", "i/sprites/yuuna/accessories/hair/black bow.png",
        "yuuHairF == 'extensions'", "i/sprites/empty.png", # stuck behind "ext" front, temp fix in AccessoryTop
        "yuuHairF == 'bun'", "i/sprites/empty.png",
        "yuuHairF == 'braided'", "i/sprites/empty.png"
        )

image yuuAccessoryTop = ConditionSwitch (
        "yuuHairF == 'default'", "i/sprites/yuuna/accessories/hair/pin.png", # temp fix
        "yuuHairF == 'extensions'", "i/sprites/yuuna/accessories/hair/clip.png", # temp fix
        "yuuHairF == 'cooking'", "i/sprites/yuuna/accessories/hair/cooking.png", # temp fix
        "yuuAccT == 'emptyimage'", "i/sprites/empty.png"
        )

image yuuAccessoryMiddle = ConditionSwitch (
        "yuuOut == 'Halloween'", "i/sprites/yuuna/accessories/hair/halloween.png",
        "yuuAccM == 'emptyimage'", "i/sprites/empty.png"
        )

image yuuAccessoryBottom = ConditionSwitch (
        "yuuAccB == 'emptyimage'", "i/sprites/empty.png"
        )
    
    

########## ~ yuuna LIVECOMPOSITE ~ ##########

image yuuna ang = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuuang",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )

image yuuna ann = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuuann",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )

image yuuna cur = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuucur",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )

image yuuna dis = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuudis",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )
    
image yuuna hap = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuuhap",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )   
    
image yuuna mis = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuumis",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )    
 
image yuuna ner = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuuner",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    ) 
    
image yuuna neu = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuuneu",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )   
    
image yuuna sad = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuusad",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )   
    
image yuuna ske = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuuske",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )    
    
image yuuna smi = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuusmi",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )    
    
image yuuna sur = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuusur",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )        
    
image yuuna thi = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuuthi",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )       
    
image yuuna win = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuuwin",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )      

image yuuna wor = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuuwor",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )    
  
image yuuna ang b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuuang",
    ( 0, 0 ), "i/sprites/yuuna/overlays/blush/1.png",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )

image yuuna ann b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuuann",
    ( 0, 0 ), "i/sprites/yuuna/overlays/blush/1.png",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )

image yuuna cur b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuucur",
    ( 0, 0 ), "i/sprites/yuuna/overlays/blush/1.png",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )

image yuuna dis b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuudis",
    ( 0, 0 ), "i/sprites/yuuna/overlays/blush/1.png",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )
    
image yuuna hap b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuuhap",
    ( 0, 0 ), "i/sprites/yuuna/overlays/blush/1.png",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )   
    
image yuuna mis b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuumis",
    ( 0, 0 ), "i/sprites/yuuna/overlays/blush/1.png",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )    
 
image yuuna ner b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuuner",
    ( 0, 0 ), "i/sprites/yuuna/overlays/blush/1.png",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    ) 
    
image yuuna neu b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuuneu",
    ( 0, 0 ), "i/sprites/yuuna/overlays/blush/1.png",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )   
    
image yuuna sad b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuusad",
    ( 0, 0 ), "i/sprites/yuuna/overlays/blush/1.png",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )   
    
image yuuna ske b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuuske",
    ( 0, 0 ), "i/sprites/yuuna/overlays/blush/1.png",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )    
    
image yuuna smi b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuusmi",
    ( 0, 0 ), "i/sprites/yuuna/overlays/blush/1.png",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )    
    
image yuuna sur b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuusur",
    ( 0, 0 ), "i/sprites/yuuna/overlays/blush/1.png",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )        
    
image yuuna thi b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuuthi",
    ( 0, 0 ), "i/sprites/yuuna/overlays/blush/1.png",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )       
    
image yuuna win b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuuwin",
    ( 0, 0 ), "i/sprites/yuuna/overlays/blush/1.png",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )      

image yuuna wor b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuuwor",
    ( 0, 0 ), "i/sprites/yuuna/overlays/blush/1.png",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )     
    
image yuuna ang b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuuang",
    ( 0, 0 ), "i/sprites/yuuna/overlays/blush/2.png",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )

image yuuna ann b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuuann",
    ( 0, 0 ), "i/sprites/yuuna/overlays/blush/2.png",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )

image yuuna cur b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuucur",
    ( 0, 0 ), "i/sprites/yuuna/overlays/blush/2.png",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )

image yuuna dis b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuudis",
    ( 0, 0 ), "i/sprites/yuuna/overlays/blush/2.png",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )
    
image yuuna hap b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuuhap",
    ( 0, 0 ), "i/sprites/yuuna/overlays/blush/2.png",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )   
    
image yuuna mis b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuumis",
    ( 0, 0 ), "i/sprites/yuuna/overlays/blush/2.png",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )    
 
image yuuna ner b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuuner",
    ( 0, 0 ), "i/sprites/yuuna/overlays/blush/2.png",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    ) 
    
image yuuna neu b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuuneu",
    ( 0, 0 ), "i/sprites/yuuna/overlays/blush/2.png",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )   
    
image yuuna sad b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuusad",
    ( 0, 0 ), "i/sprites/yuuna/overlays/blush/2.png",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )   
    
image yuuna ske b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuuske",
    ( 0, 0 ), "i/sprites/yuuna/overlays/blush/2.png",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )    
    
image yuuna smi b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuusmi",
    ( 0, 0 ), "i/sprites/yuuna/overlays/blush/2.png",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )    
    
image yuuna sur b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuusur",
    ( 0, 0 ), "i/sprites/yuuna/overlays/blush/2.png",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )        
    
image yuuna thi b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuuthi",
    ( 0, 0 ), "i/sprites/yuuna/overlays/blush/2.png",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )       
    
image yuuna win b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuuwin",
    ( 0, 0 ), "i/sprites/yuuna/overlays/blush/2.png",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )      

image yuuna wor b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuuwor",
    ( 0, 0 ), "i/sprites/yuuna/overlays/blush/2.png",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )     

image yuuna ang b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuuang",
    ( 0, 0 ), "i/sprites/yuuna/overlays/blush/3.png",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )

image yuuna ann b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuuann",
    ( 0, 0 ), "i/sprites/yuuna/overlays/blush/3.png",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )

image yuuna cur b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuucur",
    ( 0, 0 ), "i/sprites/yuuna/overlays/blush/3.png",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )

image yuuna dis b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuudis",
    ( 0, 0 ), "i/sprites/yuuna/overlays/blush/3.png",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )
    
image yuuna hap b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuuhap",
    ( 0, 0 ), "i/sprites/yuuna/overlays/blush/3.png",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )   
    
image yuuna mis b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuumis",
    ( 0, 0 ), "i/sprites/yuuna/overlays/blush/3.png",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )    
 
image yuuna ner b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuuner",
    ( 0, 0 ), "i/sprites/yuuna/overlays/blush/3.png",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    ) 
    
image yuuna neu b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuuneu",
    ( 0, 0 ), "i/sprites/yuuna/overlays/blush/3.png",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )   
    
image yuuna sad b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuusad",
    ( 0, 0 ), "i/sprites/yuuna/overlays/blush/3.png",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )   
    
image yuuna ske b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuuske",
    ( 0, 0 ), "i/sprites/yuuna/overlays/blush/3.png",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )    
    
image yuuna smi b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuusmi",
    ( 0, 0 ), "i/sprites/yuuna/overlays/blush/3.png",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )    
    
image yuuna sur b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuusur",
    ( 0, 0 ), "i/sprites/yuuna/overlays/blush/3.png",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )        
    
image yuuna thi b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuuthi",
    ( 0, 0 ), "i/sprites/yuuna/overlays/blush/3.png",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )       
    
image yuuna win b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuuwin",
    ( 0, 0 ), "i/sprites/yuuna/overlays/blush/3.png",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )      

image yuuna wor b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yuuhairback",
    ( 0, 0 ), "i/sprites/yuuna/outfits/base.png",
    ( 0, 0 ), "yuuoutfits",
    ( 0, 0 ), "yuuwor",
    ( 0, 0 ), "i/sprites/yuuna/overlays/blush/3.png",
    ( 0, 0 ), "yuuHairA",
    ( 0, 0 ), "yuuhairfront",
    ( 0, 0 ), "yuuAccessoryTop",
    ( 0, 0 ), "yuuAccessoryMiddle",
    ( 0 , 0), "yuuAccessoryBottom"
    )    
    

    
########## ~ yuuna EXPRESSIONS ~ ##########

image yuuang:
    "i/sprites/yuuna/expressions/angry/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/yuuna/expressions/angry/2.png"
    .05
    "i/sprites/yuuna/expressions/angry/3.png"
    .05
    "i/sprites/yuuna/expressions/angry/4.png"
    .05
    "i/sprites/yuuna/expressions/angry/3.png"
    .05
    "i/sprites/yuuna/expressions/angry/2.png"
    .05
    repeat

    
image yuuann:
    "i/sprites/yuuna/expressions/annoyed/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/yuuna/expressions/annoyed/2.png"
    .05
    "i/sprites/yuuna/expressions/annoyed/3.png"
    .05
    "i/sprites/yuuna/expressions/annoyed/4.png"
    .05
    "i/sprites/yuuna/expressions/annoyed/3.png"
    .05
    "i/sprites/yuuna/expressions/annoyed/2.png"
    .05
    repeat
    
    
image yuucur:
    "i/sprites/yuuna/expressions/curious/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/yuuna/expressions/curious/2.png"
    .05
    "i/sprites/yuuna/expressions/curious/3.png"
    .05
    "i/sprites/yuuna/expressions/curious/4.png"
    .05
    "i/sprites/yuuna/expressions/curious/3.png"
    .05
    "i/sprites/yuuna/expressions/curious/2.png"
    .05
    repeat
    
    
image yuudis:
    "i/sprites/yuuna/expressions/disappointed/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/yuuna/expressions/disappointed/2.png"
    .05
    "i/sprites/yuuna/expressions/disappointed/3.png"
    .05
    "i/sprites/yuuna/expressions/disappointed/4.png"
    .05
    "i/sprites/yuuna/expressions/disappointed/3.png"
    .05
    "i/sprites/yuuna/expressions/disappointed/2.png"
    .05
    repeat
    
    
image yuuhap:
    "i/sprites/yuuna/expressions/happy/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/yuuna/expressions/happy/2.png"
    .05
    "i/sprites/yuuna/expressions/happy/3.png"
    .05
    "i/sprites/yuuna/expressions/happy/4.png"
    .05
    "i/sprites/yuuna/expressions/happy/3.png"
    .05
    "i/sprites/yuuna/expressions/happy/2.png"
    .05
    repeat
    
    
image yuumis:
    "i/sprites/yuuna/expressions/mischievous/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/yuuna/expressions/mischievous/2.png"
    .05
    "i/sprites/yuuna/expressions/mischievous/3.png"
    .05
    "i/sprites/yuuna/expressions/mischievous/4.png"
    .05
    "i/sprites/yuuna/expressions/mischievous/3.png"
    .05
    "i/sprites/yuuna/expressions/mischievous/2.png"
    .05
    repeat
    
    
image yuuner:
    "i/sprites/yuuna/expressions/nervous/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/yuuna/expressions/nervous/2.png"
    .05
    "i/sprites/yuuna/expressions/nervous/3.png"
    .05
    "i/sprites/yuuna/expressions/nervous/4.png"
    .05
    "i/sprites/yuuna/expressions/nervous/3.png"
    .05
    "i/sprites/yuuna/expressions/nervous/2.png"
    .05
    repeat
    
    
image yuuneu:
    "i/sprites/yuuna/expressions/neutral/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/yuuna/expressions/neutral/2.png"
    .05
    "i/sprites/yuuna/expressions/neutral/3.png"
    .05
    "i/sprites/yuuna/expressions/neutral/4.png"
    .05
    "i/sprites/yuuna/expressions/neutral/3.png"
    .05
    "i/sprites/yuuna/expressions/neutral/2.png"
    .05
    repeat
    
    
image yuusad:
    "i/sprites/yuuna/expressions/sad/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/yuuna/expressions/sad/2.png"
    .05
    "i/sprites/yuuna/expressions/sad/3.png"
    .05
    "i/sprites/yuuna/expressions/sad/4.png"
    .05
    "i/sprites/yuuna/expressions/sad/3.png"
    .05
    "i/sprites/yuuna/expressions/sad/2.png"
    .05
    repeat
    
    
image yuuske:
    "i/sprites/yuuna/expressions/skeptical/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/yuuna/expressions/skeptical/2.png"
    .05
    "i/sprites/yuuna/expressions/skeptical/3.png"
    .05
    "i/sprites/yuuna/expressions/skeptical/4.png"
    .05
    "i/sprites/yuuna/expressions/skeptical/3.png"
    .05
    "i/sprites/yuuna/expressions/skeptical/2.png"
    .05
    repeat
    
    
image yuusmi:
    "i/sprites/yuuna/expressions/smiling/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/yuuna/expressions/smiling/2.png"
    .05
    "i/sprites/yuuna/expressions/smiling/3.png"
    .05
    "i/sprites/yuuna/expressions/smiling/4.png"
    .05
    "i/sprites/yuuna/expressions/smiling/3.png"
    .05
    "i/sprites/yuuna/expressions/smiling/2.png"
    .05
    repeat
    
    
image yuusur:
    "i/sprites/yuuna/expressions/surprised/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/yuuna/expressions/surprised/2.png"
    .05
    "i/sprites/yuuna/expressions/surprised/3.png"
    .05
    "i/sprites/yuuna/expressions/surprised/4.png"
    .05
    "i/sprites/yuuna/expressions/surprised/3.png"
    .05
    "i/sprites/yuuna/expressions/surprised/2.png"
    .05
    repeat
    
    
image yuuthi:
    "i/sprites/yuuna/expressions/thinking/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/yuuna/expressions/thinking/2.png"
    .05
    "i/sprites/yuuna/expressions/thinking/3.png"
    .05
    "i/sprites/yuuna/expressions/thinking/4.png"
    .05
    "i/sprites/yuuna/expressions/thinking/3.png"
    .05
    "i/sprites/yuuna/expressions/thinking/2.png"
    .05
    repeat
    
    
image yuuwin:
    "i/sprites/yuuna/expressions/wincing/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/yuuna/expressions/wincing/2.png"
    .05
    "i/sprites/yuuna/expressions/wincing/3.png"
    .05
    "i/sprites/yuuna/expressions/wincing/4.png"
    .05
    "i/sprites/yuuna/expressions/wincing/3.png"
    .05
    "i/sprites/yuuna/expressions/wincing/2.png"
    .05
    repeat
    
    
image yuuwor:
    "i/sprites/yuuna/expressions/worried/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/yuuna/expressions/worried/2.png"
    .05
    "i/sprites/yuuna/expressions/worried/3.png"
    .05
    "i/sprites/yuuna/expressions/worried/4.png"
    .05
    "i/sprites/yuuna/expressions/worried/3.png"
    .05
    "i/sprites/yuuna/expressions/worried/2.png"
    .05
    repeat