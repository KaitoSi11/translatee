########## ~ shou CONDITIONSWITCHES ~ ##########
    
image shohairback = ConditionSwitch (
        "shoHairB == 'default'", "i/sprites/shou/hairstyles/default/back.png"
        )
        
image shooutfits = ConditionSwitch (
        "shoOut == 'sCasual'", "i/sprites/shou/outfits/summer - casual.png",
        "shoOut == 'sGym'", "i/sprites/shou/outfits/summer - gym.png",
        "shoOut == 'sSwimsuit'", "i/sprites/shou/outfits/summer - swimsuit.png",
        "shoOut == 'sUniform'", "i/sprites/shou/outfits/summer - uniform.png",
        "shoOut == 'Halloween'", "i/sprites/shou/outfits/halloween.png",
        "shoOut == 'hotspring'", "i/sprites/shou/outfits/hotspring.png",
        "shoOut == 'outdoor'", "i/sprites/shou/outfits/outdoor.png",
        "shoOut == 'Pilot'", "i/sprites/shou/outfits/pilot - default.png"
        )
        
image shohairfront = ConditionSwitch (
        "shoHairF == 'default'", "i/sprites/shou/hairstyles/default/front.png"
        )

image shoAccessoryTop = ConditionSwitch (
        "shoOut == 'Pilot'", "i/sprites/shou/accessories/top/pilot.png",
        "shoAccT == 'emptyimage'", "i/sprites/empty.png"
        )
        
image shoAccessoryMiddle = ConditionSwitch (
        "shoAccM == 'emptyimage'", "i/sprites/empty.png"
        )
        
image shoAccessoryBottom = ConditionSwitch (
        "shoAccB == 'emptyimage'", "i/sprites/empty.png"
        )
    
    

########## ~ shou LIVECOMPOSITE ~ ##########

image shou ang = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "shoang",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )

image shou ann = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "shoann",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )

image shou cur = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "shocur",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )

image shou dis = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "shodis",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )
    
image shou hap = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "shohap",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )   
    
image shou mis = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "shomis",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )    
 
image shou ner = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "shoner",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    ) 
    
image shou neu = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "shoneu",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )   
    
image shou sad = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "shosad",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )   
    
image shou ske = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "shoske",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )    
    
image shou smi = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "shosmi",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )    
    
image shou sur = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "shosur",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )        
    
image shou thi = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "shothi",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )       
    
image shou win = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "showin",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )      

image shou wor = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "showor",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )    
  
image shou ang b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "shoang",
    ( 0, 0 ), "i/sprites/shou/overlays/blush/1.png",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )

image shou ann b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "shoann",
    ( 0, 0 ), "i/sprites/shou/overlays/blush/1.png",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )

image shou cur b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "shocur",
    ( 0, 0 ), "i/sprites/shou/overlays/blush/1.png",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )

image shou dis b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "shodis",
    ( 0, 0 ), "i/sprites/shou/overlays/blush/1.png",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )
    
image shou hap b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "shohap",
    ( 0, 0 ), "i/sprites/shou/overlays/blush/1.png",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )   
    
image shou mis b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "shomis",
    ( 0, 0 ), "i/sprites/shou/overlays/blush/1.png",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )    
 
image shou ner b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "shoner",
    ( 0, 0 ), "i/sprites/shou/overlays/blush/1.png",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    ) 
    
image shou neu b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "shoneu",
    ( 0, 0 ), "i/sprites/shou/overlays/blush/1.png",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )   
    
image shou sad b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "shosad",
    ( 0, 0 ), "i/sprites/shou/overlays/blush/1.png",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )   
    
image shou ske b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "shoske",
    ( 0, 0 ), "i/sprites/shou/overlays/blush/1.png",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )    
    
image shou smi b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "shosmi",
    ( 0, 0 ), "i/sprites/shou/overlays/blush/1.png",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )    
    
image shou sur b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "shosur",
    ( 0, 0 ), "i/sprites/shou/overlays/blush/1.png",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )        
    
image shou thi b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "shothi",
    ( 0, 0 ), "i/sprites/shou/overlays/blush/1.png",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )       
    
image shou win b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "showin",
    ( 0, 0 ), "i/sprites/shou/overlays/blush/1.png",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )      

image shou wor b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "showor",
    ( 0, 0 ), "i/sprites/shou/overlays/blush/1.png",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )     
    
image shou ang b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "shoang",
    ( 0, 0 ), "i/sprites/shou/overlays/blush/2.png",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )

image shou ann b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "shoann",
    ( 0, 0 ), "i/sprites/shou/overlays/blush/2.png",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )

image shou cur b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "shocur",
    ( 0, 0 ), "i/sprites/shou/overlays/blush/2.png",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )

image shou dis b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "shodis",
    ( 0, 0 ), "i/sprites/shou/overlays/blush/2.png",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )
    
image shou hap b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "shohap",
    ( 0, 0 ), "i/sprites/shou/overlays/blush/2.png",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )   
    
