########## ~ mayu TEST SCRIPT ~ ##########

#$ mayOut = renpy.random.choice([ 'sCasual', 'sFashion', 'sUniform' ])



########## ~ mayu CONDITIONSWITCHES ~ ##########
    
image mayhairback = ConditionSwitch (
        "mayHairF == 'hotspring'", "i/sprites/mayu/hairstyles/hotspring/back.png",
        "mayHairB == 'default'", "i/sprites/mayu/hairstyles/default/back.png"
        )
        
image mayoutfits = ConditionSwitch (
        "mayOut == 'sCasual'", "i/sprites/mayu/outfits/summer - casual.png",
        "mayOut == 'sFashion'", "i/sprites/mayu/outfits/summer - fashion.png",
        "mayOut == 'sSwimsuit'", "i/sprites/mayu/outfits/summer - swimsuit.png",
        "mayOut == 'sUniform'", "i/sprites/mayu/outfits/summer - uniform.png",
        "mayOut == 'Halloween'", "i/sprites/mayu/outfits/halloween.png",
        "mayOut == 'hotspring'", "i/sprites/mayu/outfits/hotspring.png",
        "mayOut == 'motel'", "i/sprites/mayu/outfits/motel.png",
        "mayOut == 'outdoor'", "i/sprites/mayu/outfits/outdoor.png",
        "mayOut == 'paintball'", "i/sprites/mayu/outfits/paintball_gloves.png",
        "mayOut == 'paintball no gloves'", "i/sprites/mayu/outfits/paintball_nogloves.png",
        "mayOut == 'yandere'", "i/sprites/mayu/outfits/yandere.png",
        "mayOut == 'Pilot'", "i/sprites/mayu/outfits/pilot - default.png"
        )
        
image mayhairfront = ConditionSwitch (
        "mayHairF == 'hotspring'", "i/sprites/mayu/hairstyles/hotspring/front.png",
        "mayHairF == 'default'", "i/sprites/mayu/hairstyles/default/front.png"
        )

image mayHairA = ConditionSwitch (
        "mayHairF == 'hotspring'", "i/sprites/empty.png",
        "mayHairF == 'default'", "i/sprites/empty.png"
        )

image mayAccessoryTop = ConditionSwitch (
        "mayOut == 'paintball'", "i/sprites/mayu/accessories/top/mask.png",
        "mayOut == 'Pilot'", "i/sprites/mayu/accessories/top/pilot.png",
        "mayOut == 'Halloween'", "i/sprites/mayu/accessories/hair/halloween.png",
        "mayAccT == 'emptyimage'", "i/sprites/empty.png"
        )
        
image mayAccessoryMiddle = ConditionSwitch (
        "mayAccM == 'emptyimage'", "i/sprites/empty.png"
        )
        
image mayAccessoryBottom = ConditionSwitch (
        "mayAccB == 'emptyimage'", "i/sprites/empty.png"
        )
    
    

########## ~ mayu LIVECOMPOSITE ~ ##########

image mayu ang = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "mayang",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )

image mayu ann = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "mayann",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )

image mayu cur = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "maycur",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )

image mayu dis = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "maydis",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )
    
image mayu hap = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "mayhap",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )   
    
image mayu mis = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "maymis",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )    
 
image mayu ner = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "mayner",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    ) 
    
image mayu neu = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "mayneu",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )   
    
image mayu sad = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "maysad",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )   
    
image mayu ske = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "mayske",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )    
    
image mayu smi = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "maysmi",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )    
    
image mayu sur = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "maysur",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )        
    
image mayu thi = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "maythi",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )       
    
image mayu win = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "maywin",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )      

image mayu wor = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "maywor",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )    
  
image mayu ang b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "mayang",
    ( 0, 0 ), "i/sprites/mayu/overlays/blush/1.png",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )

image mayu ann b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "mayann",
    ( 0, 0 ), "i/sprites/mayu/overlays/blush/1.png",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )

image mayu cur b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "maycur",
    ( 0, 0 ), "i/sprites/mayu/overlays/blush/1.png",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )

image mayu dis b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "maydis",
    ( 0, 0 ), "i/sprites/mayu/overlays/blush/1.png",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )
    
