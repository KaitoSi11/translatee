label E1D2S12:
    
    stop music fadeout 3
    stop ambient fadeout 3
    scene black with fade
    "..."
    play music "audio/music/Isokaze (GAME VERSION).ogg" fadein 3
    
    if (E1D2S7_ParkedFar == 1):
        play ambient "audio/ambience/Parking Lot.ogg" fadein 1
        scene bg campus parking dusk empty with fade
        "Time to make the trek all the way to far end of the lot. I wonder why they make visitors park so far away. Wouldn't that discourage rather than encourage people to visit?"
        "Although I grumble the entire way to my bike, I eventually find it in the same spot I had parked it." 
    
        if (E1D2S7_BullyFightWin == 0) and (E1D2S7_CleanMove == 1):
            pf "Time to get going."
    
        if (E1D2S3_mcwithhelmet == 1):
            "I hop on my bike and put on my helmet."
            
        if (E1D2S3_mcwithhelmet == 0):
            "I hop on my bike. I can't wait to feel the wind on my face."
            
        play sound "audio/sfx/Vehicles/Bike Ignition.ogg" fadeout 3
        stop ambient fadeout 3
        stop music fadeout 3
        scene black with fade
        "Kicking my bike into gear, I make my way home."
        play sound "audio/sfx/Vehicles/Bike driving off.ogg" fadein 1 fadeout 1
        
        #Don't need to go through images
        #scene bg campus intersection dusk with fade
        #scene bg travel openroad dusk with fade
        #scene isokaze highschool dusk with fade

        $renpy.pause(2)
        
        jump E1D2S13
        
    
    elif (E1D2S7_BullyFightWin == 1):
        play ambient "audio/ambience/Parking Lot.ogg" fadein 1
        scene bg campus parking dusk with fade
        "I walk quickly towards the parking lot, and before long, the first few spots come into view. As I get closer, I can see just how far the lot extends. It must suck for those losers who had to park on the opposite side of the school."
        "I stand where I remember parking my bike, but it's been replaced with a different one. I scan first few rows of motorcycles for my bike, but can't find it anywhere."
        "This can't be right… I'm certain I parked here."
        "Between the campus and the lot is a small building. That must be where security is. As I approach, a burly guard frowns at me."
        show guard extra at cc with dissolve
        pf "Excuse me."
        voice "audio/voice/E1/D2/S12/Guard/1.ogg"
        gua "Yes?"
        pf "I parked my motorcycle here this morning, but it's no longer here."
        "He turns towards his computer."
        voice "audio/voice/E1/D2/S12/Guard/2.ogg"
        gua "What's your pass number?"
        pf "I don't have one."
        "He looks back at me and raises an eyebrow."
        show question:
            xoffset 675
            yoffset 50
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D2/S12/Guard/3.ogg"
        gua "You parked in a reserved space without a pass. What did you think was going to happen?"
        pf "I thought my bike would still be where I left it."
        voice "audio/voice/E1/D2/S12/Guard/4.ogg"
        gua "Well, now you know better. Your motorcycle has been impounded."
        "My chest feels like a hand is squeezing my heart. My baby! What if they scratched it?"
    
        "That jerk must have called it in and gotten my bike removed once he came to. What a sore loser!"
        voice "audio/voice/E1/D2/S12/Guard/5.ogg"
        gua "You can pick it up in the morning."
        pf "Why not now?"
        "The guard looks at me as if I had two heads."
        voice "audio/voice/E1/D2/S12/Guard/6.ogg"
        gua "Don't you know what time it is?"
        pf "Uh…"
        "I check my phone."
        pf "It's one after five."
        voice "audio/voice/E1/D2/S12/Guard/7.ogg"
        gua "Exactly. I'm off work."
        pf "What? But we're still talking--"
        show storm:
            xoffset 675
            yoffset 50
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D2/S12/Guard/8.ogg"
        gua "Not anymore. We're closed. If you have a complaint, you can submit it in the morning."
        hide guard extra with dissolve
        "He ushers me out of the building and locks up. I guess I've got no choice but to take the bus home today."
        jump E1D2S12_BusConverge
        
    elif (E1D2S1_firstdaybus == 1):
        "I start to head towards the parking lot before I remember I left my bike at home today. Oh shoot, I forgot to check the bus schedules! Hopefully there's one coming soon. I scroll through the schedules as I hurry towards the front of the campus."
        scene bg campus main dusk with fade
        "Pick up and drop off are in the same location, right?"
    
        label E1D2S12_BusConverge:
            scene black with fade
            play ambient "audio/ambience/Parking Lot.ogg" fadein 1
            "When I make it to the bus stop, there are a handful of students already waiting."
            if (E1D2S2_talkwithyuunayes == 1):
                "I crane my neck to look for Yuuna, but she's not there. I guess that was wishful thinking anyway."
            else:
                "I scan the faces on the off-chance that I'd recognise someone, but I don't." 
    
            play sound "audio/sfx/Vehicles/Bus Door Open.ogg" fadein 1 fadeout 1
            "After what feels like a lifetime, the bus arrives."
            stop ambient fadeout 3
            scene bg travel bus dusk with fade
            stop music fadeout 3
            play sound "audio/sfx/Vehicles/Bus Chime.ogg" fadein 1 fadeout 1
            play ambient "audio/ambience/Bus.ogg" fadein 1
            "I'm able to find a seat right away, and have an uneventful ride home."
            scene black with fade
            $renpy.pause(1)
            play sound "audio/sfx/Vehicles/Bus Chime.ogg" fadein 1 fadeout 1
            stop ambient fadeout 3
            play sound "audio/sfx/Vehicles/Bus Door Open.ogg" fadein 1 fadeout 1
            $renpy.pause(1)
        
    jump E1D2S13
