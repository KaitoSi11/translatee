########## ~ VALERIE TEST SCRIPT ~ ##########

#$ valOut = renpy.random.choice([ 'Hoodie', 'sCute', 'sFashion', 'sFlirty', 'sDate', 'sUniform' ])
#$ valHairF = renpy.random.choice([ 'hoodieOn', 'hoodieOff', 'braided', 'extensions', 'curled', 'pony' ])
#$ valHairB = renpy.random.choice([ 'hoodieOn', 'hoodieOff', 'braided', 'extensions', 'curled', 'pony' ])



########## ~ valerie CONDITIONSWITCHES ~ ##########
    
image valhairback = ConditionSwitch (
        "valHairB == 'default'", "i/sprites/valerie/hairstyles/default/back.png",
        "valHairB == 'pony'", "i/sprites/valerie/hairstyles/pony/back.png",
        "valHairB == 'braided'", "i/sprites/valerie/hairstyles/braided/back.png",
        "valHairB == 'curled'", "i/sprites/empty.png", #<- This one doesn't exist, only front
        "valHairB == 'extensions'", "i/sprites/valerie/hairstyles/extensions/back.png",
        "valHairB == 'hoodieOff'", "i/sprites/valerie/hairstyles/hoodie/backOff.png",
        "valHairB == 'hoodieOn'", "i/sprites/valerie/hairstyles/hoodie/backOn.png",
        "valHairF == 'hotspring'", "i/sprites/valerie/hairstyles/hotspring/back.png"
        )
        
image valoutfits = ConditionSwitch (
        "valOut == 'Hoodie'", "i/sprites/valerie/outfits/special - hoodie.png",
        "valOut == 'sCasual'", "i/sprites/valerie/outfits/summer - casual.png",
        "valOut == 'sCute'", "i/sprites/valerie/outfits/summer - cute.png",
        "valOut == 'sDate'", "i/sprites/valerie/outfits/summer - date.png",
        "valOut == 'sDate2'", "i/sprites/valerie/outfits/summer - date2.png",
        "valOut == 'sFashion'", "i/sprites/valerie/outfits/summer - fashion.png",
        "valOut == 'sFlirty'", "i/sprites/valerie/outfits/summer - flirty.png",
        "valOut == 'sSwimsuit'", "i/sprites/valerie/outfits/summer - swimsuit.png",
        "valOut == 'Gym'", "i/sprites/valerie/outfits/special - gym.png",
        "valOut == 'Halloween'", "i/sprites/valerie/outfits/halloween.png",
        "valOut == 'hotspring'", "i/sprites/valerie/outfits/hotspring.png",
        "valOut == 'outdoor'", "i/sprites/valerie/outfits/outdoor.png",
        "valOut == 'sUniform'", "i/sprites/valerie/outfits/summer - uniform.png"
        )
        
image valhairfront = ConditionSwitch (
        "valHairF == 'default'", "i/sprites/valerie/hairstyles/default/front.png",
        "valHairF == 'pony'", "i/sprites/valerie/hairstyles/pony/front.png",
        "valHairF == 'braided'", "i/sprites/valerie/hairstyles/braided/front.png",
        "valHairF == 'curled'", "i/sprites/valerie/hairstyles/curled/front.png",
        "valHairF == 'extensions'", "i/sprites/valerie/hairstyles/extensions/front.png",
        "valHairF == 'hoodieOff'", "i/sprites/valerie/hairstyles/hoodie/frontOff.png",
        "valHairF == 'hoodieOn'", "i/sprites/valerie/hairstyles/hoodie/frontOn.png",
        "valHairF == 'hotspring'", "i/sprites/valerie/hairstyles/hotspring/front.png"
        )

image valHairA = ConditionSwitch (
        "valHairF == 'pony'", "i/sprites/empty.png",
        "valHairF == 'default'", "i/sprites/empty.png",
        "valHairF == 'braided'", "i/sprites/empty.png",
        "valHairF == 'curled'", "i/sprites/empty.png",
        "valHairF == 'extensions'", "i/sprites/valerie/accessories/hair/pink bow.png",
        "valHairF == 'hoodieOff'", "i/sprites/empty.png",
        "valHairF == 'hoodieOn'", "i/sprites/empty.png",
        "valHairF == 'hotspring'", "i/sprites/empty.png"
        )

image valAccessoryTop = ConditionSwitch (
        "valAccT == 'emptyimage'", "i/sprites/empty.png",
        #"valOut == 'Halloween'", "i/sprites/valerie/accessories/hair/halloween.png",
        "valAccT == 'pinkBow'", "i/sprites/valerie/accessories/hair/pink bow.png"
        )
        