image mayu hap b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "mayhap",
    ( 0, 0 ), "i/sprites/mayu/overlays/blush/1.png",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )   
    
image mayu mis b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "maymis",
    ( 0, 0 ), "i/sprites/mayu/overlays/blush/1.png",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )    
 
image mayu ner b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "mayner",
    ( 0, 0 ), "i/sprites/mayu/overlays/blush/1.png",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    ) 
    
image mayu neu b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "mayneu",
    ( 0, 0 ), "i/sprites/mayu/overlays/blush/1.png",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )   
    
image mayu sad b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "maysad",
    ( 0, 0 ), "i/sprites/mayu/overlays/blush/1.png",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )   
    
image mayu ske b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "mayske",
    ( 0, 0 ), "i/sprites/mayu/overlays/blush/1.png",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )    
    
image mayu smi b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "maysmi",
    ( 0, 0 ), "i/sprites/mayu/overlays/blush/1.png",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )    
    
image mayu sur b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "maysur",
    ( 0, 0 ), "i/sprites/mayu/overlays/blush/1.png",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )        
    
image mayu thi b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "maythi",
    ( 0, 0 ), "i/sprites/mayu/overlays/blush/1.png",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )       
    
image mayu win b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "maywin",
    ( 0, 0 ), "i/sprites/mayu/overlays/blush/1.png",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )      

image mayu wor b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "maywor",
    ( 0, 0 ), "i/sprites/mayu/overlays/blush/1.png",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )     
    
image mayu ang b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "mayang",
    ( 0, 0 ), "i/sprites/mayu/overlays/blush/2.png",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )

image mayu ann b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "mayann",
    ( 0, 0 ), "i/sprites/mayu/overlays/blush/2.png",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )

image mayu cur b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "maycur",
    ( 0, 0 ), "i/sprites/mayu/overlays/blush/2.png",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )

image mayu dis b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "maydis",
    ( 0, 0 ), "i/sprites/mayu/overlays/blush/2.png",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )
    
image mayu hap b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "mayhap",
    ( 0, 0 ), "i/sprites/mayu/overlays/blush/2.png",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )   
    
image mayu mis b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "maymis",
    ( 0, 0 ), "i/sprites/mayu/overlays/blush/2.png",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )    
 
image mayu ner b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "mayner",
    ( 0, 0 ), "i/sprites/mayu/overlays/blush/2.png",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    ) 
    
image mayu neu b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "mayneu",
    ( 0, 0 ), "i/sprites/mayu/overlays/blush/2.png",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )   
    
image mayu sad b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "maysad",
    ( 0, 0 ), "i/sprites/mayu/overlays/blush/2.png",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )   
    
image mayu ske b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "mayske",
    ( 0, 0 ), "i/sprites/mayu/overlays/blush/2.png",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )    
    
image mayu smi b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "maysmi",
    ( 0, 0 ), "i/sprites/mayu/overlays/blush/2.png",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )    
    
image mayu sur b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "maysur",
    ( 0, 0 ), "i/sprites/mayu/overlays/blush/2.png",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )        
    
image mayu thi b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "maythi",
    ( 0, 0 ), "i/sprites/mayu/overlays/blush/2.png",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )       
    
image mayu win b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "maywin",
    ( 0, 0 ), "i/sprites/mayu/overlays/blush/2.png",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )      

image mayu wor b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "maywor",
    ( 0, 0 ), "i/sprites/mayu/overlays/blush/2.png",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )     

image mayu ang b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "mayang",
    ( 0, 0 ), "i/sprites/mayu/overlays/blush/3.png",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )

image mayu ann b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "mayann",
    ( 0, 0 ), "i/sprites/mayu/overlays/blush/3.png",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )

image mayu cur b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "maycur",
    ( 0, 0 ), "i/sprites/mayu/overlays/blush/3.png",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )

image mayu dis b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "maydis",
    ( 0, 0 ), "i/sprites/mayu/overlays/blush/3.png",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )
    
image mayu hap b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "mayhap",
    ( 0, 0 ), "i/sprites/mayu/overlays/blush/3.png",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )   
    
