#
label E4D3S1:
    
    $ kaoOut = "sCasual"
    $ kaoHairF = "default"
    $ kaoHairB = "default"
    
    
    $ mayHairF = "default"
    $ mayHairB = mayHairF
    $ mayOut = "sCasual"
    
    $ nikHairF = "default"
    $ nikHairB = nikHairF
    $ nikOut = "sUniform"
    
    $ shoHairF = "default"
    $ shoHairB = shoHairF
    $ shoOut = "sCasual"
    
    $ valHairF = "default"
    $ valHairB = valHairF
    $ valOut = "sCasual"
    
    $ yuuHairF = "default"
    $ yuuHairB = yuuHairF
    $ yuuOut = "sCasual"
    
    $ day = 3
    $ timeSpent = "none"
    
    play ambient "audio/ambience/Morning.ogg" fadein 1
    $renpy.pause(1)
    # sfx - we should definitely try and get this lol
    #show kaori smi at r1
    "I'm woken up at the crack of dawn by the most irritating clucking noises. Apparently Shou's alarm is of a rooster crowing. {w}Bruh, why?"
    "After unceremoniously stifling yawns and getting dressed, I make a quick sweep of the room to make sure I packed all of my things. Shou had to make two sweeps because he kept yawning during his first and forgetting where he'd already looked."
    scene bg campus lounge day with fade
    show yuuna dis at l3 with dissolve:
        xoffset -200
        xzoom 0.75
        yzoom 0.75
    show mayu smi at l2 behind yuuna  with dissolve:
        xoffset -50
        xzoom 0.75
        yzoom 0.75
    show valerie neu at l1 with dissolve:
        xoffset 75
        xzoom 0.75
        yzoom 0.75
    show kaori smi at r1 behind shou with dissolve:
        xoffset -75
        xzoom 0.75
        yzoom 0.75
    show shou wor at r3 with dissolve:
        xoffset 100
        xzoom -0.75
        yzoom 0.75
    "We're all silent as we meet in the lobby. Mayu and Kaori are both wide awake and as perky as either of them could ever be. {w}Yuuna and Valerie seem even more exhausted than Shou and I… I wonder what was going on in their room…"
    show kaori dis
    #show kaori dis
    "Before my mind can wander too far, I snap back to reality and glance guiltily at Kaori who has her eyes narrowed."
    show dots:
        xoffset 925
        yoffset 110
        xzoom .5
        yzoom .5
    "Can she read my thoughts now too?! Good thing I wasn't thinking anything perverted…"
    stop ambient fadeout 3
    scene black with fade
    $renpy.pause(0.5)
    play ambient "audio/ambience/Bullet Train.ogg" fadein 1
    $renpy.pause(1)
    scene bg travel train day with fade
    "Still in silence, we make our way to the train station. The train ride home feels even longer than the ride to the hot springs. {w}I resist the urge to ask \"are we there yet\"?"
    stop ambient fadeout 5
    scene black with fade
    play sound "audio/sfx/Vehicles/Bus Chime.ogg"
    $renpy.pause(1)
    "After what feels like an eternity, we arrive at Isokaze. {w}Finally! Napping on the uncomfortable train was nearly impossible and my thoughts kept drifting to my warm bed."
    "I say a quick goodbye to everyone and practically speed home. As soon as I arrive, I make a beeline for my room and collapse onto my bed."
    
    #time pass
    $renpy.pause(1)
    play ambient "audio/ambience/Morning.ogg" fadein 1
    $renpy.pause(1)
    scene bg homekaito myroom day with fade
    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 3
    
    "Bright sunlight shines on my face and I slowly blink my eyes open. Then I jolt upright in bed. {w}What time is it?! Did I miss the coaching session?"
    "I fumble around looking for my clock, but it's only 11 AM. Coach Ivan won't arrive until mid-afternoon. I have plenty of time!"
    "In that case, I wonder if anyone is free..."
    
    #Afternoon
    $ freeTime = "afternoon"
    
    call E4FreeTime from _call_E4FreeTime_1
    
    jump E4D3S2
