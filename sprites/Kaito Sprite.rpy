########## ~ kaito CONDITIONSWITCHES ~ ##########
    
image kaihairback = ConditionSwitch (
        "kaiHairB == 'default'", "i/sprites/kaito/hairstyles/default/back.png"
        )
        
image kaioutfits = ConditionSwitch (
        "kaiOut == 'sCasual'", "i/sprites/kaito/outfits/summer - casual.png",
        "kaiOut == 'sWork'", "i/sprites/kaito/outfits/summer - work.png"
        )
        
image kaihairfront = ConditionSwitch (
        "kaiHairF == 'default'", "i/sprites/kaito/hairstyles/default/front.png"
        )

image kaiAccessoryTop = ConditionSwitch (
        "kaiAccT == 'emptyimage'", "i/sprites/empty.png"
        )
        
image kaiAccessoryMiddle = ConditionSwitch (
        "kaiAccM == 'emptyimage'", "i/sprites/empty.png"
        )
        
image kaiAccessoryBottom = ConditionSwitch (
        "kaiAccB == 'emptyimage'", "i/sprites/empty.png"
        )
    
    

########## ~ kaito LIVECOMPOSITE ~ ##########

image kaito ang = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaiang",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )

image kaito ann = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaiann",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )

image kaito cur = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaicur",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )

image kaito dis = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaidis",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )
    
image kaito hap = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaihap",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )   
    
image kaito mis = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaimis",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )    
 
image kaito ner = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kainer",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    ) 
    
image kaito neu = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaineu",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )   
    
image kaito sad = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaisad",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )   
    
image kaito ske = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaiske",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )    
    
image kaito smi = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaismi",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )    
    
image kaito sur = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaisur",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )        
    
image kaito thi = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaithi",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )       
    
image kaito win = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaiwin",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )      

image kaito wor = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaiwor",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )    
  
image kaito ang b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaiang",
    ( 0, 0 ), "i/sprites/kaito/overlays/blush/1.png",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )

image kaito ann b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaiann",
    ( 0, 0 ), "i/sprites/kaito/overlays/blush/1.png",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )

image kaito cur b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaicur",
    ( 0, 0 ), "i/sprites/kaito/overlays/blush/1.png",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )

image kaito dis b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaidis",
    ( 0, 0 ), "i/sprites/kaito/overlays/blush/1.png",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )
    
image kaito hap b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaihap",
    ( 0, 0 ), "i/sprites/kaito/overlays/blush/1.png",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )   
    
image kaito mis b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaimis",
    ( 0, 0 ), "i/sprites/kaito/overlays/blush/1.png",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )    
 
image kaito ner b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kainer",
    ( 0, 0 ), "i/sprites/kaito/overlays/blush/1.png",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    ) 
    
image kaito neu b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaineu",
    ( 0, 0 ), "i/sprites/kaito/overlays/blush/1.png",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )   
    
image kaito sad b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaisad",
    ( 0, 0 ), "i/sprites/kaito/overlays/blush/1.png",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )   
    
image kaito ske b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaiske",
    ( 0, 0 ), "i/sprites/kaito/overlays/blush/1.png",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )    
    
image kaito smi b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaismi",
    ( 0, 0 ), "i/sprites/kaito/overlays/blush/1.png",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )    
    
image kaito sur b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaisur",
    ( 0, 0 ), "i/sprites/kaito/overlays/blush/1.png",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )        
    
image kaito thi b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaithi",
    ( 0, 0 ), "i/sprites/kaito/overlays/blush/1.png",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )       
    
image kaito win b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaiwin",
    ( 0, 0 ), "i/sprites/kaito/overlays/blush/1.png",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )      

image kaito wor b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaiwor",
    ( 0, 0 ), "i/sprites/kaito/overlays/blush/1.png",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )     
    
image kaito ang b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaiang",
    ( 0, 0 ), "i/sprites/kaito/overlays/blush/2.png",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )

image kaito ann b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaiann",
    ( 0, 0 ), "i/sprites/kaito/overlays/blush/2.png",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )

image kaito cur b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaicur",
    ( 0, 0 ), "i/sprites/kaito/overlays/blush/2.png",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )

image kaito dis b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaidis",
    ( 0, 0 ), "i/sprites/kaito/overlays/blush/2.png",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )
    
image kaito hap b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaihap",
    ( 0, 0 ), "i/sprites/kaito/overlays/blush/2.png",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )   
    
image kaito mis b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaimis",
    ( 0, 0 ), "i/sprites/kaito/overlays/blush/2.png",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )    
 
image kaito ner b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kainer",
    ( 0, 0 ), "i/sprites/kaito/overlays/blush/2.png",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    ) 
    
image kaito neu b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaineu",
    ( 0, 0 ), "i/sprites/kaito/overlays/blush/2.png",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )   
    
image kaito sad b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaisad",
    ( 0, 0 ), "i/sprites/kaito/overlays/blush/2.png",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )   
    