image shou mis b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "shomis",
    ( 0, 0 ), "i/sprites/shou/overlays/blush/2.png",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )    
 
image shou ner b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "shoner",
    ( 0, 0 ), "i/sprites/shou/overlays/blush/2.png",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    ) 
    
image shou neu b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "shoneu",
    ( 0, 0 ), "i/sprites/shou/overlays/blush/2.png",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )   
    
image shou sad b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "shosad",
    ( 0, 0 ), "i/sprites/shou/overlays/blush/2.png",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )   
    
image shou ske b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "shoske",
    ( 0, 0 ), "i/sprites/shou/overlays/blush/2.png",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )    
    
image shou smi b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "shosmi",
    ( 0, 0 ), "i/sprites/shou/overlays/blush/2.png",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )    
    
image shou sur b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "shosur",
    ( 0, 0 ), "i/sprites/shou/overlays/blush/2.png",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )        
    
image shou thi b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "shothi",
    ( 0, 0 ), "i/sprites/shou/overlays/blush/2.png",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )       
    
image shou win b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "showin",
    ( 0, 0 ), "i/sprites/shou/overlays/blush/2.png",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )      

image shou wor b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "showor",
    ( 0, 0 ), "i/sprites/shou/overlays/blush/2.png",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )     

image shou ang b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "shoang",
    ( 0, 0 ), "i/sprites/shou/overlays/blush/3.png",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )

image shou ann b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "shoann",
    ( 0, 0 ), "i/sprites/shou/overlays/blush/3.png",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )

image shou cur b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "shocur",
    ( 0, 0 ), "i/sprites/shou/overlays/blush/3.png",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )

image shou dis b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "shodis",
    ( 0, 0 ), "i/sprites/shou/overlays/blush/3.png",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )
    
image shou hap b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "shohap",
    ( 0, 0 ), "i/sprites/shou/overlays/blush/3.png",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )   
    
image shou mis b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "shomis",
    ( 0, 0 ), "i/sprites/shou/overlays/blush/3.png",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )    
 
image shou ner b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "shoner",
    ( 0, 0 ), "i/sprites/shou/overlays/blush/3.png",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    ) 
    
image shou neu b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "shoneu",
    ( 0, 0 ), "i/sprites/shou/overlays/blush/3.png",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )   
    
image shou sad b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "shosad",
    ( 0, 0 ), "i/sprites/shou/overlays/blush/3.png",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )   
    
image shou ske b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "shoske",
    ( 0, 0 ), "i/sprites/shou/overlays/blush/3.png",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )    
    
image shou smi b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "shosmi",
    ( 0, 0 ), "i/sprites/shou/overlays/blush/3.png",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )    
    
image shou sur b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "shosur",
    ( 0, 0 ), "i/sprites/shou/overlays/blush/3.png",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )        
    
image shou thi b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "shothi",
    ( 0, 0 ), "i/sprites/shou/overlays/blush/3.png",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )       
    
image shou win b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "showin",
    ( 0, 0 ), "i/sprites/shou/overlays/blush/3.png",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )      

image shou wor b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "shohairback",
    ( 0, 0 ), "i/sprites/shou/outfits/base.png",
    ( 0, 0 ), "shooutfits",
    ( 0, 0 ), "showor",
    ( 0, 0 ), "i/sprites/shou/overlays/blush/3.png",
    ( 0, 0 ), "shohairfront",
    ( 0, 0 ), "shoAccessoryTop",
    ( 0, 0 ), "shoAccessoryMiddle",
    ( 0 , 0), "shoAccessoryBottom"
    )    
    

    
########## ~ shou EXPRESSIONS ~ ##########

image shoang:
    "i/sprites/shou/expressions/angry/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/shou/expressions/angry/2.png"
    .05
    "i/sprites/shou/expressions/angry/3.png"
    .05
    "i/sprites/shou/expressions/angry/4.png"
    .05
    "i/sprites/shou/expressions/angry/3.png"
    .05
    "i/sprites/shou/expressions/angry/2.png"
    .05
    repeat

    
image shoann:
    "i/sprites/shou/expressions/annoyed/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/shou/expressions/annoyed/2.png"
    .05
    "i/sprites/shou/expressions/annoyed/3.png"
    .05
    "i/sprites/shou/expressions/annoyed/4.png"
    .05
    "i/sprites/shou/expressions/annoyed/3.png"
    .05
    "i/sprites/shou/expressions/annoyed/2.png"
    .05
    repeat
    
    
image shocur:
    "i/sprites/shou/expressions/curious/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/shou/expressions/curious/2.png"
    .05
    "i/sprites/shou/expressions/curious/3.png"
    .05
    "i/sprites/shou/expressions/curious/4.png"
    .05
    "i/sprites/shou/expressions/curious/3.png"
    .05
    "i/sprites/shou/expressions/curious/2.png"
    .05
    repeat
    
    
