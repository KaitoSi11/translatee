########## ~ yuki CONDITIONSWITCHES ~ ##########
    
image yukhairback = ConditionSwitch (
        "yukHairB == 'default'", "i/sprites/yuki/hairstyles/default/back.png"
        )
        
image yukoutfits = ConditionSwitch (
        "yukOut == 'default'", "i/sprites/yuki/outfits/default.png",
        "yukOut == 'coat'", "i/sprites/yuki/outfits/coat.png",
        "yukOut == 'sweater'", "i/sprites/yuki/outfits/sweater.png"
        )
        
image yukhairfront = ConditionSwitch (
        "yukHairF == 'default'", "i/sprites/yuki/hairstyles/default/front.png"
        )

image yukHairA = ConditionSwitch (
        "yukHairF == 'default'", "i/sprites/empty.png"
        )

image yukAccessoryTop = ConditionSwitch (
        "yukAccT == 'emptyimage'", "i/sprites/empty.png"
        )
        
image yukAccessoryMiddle = ConditionSwitch (
        "yukAccM == 'emptyimage'", "i/sprites/empty.png"
        )
        
image yukAccessoryBottom = ConditionSwitch (
        "yukAccB == 'emptyimage'", "i/sprites/empty.png"
        )
    
    

########## ~ yuki LIVECOMPOSITE ~ ##########

image yuki ang = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yukang",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )

image yuki ann = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yukann",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )

image yuki cur = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yukcur",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )

image yuki dis = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yukdis",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )
    
image yuki hap = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yukhap",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )   
    
image yuki mis = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yukmis",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )    
 
image yuki ner = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yukner",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    ) 
    
image yuki neu = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yukneu",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )   
    
image yuki sad = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yuksad",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )   
    
image yuki ske = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yukske",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )    
    
image yuki smi = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yuksmi",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )    
    
image yuki sur = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yuksur",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )        
    
image yuki thi = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yukthi",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )       
    
image yuki win = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yukwin",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )      

image yuki wor = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yukwor",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )

image yuki ang b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yukang",
    ( 0, 0 ), "i/sprites/yuki/overlays/blush/1.png",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )

image yuki ann b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yukann",
    ( 0, 0 ), "i/sprites/yuki/overlays/blush/1.png",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )

image yuki cur b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yukcur",
    ( 0, 0 ), "i/sprites/yuki/overlays/blush/1.png",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )

image yuki dis b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yukdis",
    ( 0, 0 ), "i/sprites/yuki/overlays/blush/1.png",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )
    
image yuki hap b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yukhap",
    ( 0, 0 ), "i/sprites/yuki/overlays/blush/1.png",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )   
    
image yuki mis b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yukmis",
    ( 0, 0 ), "i/sprites/yuki/overlays/blush/1.png",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )    
 
image yuki ner b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yukner",
    ( 0, 0 ), "i/sprites/yuki/overlays/blush/1.png",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    ) 
    
image yuki neu b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yukneu",
    ( 0, 0 ), "i/sprites/yuki/overlays/blush/1.png",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )   
    
image yuki sad b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yuksad",
    ( 0, 0 ), "i/sprites/yuki/overlays/blush/1.png",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )   
    
image yuki ske b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yukske",
    ( 0, 0 ), "i/sprites/yuki/overlays/blush/1.png",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )    
    
image yuki smi b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yuksmi",
    ( 0, 0 ), "i/sprites/yuki/overlays/blush/1.png",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )    
    
image yuki sur b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yuksur",
    ( 0, 0 ), "i/sprites/yuki/overlays/blush/1.png",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )        
    
image yuki thi b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yukthi",
    ( 0, 0 ), "i/sprites/yuki/overlays/blush/1.png",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )       
    
image yuki win b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yukwin",
    ( 0, 0 ), "i/sprites/yuki/overlays/blush/1.png",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )      

image yuki wor b1 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yukwor",
    ( 0, 0 ), "i/sprites/yuki/overlays/blush/1.png",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )     
    
image yuki ang b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yukang",
    ( 0, 0 ), "i/sprites/yuki/overlays/blush/2.png",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )

image yuki ann b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yukann",
    ( 0, 0 ), "i/sprites/yuki/overlays/blush/2.png",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )

image yuki cur b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yukcur",
    ( 0, 0 ), "i/sprites/yuki/overlays/blush/2.png",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )

image yuki dis b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yukdis",
    ( 0, 0 ), "i/sprites/yuki/overlays/blush/2.png",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )
    
image yuki hap b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yukhap",
    ( 0, 0 ), "i/sprites/yuki/overlays/blush/2.png",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )   
    
image yuki mis b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yukmis",
    ( 0, 0 ), "i/sprites/yuki/overlays/blush/2.png",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )    
 
image yuki ner b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yukner",
    ( 0, 0 ), "i/sprites/yuki/overlays/blush/2.png",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    ) 
    
