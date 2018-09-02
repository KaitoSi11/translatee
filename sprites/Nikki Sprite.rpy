########## ~ kaori TEST SCRIPT ~ ##########

#$ nikOut = renpy.random.choice([ 'sCasual', 'sCasual2', 'sUniform', 'sSleepwear' ])
#$ nikHairF = renpy.random.choice([ 'default', 'pony', 'long' ])
#$ nikHairB = renpy.random.choice([ 'default', 'pony', 'long' ])



########## ~ nikki CONDITIONSWITCHES ~ ##########
    
image nikhairback = ConditionSwitch (
        "nikHairB == 'default'", "i/sprites/nikki/hairstyles/default/back.png",
        "nikHairB == 'pony'", "i/sprites/nikki/hairstyles/pony/back.png",
        "nikHairB == 'banded'", "i/sprites/nikki/hairstyles/banded/back.png"
        )
        
image nikoutfits = ConditionSwitch (
        "nikOut == 'sCasual'", "i/sprites/nikki/outfits/summer - casual.png",
        "nikOut == 'sCasual2'", "i/sprites/nikki/outfits/summer - casual2.png",
        "nikOut == 'date'", "i/sprites/nikki/outfits/date.png",
        "nikOut == 'maid'", "i/sprites/nikki/outfits/maid.png",
        "nikOut == 'sSwimsuit'", "i/sprites/nikki/outfits/summer - swimsuit.png",
        "nikOut == 'sUniform'", "i/sprites/nikki/outfits/summer - uniform.png",
        "nikOut == 'sSleepwear'", "i/sprites/nikki/outfits/summer - sleepwear.png"
        )
        
image nikhairfront = ConditionSwitch (
        "nikHairF == 'default'", "i/sprites/nikki/hairstyles/default/front.png",
        "nikHairF == 'pony'", "i/sprites/nikki/hairstyles/pony/front.png",
        "nikHairF == 'banded'", "i/sprites/nikki/hairstyles/banded/front.png"
        )

image nikHairA = ConditionSwitch (
        "nikHairF == 'default'", "i/sprites/empty.png",
        "nikHairF == 'pony'", "i/sprites/empty.png",
        "nikHairF == 'banded'", "i/sprites/empty.png" # stuck behind "banded" front, temp fix in AccessoryMiddle
        )

image nikAccessoryTop = ConditionSwitch (
        "nikHairF == 'banded'", "i/sprites/nikki/accessories/hair/pink band.png", # temp fix
        "nikAccT == 'emptyimage'", "i/sprites/empty.png"
        )
        
image nikAccessoryMiddle = ConditionSwitch (
        #"nikOut == 'date'", "i/sprites/nikki/accessories/middle/date_hat.png",
        "nikOut == 'maid'", "i/sprites/nikki/accessories/middle/maid_hat.png",
        "nikAccM == 'emptyimage'", "i/sprites/empty.png"
        )
        
image nikAccessoryBottom = ConditionSwitch (
        "nikAccB == 'emptyimage'", "i/sprites/empty.png"
        )
    
    

########## ~ nikki LIVECOMPOSITE ~ ##########

image nikki ang = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "nikang",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )

image nikki ann = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "nikann",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )

image nikki cur = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "nikcur",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )

image nikki dis = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "nikdis",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )
    
image nikki hap = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "nikhap",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )   
    
image nikki mis = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "nikmis",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )    
 
image nikki ner = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "nikner",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    ) 
    
image nikki neu = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "nikneu",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )   
    
image nikki sad = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "niksad",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )   
    
image nikki ske = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "nikske",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )    
    
image nikki smi = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "niksmi",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )    
    
image nikki sur = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "niksur",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )        
    
image nikki thi = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "nikthi",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )       
    
image nikki win = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "nikwin",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )      

image nikki wor = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "nikwor",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )    
  
image nikki ang b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "nikang",
    ( 0, 0 ), "i/sprites/nikki/overlays/blush/1.png",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )

image nikki ann b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "nikann",
    ( 0, 0 ), "i/sprites/nikki/overlays/blush/1.png",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )

image nikki cur b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "nikcur",
    ( 0, 0 ), "i/sprites/nikki/overlays/blush/1.png",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )

