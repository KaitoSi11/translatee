########## ~ akira CONDITIONSWITCHES ~ ##########
    
image akihairback = ConditionSwitch (
        "akiHairB == 'default'", "i/sprites/akira/hairstyles/default/back.png"
        )
        
image akioutfits = ConditionSwitch (
        "akiOut == 'hotspring'", "i/sprites/akira/outfits/hotspring.png",
        "akiOut == 'sUniform'", "i/sprites/akira/outfits/summer - uniform.png",
        "akiOut == 'sSwimsuit'", "i/sprites/akira/outfits/summer - swimsuit.png"
        )
        
image akihairfront = ConditionSwitch (
        "akiHairF == 'default'", "i/sprites/akira/hairstyles/default/front.png"
        )

image akiAccessoryTop = ConditionSwitch (
        "akiAccT == 'emptyimage'", "i/sprites/empty.png"
        )
        
image akiAccessoryMiddle = ConditionSwitch (
        "akiAccM == 'emptyimage'", "i/sprites/empty.png"
        )
        
image akiAccessoryBottom = ConditionSwitch (
        "akiAccB == 'emptyimage'", "i/sprites/empty.png"
        )
    
    

########## ~ akira LIVECOMPOSITE ~ ##########

image akira ang = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akiang",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )

image akira ann = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akiann",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )

image akira cur = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akicur",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )

image akira dis = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akidis",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )
    
image akira hap = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akihap",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )   
    
image akira mis = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akimis",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )    
 
image akira ner = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akiner",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    ) 
    
image akira neu = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akineu",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )   
    
image akira sad = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akisad",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )   
    
image akira ske = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akiske",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )    
    
image akira smi = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akismi",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )    
    
image akira sur = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akisur",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )        
    
image akira thi = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akithi",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )       
    
image akira win = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akiwin",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )      

image akira wor = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akiwor",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )    
  
image akira ang b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akiang",
    ( 0, 0 ), "i/sprites/akira/overlays/blush/1.png",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )

image akira ann b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akiann",
    ( 0, 0 ), "i/sprites/akira/overlays/blush/1.png",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )

image akira cur b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akicur",
    ( 0, 0 ), "i/sprites/akira/overlays/blush/1.png",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )

image akira dis b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akidis",
    ( 0, 0 ), "i/sprites/akira/overlays/blush/1.png",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )
    
image akira hap b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akihap",
    ( 0, 0 ), "i/sprites/akira/overlays/blush/1.png",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )   
    
image akira mis b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akimis",
    ( 0, 0 ), "i/sprites/akira/overlays/blush/1.png",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )    
 
image akira ner b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akiner",
    ( 0, 0 ), "i/sprites/akira/overlays/blush/1.png",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    ) 
    
image akira neu b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akineu",
    ( 0, 0 ), "i/sprites/akira/overlays/blush/1.png",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )   
    
image akira sad b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akisad",
    ( 0, 0 ), "i/sprites/akira/overlays/blush/1.png",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )   
    
image akira ske b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akiske",
    ( 0, 0 ), "i/sprites/akira/overlays/blush/1.png",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )    
    
image akira smi b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akismi",
    ( 0, 0 ), "i/sprites/akira/overlays/blush/1.png",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )    
    
image akira sur b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akisur",
    ( 0, 0 ), "i/sprites/akira/overlays/blush/1.png",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )        
    
image akira thi b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akithi",
    ( 0, 0 ), "i/sprites/akira/overlays/blush/1.png",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )       
    
image akira win b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akiwin",
    ( 0, 0 ), "i/sprites/akira/overlays/blush/1.png",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )      

image akira wor b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akiwor",
    ( 0, 0 ), "i/sprites/akira/overlays/blush/1.png",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )     
    
image akira ang b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akiang",
    ( 0, 0 ), "i/sprites/akira/overlays/blush/2.png",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )

image akira ann b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akiann",
    ( 0, 0 ), "i/sprites/akira/overlays/blush/2.png",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )

image akira cur b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akicur",
    ( 0, 0 ), "i/sprites/akira/overlays/blush/2.png",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )

image akira dis b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akidis",
    ( 0, 0 ), "i/sprites/akira/overlays/blush/2.png",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )
    
image akira hap b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akihap",
    ( 0, 0 ), "i/sprites/akira/overlays/blush/2.png",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )   
    
image akira mis b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akimis",
    ( 0, 0 ), "i/sprites/akira/overlays/blush/2.png",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )    
 
image akira ner b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akiner",
    ( 0, 0 ), "i/sprites/akira/overlays/blush/2.png",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    ) 
    
image akira neu b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akineu",
    ( 0, 0 ), "i/sprites/akira/overlays/blush/2.png",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )   
    
