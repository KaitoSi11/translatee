########## ~ kaori TEST SCRIPT ~ ##########

#$ kaoOut = renpy.random.choice(['comfort'])
#$ kaoHairF = renpy.random.choice([ 'banded', 'braided', 'tied', 'long' ])
#$ kaoHairB = renpy.random.choice([ 'banded', 'braided', 'tied', 'long' ])



########## ~ kaori CONDITIONSWITCHES ~ ##########
    
image kaohairback = ConditionSwitch (
        "kaoHairB == 'default'", "i/sprites/kaori/hairstyles/default/back.png",
        "kaoHairB == 'long'", "i/sprites/kaori/hairstyles/long/back.png",
        "kaoHairB == 'tied'", "i/sprites/kaori/hairstyles/tied/back.png",
        "kaoHairB == 'braided'", "i/sprites/empty.png", #<- This one doesn't exist, only front
        "kaoHairB == 'banded'", "i/sprites/kaori/hairstyles/banded/back.png"
        )
        
image kaooutfits = ConditionSwitch (
        "kaoOut == 'sCasual'", "i/sprites/kaori/outfits/summer - casual.png",
        "kaoOut == 'sCute'", "i/sprites/kaori/outfits/summer - cute.png",
        "kaoOut == 'sFashion'", "i/sprites/kaori/outfits/summer - fashion.png",
        "kaoOut == 'sFlirty'", "i/sprites/kaori/outfits/summer - flirty.png",
        "kaoOut == 'sGym'", "i/sprites/kaori/outfits/summer - gym.png",
        "kaoOut == 'sSwimsuit'", "i/sprites/kaori/outfits/summer - swimsuit.png",
        "kaoOut == 'sUniform'", "i/sprites/kaori/outfits/summer - uniform.png",
        "kaoOut == 'comfort'", "i/sprites/kaori/outfits/comfort.png",
        "kaoOut == 'Halloween'", "i/sprites/kaori/outfits/halloween.png",
        "kaoOut == 'hotel'", "i/sprites/kaori/outfits/hotel.png",
        "kaoOut == 'hotspring'", "i/sprites/kaori/outfits/hotspring.png",
        "kaoOut == 'kindergarten'", "i/sprites/kaori/outfits/kindergarten.png",
        "kaoOut == 'outdoor'", "i/sprites/kaori/outfits/outdoor.png",
        #"kaoOut == 'outdoor hat'", "i/sprites/kaori/outfits/outdoor_hat.png", # not a whole outfit
        "kaoOut == 'Pilot'", "i/sprites/kaori/outfits/pilot - default.png"
        )
        
image kaohairfront = ConditionSwitch (
        "kaoHairF == 'default'", "i/sprites/kaori/hairstyles/default/front.png",
        "kaoHairF == 'hotspring'", "i/sprites/kaori/hairstyles/hotspring/front.png",
        "kaoHairF == 'long'", "i/sprites/kaori/hairstyles/long/front.png",
        "kaoHairF == 'tied'", "i/sprites/kaori/hairstyles/tied/front.png",
        "kaoHairF == 'braided'", "i/sprites/kaori/hairstyles/braided/front.png",
        "kaoHairF == 'banded'", "i/sprites/kaori/hairstyles/banded/front.png"
        )

image kaoHairA = ConditionSwitch (
        "kaoHairF == 'default'", "i/sprites/empty.png",
        "kaoHairF == 'hotspring'", "i/sprites/empty.png",
        "kaoHairF == 'tied'", "i/sprites/kaori/accessories/hair/tie.png",
        "kaoHairF == 'banded'", "i/sprites/empty.png", # stuck behind "banded" front, temp fix in AccessoryMiddle
        "kaoHairF == 'long'", "i/sprites/empty.png",
        "kaoHairF == 'braided'", "i/sprites/empty.png"
        )

image kaoAccessoryTop = ConditionSwitch (
        "kaoOut == 'Pilot'", "i/sprites/kaori/accessories/top/pilot.png",
        "kaoOut == 'outdoor'", "i/sprites/kaori/outfits/outdoor_hat.png",
        "kaoAccT == 'emptyimage'", "i/sprites/empty.png"
        )
        
image kaoAccessoryMiddle = ConditionSwitch (
        "kaoHairF == 'banded'", "i/sprites/kaori/accessories/hair/band.png", # temp fix
        "kaoAccM == 'emptyimage'", "i/sprites/empty.png"
        )
        
