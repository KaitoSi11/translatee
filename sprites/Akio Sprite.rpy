########## ~ akio CONDITIONSWITCHES ~ ##########
    
image akshairback = ConditionSwitch (
        "aksHairB == 'default'", "i/sprites/akio/hairstyles/default/back.png"
        )
        
image aksoutfits = ConditionSwitch (
        "aksOut == 'default'", "i/sprites/akio/outfits/default.png"
        )
        
image akshairfront = ConditionSwitch (
        "aksHairF == 'default'", "i/sprites/akio/hairstyles/default/front.png"
        )

image aksAccessoryTop = ConditionSwitch (
        "aksAccT == 'Glasses'", "i/sprites/akio/accessories/glasses.png",
        "aksAccT == 'emptyimage'", "i/sprites/empty.png"
        )
        
image aksAccessoryMiddle = ConditionSwitch (
        "aksAccM == 'emptyimage'", "i/sprites/empty.png"
        )
        
image aksAccessoryBottom = ConditionSwitch (
        "aksAccB == 'emptyimage'", "i/sprites/empty.png"
        )
    
    

########## ~ akio LIVECOMPOSITE ~ ##########

image akio ang = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "aksang",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )

image akio ann = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "aksann",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )

image akio cur = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "akscur",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )

image akio dis = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "aksdis",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )
    
image akio hap = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "akshap",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )   
    
image akio mis = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "aksmis",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )    
 
image akio ner = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "aksner",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    ) 
    
image akio neu = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "aksneu",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )   
    
image akio sad = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "akssad",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )   
    
image akio ske = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "aksske",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )    
    
image akio smi = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "akssmi",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )    
    
image akio sur = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "akssur",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )        
    
image akio thi = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "aksthi",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )       
    
image akio win = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "akswin",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )      

image akio wor = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "akswor",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )    
  
image akio ang b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "aksang",
    ( 0, 0 ), "i/sprites/akio/overlays/blush/1.png",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )

image akio ann b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "aksann",
    ( 0, 0 ), "i/sprites/akio/overlays/blush/1.png",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )

image akio cur b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "akscur",
    ( 0, 0 ), "i/sprites/akio/overlays/blush/1.png",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )

image akio dis b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "aksdis",
    ( 0, 0 ), "i/sprites/akio/overlays/blush/1.png",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )
    
image akio hap b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "akshap",
    ( 0, 0 ), "i/sprites/akio/overlays/blush/1.png",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )   
    
image akio mis b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "aksmis",
    ( 0, 0 ), "i/sprites/akio/overlays/blush/1.png",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )    
 
image akio ner b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "aksner",
    ( 0, 0 ), "i/sprites/akio/overlays/blush/1.png",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    ) 
    
image akio neu b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "aksneu",
    ( 0, 0 ), "i/sprites/akio/overlays/blush/1.png",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )   
    
image akio sad b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "akssad",
    ( 0, 0 ), "i/sprites/akio/overlays/blush/1.png",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )   
    
image akio ske b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "aksske",
    ( 0, 0 ), "i/sprites/akio/overlays/blush/1.png",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )    
    
image akio smi b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "akssmi",
    ( 0, 0 ), "i/sprites/akio/overlays/blush/1.png",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )    
    
image akio sur b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "akssur",
    ( 0, 0 ), "i/sprites/akio/overlays/blush/1.png",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )        
    
image akio thi b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "aksthi",
    ( 0, 0 ), "i/sprites/akio/overlays/blush/1.png",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )       
    
image akio win b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "akswin",
    ( 0, 0 ), "i/sprites/akio/overlays/blush/1.png",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )      

image akio wor b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "akswor",
    ( 0, 0 ), "i/sprites/akio/overlays/blush/1.png",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )     
    
image akio ang b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "aksang",
    ( 0, 0 ), "i/sprites/akio/overlays/blush/2.png",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )

image akio ann b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "aksann",
    ( 0, 0 ), "i/sprites/akio/overlays/blush/2.png",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )

image akio cur b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "akscur",
    ( 0, 0 ), "i/sprites/akio/overlays/blush/2.png",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )

image akio dis b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "aksdis",
    ( 0, 0 ), "i/sprites/akio/overlays/blush/2.png",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )
    
image akio hap b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "akshap",
    ( 0, 0 ), "i/sprites/akio/overlays/blush/2.png",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )   
    
image akio mis b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "aksmis",
    ( 0, 0 ), "i/sprites/akio/overlays/blush/2.png",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )    
 
image akio ner b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "aksner",
    ( 0, 0 ), "i/sprites/akio/overlays/blush/2.png",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    ) 
    
image akio neu b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "aksneu",
    ( 0, 0 ), "i/sprites/akio/overlays/blush/2.png",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )   
    