image akira sad b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akisad",
    ( 0, 0 ), "i/sprites/akira/overlays/blush/2.png",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )   
    
image akira ske b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akiske",
    ( 0, 0 ), "i/sprites/akira/overlays/blush/2.png",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )    
    
image akira smi b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akismi",
    ( 0, 0 ), "i/sprites/akira/overlays/blush/2.png",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )    
    
image akira sur b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akisur",
    ( 0, 0 ), "i/sprites/akira/overlays/blush/2.png",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )        
    
image akira thi b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akithi",
    ( 0, 0 ), "i/sprites/akira/overlays/blush/2.png",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )       
    
image akira win b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akiwin",
    ( 0, 0 ), "i/sprites/akira/overlays/blush/2.png",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )      

image akira wor b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akiwor",
    ( 0, 0 ), "i/sprites/akira/overlays/blush/2.png",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )     

image akira ang b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akiang",
    ( 0, 0 ), "i/sprites/akira/overlays/blush/3.png",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )

image akira ann b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akiann",
    ( 0, 0 ), "i/sprites/akira/overlays/blush/3.png",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )

image akira cur b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akicur",
    ( 0, 0 ), "i/sprites/akira/overlays/blush/3.png",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )

image akira dis b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akidis",
    ( 0, 0 ), "i/sprites/akira/overlays/blush/3.png",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )
    
image akira hap b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akihap",
    ( 0, 0 ), "i/sprites/akira/overlays/blush/3.png",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )   
    
image akira mis b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akimis",
    ( 0, 0 ), "i/sprites/akira/overlays/blush/3.png",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )    
 
image akira ner b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akiner",
    ( 0, 0 ), "i/sprites/akira/overlays/blush/3.png",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    ) 
    
image akira neu b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akineu",
    ( 0, 0 ), "i/sprites/akira/overlays/blush/3.png",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )   
    
image akira sad b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akisad",
    ( 0, 0 ), "i/sprites/akira/overlays/blush/3.png",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )   
    
image akira ske b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akiske",
    ( 0, 0 ), "i/sprites/akira/overlays/blush/3.png",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )    
    
image akira smi b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akismi",
    ( 0, 0 ), "i/sprites/akira/overlays/blush/3.png",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )    
    
image akira sur b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akisur",
    ( 0, 0 ), "i/sprites/akira/overlays/blush/3.png",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )        
    
image akira thi b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akithi",
    ( 0, 0 ), "i/sprites/akira/overlays/blush/3.png",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )       
    
image akira win b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akiwin",
    ( 0, 0 ), "i/sprites/akira/overlays/blush/3.png",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )      

image akira wor b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "akihairback",
    ( 0, 0 ), "i/sprites/akira/outfits/base.png",
    ( 0, 0 ), "akioutfits",
    ( 0, 0 ), "akiwor",
    ( 0, 0 ), "i/sprites/akira/overlays/blush/3.png",
    ( 0, 0 ), "akihairfront",
    ( 0, 0 ), "akiAccessoryTop",
    ( 0, 0 ), "akiAccessoryMiddle",
    ( 0 , 0), "akiAccessoryBottom"
    )    
    

    
########## ~ akira EXPRESSIONS ~ ##########

image akiang:
    "i/sprites/akira/expressions/angry/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/akira/expressions/angry/2.png"
    .05
    "i/sprites/akira/expressions/angry/3.png"
    .05
    "i/sprites/akira/expressions/angry/4.png"
    .05
    "i/sprites/akira/expressions/angry/3.png"
    .05
    "i/sprites/akira/expressions/angry/2.png"
    .05
    repeat

    
image akiann:
    "i/sprites/akira/expressions/annoyed/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/akira/expressions/annoyed/2.png"
    .05
    "i/sprites/akira/expressions/annoyed/3.png"
    .05
    "i/sprites/akira/expressions/annoyed/4.png"
    .05
    "i/sprites/akira/expressions/annoyed/3.png"
    .05
    "i/sprites/akira/expressions/annoyed/2.png"
    .05
    repeat
    
    
image akicur:
    "i/sprites/akira/expressions/curious/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/akira/expressions/curious/2.png"
    .05
    "i/sprites/akira/expressions/curious/3.png"
    .05
    "i/sprites/akira/expressions/curious/4.png"
    .05
    "i/sprites/akira/expressions/curious/3.png"
    .05
    "i/sprites/akira/expressions/curious/2.png"
    .05
    repeat
    
    
image akidis:
    "i/sprites/akira/expressions/disappointed/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/akira/expressions/disappointed/2.png"
    .05
    "i/sprites/akira/expressions/disappointed/3.png"
    .05
    "i/sprites/akira/expressions/disappointed/4.png"
    .05
    "i/sprites/akira/expressions/disappointed/3.png"
    .05
    "i/sprites/akira/expressions/disappointed/2.png"
    .05
    repeat
    
    