image kaoAccessoryBottom = ConditionSwitch (
        "kaoAccB == 'emptyimage'", "i/sprites/empty.png"
        )
    
    

########## ~ kaori LIVECOMPOSITE ~ ##########

image kaori ang = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaoang",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )

image kaori ann = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaoann",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )

image kaori cur = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaocur",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )

image kaori dis = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaodis",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )
    
image kaori hap = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaohap",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )   
    
image kaori mis = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaomis",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )    
 
image kaori ner = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaoner",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    ) 
    
image kaori neu = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaoneu",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )   
    
image kaori sad = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaosad",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )   
    
image kaori ske = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaoske",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )    
    
image kaori smi = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaosmi",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )    
    
image kaori sur = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaosur",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )        
    
image kaori thi = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaothi",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )       
    
image kaori win = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaowin",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )      

image kaori wor = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaowor",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )
  
image kaori ang b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaoang",
    ( 0, 0 ), "i/sprites/kaori/overlays/blush/1.png",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )

image kaori ann b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaoann",
    ( 0, 0 ), "i/sprites/kaori/overlays/blush/1.png",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )

image kaori cur b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaocur",
    ( 0, 0 ), "i/sprites/kaori/overlays/blush/1.png",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )

image kaori dis b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaodis",
    ( 0, 0 ), "i/sprites/kaori/overlays/blush/1.png",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )
    
image kaori hap b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaohap",
    ( 0, 0 ), "i/sprites/kaori/overlays/blush/1.png",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )   
    
image kaori mis b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaomis",
    ( 0, 0 ), "i/sprites/kaori/overlays/blush/1.png",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )    
 
image kaori ner b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaoner",
    ( 0, 0 ), "i/sprites/kaori/overlays/blush/1.png",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    ) 
    
image kaori neu b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaoneu",
    ( 0, 0 ), "i/sprites/kaori/overlays/blush/1.png",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )   
    
image kaori sad b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaosad",
    ( 0, 0 ), "i/sprites/kaori/overlays/blush/1.png",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )   
    
image kaori ske b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaoske",
    ( 0, 0 ), "i/sprites/kaori/overlays/blush/1.png",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )    
    
image kaori smi b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaosmi",
    ( 0, 0 ), "i/sprites/kaori/overlays/blush/1.png",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )    
    
image kaori sur b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaosur",
    ( 0, 0 ), "i/sprites/kaori/overlays/blush/1.png",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )        
    
image kaori thi b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaothi",
    ( 0, 0 ), "i/sprites/kaori/overlays/blush/1.png",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )       
    
image kaori win b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaowin",
    ( 0, 0 ), "i/sprites/kaori/overlays/blush/1.png",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )      

image kaori wor b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaowor",
    ( 0, 0 ), "i/sprites/kaori/overlays/blush/1.png",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )     
    
image kaori ang b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaoang",
    ( 0, 0 ), "i/sprites/kaori/overlays/blush/2.png",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )

image kaori ann b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaoann",
    ( 0, 0 ), "i/sprites/kaori/overlays/blush/2.png",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )

image kaori cur b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaocur",
    ( 0, 0 ), "i/sprites/kaori/overlays/blush/2.png",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )

image kaori dis b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaodis",
    ( 0, 0 ), "i/sprites/kaori/overlays/blush/2.png",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )
    
image kaori hap b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaohap",
    ( 0, 0 ), "i/sprites/kaori/overlays/blush/2.png",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )   
    
image kaori mis b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaomis",
    ( 0, 0 ), "i/sprites/kaori/overlays/blush/2.png",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )    
 
image kaori ner b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaoner",
    ( 0, 0 ), "i/sprites/kaori/overlays/blush/2.png",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    ) 
    
image kaori neu b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaoneu",
    ( 0, 0 ), "i/sprites/kaori/overlays/blush/2.png",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )   
    
image kaori sad b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaosad",
    ( 0, 0 ), "i/sprites/kaori/overlays/blush/2.png",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )   
    
image kaori ske b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaoske",
    ( 0, 0 ), "i/sprites/kaori/overlays/blush/2.png",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )    
    
image kaori smi b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaosmi",
    ( 0, 0 ), "i/sprites/kaori/overlays/blush/2.png",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )    
    
image kaori sur b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaosur",
    ( 0, 0 ), "i/sprites/kaori/overlays/blush/2.png",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )        
    
image kaori thi b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaothi",
    ( 0, 0 ), "i/sprites/kaori/overlays/blush/2.png",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )       
    