image akio sad b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "akssad",
    ( 0, 0 ), "i/sprites/akio/overlays/blush/2.png",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )   
    
image akio ske b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "aksske",
    ( 0, 0 ), "i/sprites/akio/overlays/blush/2.png",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )    
    
image akio smi b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "akssmi",
    ( 0, 0 ), "i/sprites/akio/overlays/blush/2.png",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )    
    
image akio sur b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "akssur",
    ( 0, 0 ), "i/sprites/akio/overlays/blush/2.png",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )        
    
image akio thi b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "aksthi",
    ( 0, 0 ), "i/sprites/akio/overlays/blush/2.png",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )       
    
image akio win b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "akswin",
    ( 0, 0 ), "i/sprites/akio/overlays/blush/2.png",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )      

image akio wor b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "akswor",
    ( 0, 0 ), "i/sprites/akio/overlays/blush/2.png",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )     

image akio ang b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "aksang",
    ( 0, 0 ), "i/sprites/akio/overlays/blush/3.png",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )

image akio ann b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "aksann",
    ( 0, 0 ), "i/sprites/akio/overlays/blush/3.png",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )

image akio cur b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "akscur",
    ( 0, 0 ), "i/sprites/akio/overlays/blush/3.png",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )

image akio dis b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "aksdis",
    ( 0, 0 ), "i/sprites/akio/overlays/blush/3.png",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )
    
image akio hap b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "akshap",
    ( 0, 0 ), "i/sprites/akio/overlays/blush/3.png",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )   
    
image akio mis b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "aksmis",
    ( 0, 0 ), "i/sprites/akio/overlays/blush/3.png",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )    
 
image akio ner b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "aksner",
    ( 0, 0 ), "i/sprites/akio/overlays/blush/3.png",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    ) 
    
image akio neu b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "aksneu",
    ( 0, 0 ), "i/sprites/akio/overlays/blush/3.png",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )   
    
image akio sad b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "akssad",
    ( 0, 0 ), "i/sprites/akio/overlays/blush/3.png",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )   
    
image akio ske b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "aksske",
    ( 0, 0 ), "i/sprites/akio/overlays/blush/3.png",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )    
    
image akio smi b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "akssmi",
    ( 0, 0 ), "i/sprites/akio/overlays/blush/3.png",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )    
    
image akio sur b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "akssur",
    ( 0, 0 ), "i/sprites/akio/overlays/blush/3.png",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )        
    
image akio thi b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "aksthi",
    ( 0, 0 ), "i/sprites/akio/overlays/blush/3.png",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )       
    
image akio win b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "akswin",
    ( 0, 0 ), "i/sprites/akio/overlays/blush/3.png",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )      

image akio wor b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akshairback",
    ( 0, 0 ), "i/sprites/akio/outfits/base.png",
    ( 0, 0 ), "aksoutfits",
    ( 0, 0 ), "akswor",
    ( 0, 0 ), "i/sprites/akio/overlays/blush/3.png",
    ( 0, 0 ), "akshairfront",
    ( 0, 0 ), "aksAccessoryTop",
    ( 0, 0 ), "aksAccessoryMiddle",
    ( 0 , 0), "aksAccessoryBottom"
    )    
    

    
########## ~ akio EXPRESSIONS ~ ##########

image aksang:
    "i/sprites/akio/expressions/angry/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/akio/expressions/angry/2.png"
    .05
    "i/sprites/akio/expressions/angry/3.png"
    .05
    "i/sprites/akio/expressions/angry/4.png"
    .05
    "i/sprites/akio/expressions/angry/3.png"
    .05
    "i/sprites/akio/expressions/angry/2.png"
    .05
    repeat

    
image aksann:
    "i/sprites/akio/expressions/annoyed/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/akio/expressions/annoyed/2.png"
    .05
    "i/sprites/akio/expressions/annoyed/3.png"
    .05
    "i/sprites/akio/expressions/annoyed/4.png"
    .05
    "i/sprites/akio/expressions/annoyed/3.png"
    .05
    "i/sprites/akio/expressions/annoyed/2.png"
    .05
    repeat
    
    
image akscur:
    "i/sprites/akio/expressions/curious/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/akio/expressions/curious/2.png"
    .05
    "i/sprites/akio/expressions/curious/3.png"
    .05
    "i/sprites/akio/expressions/curious/4.png"
    .05
    "i/sprites/akio/expressions/curious/3.png"
    .05
    "i/sprites/akio/expressions/curious/2.png"
    .05
    repeat
    
    
image aksdis:
    "i/sprites/akio/expressions/disappointed/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/akio/expressions/disappointed/2.png"
    .05
    "i/sprites/akio/expressions/disappointed/3.png"
    .05
    "i/sprites/akio/expressions/disappointed/4.png"
    .05
    "i/sprites/akio/expressions/disappointed/3.png"
    .05
    "i/sprites/akio/expressions/disappointed/2.png"
    .05
    repeat
    
    