image yuki neu b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yukneu",
    ( 0, 0 ), "i/sprites/yuki/overlays/blush/2.png",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )   
    
image yuki sad b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yuksad",
    ( 0, 0 ), "i/sprites/yuki/overlays/blush/2.png",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )   
    
image yuki ske b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yukske",
    ( 0, 0 ), "i/sprites/yuki/overlays/blush/2.png",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )    
    
image yuki smi b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yuksmi",
    ( 0, 0 ), "i/sprites/yuki/overlays/blush/2.png",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )    
    
image yuki sur b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yuksur",
    ( 0, 0 ), "i/sprites/yuki/overlays/blush/2.png",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )        
    
image yuki thi b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yukthi",
    ( 0, 0 ), "i/sprites/yuki/overlays/blush/2.png",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )       
    
image yuki win b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yukwin",
    ( 0, 0 ), "i/sprites/yuki/overlays/blush/2.png",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )      

image yuki wor b2 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yukwor",
    ( 0, 0 ), "i/sprites/yuki/overlays/blush/2.png",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )     

image yuki ang b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yukang",
    ( 0, 0 ), "i/sprites/yuki/overlays/blush/3.png",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )

image yuki ann b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yukann",
    ( 0, 0 ), "i/sprites/yuki/overlays/blush/3.png",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )

image yuki cur b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yukcur",
    ( 0, 0 ), "i/sprites/yuki/overlays/blush/3.png",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )

image yuki dis b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yukdis",
    ( 0, 0 ), "i/sprites/yuki/overlays/blush/3.png",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )
    
image yuki hap b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yukhap",
    ( 0, 0 ), "i/sprites/yuki/overlays/blush/3.png",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )   
    
image yuki mis b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yukmis",
    ( 0, 0 ), "i/sprites/yuki/overlays/blush/3.png",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )    
 
image yuki ner b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yukner",
    ( 0, 0 ), "i/sprites/yuki/overlays/blush/3.png",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    ) 
    
image yuki neu b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yukneu",
    ( 0, 0 ), "i/sprites/yuki/overlays/blush/3.png",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )   
    
image yuki sad b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yuksad",
    ( 0, 0 ), "i/sprites/yuki/overlays/blush/3.png",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )   
    
image yuki ske b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yukske",
    ( 0, 0 ), "i/sprites/yuki/overlays/blush/3.png",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )    
    
image yuki smi b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yuksmi",
    ( 0, 0 ), "i/sprites/yuki/overlays/blush/3.png",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )    
    
image yuki sur b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yuksur",
    ( 0, 0 ), "i/sprites/yuki/overlays/blush/3.png",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )        
    
image yuki thi b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yukthi",
    ( 0, 0 ), "i/sprites/yuki/overlays/blush/3.png",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )       
    
image yuki win b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yukwin",
    ( 0, 0 ), "i/sprites/yuki/overlays/blush/3.png",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )      

image yuki wor b3 = LiveComposite(
    ( 952, 1850 ),
    ( 0, 0 ), "yukhairback",
    ( 0, 0 ), "i/sprites/yuki/outfits/base.png",
    ( 0, 0 ), "yukoutfits",
    ( 0, 0 ), "yukwor",
    ( 0, 0 ), "i/sprites/yuki/overlays/blush/3.png",
    ( 0, 0 ), "yukHairA",
    ( 0, 0 ), "yukhairfront",
    ( 0, 0 ), "yukAccessoryTop",
    ( 0, 0 ), "yukAccessoryMiddle",
    ( 0 , 0), "yukAccessoryBottom"
    )   


image yukang:
    "i/sprites/yuki/expressions/angry/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/yuki/expressions/angry/2.png"
    .05
    "i/sprites/yuki/expressions/angry/3.png"
    .05
    "i/sprites/yuki/expressions/angry/4.png"
    .05
    "i/sprites/yuki/expressions/angry/3.png"
    .05
    "i/sprites/yuki/expressions/angry/2.png"
    .05
    repeat

    
image yukann:
    "i/sprites/yuki/expressions/annoyed/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/yuki/expressions/annoyed/2.png"
    .05
    "i/sprites/yuki/expressions/annoyed/3.png"
    .05
    "i/sprites/yuki/expressions/annoyed/4.png"
    .05
    "i/sprites/yuki/expressions/annoyed/3.png"
    .05
    "i/sprites/yuki/expressions/annoyed/2.png"
    .05
    repeat
    
    
image yukcur:
    "i/sprites/yuki/expressions/curious/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/yuki/expressions/curious/2.png"
    .05
    "i/sprites/yuki/expressions/curious/3.png"
    .05
    "i/sprites/yuki/expressions/curious/4.png"
    .05
    "i/sprites/yuki/expressions/curious/3.png"
    .05
    "i/sprites/yuki/expressions/curious/2.png"
    .05
    repeat
    
    