image mayu mis b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "maymis",
    ( 0, 0 ), "i/sprites/mayu/overlays/blush/3.png",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )    
 
image mayu ner b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "mayner",
    ( 0, 0 ), "i/sprites/mayu/overlays/blush/3.png",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    ) 
    
image mayu neu b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "mayneu",
    ( 0, 0 ), "i/sprites/mayu/overlays/blush/3.png",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )   
    
image mayu sad b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "maysad",
    ( 0, 0 ), "i/sprites/mayu/overlays/blush/3.png",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )   
    
image mayu ske b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "mayske",
    ( 0, 0 ), "i/sprites/mayu/overlays/blush/3.png",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )    
    
image mayu smi b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "maysmi",
    ( 0, 0 ), "i/sprites/mayu/overlays/blush/3.png",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )    
    
image mayu sur b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "maysur",
    ( 0, 0 ), "i/sprites/mayu/overlays/blush/3.png",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )        
    
image mayu thi b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "maythi",
    ( 0, 0 ), "i/sprites/mayu/overlays/blush/3.png",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )       
    
image mayu win b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "maywin",
    ( 0, 0 ), "i/sprites/mayu/overlays/blush/3.png",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )      

image mayu wor b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "mayhairback",
    ( 0, 0 ), "i/sprites/mayu/outfits/base.png",
    ( 0, 0 ), "mayoutfits",
    ( 0, 0 ), "maywor",
    ( 0, 0 ), "i/sprites/mayu/overlays/blush/3.png",
    ( 0, 0 ), "mayHairA",
    ( 0, 0 ), "mayhairfront",
    ( 0, 0 ), "mayAccessoryTop",
    ( 0, 0 ), "mayAccessoryMiddle",
    ( 0 , 0), "mayAccessoryBottom"
    )    
    

    
########## ~ mayu EXPRESSIONS ~ ##########

image mayang:
    "i/sprites/mayu/expressions/angry/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/mayu/expressions/angry/2.png"
    .05
    "i/sprites/mayu/expressions/angry/3.png"
    .05
    "i/sprites/mayu/expressions/angry/4.png"
    .05
    "i/sprites/mayu/expressions/angry/3.png"
    .05
    "i/sprites/mayu/expressions/angry/2.png"
    .05
    repeat

    
image mayann:
    "i/sprites/mayu/expressions/annoyed/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/mayu/expressions/annoyed/2.png"
    .05
    "i/sprites/mayu/expressions/annoyed/3.png"
    .05
    "i/sprites/mayu/expressions/annoyed/4.png"
    .05
    "i/sprites/mayu/expressions/annoyed/3.png"
    .05
    "i/sprites/mayu/expressions/annoyed/2.png"
    .05
    repeat
    
    
image maycur:
    "i/sprites/mayu/expressions/curious/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/mayu/expressions/curious/2.png"
    .05
    "i/sprites/mayu/expressions/curious/3.png"
    .05
    "i/sprites/mayu/expressions/curious/4.png"
    .05
    "i/sprites/mayu/expressions/curious/3.png"
    .05
    "i/sprites/mayu/expressions/curious/2.png"
    .05
    repeat
    
    
image maydis:
    "i/sprites/mayu/expressions/disappointed/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/mayu/expressions/disappointed/2.png"
    .05
    "i/sprites/mayu/expressions/disappointed/3.png"
    .05
    "i/sprites/mayu/expressions/disappointed/4.png"
    .05
    "i/sprites/mayu/expressions/disappointed/3.png"
    .05
    "i/sprites/mayu/expressions/disappointed/2.png"
    .05
    repeat
    
    
image mayhap:
    "i/sprites/mayu/expressions/happy/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/mayu/expressions/happy/2.png"
    .05
    "i/sprites/mayu/expressions/happy/3.png"
    .05
    "i/sprites/mayu/expressions/happy/4.png"
    .05
    "i/sprites/mayu/expressions/happy/3.png"
    .05
    "i/sprites/mayu/expressions/happy/2.png"
    .05
    repeat
    
    