image kaito ske b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaiske",
    ( 0, 0 ), "i/sprites/kaito/overlays/blush/2.png",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )    
    
image kaito smi b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaismi",
    ( 0, 0 ), "i/sprites/kaito/overlays/blush/2.png",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )    
    
image kaito sur b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaisur",
    ( 0, 0 ), "i/sprites/kaito/overlays/blush/2.png",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )        
    
image kaito thi b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaithi",
    ( 0, 0 ), "i/sprites/kaito/overlays/blush/2.png",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )       
    
image kaito win b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaiwin",
    ( 0, 0 ), "i/sprites/kaito/overlays/blush/2.png",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )      

image kaito wor b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaiwor",
    ( 0, 0 ), "i/sprites/kaito/overlays/blush/2.png",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )     

image kaito ang b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaiang",
    ( 0, 0 ), "i/sprites/kaito/overlays/blush/3.png",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )

image kaito ann b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaiann",
    ( 0, 0 ), "i/sprites/kaito/overlays/blush/3.png",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )

image kaito cur b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaicur",
    ( 0, 0 ), "i/sprites/kaito/overlays/blush/3.png",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )

image kaito dis b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaidis",
    ( 0, 0 ), "i/sprites/kaito/overlays/blush/3.png",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )
    
image kaito hap b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaihap",
    ( 0, 0 ), "i/sprites/kaito/overlays/blush/3.png",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )   
    
image kaito mis b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaimis",
    ( 0, 0 ), "i/sprites/kaito/overlays/blush/3.png",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )    
 
image kaito ner b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kainer",
    ( 0, 0 ), "i/sprites/kaito/overlays/blush/3.png",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    ) 
    
image kaito neu b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaineu",
    ( 0, 0 ), "i/sprites/kaito/overlays/blush/3.png",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )   
    
image kaito sad b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaisad",
    ( 0, 0 ), "i/sprites/kaito/overlays/blush/3.png",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )   
    
image kaito ske b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaiske",
    ( 0, 0 ), "i/sprites/kaito/overlays/blush/3.png",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )    
    
image kaito smi b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaismi",
    ( 0, 0 ), "i/sprites/kaito/overlays/blush/3.png",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )    
    
image kaito sur b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaisur",
    ( 0, 0 ), "i/sprites/kaito/overlays/blush/3.png",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )        
    
image kaito thi b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaithi",
    ( 0, 0 ), "i/sprites/kaito/overlays/blush/3.png",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )       
    
image kaito win b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaiwin",
    ( 0, 0 ), "i/sprites/kaito/overlays/blush/3.png",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )      

image kaito wor b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "kaihairback",
    ( 0, 0 ), "i/sprites/kaito/outfits/base.png",
    ( 0, 0 ), "kaioutfits",
    ( 0, 0 ), "kaiwor",
    ( 0, 0 ), "i/sprites/kaito/overlays/blush/3.png",
    ( 0, 0 ), "kaihairfront",
    ( 0, 0 ), "kaiAccessoryTop",
    ( 0, 0 ), "kaiAccessoryMiddle",
    ( 0 , 0), "kaiAccessoryBottom"
    )    
    

    
########## ~ kaito EXPRESSIONS ~ ##########

image kaiang:
    "i/sprites/kaito/expressions/angry/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/kaito/expressions/angry/2.png"
    .05
    "i/sprites/kaito/expressions/angry/3.png"
    .05
    "i/sprites/kaito/expressions/angry/4.png"
    .05
    "i/sprites/kaito/expressions/angry/3.png"
    .05
    "i/sprites/kaito/expressions/angry/2.png"
    .05
    repeat

    
image kaiann:
    "i/sprites/kaito/expressions/annoyed/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/kaito/expressions/annoyed/2.png"
    .05
    "i/sprites/kaito/expressions/annoyed/3.png"
    .05
    "i/sprites/kaito/expressions/annoyed/4.png"
    .05
    "i/sprites/kaito/expressions/annoyed/3.png"
    .05
    "i/sprites/kaito/expressions/annoyed/2.png"
    .05
    repeat
    
    
image kaicur:
    "i/sprites/kaito/expressions/curious/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/kaito/expressions/curious/2.png"
    .05
    "i/sprites/kaito/expressions/curious/3.png"
    .05
    "i/sprites/kaito/expressions/curious/4.png"
    .05
    "i/sprites/kaito/expressions/curious/3.png"
    .05
    "i/sprites/kaito/expressions/curious/2.png"
    .05
    repeat
    
    
image kaidis:
    "i/sprites/kaito/expressions/disappointed/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/kaito/expressions/disappointed/2.png"
    .05
    "i/sprites/kaito/expressions/disappointed/3.png"
    .05
    "i/sprites/kaito/expressions/disappointed/4.png"
    .05
    "i/sprites/kaito/expressions/disappointed/3.png"
    .05
    "i/sprites/kaito/expressions/disappointed/2.png"
    .05
    repeat
    
    