image valAccessoryMiddle = ConditionSwitch (
        "valOut == 'Halloween'", "i/sprites/valerie/accessories/hair/halloween.png",
        "valAccM == 'emptyimage'", "i/sprites/empty.png"
        )
        
image valAccessoryBottom = ConditionSwitch (
        "valAccB == 'emptyimage'", "i/sprites/empty.png"
        )
    
    

########## ~ valerie LIVECOMPOSITE ~ ##########

image valerie ang = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valang",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )

image valerie ann = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valann",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )

image valerie cur = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valcur",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )

image valerie dis = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valdis",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )
    
image valerie hap = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valhap",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )   
    
image valerie mis = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valmis",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )    
 
image valerie ner = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valner",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    ) 
    
image valerie neu = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valneu",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )   
    
image valerie sad = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valsad",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )   
    
image valerie ske = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valske",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )    
    
image valerie smi = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valsmi",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )    
    
image valerie sur = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valsur",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )        
    
image valerie thi = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valthi",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )       
    
image valerie win = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valwin",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )      

image valerie wor = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valwor",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )    
  
image valerie ang b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valang",
    ( 0, 0 ), "i/sprites/valerie/overlays/blush/1.png",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )

image valerie ann b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valann",
    ( 0, 0 ), "i/sprites/valerie/overlays/blush/1.png",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )

image valerie cur b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valcur",
    ( 0, 0 ), "i/sprites/valerie/overlays/blush/1.png",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )

image valerie dis b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valdis",
    ( 0, 0 ), "i/sprites/valerie/overlays/blush/1.png",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )
    
image valerie hap b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valhap",
    ( 0, 0 ), "i/sprites/valerie/overlays/blush/1.png",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )   
    
image valerie mis b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valmis",
    ( 0, 0 ), "i/sprites/valerie/overlays/blush/1.png",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )    
 
image valerie ner b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valner",
    ( 0, 0 ), "i/sprites/valerie/overlays/blush/1.png",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    ) 
    
image valerie neu b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valneu",
    ( 0, 0 ), "i/sprites/valerie/overlays/blush/1.png",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )   
    
image valerie sad b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valsad",
    ( 0, 0 ), "i/sprites/valerie/overlays/blush/1.png",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )   
    
image valerie ske b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valske",
    ( 0, 0 ), "i/sprites/valerie/overlays/blush/1.png",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )    
    
image valerie smi b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valsmi",
    ( 0, 0 ), "i/sprites/valerie/overlays/blush/1.png",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )    
    
image valerie sur b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valsur",
    ( 0, 0 ), "i/sprites/valerie/overlays/blush/1.png",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )        
    
image valerie thi b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valthi",
    ( 0, 0 ), "i/sprites/valerie/overlays/blush/1.png",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )       
    
image valerie win b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valwin",
    ( 0, 0 ), "i/sprites/valerie/overlays/blush/1.png",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )      

image valerie wor b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valwor",
    ( 0, 0 ), "i/sprites/valerie/overlays/blush/1.png",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )     
    
image valerie ang b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valang",
    ( 0, 0 ), "i/sprites/valerie/overlays/blush/2.png",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )

image valerie ann b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valann",
    ( 0, 0 ), "i/sprites/valerie/overlays/blush/2.png",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )

image valerie cur b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valcur",
    ( 0, 0 ), "i/sprites/valerie/overlays/blush/2.png",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )

image valerie dis b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valdis",
    ( 0, 0 ), "i/sprites/valerie/overlays/blush/2.png",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )
    
image valerie hap b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valhap",
    ( 0, 0 ), "i/sprites/valerie/overlays/blush/2.png",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )   
    
image valerie mis b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valmis",
    ( 0, 0 ), "i/sprites/valerie/overlays/blush/2.png",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )    
 
image valerie ner b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valner",
    ( 0, 0 ), "i/sprites/valerie/overlays/blush/2.png",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    ) 
    
image valerie neu b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valneu",
    ( 0, 0 ), "i/sprites/valerie/overlays/blush/2.png",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )   
    
image valerie sad b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valsad",
    ( 0, 0 ), "i/sprites/valerie/overlays/blush/2.png",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )   
    
image valerie ske b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valske",
    ( 0, 0 ), "i/sprites/valerie/overlays/blush/2.png",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )    
    
image valerie smi b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valsmi",
    ( 0, 0 ), "i/sprites/valerie/overlays/blush/2.png",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )    
    
image valerie sur b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valsur",
    ( 0, 0 ), "i/sprites/valerie/overlays/blush/2.png",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )        
    