image kaori win b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaowin",
    ( 0, 0 ), "i/sprites/kaori/overlays/blush/2.png",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )      

image kaori wor b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaowor",
    ( 0, 0 ), "i/sprites/kaori/overlays/blush/2.png",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )     

image kaori ang b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaoang",
    ( 0, 0 ), "i/sprites/kaori/overlays/blush/3.png",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )

image kaori ann b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaoann",
    ( 0, 0 ), "i/sprites/kaori/overlays/blush/3.png",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )

image kaori cur b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaocur",
    ( 0, 0 ), "i/sprites/kaori/overlays/blush/3.png",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )

image kaori dis b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaodis",
    ( 0, 0 ), "i/sprites/kaori/overlays/blush/3.png",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )
    
image kaori hap b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaohap",
    ( 0, 0 ), "i/sprites/kaori/overlays/blush/3.png",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )   
    
image kaori mis b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaomis",
    ( 0, 0 ), "i/sprites/kaori/overlays/blush/3.png",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )    
 
image kaori ner b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaoner",
    ( 0, 0 ), "i/sprites/kaori/overlays/blush/3.png",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    ) 
    
image kaori neu b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaoneu",
    ( 0, 0 ), "i/sprites/kaori/overlays/blush/3.png",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )   
    
image kaori sad b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaosad",
    ( 0, 0 ), "i/sprites/kaori/overlays/blush/3.png",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )   
    
image kaori ske b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaoske",
    ( 0, 0 ), "i/sprites/kaori/overlays/blush/3.png",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )    
    
image kaori smi b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaosmi",
    ( 0, 0 ), "i/sprites/kaori/overlays/blush/3.png",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )    
    
image kaori sur b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaosur",
    ( 0, 0 ), "i/sprites/kaori/overlays/blush/3.png",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )        
    
image kaori thi b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaothi",
    ( 0, 0 ), "i/sprites/kaori/overlays/blush/3.png",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )       
    
image kaori win b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaowin",
    ( 0, 0 ), "i/sprites/kaori/overlays/blush/3.png",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )      

image kaori wor b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaohairback",
    ( 0, 0 ), "i/sprites/kaori/outfits/base.png",
    ( 0, 0 ), "kaooutfits",
    ( 0, 0 ), "kaowor",
    ( 0, 0 ), "i/sprites/kaori/overlays/blush/3.png",
    ( 0, 0 ), "kaoHairA",
    ( 0, 0 ), "kaohairfront",
    ( 0, 0 ), "kaoAccessoryTop",
    ( 0, 0 ), "kaoAccessoryMiddle",
    ( 0 , 0), "kaoAccessoryBottom"
    )    
    

    
########## ~ kaori EXPRESSIONS ~ ##########

image kaoang:
    "i/sprites/kaori/expressions/angry/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/kaori/expressions/angry/2.png"
    .05
    "i/sprites/kaori/expressions/angry/3.png"
    .05
    "i/sprites/kaori/expressions/angry/4.png"
    .05
    "i/sprites/kaori/expressions/angry/3.png"
    .05
    "i/sprites/kaori/expressions/angry/2.png"
    .05
    repeat

    
image kaoann:
    "i/sprites/kaori/expressions/annoyed/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/kaori/expressions/annoyed/2.png"
    .05
    "i/sprites/kaori/expressions/annoyed/3.png"
    .05
    "i/sprites/kaori/expressions/annoyed/4.png"
    .05
    "i/sprites/kaori/expressions/annoyed/3.png"
    .05
    "i/sprites/kaori/expressions/annoyed/2.png"
    .05
    repeat
    
    
image kaocur:
    "i/sprites/kaori/expressions/curious/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/kaori/expressions/curious/2.png"
    .05
    "i/sprites/kaori/expressions/curious/3.png"
    .05
    "i/sprites/kaori/expressions/curious/4.png"
    .05
    "i/sprites/kaori/expressions/curious/3.png"
    .05
    "i/sprites/kaori/expressions/curious/2.png"
    .05
    repeat
    
    
image kaodis:
    "i/sprites/kaori/expressions/disappointed/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/kaori/expressions/disappointed/2.png"
    .05
    "i/sprites/kaori/expressions/disappointed/3.png"
    .05
    "i/sprites/kaori/expressions/disappointed/4.png"
    .05
    "i/sprites/kaori/expressions/disappointed/3.png"
    .05
    "i/sprites/kaori/expressions/disappointed/2.png"
    .05
    repeat
    
    