image yukdis:
    "i/sprites/yuki/expressions/disappointed/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/yuki/expressions/disappointed/2.png"
    .05
    "i/sprites/yuki/expressions/disappointed/3.png"
    .05
    "i/sprites/yuki/expressions/disappointed/4.png"
    .05
    "i/sprites/yuki/expressions/disappointed/3.png"
    .05
    "i/sprites/yuki/expressions/disappointed/2.png"
    .05
    repeat
    
    
image yukhap:
    "i/sprites/yuki/expressions/happy/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/yuki/expressions/happy/1.png"
    .05
    "i/sprites/yuki/expressions/happy/1.png"
    .05
    "i/sprites/yuki/expressions/happy/1.png"
    .05
    "i/sprites/yuki/expressions/happy/1.png"
    .05
    "i/sprites/yuki/expressions/happy/1.png"
    .05
    repeat
    
    
image yukmis:
    "i/sprites/yuki/expressions/mischievous/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/yuki/expressions/mischievous/2.png"
    .05
    "i/sprites/yuki/expressions/mischievous/3.png"
    .05
    "i/sprites/yuki/expressions/mischievous/4.png"
    .05
    "i/sprites/yuki/expressions/mischievous/3.png"
    .05
    "i/sprites/yuki/expressions/mischievous/2.png"
    .05
    repeat
    
    
image yukner:
    "i/sprites/yuki/expressions/nervous/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/yuki/expressions/nervous/2.png"
    .05
    "i/sprites/yuki/expressions/nervous/3.png"
    .05
    "i/sprites/yuki/expressions/nervous/4.png"
    .05
    "i/sprites/yuki/expressions/nervous/3.png"
    .05
    "i/sprites/yuki/expressions/nervous/2.png"
    .05
    repeat
    
    
image yukneu:
    "i/sprites/yuki/expressions/neutral/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/yuki/expressions/neutral/2.png"
    .05
    "i/sprites/yuki/expressions/neutral/3.png"
    .05
    "i/sprites/yuki/expressions/neutral/4.png"
    .05
    "i/sprites/yuki/expressions/neutral/3.png"
    .05
    "i/sprites/yuki/expressions/neutral/2.png"
    .05
    repeat
    
    
image yuksad:
    "i/sprites/yuki/expressions/sad/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/yuki/expressions/sad/2.png"
    .05
    "i/sprites/yuki/expressions/sad/3.png"
    .05
    "i/sprites/yuki/expressions/sad/4.png"
    .05
    "i/sprites/yuki/expressions/sad/3.png"
    .05
    "i/sprites/yuki/expressions/sad/2.png"
    .05
    repeat
    
    
image yukske:
    "i/sprites/yuki/expressions/skeptical/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/yuki/expressions/skeptical/2.png"
    .05
    "i/sprites/yuki/expressions/skeptical/3.png"
    .05
    "i/sprites/yuki/expressions/skeptical/4.png"
    .05
    "i/sprites/yuki/expressions/skeptical/3.png"
    .05
    "i/sprites/yuki/expressions/skeptical/2.png"
    .05
    repeat
    
    
image yuksmi:
    "i/sprites/yuki/expressions/smiling/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/yuki/expressions/smiling/2.png"
    .05
    "i/sprites/yuki/expressions/smiling/3.png"
    .05
    "i/sprites/yuki/expressions/smiling/4.png"
    .05
    "i/sprites/yuki/expressions/smiling/3.png"
    .05
    "i/sprites/yuki/expressions/smiling/2.png"
    .05
    repeat
    
    
image yuksur:
    "i/sprites/yuki/expressions/surprised/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/yuki/expressions/surprised/2.png"
    .05
    "i/sprites/yuki/expressions/surprised/3.png"
    .05
    "i/sprites/yuki/expressions/surprised/4.png"
    .05
    "i/sprites/yuki/expressions/surprised/3.png"
    .05
    "i/sprites/yuki/expressions/surprised/2.png"
    .05
    repeat
    
    
image yukthi:
    "i/sprites/yuki/expressions/thinking/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/yuki/expressions/thinking/2.png"
    .05
    "i/sprites/yuki/expressions/thinking/3.png"
    .05
    "i/sprites/yuki/expressions/thinking/4.png"
    .05
    "i/sprites/yuki/expressions/thinking/3.png"
    .05
    "i/sprites/yuki/expressions/thinking/2.png"
    .05
    repeat
    
    
image yukwin:
    "i/sprites/yuki/expressions/wincing/1.png"
    
    
image yukwor:
    "i/sprites/yuki/expressions/worried/1.png"
    choice:
        3.5
    choice:
        4.5
    choice:
        5.5
    "i/sprites/yuki/expressions/worried/2.png"
    .05
    "i/sprites/yuki/expressions/worried/3.png"
    .05
    "i/sprites/yuki/expressions/worried/4.png"
    .05
    "i/sprites/yuki/expressions/worried/3.png"
    .05
    "i/sprites/yuki/expressions/worried/2.png"
    .05
    repeat
    