image valerie thi b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valthi",
    ( 0, 0 ), "i/sprites/valerie/overlays/blush/2.png",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )       
    
image valerie win b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valwin",
    ( 0, 0 ), "i/sprites/valerie/overlays/blush/2.png",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )      

image valerie wor b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valwor",
    ( 0, 0 ), "i/sprites/valerie/overlays/blush/2.png",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )     

image valerie ang b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valang",
    ( 0, 0 ), "i/sprites/valerie/overlays/blush/3.png",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )

image valerie ann b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valann",
    ( 0, 0 ), "i/sprites/valerie/overlays/blush/3.png",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )

image valerie cur b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valcur",
    ( 0, 0 ), "i/sprites/valerie/overlays/blush/3.png",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )

image valerie dis b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valdis",
    ( 0, 0 ), "i/sprites/valerie/overlays/blush/3.png",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )
    
image valerie hap b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valhap",
    ( 0, 0 ), "i/sprites/valerie/overlays/blush/3.png",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )   
    
image valerie mis b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valmis",
    ( 0, 0 ), "i/sprites/valerie/overlays/blush/3.png",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )    
 
image valerie ner b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valner",
    ( 0, 0 ), "i/sprites/valerie/overlays/blush/3.png",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    ) 
    
image valerie neu b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valneu",
    ( 0, 0 ), "i/sprites/valerie/overlays/blush/3.png",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )   
    
image valerie sad b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valsad",
    ( 0, 0 ), "i/sprites/valerie/overlays/blush/3.png",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )   
    
image valerie ske b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valske",
    ( 0, 0 ), "i/sprites/valerie/overlays/blush/3.png",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )    
    
image valerie smi b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valsmi",
    ( 0, 0 ), "i/sprites/valerie/overlays/blush/3.png",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )    
    
image valerie sur b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valsur",
    ( 0, 0 ), "i/sprites/valerie/overlays/blush/3.png",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )        
    
image valerie thi b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valthi",
    ( 0, 0 ), "i/sprites/valerie/overlays/blush/3.png",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )       
    
image valerie win b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valwin",
    ( 0, 0 ), "i/sprites/valerie/overlays/blush/3.png",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )      

image valerie wor b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "valhairback",
    ( 0, 0 ), "i/sprites/valerie/outfits/base.png",
    ( 0, 0 ), "valoutfits",
    ( 0, 0 ), "valwor",
    ( 0, 0 ), "i/sprites/valerie/overlays/blush/3.png",
    ( 0, 0 ), "valHairA",
    ( 0, 0 ), "valhairfront",
    ( 0, 0 ), "valAccessoryTop",
    ( 0, 0 ), "valAccessoryMiddle",
    ( 0 , 0), "valAccessoryBottom"
    )    
    

    
########## ~ valerie EXPRESSIONS ~ ##########

image valang:
    "i/sprites/valerie/expressions/angry/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/valerie/expressions/angry/2.png"
    .05
    "i/sprites/valerie/expressions/angry/3.png"
    .05
    "i/sprites/valerie/expressions/angry/4.png"
    .05
    "i/sprites/valerie/expressions/angry/3.png"
    .05
    "i/sprites/valerie/expressions/angry/2.png"
    .05
    repeat

    
image valann:
    "i/sprites/valerie/expressions/annoyed/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/valerie/expressions/annoyed/2.png"
    .05
    "i/sprites/valerie/expressions/annoyed/3.png"
    .05
    "i/sprites/valerie/expressions/annoyed/4.png"
    .05
    "i/sprites/valerie/expressions/annoyed/3.png"
    .05
    "i/sprites/valerie/expressions/annoyed/2.png"
    .05
    repeat
    
    
image valcur:
    "i/sprites/valerie/expressions/curious/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/valerie/expressions/curious/2.png"
    .05
    "i/sprites/valerie/expressions/curious/3.png"
    .05
    "i/sprites/valerie/expressions/curious/4.png"
    .05
    "i/sprites/valerie/expressions/curious/3.png"
    .05
    "i/sprites/valerie/expressions/curious/2.png"
    .05
    repeat
    
    
image valdis:
    "i/sprites/valerie/expressions/disappointed/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/valerie/expressions/disappointed/2.png"
    .05
    "i/sprites/valerie/expressions/disappointed/3.png"
    .05
    "i/sprites/valerie/expressions/disappointed/4.png"
    .05
    "i/sprites/valerie/expressions/disappointed/3.png"
    .05
    "i/sprites/valerie/expressions/disappointed/2.png"
    .05
    repeat
    
    
