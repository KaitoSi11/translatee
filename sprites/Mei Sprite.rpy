########## ~ mei CONDITIONSWITCHES ~ ##########
    
image meihairback = ConditionSwitch (
        "meiHairF == 'hotspring'", "i/sprites/mei/hairstyles/hotspring/back.png",
        "meiHairB == 'default'", "i/sprites/mei/hairstyles/default/back.png"
        )
        
image meioutfits = ConditionSwitch (
        "meiOut == 'hotspring'", "i/sprites/mei/outfits/hotspring.png",
        "meiOut == 'sSwimsuit'", "i/sprites/mei/outfits/summer - swimsuit.png",
        "meiOut == 'sCasual'", "i/sprites/mei/outfits/summer - casual.png",
        "meiOut == 'sUniform'", "i/sprites/mei/outfits/summer - uniform.png"
        )
        
image meihairfront = ConditionSwitch (
        "meiHairF == 'hotspring'", "i/sprites/mei/hairstyles/hotspring/front.png",
        "meiHairF == 'default'", "i/sprites/mei/hairstyles/default/front.png"
        )

image meiHairA = ConditionSwitch (
        "meiHairF == 'hotspring'", "i/sprites/empty.png",
        "meiHairF == 'default'", "i/sprites/empty.png"
        )

image meiAccessoryTop = ConditionSwitch (
        "meiAccT == 'emptyimage'", "i/sprites/empty.png"
        )
        
image meiAccessoryMiddle = ConditionSwitch (
        "meiAccM == 'emptyimage'", "i/sprites/empty.png"
        )
        
image meiAccessoryBottom = ConditionSwitch (
        "meiAccB == 'emptyimage'", "i/sprites/empty.png"
        )



########## ~ mei LIVECOMPOSITE ~ ##########

image mei ang = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meiang",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )

image mei ann = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meiann",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )

image mei cur = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meicur",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )

image mei dis = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meidis",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )
    
image mei hap = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meihap",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )   
    
image mei mis = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meimis",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )    
 
image mei ner = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meiner",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    ) 
    
image mei neu = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meineu",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )   
    
image mei sad = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meisad",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )   
    
image mei ske = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meiske",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )    
    
image mei smi = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meismi",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )    
    
image mei sur = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meisur",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )        
    
image mei thi = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meithi",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )       
    
image mei win = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meiwin",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )      

image mei wor = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meiwor",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )    
  
image mei ang b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meiang",
    ( 0, 0 ), "i/sprites/mei/overlays/blush/1.png",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )

image mei ann b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meiann",
    ( 0, 0 ), "i/sprites/mei/overlays/blush/1.png",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )

image mei cur b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meicur",
    ( 0, 0 ), "i/sprites/mei/overlays/blush/1.png",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )

image mei dis b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meidis",
    ( 0, 0 ), "i/sprites/mei/overlays/blush/1.png",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )
    
image mei hap b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meihap",
    ( 0, 0 ), "i/sprites/mei/overlays/blush/1.png",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )   
    
image mei mis b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meimis",
    ( 0, 0 ), "i/sprites/mei/overlays/blush/1.png",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )    
 
image mei ner b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meiner",
    ( 0, 0 ), "i/sprites/mei/overlays/blush/1.png",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    ) 
    
image mei neu b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meineu",
    ( 0, 0 ), "i/sprites/mei/overlays/blush/1.png",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )   
    
image mei sad b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meisad",
    ( 0, 0 ), "i/sprites/mei/overlays/blush/1.png",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )   
    
image mei ske b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meiske",
    ( 0, 0 ), "i/sprites/mei/overlays/blush/1.png",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )    
    
image mei smi b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meismi",
    ( 0, 0 ), "i/sprites/mei/overlays/blush/1.png",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )    
    
image mei sur b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meisur",
    ( 0, 0 ), "i/sprites/mei/overlays/blush/1.png",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )        
    
image mei thi b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meithi",
    ( 0, 0 ), "i/sprites/mei/overlays/blush/1.png",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )       
    
image mei win b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meiwin",
    ( 0, 0 ), "i/sprites/mei/overlays/blush/1.png",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )      

image mei wor b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meiwor",
    ( 0, 0 ), "i/sprites/mei/overlays/blush/1.png",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )     
    
image mei ang b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meiang",
    ( 0, 0 ), "i/sprites/mei/overlays/blush/2.png",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )

image mei ann b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meiann",
    ( 0, 0 ), "i/sprites/mei/overlays/blush/2.png",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )

image mei cur b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meicur",
    ( 0, 0 ), "i/sprites/mei/overlays/blush/2.png",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )

image mei dis b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meidis",
    ( 0, 0 ), "i/sprites/mei/overlays/blush/2.png",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )
    
image mei hap b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meihap",
    ( 0, 0 ), "i/sprites/mei/overlays/blush/2.png",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )   
    
image mei mis b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meimis",
    ( 0, 0 ), "i/sprites/mei/overlays/blush/2.png",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )    
 
