#
label E3_5S2:
    
    #EPISODE 3.5 (October 30th)
    $ nikOut = "sCasual2"
    $ nikHairF = "pony"
    $ nikHairB = "pony"
    $ kaiOut = "sWork"
    $renpy.pause(1)
    play music "audio/music/Open Road (GAME VERSION).ogg" fadein 3
    scene bg travel openroad dusk with Dissolve(1.5)
    "It's been two weeks since the Ex Zee concert and my conversation with Uncle Kaito. In that time, my team is still undefeated and stronger than ever. Kaori, Shou, Mayu and I put in extra hours of practice as we prepare ourselves for more difficult opponents."
    
    if mayrelatonship == 1:
        "Things have been going amazingly well between Mayu and I. {w}After the incident with her letter, the next time we saw each other was a little awkward. We knew our relationship had changed, but we weren't sure how and it made both us self-conscious and unsure how to act around each other."
        "The more time we spent together, the more we relaxed. We realised our relationship is still the same, just better. Every time I'm with her, I feel lucky to have her."
    
    elif yuurelatonship == 1:
        "Things have been going amazingly well between Yuuna and I. She passed her English speaking exam with flying colours, and now we practice \"oral\" all the time. {w}Lately, she's improved immensely and we try to use English as often as possible."
        "I hadn't realised how much I missed speaking English until now. It's nice to have a partner to chat with… When I'm with her, I'm reminded of home."
    
    elif kaorelatonship == 1:
        "Things have been going amazingly well between Kaori and I. Ever since I showed up unannounced in her room, Kaori has been non-stop sending me health tips and recipes. I can't tell if she's trying to hint at something or if she's just sharing another interest with me."
        "Either way, I use it to my advantage and get delicious Kaori-made bentos whenever I ask for samples of her recipes. I'm sure she's caught on that I just want to eat her cooking, but she doesn't seem to mind."
    
    elif valrelatonship == 1:
        "Things have been going amazingly well between Valerie and I. After our adventure in the mall, Valerie is not shy about showing her affection for me, much to the embarrassment of those around us."
        "She also keeps the sketch I drew of her on her desk. She says it inspires her whenever she has \"artist's block\". We've had plenty of modeling sessions since. Needless to say, our experiences as a couple has been full of \"bonheur\"."
    
    elif E3SSS3_Completed== 1:
        "Things have been going well with Shou, even after the incident with his brother. Although, I still think about that day, Shou acts as if it never happened."
        "Since he doesn't bring it up, I don't talk about it either, and we continue to hang out like usual."
    
    "Nikki is up to her usual tricks in the kitchen. When they were short-staffed at the cafe, Nikki finally had her chance to show off her skills as a cook. She impressed the chef so much that she no longer has to spend her time washing dishes! {w}Of course, with greater responsibility comes longer hours at work."
    
    "Uncle Kaito has been working harder than ever. This last week in particular he's been leaving the house earlier in the morning and coming home way past midnight."
    
    if MCStory == 3:
        "I have a feeling it's not just work that's keeping him busy… Maybe he's started to reconcile his relationship with a certain favourite aunt…"
    
    else:
        "Work must be treating him {i}very{/i} well because whenever I see him he has a bright smile on his face."
        
    stop music fadeout 3
    $renpy.pause(1)
    #start scene
    play ambient "audio/ambience/Night Crickets.ogg" fadein 3
    scene bg homekaito main night with fade
    "Tonight is one of those rare nights when both Nikki and Uncle Kaito are off work and I have no plans. {w}After devouring the delicious meal that Nikki made, I'm happily nursing my food baby while Uncle Kaito clears the dishes."
    play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 3
    "Nikki sighs heavily and slumps on the table."
    show nikki sad at l2 with dissolve
    voice "audio/voice/E4/Nikki/Day 0/Nikki_04_001.ogg"
    sf "I can't believe that nobody here really celebrates Halloween."
    "I think about the Halloween party I'm supposed to attend tomorrow."
    pf "Uh, yeah they do…"
    show nikki thi
    voice "audio/voice/E4/Nikki/Day 0/Nikki_04_002.ogg"
    sf "Well, sort of. They don't decorate, though!"
    "I sigh wistfully."
    pf "That's true."
    show nikki mis
    "Nikki snorts."
    voice "audio/voice/E4/Nikki/Day 0/Nikki_04_003.ogg"
    sf "I bet all you really care about are the slutty costume parties."
    
    menu:
        "No, I like the decorations best.":
            pf "Actually, my favourite part of Halloween was watching our town turn into a spooky graveyard or haunted house."
            show nikki hap
            show note:
                xoffset 365
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E4/Nikki/Day 0/Nikki_04_004.ogg"
            sf "Oh yeah! Dad used to go all out with decorating. It was fun, but those fake cobwebs are surprisingly sticky…"
            pf "Yeah, somehow they'd get caught in everything."
    
        "Who doesn't miss that?":
            "I sigh happily. I had no idea so many things were sexy... Like a lobster, a rat, a lampshade…"
            pf "I plead the 5th."
            show nikki ske
            "Nikki raises an eyebrow."
            show drop:
                xoffset 365
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E4/Nikki/Day 0/Nikki_04_005.ogg"
            sf "You can't plead the 5th in Japan."
            "Damn, she has a point."
            pf "...I plead the Japanese equivalent of the 5th...?"
    
        "Halloween is lame without candy.":
            pf "I miss trick-or-treating. Buying your own candy just isn't the same."
            show nikki cur
            "Nikki has a faraway look in her eyes."
            show shiny:
                xoffset 365
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E4/Nikki/Day 0/Nikki_04_006.ogg"
            sf "All those peanut butter cuppes…"
    
        "Halloween blows.":
            pf "I never understood the appeal of Halloween. It's so juvenile."
            show nikki dis
            show storm:
                xoffset 365
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E4/Nikki/Day 0/Nikki_04_007.ogg"
            sf "Whatever, party pooper."
            
    show kaito ske at r2 with dissolve:
        xzoom -1
    "Uncle Kaito sits down and looks intrigued yet confused."
    voice "audio/voice/E4/Kaito/d00/(19).ogg"
    hk "Is that really a tradition?"
    show nikki neu
    voice "audio/voice/E4/Nikki/Day 0/Nikki_04_008.ogg"
    sf "Yup."
    show kaito neu
    voice "audio/voice/E4/Kaito/d00/(20).ogg"
    hk "Interesting…"
    show nikki smi
    voice "audio/voice/E4/Nikki/Day 0/Nikki_04_009.ogg"
    sf "But that's not the best part of Halloween!"
    show question:
        xoffset 1040
        yoffset 5
        xzoom .75
        yzoom .75
    show kaito cur
    voice "audio/voice/E4/Kaito/d00/(21).ogg"
    hk "No?"
    pf "Yes, it is."
    show nikki dis
    "Nikki glares at me."
    voice "audio/voice/E4/Nikki/Day 0/Nikki_04_010.ogg"
    sf "No, the best part about Halloween are pumpkins!"
    show kaito neu
    show nikki smi
    voice "audio/voice/E4/Nikki/Day 0/Nikki_04_011.ogg"
    sf "More specifically, jack-o-lanterns!"
    pf "Oh yeah! Carving pumpkins with Mom was both fun and frustrating."
    show nikki hap
    voice "audio/voice/E4/Nikki/Day 0/Nikki_04_012.ogg"
    sf "It's because she was just SO good at it! I mean, ridiculously good."
    pf "Remember that one time she carved the headless horseman in her pumpkin?"
    show nikki smi
    "Nikki laughs."
    voice "audio/voice/E4/Nikki/Day 0/Nikki_04_013.ogg"
    sf "Yes! I had been so proud of my pumpkin because I carved vampire fangs instead of square teeth."
    pf "You yelled at Mom for cheating and cried until she promised to carve another one with you."
    show nikki sur
    voice "audio/voice/E4/Nikki/Day 0/Nikki_04_014.ogg"
    sf "I didn't cry!"
    pf "Yeah, you did."
    show kaito mis
    show nikki smi
    voice "audio/voice/E4/Nikki/Day 0/Nikki_04_015.ogg"
    sf "Well, my pumpkin still ended up being better than yours."
    pf "Says you."
    show nikki mis
    voice "audio/voice/E4/Nikki/Day 0/Nikki_04_016.ogg"
    sf "You think you can do better?"
    pf "Please, your pumpkins could never compete with mine."
    show nikki neu
    "Uncle Kaito had been laughing while listening to us banter, but he finally interjects."
    show kaito smi
    voice "audio/voice/E4/Kaito/d00/(22).ogg"
    hk "Actually, your mom wasn't the only person in this family with amazing art skills. I bet my carving skills could outdo even your mom's."
    show nikki mis
    "Nikki grins."
    voice "audio/voice/E4/Nikki/Day 0/Nikki_04_017.ogg"
    sf "That's a pretty serious claim."
    pf "There's only one way to find out…"
    show kaito hap
    voice "audio/voice/E4/Kaito/d00/(23).ogg"
    hk "Where are my keys? I'll go buy the pumpkins."
    hide kaito
    hide nikki
    with dissolve
    "Kaito changes out of his suit and runs to the store. Meanwhile, Nikki and I scrounge around the house for some carving knives and old newspapers."
    scene black with fade
    jump E3_5S3