image valhap:
    "i/sprites/valerie/expressions/happy/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/valerie/expressions/happy/2.png"
    .05
    "i/sprites/valerie/expressions/happy/3.png"
    .05
    "i/sprites/valerie/expressions/happy/4.png"
    .05
    "i/sprites/valerie/expressions/happy/3.png"
    .05
    "i/sprites/valerie/expressions/happy/2.png"
    .05
    repeat
    
    
image valmis:
    "i/sprites/valerie/expressions/mischievous/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/valerie/expressions/mischievous/2.png"
    .05
    "i/sprites/valerie/expressions/mischievous/3.png"
    .05
    "i/sprites/valerie/expressions/mischievous/4.png"
    .05
    "i/sprites/valerie/expressions/mischievous/3.png"
    .05
    "i/sprites/valerie/expressions/mischievous/2.png"
    .05
    repeat
    
    
image valner:
    "i/sprites/valerie/expressions/nervous/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/valerie/expressions/nervous/2.png"
    .05
    "i/sprites/valerie/expressions/nervous/3.png"
    .05
    "i/sprites/valerie/expressions/nervous/4.png"
    .05
    "i/sprites/valerie/expressions/nervous/3.png"
    .05
    "i/sprites/valerie/expressions/nervous/2.png"
    .05
    repeat
    
    
image valneu:
    "i/sprites/valerie/expressions/neutral/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/valerie/expressions/neutral/2.png"
    .05
    "i/sprites/valerie/expressions/neutral/3.png"
    .05
    "i/sprites/valerie/expressions/neutral/4.png"
    .05
    "i/sprites/valerie/expressions/neutral/3.png"
    .05
    "i/sprites/valerie/expressions/neutral/2.png"
    .05
    repeat
    
    
image valsad:
    "i/sprites/valerie/expressions/sad/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/valerie/expressions/sad/2.png"
    .05
    "i/sprites/valerie/expressions/sad/3.png"
    .05
    "i/sprites/valerie/expressions/sad/4.png"
    .05
    "i/sprites/valerie/expressions/sad/3.png"
    .05
    "i/sprites/valerie/expressions/sad/2.png"
    .05
    repeat
    
    
image valske:
    "i/sprites/valerie/expressions/skeptical/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/valerie/expressions/skeptical/2.png"
    .05
    "i/sprites/valerie/expressions/skeptical/3.png"
    .05
    "i/sprites/valerie/expressions/skeptical/4.png"
    .05
    "i/sprites/valerie/expressions/skeptical/3.png"
    .05
    "i/sprites/valerie/expressions/skeptical/2.png"
    .05
    repeat
    
    
image valsmi:
    "i/sprites/valerie/expressions/smiling/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/valerie/expressions/smiling/2.png"
    .05
    "i/sprites/valerie/expressions/smiling/3.png"
    .05
    "i/sprites/valerie/expressions/smiling/4.png"
    .05
    "i/sprites/valerie/expressions/smiling/3.png"
    .05
    "i/sprites/valerie/expressions/smiling/2.png"
    .05
    repeat
    
    
image valsur:
    "i/sprites/valerie/expressions/surprised/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/valerie/expressions/surprised/2.png"
    .05
    "i/sprites/valerie/expressions/surprised/3.png"
    .05
    "i/sprites/valerie/expressions/surprised/4.png"
    .05
    "i/sprites/valerie/expressions/surprised/3.png"
    .05
    "i/sprites/valerie/expressions/surprised/2.png"
    .05
    repeat
    
    
image valthi:
    "i/sprites/valerie/expressions/thinking/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/valerie/expressions/thinking/2.png"
    .05
    "i/sprites/valerie/expressions/thinking/3.png"
    .05
    "i/sprites/valerie/expressions/thinking/4.png"
    .05
    "i/sprites/valerie/expressions/thinking/3.png"
    .05
    "i/sprites/valerie/expressions/thinking/2.png"
    .05
    repeat
    
    
image valwin:
    "i/sprites/valerie/expressions/wincing/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/valerie/expressions/wincing/2.png"
    .05
    "i/sprites/valerie/expressions/wincing/3.png"
    .05
    "i/sprites/valerie/expressions/wincing/4.png"
    .05
    "i/sprites/valerie/expressions/wincing/3.png"
    .05
    "i/sprites/valerie/expressions/wincing/2.png"
    .05
    repeat
    
    
image valwor:
    "i/sprites/valerie/expressions/worried/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/valerie/expressions/worried/2.png"
    .05
    "i/sprites/valerie/expressions/worried/3.png"
    .05
    "i/sprites/valerie/expressions/worried/4.png"
    .05
    "i/sprites/valerie/expressions/worried/3.png"
    .05
    "i/sprites/valerie/expressions/worried/2.png"
    .05
    repeat