image nikki dis b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "nikdis",
    ( 0, 0 ), "i/sprites/nikki/overlays/blush/1.png",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )
    
image nikki hap b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "nikhap",
    ( 0, 0 ), "i/sprites/nikki/overlays/blush/1.png",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )   
    
image nikki mis b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "nikmis",
    ( 0, 0 ), "i/sprites/nikki/overlays/blush/1.png",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )    
 
image nikki ner b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "nikner",
    ( 0, 0 ), "i/sprites/nikki/overlays/blush/1.png",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    ) 
    
image nikki neu b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "nikneu",
    ( 0, 0 ), "i/sprites/nikki/overlays/blush/1.png",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )   
    
image nikki sad b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "niksad",
    ( 0, 0 ), "i/sprites/nikki/overlays/blush/1.png",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )   
    
image nikki ske b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "nikske",
    ( 0, 0 ), "i/sprites/nikki/overlays/blush/1.png",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )    
    
image nikki smi b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "niksmi",
    ( 0, 0 ), "i/sprites/nikki/overlays/blush/1.png",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )    
    
image nikki sur b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "niksur",
    ( 0, 0 ), "i/sprites/nikki/overlays/blush/1.png",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )        
    
image nikki thi b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "nikthi",
    ( 0, 0 ), "i/sprites/nikki/overlays/blush/1.png",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )       
    
image nikki win b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "nikwin",
    ( 0, 0 ), "i/sprites/nikki/overlays/blush/1.png",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )      

image nikki wor b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "nikwor",
    ( 0, 0 ), "i/sprites/nikki/overlays/blush/1.png",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )     
    
image nikki ang b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "nikang",
    ( 0, 0 ), "i/sprites/nikki/overlays/blush/2.png",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )

image nikki ann b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "nikann",
    ( 0, 0 ), "i/sprites/nikki/overlays/blush/2.png",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )

image nikki cur b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "nikcur",
    ( 0, 0 ), "i/sprites/nikki/overlays/blush/2.png",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )

image nikki dis b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "nikdis",
    ( 0, 0 ), "i/sprites/nikki/overlays/blush/2.png",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )
    
image nikki hap b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "nikhap",
    ( 0, 0 ), "i/sprites/nikki/overlays/blush/2.png",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )   
    
image nikki mis b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "nikmis",
    ( 0, 0 ), "i/sprites/nikki/overlays/blush/2.png",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )    
 
image nikki ner b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "nikner",
    ( 0, 0 ), "i/sprites/nikki/overlays/blush/2.png",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    ) 
    
image nikki neu b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "nikneu",
    ( 0, 0 ), "i/sprites/nikki/overlays/blush/2.png",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )   
    
image nikki sad b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "niksad",
    ( 0, 0 ), "i/sprites/nikki/overlays/blush/2.png",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )   
    
image nikki ske b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "nikske",
    ( 0, 0 ), "i/sprites/nikki/overlays/blush/2.png",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )    
    
image nikki smi b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "niksmi",
    ( 0, 0 ), "i/sprites/nikki/overlays/blush/2.png",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )    
    
image nikki sur b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "niksur",
    ( 0, 0 ), "i/sprites/nikki/overlays/blush/2.png",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )        
    
image nikki thi b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "nikthi",
    ( 0, 0 ), "i/sprites/nikki/overlays/blush/2.png",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )       
    
image nikki win b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "nikwin",
    ( 0, 0 ), "i/sprites/nikki/overlays/blush/2.png",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )      

image nikki wor b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "nikwor",
    ( 0, 0 ), "i/sprites/nikki/overlays/blush/2.png",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )     

image nikki ang b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "nikang",
    ( 0, 0 ), "i/sprites/nikki/overlays/blush/3.png",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )

image nikki ann b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "nikann",
    ( 0, 0 ), "i/sprites/nikki/overlays/blush/3.png",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )

image nikki cur b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "nikcur",
    ( 0, 0 ), "i/sprites/nikki/overlays/blush/3.png",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )

image nikki dis b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "nikdis",
    ( 0, 0 ), "i/sprites/nikki/overlays/blush/3.png",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )
    
image nikki hap b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "nikhap",
    ( 0, 0 ), "i/sprites/nikki/overlays/blush/3.png",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )   
    