image kaihap:
    "i/sprites/kaito/expressions/happy/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/kaito/expressions/happy/2.png"
    .05
    "i/sprites/kaito/expressions/happy/3.png"
    .05
    "i/sprites/kaito/expressions/happy/4.png"
    .05
    "i/sprites/kaito/expressions/happy/3.png"
    .05
    "i/sprites/kaito/expressions/happy/2.png"
    .05
    repeat
    
    
image kaimis:
    "i/sprites/kaito/expressions/mischievous/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/kaito/expressions/mischievous/2.png"
    .05
    "i/sprites/kaito/expressions/mischievous/3.png"
    .05
    "i/sprites/kaito/expressions/mischievous/4.png"
    .05
    "i/sprites/kaito/expressions/mischievous/3.png"
    .05
    "i/sprites/kaito/expressions/mischievous/2.png"
    .05
    repeat
    
    
image kainer:
    "i/sprites/kaito/expressions/nervous/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/kaito/expressions/nervous/2.png"
    .05
    "i/sprites/kaito/expressions/nervous/3.png"
    .05
    "i/sprites/kaito/expressions/nervous/4.png"
    .05
    "i/sprites/kaito/expressions/nervous/3.png"
    .05
    "i/sprites/kaito/expressions/nervous/2.png"
    .05
    repeat
    
    
image kaineu:
    "i/sprites/kaito/expressions/neutral/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/kaito/expressions/neutral/2.png"
    .05
    "i/sprites/kaito/expressions/neutral/3.png"
    .05
    "i/sprites/kaito/expressions/neutral/4.png"
    .05
    "i/sprites/kaito/expressions/neutral/3.png"
    .05
    "i/sprites/kaito/expressions/neutral/2.png"
    .05
    repeat
    
    
image kaisad:
    "i/sprites/kaito/expressions/sad/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/kaito/expressions/sad/2.png"
    .05
    "i/sprites/kaito/expressions/sad/3.png"
    .05
    "i/sprites/kaito/expressions/sad/4.png"
    .05
    "i/sprites/kaito/expressions/sad/3.png"
    .05
    "i/sprites/kaito/expressions/sad/2.png"
    .05
    repeat
    
    
image kaiske:
    "i/sprites/kaito/expressions/skeptical/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/kaito/expressions/skeptical/2.png"
    .05
    "i/sprites/kaito/expressions/skeptical/3.png"
    .05
    "i/sprites/kaito/expressions/skeptical/4.png"
    .05
    "i/sprites/kaito/expressions/skeptical/3.png"
    .05
    "i/sprites/kaito/expressions/skeptical/2.png"
    .05
    repeat
    
    
image kaismi:
    "i/sprites/kaito/expressions/smiling/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/kaito/expressions/smiling/2.png"
    .05
    "i/sprites/kaito/expressions/smiling/3.png"
    .05
    "i/sprites/kaito/expressions/smiling/4.png"
    .05
    "i/sprites/kaito/expressions/smiling/3.png"
    .05
    "i/sprites/kaito/expressions/smiling/2.png"
    .05
    repeat
    
    
image kaisur:
    "i/sprites/kaito/expressions/surprised/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/kaito/expressions/surprised/2.png"
    .05
    "i/sprites/kaito/expressions/surprised/3.png"
    .05
    "i/sprites/kaito/expressions/surprised/4.png"
    .05
    "i/sprites/kaito/expressions/surprised/3.png"
    .05
    "i/sprites/kaito/expressions/surprised/2.png"
    .05
    repeat
    
    
image kaithi:
    "i/sprites/kaito/expressions/thinking/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/kaito/expressions/thinking/2.png"
    .05
    "i/sprites/kaito/expressions/thinking/3.png"
    .05
    "i/sprites/kaito/expressions/thinking/4.png"
    .05
    "i/sprites/kaito/expressions/thinking/3.png"
    .05
    "i/sprites/kaito/expressions/thinking/2.png"
    .05
    repeat
    
    
image kaiwin:
    "i/sprites/kaito/expressions/wincing/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/kaito/expressions/wincing/2.png"
    .05
    "i/sprites/kaito/expressions/wincing/3.png"
    .05
    "i/sprites/kaito/expressions/wincing/4.png"
    .05
    "i/sprites/kaito/expressions/wincing/3.png"
    .05
    "i/sprites/kaito/expressions/wincing/2.png"
    .05
    repeat
    
    
image kaiwor:
    "i/sprites/kaito/expressions/worried/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/kaito/expressions/worried/2.png"
    .05
    "i/sprites/kaito/expressions/worried/3.png"
    .05
    "i/sprites/kaito/expressions/worried/4.png"
    .05
    "i/sprites/kaito/expressions/worried/3.png"
    .05
    "i/sprites/kaito/expressions/worried/2.png"
    .05
    repeat