image akshap:
    "i/sprites/akio/expressions/happy/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/akio/expressions/happy/2.png"
    .05
    "i/sprites/akio/expressions/happy/3.png"
    .05
    "i/sprites/akio/expressions/happy/4.png"
    .05
    "i/sprites/akio/expressions/happy/3.png"
    .05
    "i/sprites/akio/expressions/happy/2.png"
    .05
    repeat
    
    
image aksmis:
    "i/sprites/akio/expressions/mischievous/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/akio/expressions/mischievous/2.png"
    .05
    "i/sprites/akio/expressions/mischievous/3.png"
    .05
    "i/sprites/akio/expressions/mischievous/4.png"
    .05
    "i/sprites/akio/expressions/mischievous/3.png"
    .05
    "i/sprites/akio/expressions/mischievous/2.png"
    .05
    repeat
    
    
image aksner:
    "i/sprites/akio/expressions/nervous/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/akio/expressions/nervous/2.png"
    .05
    "i/sprites/akio/expressions/nervous/3.png"
    .05
    "i/sprites/akio/expressions/nervous/4.png"
    .05
    "i/sprites/akio/expressions/nervous/3.png"
    .05
    "i/sprites/akio/expressions/nervous/2.png"
    .05
    repeat
    
    
image aksneu:
    "i/sprites/akio/expressions/neutral/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/akio/expressions/neutral/2.png"
    .05
    "i/sprites/akio/expressions/neutral/3.png"
    .05
    "i/sprites/akio/expressions/neutral/4.png"
    .05
    "i/sprites/akio/expressions/neutral/3.png"
    .05
    "i/sprites/akio/expressions/neutral/2.png"
    .05
    repeat
    
    
image akssad:
    "i/sprites/akio/expressions/sad/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/akio/expressions/sad/2.png"
    .05
    "i/sprites/akio/expressions/sad/3.png"
    .05
    "i/sprites/akio/expressions/sad/4.png"
    .05
    "i/sprites/akio/expressions/sad/3.png"
    .05
    "i/sprites/akio/expressions/sad/2.png"
    .05
    repeat
    
    
image aksske:
    "i/sprites/akio/expressions/skeptical/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/akio/expressions/skeptical/2.png"
    .05
    "i/sprites/akio/expressions/skeptical/3.png"
    .05
    "i/sprites/akio/expressions/skeptical/4.png"
    .05
    "i/sprites/akio/expressions/skeptical/3.png"
    .05
    "i/sprites/akio/expressions/skeptical/2.png"
    .05
    repeat
    
    
image akssmi:
    "i/sprites/akio/expressions/smiling/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/akio/expressions/smiling/2.png"
    .05
    "i/sprites/akio/expressions/smiling/3.png"
    .05
    "i/sprites/akio/expressions/smiling/4.png"
    .05
    "i/sprites/akio/expressions/smiling/3.png"
    .05
    "i/sprites/akio/expressions/smiling/2.png"
    .05
    repeat
    
    
image akssur:
    "i/sprites/akio/expressions/surprised/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/akio/expressions/surprised/2.png"
    .05
    "i/sprites/akio/expressions/surprised/3.png"
    .05
    "i/sprites/akio/expressions/surprised/4.png"
    .05
    "i/sprites/akio/expressions/surprised/3.png"
    .05
    "i/sprites/akio/expressions/surprised/2.png"
    .05
    repeat
    
    
image aksthi:
    "i/sprites/akio/expressions/thinking/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/akio/expressions/thinking/2.png"
    .05
    "i/sprites/akio/expressions/thinking/3.png"
    .05
    "i/sprites/akio/expressions/thinking/4.png"
    .05
    "i/sprites/akio/expressions/thinking/3.png"
    .05
    "i/sprites/akio/expressions/thinking/2.png"
    .05
    repeat
    
    
image akswin:
    "i/sprites/akio/expressions/wincing/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/akio/expressions/wincing/2.png"
    .05
    "i/sprites/akio/expressions/wincing/3.png"
    .05
    "i/sprites/akio/expressions/wincing/4.png"
    .05
    "i/sprites/akio/expressions/wincing/3.png"
    .05
    "i/sprites/akio/expressions/wincing/2.png"
    .05
    repeat
    
    
image akswor:
    "i/sprites/akio/expressions/worried/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/akio/expressions/worried/2.png"
    .05
    "i/sprites/akio/expressions/worried/3.png"
    .05
    "i/sprites/akio/expressions/worried/4.png"
    .05
    "i/sprites/akio/expressions/worried/3.png"
    .05
    "i/sprites/akio/expressions/worried/2.png"
    .05
    repeat