image nikki mis b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "nikmis",
    ( 0, 0 ), "i/sprites/nikki/overlays/blush/3.png",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )    
 
image nikki ner b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "nikner",
    ( 0, 0 ), "i/sprites/nikki/overlays/blush/3.png",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    ) 
    
image nikki neu b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "nikneu",
    ( 0, 0 ), "i/sprites/nikki/overlays/blush/3.png",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )   
    
image nikki sad b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "niksad",
    ( 0, 0 ), "i/sprites/nikki/overlays/blush/3.png",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )   
    
image nikki ske b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "nikske",
    ( 0, 0 ), "i/sprites/nikki/overlays/blush/3.png",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )    
    
image nikki smi b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "niksmi",
    ( 0, 0 ), "i/sprites/nikki/overlays/blush/3.png",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )    
    
image nikki sur b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "niksur",
    ( 0, 0 ), "i/sprites/nikki/overlays/blush/3.png",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )        
    
image nikki thi b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "nikthi",
    ( 0, 0 ), "i/sprites/nikki/overlays/blush/3.png",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )       
    
image nikki win b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "nikwin",
    ( 0, 0 ), "i/sprites/nikki/overlays/blush/3.png",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )      

image nikki wor b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "nikhairback",
    ( 0, 0 ), "i/sprites/nikki/outfits/base.png",
    ( 0, 0 ), "nikoutfits",
    ( 0, 0 ), "nikwor",
    ( 0, 0 ), "i/sprites/nikki/overlays/blush/3.png",
    ( 0, 0 ), "nikhairfront",
    ( 0, 0 ), "nikAccessoryTop",
    ( 0, 0 ), "nikAccessoryMiddle",
    ( 0 , 0), "nikAccessoryBottom"
    )    
    

    
########## ~ nikki EXPRESSIONS ~ ##########

image nikang:
    "i/sprites/nikki/expressions/angry/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/nikki/expressions/angry/2.png"
    .05
    "i/sprites/nikki/expressions/angry/3.png"
    .05
    "i/sprites/nikki/expressions/angry/4.png"
    .05
    "i/sprites/nikki/expressions/angry/3.png"
    .05
    "i/sprites/nikki/expressions/angry/2.png"
    .05
    repeat

    
image nikann:
    "i/sprites/nikki/expressions/annoyed/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/nikki/expressions/annoyed/2.png"
    .05
    "i/sprites/nikki/expressions/annoyed/3.png"
    .05
    "i/sprites/nikki/expressions/annoyed/4.png"
    .05
    "i/sprites/nikki/expressions/annoyed/3.png"
    .05
    "i/sprites/nikki/expressions/annoyed/2.png"
    .05
    repeat
    
    
image nikcur:
    "i/sprites/nikki/expressions/curious/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/nikki/expressions/curious/2.png"
    .05
    "i/sprites/nikki/expressions/curious/3.png"
    .05
    "i/sprites/nikki/expressions/curious/4.png"
    .05
    "i/sprites/nikki/expressions/curious/3.png"
    .05
    "i/sprites/nikki/expressions/curious/2.png"
    .05
    repeat
    
    
image nikdis:
    "i/sprites/nikki/expressions/disappointed/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/nikki/expressions/disappointed/2.png"
    .05
    "i/sprites/nikki/expressions/disappointed/3.png"
    .05
    "i/sprites/nikki/expressions/disappointed/4.png"
    .05
    "i/sprites/nikki/expressions/disappointed/3.png"
    .05
    "i/sprites/nikki/expressions/disappointed/2.png"
    .05
    repeat
    
    
image nikhap:
    "i/sprites/nikki/expressions/happy/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/nikki/expressions/happy/2.png"
    .05
    "i/sprites/nikki/expressions/happy/3.png"
    .05
    "i/sprites/nikki/expressions/happy/4.png"
    .05
    "i/sprites/nikki/expressions/happy/3.png"
    .05
    "i/sprites/nikki/expressions/happy/2.png"
    .05
    repeat
    
    