image kaohap:
    "i/sprites/kaori/expressions/happy/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/kaori/expressions/happy/2.png"
    .05
    "i/sprites/kaori/expressions/happy/3.png"
    .05
    "i/sprites/kaori/expressions/happy/4.png"
    .05
    "i/sprites/kaori/expressions/happy/3.png"
    .05
    "i/sprites/kaori/expressions/happy/2.png"
    .05
    repeat
    
    
image kaomis:
    "i/sprites/kaori/expressions/mischievous/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/kaori/expressions/mischievous/2.png"
    .05
    "i/sprites/kaori/expressions/mischievous/3.png"
    .05
    "i/sprites/kaori/expressions/mischievous/4.png"
    .05
    "i/sprites/kaori/expressions/mischievous/3.png"
    .05
    "i/sprites/kaori/expressions/mischievous/2.png"
    .05
    repeat
    
    
image kaoner:
    "i/sprites/kaori/expressions/nervous/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/kaori/expressions/nervous/2.png"
    .05
    "i/sprites/kaori/expressions/nervous/3.png"
    .05
    "i/sprites/kaori/expressions/nervous/4.png"
    .05
    "i/sprites/kaori/expressions/nervous/3.png"
    .05
    "i/sprites/kaori/expressions/nervous/2.png"
    .05
    repeat
    
    
image kaoneu:
    "i/sprites/kaori/expressions/neutral/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/kaori/expressions/neutral/2.png"
    .05
    "i/sprites/kaori/expressions/neutral/3.png"
    .05
    "i/sprites/kaori/expressions/neutral/4.png"
    .05
    "i/sprites/kaori/expressions/neutral/3.png"
    .05
    "i/sprites/kaori/expressions/neutral/2.png"
    .05
    repeat
    
    
image kaosad:
    "i/sprites/kaori/expressions/sad/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/kaori/expressions/sad/2.png"
    .05
    "i/sprites/kaori/expressions/sad/3.png"
    .05
    "i/sprites/kaori/expressions/sad/4.png"
    .05
    "i/sprites/kaori/expressions/sad/3.png"
    .05
    "i/sprites/kaori/expressions/sad/2.png"
    .05
    repeat
    
    
image kaoske:
    "i/sprites/kaori/expressions/skeptical/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/kaori/expressions/skeptical/2.png"
    .05
    "i/sprites/kaori/expressions/skeptical/3.png"
    .05
    "i/sprites/kaori/expressions/skeptical/4.png"
    .05
    "i/sprites/kaori/expressions/skeptical/3.png"
    .05
    "i/sprites/kaori/expressions/skeptical/2.png"
    .05
    repeat
    
    
image kaosmi:
    "i/sprites/kaori/expressions/smiling/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/kaori/expressions/smiling/2.png"
    .05
    "i/sprites/kaori/expressions/smiling/3.png"
    .05
    "i/sprites/kaori/expressions/smiling/4.png"
    .05
    "i/sprites/kaori/expressions/smiling/3.png"
    .05
    "i/sprites/kaori/expressions/smiling/2.png"
    .05
    repeat
    
    
image kaosur:
    "i/sprites/kaori/expressions/surprised/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/kaori/expressions/surprised/2.png"
    .05
    "i/sprites/kaori/expressions/surprised/3.png"
    .05
    "i/sprites/kaori/expressions/surprised/4.png"
    .05
    "i/sprites/kaori/expressions/surprised/3.png"
    .05
    "i/sprites/kaori/expressions/surprised/2.png"
    .05
    repeat
    
    
image kaothi:
    "i/sprites/kaori/expressions/thinking/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/kaori/expressions/thinking/2.png"
    .05
    "i/sprites/kaori/expressions/thinking/3.png"
    .05
    "i/sprites/kaori/expressions/thinking/4.png"
    .05
    "i/sprites/kaori/expressions/thinking/3.png"
    .05
    "i/sprites/kaori/expressions/thinking/2.png"
    .05
    repeat
    
    
image kaowin:
    "i/sprites/kaori/expressions/wincing/1.png"
    
    
image kaowor:
    "i/sprites/kaori/expressions/worried/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/kaori/expressions/worried/2.png"
    .05
    "i/sprites/kaori/expressions/worried/3.png"
    .05
    "i/sprites/kaori/expressions/worried/4.png"
    .05
    "i/sprites/kaori/expressions/worried/3.png"
    .05
    "i/sprites/kaori/expressions/worried/2.png"
    .05
    repeat