image akihap:
    "i/sprites/akira/expressions/happy/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/akira/expressions/happy/2.png"
    .05
    "i/sprites/akira/expressions/happy/3.png"
    .05
    "i/sprites/akira/expressions/happy/4.png"
    .05
    "i/sprites/akira/expressions/happy/3.png"
    .05
    "i/sprites/akira/expressions/happy/2.png"
    .05
    repeat
    
    
image akimis:
    "i/sprites/akira/expressions/mischievous/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/akira/expressions/mischievous/2.png"
    .05
    "i/sprites/akira/expressions/mischievous/3.png"
    .05
    "i/sprites/akira/expressions/mischievous/4.png"
    .05
    "i/sprites/akira/expressions/mischievous/3.png"
    .05
    "i/sprites/akira/expressions/mischievous/2.png"
    .05
    repeat
    
    
image akiner:
    "i/sprites/akira/expressions/nervous/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/akira/expressions/nervous/2.png"
    .05
    "i/sprites/akira/expressions/nervous/3.png"
    .05
    "i/sprites/akira/expressions/nervous/4.png"
    .05
    "i/sprites/akira/expressions/nervous/3.png"
    .05
    "i/sprites/akira/expressions/nervous/2.png"
    .05
    repeat
    
    
image akineu:
    "i/sprites/akira/expressions/neutral/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/akira/expressions/neutral/2.png"
    .05
    "i/sprites/akira/expressions/neutral/3.png"
    .05
    "i/sprites/akira/expressions/neutral/4.png"
    .05
    "i/sprites/akira/expressions/neutral/3.png"
    .05
    "i/sprites/akira/expressions/neutral/2.png"
    .05
    repeat
    
    
image akisad:
    "i/sprites/akira/expressions/sad/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/akira/expressions/sad/2.png"
    .05
    "i/sprites/akira/expressions/sad/3.png"
    .05
    "i/sprites/akira/expressions/sad/4.png"
    .05
    "i/sprites/akira/expressions/sad/3.png"
    .05
    "i/sprites/akira/expressions/sad/2.png"
    .05
    repeat
    
    
image akiske:
    "i/sprites/akira/expressions/skeptical/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/akira/expressions/skeptical/2.png"
    .05
    "i/sprites/akira/expressions/skeptical/3.png"
    .05
    "i/sprites/akira/expressions/skeptical/4.png"
    .05
    "i/sprites/akira/expressions/skeptical/3.png"
    .05
    "i/sprites/akira/expressions/skeptical/2.png"
    .05
    repeat
    
    
image akismi:
    "i/sprites/akira/expressions/smiling/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/akira/expressions/smiling/2.png"
    .05
    "i/sprites/akira/expressions/smiling/3.png"
    .05
    "i/sprites/akira/expressions/smiling/4.png"
    .05
    "i/sprites/akira/expressions/smiling/3.png"
    .05
    "i/sprites/akira/expressions/smiling/2.png"
    .05
    repeat
    
    
image akisur:
    "i/sprites/akira/expressions/surprised/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/akira/expressions/surprised/2.png"
    .05
    "i/sprites/akira/expressions/surprised/3.png"
    .05
    "i/sprites/akira/expressions/surprised/4.png"
    .05
    "i/sprites/akira/expressions/surprised/3.png"
    .05
    "i/sprites/akira/expressions/surprised/2.png"
    .05
    repeat
    
    
image akithi:
    "i/sprites/akira/expressions/thinking/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/akira/expressions/thinking/2.png"
    .05
    "i/sprites/akira/expressions/thinking/3.png"
    .05
    "i/sprites/akira/expressions/thinking/4.png"
    .05
    "i/sprites/akira/expressions/thinking/3.png"
    .05
    "i/sprites/akira/expressions/thinking/2.png"
    .05
    repeat
    
    
image akiwin:
    "i/sprites/akira/expressions/wincing/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/akira/expressions/wincing/2.png"
    .05
    "i/sprites/akira/expressions/wincing/3.png"
    .05
    "i/sprites/akira/expressions/wincing/4.png"
    .05
    "i/sprites/akira/expressions/wincing/3.png"
    .05
    "i/sprites/akira/expressions/wincing/2.png"
    .05
    repeat
    
    
image akiwor:
    "i/sprites/akira/expressions/worried/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/akira/expressions/worried/2.png"
    .05
    "i/sprites/akira/expressions/worried/3.png"
    .05
    "i/sprites/akira/expressions/worried/4.png"
    .05
    "i/sprites/akira/expressions/worried/3.png"
    .05
    "i/sprites/akira/expressions/worried/2.png"
    .05
    repeat