image mei ner b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meiner",
    ( 0, 0 ), "i/sprites/mei/overlays/blush/2.png",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    ) 
    
image mei neu b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meineu",
    ( 0, 0 ), "i/sprites/mei/overlays/blush/2.png",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )   
    
image mei sad b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meisad",
    ( 0, 0 ), "i/sprites/mei/overlays/blush/2.png",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )   
    
image mei ske b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meiske",
    ( 0, 0 ), "i/sprites/mei/overlays/blush/2.png",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )    
    
image mei smi b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meismi",
    ( 0, 0 ), "i/sprites/mei/overlays/blush/2.png",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )    
    
image mei sur b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meisur",
    ( 0, 0 ), "i/sprites/mei/overlays/blush/2.png",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )        
    
image mei thi b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meithi",
    ( 0, 0 ), "i/sprites/mei/overlays/blush/2.png",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )       
    
image mei win b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meiwin",
    ( 0, 0 ), "i/sprites/mei/overlays/blush/2.png",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )      

image mei wor b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meiwor",
    ( 0, 0 ), "i/sprites/mei/overlays/blush/2.png",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )     

image mei ang b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meiang",
    ( 0, 0 ), "i/sprites/mei/overlays/blush/3.png",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )

image mei ann b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meiann",
    ( 0, 0 ), "i/sprites/mei/overlays/blush/3.png",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )

image mei cur b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meicur",
    ( 0, 0 ), "i/sprites/mei/overlays/blush/3.png",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )

image mei dis b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meidis",
    ( 0, 0 ), "i/sprites/mei/overlays/blush/3.png",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )
    
image mei hap b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meihap",
    ( 0, 0 ), "i/sprites/mei/overlays/blush/3.png",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )   
    
image mei mis b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meimis",
    ( 0, 0 ), "i/sprites/mei/overlays/blush/3.png",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )    
 
image mei ner b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meiner",
    ( 0, 0 ), "i/sprites/mei/overlays/blush/3.png",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    ) 
    
image mei neu b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meineu",
    ( 0, 0 ), "i/sprites/mei/overlays/blush/3.png",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )   
    
image mei sad b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meisad",
    ( 0, 0 ), "i/sprites/mei/overlays/blush/3.png",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )   
    
image mei ske b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meiske",
    ( 0, 0 ), "i/sprites/mei/overlays/blush/3.png",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )    
    
image mei smi b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meismi",
    ( 0, 0 ), "i/sprites/mei/overlays/blush/3.png",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )    
    
image mei sur b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meisur",
    ( 0, 0 ), "i/sprites/mei/overlays/blush/3.png",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )        
    
image mei thi b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meithi",
    ( 0, 0 ), "i/sprites/mei/overlays/blush/3.png",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )       
    
image mei win b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meiwin",
    ( 0, 0 ), "i/sprites/mei/overlays/blush/3.png",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )      

image mei wor b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "meihairback",
    ( 0, 0 ), "i/sprites/mei/outfits/base.png",
    ( 0, 0 ), "meioutfits",
    ( 0, 0 ), "meiwor",
    ( 0, 0 ), "i/sprites/mei/overlays/blush/3.png",
    ( 0, 0 ), "meiHairA",
    ( 0, 0 ), "meihairfront",
    ( 0, 0 ), "meiAccessoryTop",
    ( 0, 0 ), "meiAccessoryMiddle",
    ( 0 , 0), "meiAccessoryBottom"
    )    


########## ~ mei EXPRESSIONS ~ ##########

image meiang:
    "i/sprites/mei/expressions/angry/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/mei/expressions/angry/2.png"
    .05
    "i/sprites/mei/expressions/angry/3.png"
    .05
    "i/sprites/mei/expressions/angry/4.png"
    .05
    "i/sprites/mei/expressions/angry/3.png"
    .05
    "i/sprites/mei/expressions/angry/2.png"
    .05
    repeat
    
image meiann:
    "i/sprites/mei/expressions/annoyed/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/mei/expressions/annoyed/2.png"
    .05
    "i/sprites/mei/expressions/annoyed/3.png"
    .05
    "i/sprites/mei/expressions/annoyed/4.png"
    .05
    "i/sprites/mei/expressions/annoyed/3.png"
    .05
    "i/sprites/mei/expressions/annoyed/2.png"
    .05
    repeat
    
    
image meicur:
    "i/sprites/mei/expressions/curious/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/mei/expressions/curious/2.png"
    .05
    "i/sprites/mei/expressions/curious/3.png"
    .05
    "i/sprites/mei/expressions/curious/4.png"
    .05
    "i/sprites/mei/expressions/curious/3.png"
    .05
    "i/sprites/mei/expressions/curious/2.png"
    .05
    repeat
    
    
