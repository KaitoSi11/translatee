#
label E4D2KI:
    
    "As I glance around the group, everyone seems to be focused on the greenery around us. I scan the field of flowers and I'm impressed by the size and scope of the garden. It seems to go on forever!"
    "While we meander along, I spot a few trees with low hanging branches full of ripe berries a few paces off of the path. My stomach growls in response." 
    
    menu:
        "Don't eat them.":
            "Shut up, stomach! We don't know if those berries are poisonous. It would be smarter to wait until we're done with the tour to get food."
        
        "Yummy in my tummy!":
            "I surreptitiously check to make sure no one is watching. Satisfied, I sneak off the path and head straight for the trees. The plump berries are a bright shade of red and my mouth waters at the thought of eating them."
            stop music fadeout 3
            "I pick a handful and I'm about to put them in my mouth when somebody slaps them right out of my hand!"
            # screen shake?
            # sfx? slap
            pf "Ow!"
            play music "audio/music/Baka! (GAME VERSION).ogg" fadein 3
            show kaori ann at cc with dissolve
            "I look over to see Kaori scowling at me."
            pf "What'd you do that for?"
            voice "audio/voice/E4/Kaori/D2/Kaori_20_d1.ogg"
            ki "You can't just shove the first thing you see into your mouth!"
            "I snort as I try to hold back a retort. Kaori does not seem amused."
            show vein:
                xoffset 720
                yoffset 110
                xzoom .75
                yzoom .75
            show kaori ang
            voice "audio/voice/E4/Kaori/D2/Kaori_21_d1.ogg"
            ki "You have to pay attention. They might be poisonous!"
            show kaori ann
            "I don't even bother holding back this laugh."
            pf "Kaori, why would a beautiful garden like this, frequented by all types of people, including children, have poisonous berries?"
            show kaori dis
            "Instead of answering, Kaori points to a sign posted beneath the tree."
            "{i}Danger! Do not eat!{/i}"
            pf "Oh…"
            show kaori mis
            "Kaori crosses her arms, but wears a satisfied smirk."
            pf "They should post that sign up higher. Who's going to see it so close to the ground?"
            stop music fadeout 5
            voice "audio/voice/E4/Kaori/D2/Kaori_22_d1.ogg"
            ki "Children--the ones who are most likely to eat things they shouldn't."
            "Touché."
            #play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 5
            "I look at Kaori again, and smile. Of course she'd be the one to notice I'm away. As much as she pretends not to care, I'm still surprised by what a big heart she has. {w}Kaori frowns."
            show kaori ske
            voice "audio/voice/E4/Kaori/D2/Kaori_23_d1.ogg"
            ki "Why are you looking at me like that?"
            pf "I had no idea you cared so much about me."
            show kaori cur b1
            "She blinks in surprise, then looks away as her cheeks turn pink."
            show kaori thi b1
            voice "audio/voice/E4/Kaori/D2/Kaori_24_d1.ogg"
            ki "I don't. I just don't want you to die yet… not until we've played our last match for the semester."
            "My smile broadens at her response."
            play music "audio/music/After a Long Day (GAME VERSION).ogg" fadein 5
            pf "That's a strange way to show your affection."
            show kaori thi b2 with dissolve
            "Her blush deepens."
            show tsuBlush:
                xoffset 720
                yoffset 110
                xzoom .75
                yzoom .75
            voice "audio/voice/E4/Kaori/D2/Kaori_25_d1.ogg"
            ki "D-Don't be stupid!"
            
            menu:
                "Let me show you what affection is.":
                    show kaori cur b2
                    "Our lips lock in a passionate kiss and I scoop her into my embrace."
                    show kaori smi b3 with dissolve
                    "At first, Kaori tenses up in surprise but then quickly melts into the kiss. She slowly pulls away and tries to catch her breath. Her face is bright red, but a broad smile is on her lips."
                    pf "That is how you show affection."
                    show heart:
                        xoffset 720
                        yoffset 110
                        xzoom .75
                        yzoom .75
                    "She playfully hits my arm, but laughs anyway."
                    #black screen
                    scene black with fade
                    "We spent some time together before rejoining the group."
                
                "That's enough excitement for one day.":
                    stop music fadeout 3
                    "I can't hold back my smile. She's so cute when she's flustered."
                    voice "audio/voice/E4/Kaori/D2/Kaori_26_d1.ogg"
                    ki "Let's get back to the group before they notice we're gone."
                    show kaori cur b2
                    "I nod and take her hand in mine as I begin to lead us back on the path. She blinks in surprise, and turns her head so I don't see her blush but doesn't pull away."
                    scene black with fade
                    "Soon we return to the group."
                    
            stop music fadeout 1.5
                    
    jump E4D2S2