image shodis:
    "i/sprites/shou/expressions/disappointed/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/shou/expressions/disappointed/2.png"
    .05
    "i/sprites/shou/expressions/disappointed/3.png"
    .05
    "i/sprites/shou/expressions/disappointed/4.png"
    .05
    "i/sprites/shou/expressions/disappointed/3.png"
    .05
    "i/sprites/shou/expressions/disappointed/2.png"
    .05
    repeat
    
    
image shohap:
    "i/sprites/shou/expressions/happy/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/shou/expressions/happy/2.png"
    .05
    "i/sprites/shou/expressions/happy/3.png"
    .05
    "i/sprites/shou/expressions/happy/4.png"
    .05
    "i/sprites/shou/expressions/happy/3.png"
    .05
    "i/sprites/shou/expressions/happy/2.png"
    .05
    repeat
    
    
image shomis:
    "i/sprites/shou/expressions/mischievous/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/shou/expressions/mischievous/2.png"
    .05
    "i/sprites/shou/expressions/mischievous/3.png"
    .05
    "i/sprites/shou/expressions/mischievous/4.png"
    .05
    "i/sprites/shou/expressions/mischievous/3.png"
    .05
    "i/sprites/shou/expressions/mischievous/2.png"
    .05
    repeat
    
    
image shoner:
    "i/sprites/shou/expressions/nervous/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/shou/expressions/nervous/2.png"
    .05
    "i/sprites/shou/expressions/nervous/3.png"
    .05
    "i/sprites/shou/expressions/nervous/4.png"
    .05
    "i/sprites/shou/expressions/nervous/3.png"
    .05
    "i/sprites/shou/expressions/nervous/2.png"
    .05
    repeat
    
    
image shoneu:
    "i/sprites/shou/expressions/neutral/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/shou/expressions/neutral/2.png"
    .05
    "i/sprites/shou/expressions/neutral/3.png"
    .05
    "i/sprites/shou/expressions/neutral/4.png"
    .05
    "i/sprites/shou/expressions/neutral/3.png"
    .05
    "i/sprites/shou/expressions/neutral/2.png"
    .05
    repeat
    
    
image shosad:
    "i/sprites/shou/expressions/sad/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/shou/expressions/sad/2.png"
    .05
    "i/sprites/shou/expressions/sad/3.png"
    .05
    "i/sprites/shou/expressions/sad/4.png"
    .05
    "i/sprites/shou/expressions/sad/3.png"
    .05
    "i/sprites/shou/expressions/sad/2.png"
    .05
    repeat
    
    
image shoske:
    "i/sprites/shou/expressions/skeptical/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/shou/expressions/skeptical/2.png"
    .05
    "i/sprites/shou/expressions/skeptical/3.png"
    .05
    "i/sprites/shou/expressions/skeptical/4.png"
    .05
    "i/sprites/shou/expressions/skeptical/3.png"
    .05
    "i/sprites/shou/expressions/skeptical/2.png"
    .05
    repeat
    
    
image shosmi:
    "i/sprites/shou/expressions/smiling/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/shou/expressions/smiling/2.png"
    .05
    "i/sprites/shou/expressions/smiling/3.png"
    .05
    "i/sprites/shou/expressions/smiling/4.png"
    .05
    "i/sprites/shou/expressions/smiling/3.png"
    .05
    "i/sprites/shou/expressions/smiling/2.png"
    .05
    repeat
    
    
image shosur:
    "i/sprites/shou/expressions/surprised/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/shou/expressions/surprised/2.png"
    .05
    "i/sprites/shou/expressions/surprised/3.png"
    .05
    "i/sprites/shou/expressions/surprised/4.png"
    .05
    "i/sprites/shou/expressions/surprised/3.png"
    .05
    "i/sprites/shou/expressions/surprised/2.png"
    .05
    repeat
    
    
image shothi:
    "i/sprites/shou/expressions/thinking/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/shou/expressions/thinking/2.png"
    .05
    "i/sprites/shou/expressions/thinking/3.png"
    .05
    "i/sprites/shou/expressions/thinking/4.png"
    .05
    "i/sprites/shou/expressions/thinking/3.png"
    .05
    "i/sprites/shou/expressions/thinking/2.png"
    .05
    repeat
    
    
image showin:
    "i/sprites/shou/expressions/wincing/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/shou/expressions/wincing/2.png"
    .05
    "i/sprites/shou/expressions/wincing/3.png"
    .05
    "i/sprites/shou/expressions/wincing/4.png"
    .05
    "i/sprites/shou/expressions/wincing/3.png"
    .05
    "i/sprites/shou/expressions/wincing/2.png"
    .05
    repeat
    
    
image showor:
    "i/sprites/shou/expressions/worried/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/shou/expressions/worried/2.png"
    .05
    "i/sprites/shou/expressions/worried/3.png"
    .05
    "i/sprites/shou/expressions/worried/4.png"
    .05
    "i/sprites/shou/expressions/worried/3.png"
    .05
    "i/sprites/shou/expressions/worried/2.png"
    .05
    repeat