image maymis:
    "i/sprites/mayu/expressions/mischievous/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/mayu/expressions/mischievous/2.png"
    .05
    "i/sprites/mayu/expressions/mischievous/3.png"
    .05
    "i/sprites/mayu/expressions/mischievous/4.png"
    .05
    "i/sprites/mayu/expressions/mischievous/3.png"
    .05
    "i/sprites/mayu/expressions/mischievous/2.png"
    .05
    repeat
    
    
image mayner:
    "i/sprites/mayu/expressions/nervous/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/mayu/expressions/nervous/2.png"
    .05
    "i/sprites/mayu/expressions/nervous/3.png"
    .05
    "i/sprites/mayu/expressions/nervous/4.png"
    .05
    "i/sprites/mayu/expressions/nervous/3.png"
    .05
    "i/sprites/mayu/expressions/nervous/2.png"
    .05
    repeat
    
    
image mayneu:
    "i/sprites/mayu/expressions/neutral/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/mayu/expressions/neutral/2.png"
    .05
    "i/sprites/mayu/expressions/neutral/3.png"
    .05
    "i/sprites/mayu/expressions/neutral/4.png"
    .05
    "i/sprites/mayu/expressions/neutral/3.png"
    .05
    "i/sprites/mayu/expressions/neutral/2.png"
    .05
    repeat
    
    
image maysad:
    "i/sprites/mayu/expressions/sad/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/mayu/expressions/sad/2.png"
    .05
    "i/sprites/mayu/expressions/sad/3.png"
    .05
    "i/sprites/mayu/expressions/sad/4.png"
    .05
    "i/sprites/mayu/expressions/sad/3.png"
    .05
    "i/sprites/mayu/expressions/sad/2.png"
    .05
    repeat
    
    
image mayske:
    "i/sprites/mayu/expressions/skeptical/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/mayu/expressions/skeptical/2.png"
    .05
    "i/sprites/mayu/expressions/skeptical/3.png"
    .05
    "i/sprites/mayu/expressions/skeptical/4.png"
    .05
    "i/sprites/mayu/expressions/skeptical/3.png"
    .05
    "i/sprites/mayu/expressions/skeptical/2.png"
    .05
    repeat
    
    
image maysmi:
    "i/sprites/mayu/expressions/smiling/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/mayu/expressions/smiling/2.png"
    .05
    "i/sprites/mayu/expressions/smiling/3.png"
    .05
    "i/sprites/mayu/expressions/smiling/4.png"
    .05
    "i/sprites/mayu/expressions/smiling/3.png"
    .05
    "i/sprites/mayu/expressions/smiling/2.png"
    .05
    repeat
    
    
image maysur:
    "i/sprites/mayu/expressions/surprised/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/mayu/expressions/surprised/2.png"
    .05
    "i/sprites/mayu/expressions/surprised/3.png"
    .05
    "i/sprites/mayu/expressions/surprised/4.png"
    .05
    "i/sprites/mayu/expressions/surprised/3.png"
    .05
    "i/sprites/mayu/expressions/surprised/2.png"
    .05
    repeat
    
    
image maythi:
    "i/sprites/mayu/expressions/thinking/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/mayu/expressions/thinking/2.png"
    .05
    "i/sprites/mayu/expressions/thinking/3.png"
    .05
    "i/sprites/mayu/expressions/thinking/4.png"
    .05
    "i/sprites/mayu/expressions/thinking/3.png"
    .05
    "i/sprites/mayu/expressions/thinking/2.png"
    .05
    repeat
    
    
image maywin:
    "i/sprites/mayu/expressions/wincing/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/mayu/expressions/wincing/2.png"
    .05
    "i/sprites/mayu/expressions/wincing/3.png"
    .05
    "i/sprites/mayu/expressions/wincing/4.png"
    .05
    "i/sprites/mayu/expressions/wincing/3.png"
    .05
    "i/sprites/mayu/expressions/wincing/2.png"
    .05
    repeat
    
    
image maywor:
    "i/sprites/mayu/expressions/worried/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/mayu/expressions/worried/2.png"
    .05
    "i/sprites/mayu/expressions/worried/3.png"
    .05
    "i/sprites/mayu/expressions/worried/4.png"
    .05
    "i/sprites/mayu/expressions/worried/3.png"
    .05
    "i/sprites/mayu/expressions/worried/2.png"
    .05
    repeat