image nikmis:
    "i/sprites/nikki/expressions/mischievous/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/nikki/expressions/mischievous/2.png"
    .05
    "i/sprites/nikki/expressions/mischievous/3.png"
    .05
    "i/sprites/nikki/expressions/mischievous/4.png"
    .05
    "i/sprites/nikki/expressions/mischievous/3.png"
    .05
    "i/sprites/nikki/expressions/mischievous/2.png"
    .05
    repeat
    
    
image nikner:
    "i/sprites/nikki/expressions/nervous/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/nikki/expressions/nervous/2.png"
    .05
    "i/sprites/nikki/expressions/nervous/3.png"
    .05
    "i/sprites/nikki/expressions/nervous/4.png"
    .05
    "i/sprites/nikki/expressions/nervous/3.png"
    .05
    "i/sprites/nikki/expressions/nervous/2.png"
    .05
    repeat
    
    
image nikneu:
    "i/sprites/nikki/expressions/neutral/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/nikki/expressions/neutral/2.png"
    .05
    "i/sprites/nikki/expressions/neutral/3.png"
    .05
    "i/sprites/nikki/expressions/neutral/4.png"
    .05
    "i/sprites/nikki/expressions/neutral/3.png"
    .05
    "i/sprites/nikki/expressions/neutral/2.png"
    .05
    repeat
    
    
image niksad:
    "i/sprites/nikki/expressions/sad/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/nikki/expressions/sad/2.png"
    .05
    "i/sprites/nikki/expressions/sad/3.png"
    .05
    "i/sprites/nikki/expressions/sad/4.png"
    .05
    "i/sprites/nikki/expressions/sad/3.png"
    .05
    "i/sprites/nikki/expressions/sad/2.png"
    .05
    repeat
    
    
image nikske:
    "i/sprites/nikki/expressions/skeptical/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/nikki/expressions/skeptical/2.png"
    .05
    "i/sprites/nikki/expressions/skeptical/3.png"
    .05
    "i/sprites/nikki/expressions/skeptical/4.png"
    .05
    "i/sprites/nikki/expressions/skeptical/3.png"
    .05
    "i/sprites/nikki/expressions/skeptical/2.png"
    .05
    repeat
    
    
image niksmi:
    "i/sprites/nikki/expressions/smiling/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/nikki/expressions/smiling/2.png"
    .05
    "i/sprites/nikki/expressions/smiling/3.png"
    .05
    "i/sprites/nikki/expressions/smiling/4.png"
    .05
    "i/sprites/nikki/expressions/smiling/3.png"
    .05
    "i/sprites/nikki/expressions/smiling/2.png"
    .05
    repeat
    
    
image niksur:
    "i/sprites/nikki/expressions/surprised/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/nikki/expressions/surprised/2.png"
    .05
    "i/sprites/nikki/expressions/surprised/3.png"
    .05
    "i/sprites/nikki/expressions/surprised/4.png"
    .05
    "i/sprites/nikki/expressions/surprised/3.png"
    .05
    "i/sprites/nikki/expressions/surprised/2.png"
    .05
    repeat
    
    
image nikthi:
    "i/sprites/nikki/expressions/thinking/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/nikki/expressions/thinking/2.png"
    .05
    "i/sprites/nikki/expressions/thinking/3.png"
    .05
    "i/sprites/nikki/expressions/thinking/4.png"
    .05
    "i/sprites/nikki/expressions/thinking/3.png"
    .05
    "i/sprites/nikki/expressions/thinking/2.png"
    .05
    repeat
    
    
image nikwin:
    "i/sprites/nikki/expressions/wincing/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/nikki/expressions/wincing/2.png"
    .05
    "i/sprites/nikki/expressions/wincing/3.png"
    .05
    "i/sprites/nikki/expressions/wincing/4.png"
    .05
    "i/sprites/nikki/expressions/wincing/3.png"
    .05
    "i/sprites/nikki/expressions/wincing/2.png"
    .05
    repeat
    
    
image nikwor:
    "i/sprites/nikki/expressions/worried/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/nikki/expressions/worried/2.png"
    .05
    "i/sprites/nikki/expressions/worried/3.png"
    .05
    "i/sprites/nikki/expressions/worried/4.png"
    .05
    "i/sprites/nikki/expressions/worried/3.png"
    .05
    "i/sprites/nikki/expressions/worried/2.png"
    .05
    repeat