image meidis:
    "i/sprites/mei/expressions/disappointed/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/mei/expressions/disappointed/2.png"
    .05
    "i/sprites/mei/expressions/disappointed/3.png"
    .05
    "i/sprites/mei/expressions/disappointed/4.png"
    .05
    "i/sprites/mei/expressions/disappointed/3.png"
    .05
    "i/sprites/mei/expressions/disappointed/2.png"
    .05
    repeat
    
    
image meihap:
    "i/sprites/mei/expressions/happy/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/mei/expressions/happy/2.png"
    .05
    "i/sprites/mei/expressions/happy/3.png"
    .05
    "i/sprites/mei/expressions/happy/4.png"
    .05
    "i/sprites/mei/expressions/happy/3.png"
    .05
    "i/sprites/mei/expressions/happy/2.png"
    .05
    repeat
    
    
image meimis:
    "i/sprites/mei/expressions/mischievous/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/mei/expressions/mischievous/2.png"
    .05
    "i/sprites/mei/expressions/mischievous/3.png"
    .05
    "i/sprites/mei/expressions/mischievous/4.png"
    .05
    "i/sprites/mei/expressions/mischievous/3.png"
    .05
    "i/sprites/mei/expressions/mischievous/2.png"
    .05
    repeat
    
    
image meiner:
    "i/sprites/mei/expressions/nervous/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/mei/expressions/nervous/2.png"
    .05
    "i/sprites/mei/expressions/nervous/3.png"
    .05
    "i/sprites/mei/expressions/nervous/4.png"
    .05
    "i/sprites/mei/expressions/nervous/3.png"
    .05
    "i/sprites/mei/expressions/nervous/2.png"
    .05
    repeat
    
    
image meineu:
    "i/sprites/mei/expressions/neutral/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/mei/expressions/neutral/2.png"
    .05
    "i/sprites/mei/expressions/neutral/3.png"
    .05
    "i/sprites/mei/expressions/neutral/4.png"
    .05
    "i/sprites/mei/expressions/neutral/3.png"
    .05
    "i/sprites/mei/expressions/neutral/2.png"
    .05
    repeat
    
    
image meisad:
    "i/sprites/mei/expressions/sad/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/mei/expressions/sad/2.png"
    .05
    "i/sprites/mei/expressions/sad/3.png"
    .05
    "i/sprites/mei/expressions/sad/4.png"
    .05
    "i/sprites/mei/expressions/sad/3.png"
    .05
    "i/sprites/mei/expressions/sad/2.png"
    .05
    repeat
    
    
image meiske:
    "i/sprites/mei/expressions/skeptical/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/mei/expressions/skeptical/2.png"
    .05
    "i/sprites/mei/expressions/skeptical/3.png"
    .05
    "i/sprites/mei/expressions/skeptical/4.png"
    .05
    "i/sprites/mei/expressions/skeptical/3.png"
    .05
    "i/sprites/mei/expressions/skeptical/2.png"
    .05
    repeat
    
    
image meismi:
    "i/sprites/mei/expressions/smiling/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/mei/expressions/smiling/2.png"
    .05
    "i/sprites/mei/expressions/smiling/3.png"
    .05
    "i/sprites/mei/expressions/smiling/4.png"
    .05
    "i/sprites/mei/expressions/smiling/3.png"
    .05
    "i/sprites/mei/expressions/smiling/2.png"
    .05
    repeat
    
    
image meisur:
    "i/sprites/mei/expressions/surprised/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/mei/expressions/surprised/2.png"
    .05
    "i/sprites/mei/expressions/surprised/3.png"
    .05
    "i/sprites/mei/expressions/surprised/4.png"
    .05
    "i/sprites/mei/expressions/surprised/3.png"
    .05
    "i/sprites/mei/expressions/surprised/2.png"
    .05
    repeat
    
    
image meithi:
    "i/sprites/mei/expressions/thinking/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/mei/expressions/thinking/2.png"
    .05
    "i/sprites/mei/expressions/thinking/3.png"
    .05
    "i/sprites/mei/expressions/thinking/4.png"
    .05
    "i/sprites/mei/expressions/thinking/3.png"
    .05
    "i/sprites/mei/expressions/thinking/2.png"
    .05
    repeat
    
    
image meiwin:
    "i/sprites/mei/expressions/wincing/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/mei/expressions/wincing/2.png"
    .05
    "i/sprites/mei/expressions/wincing/3.png"
    .05
    "i/sprites/mei/expressions/wincing/4.png"
    .05
    "i/sprites/mei/expressions/wincing/3.png"
    .05
    "i/sprites/mei/expressions/wincing/2.png"
    .05
    repeat
    
    
image meiwor:
    "i/sprites/mei/expressions/worried/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/mei/expressions/worried/2.png"
    .05
    "i/sprites/mei/expressions/worried/3.png"
    .05
    "i/sprites/mei/expressions/worried/4.png"
    .05
    "i/sprites/mei/expressions/worried/3.png"
    .05
    "i/sprites/mei/expressions/worried/2.png"
    .05
    repeat
