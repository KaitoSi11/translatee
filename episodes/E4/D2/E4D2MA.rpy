#
label E4D2MA:
    
    show mayu smi at cc with dissolve:
        xzoom 0.75
        yzoom 0.75
    "As I glance around the group, everyone seems to be focused on the greenery around us… especially Mayu. She kneels beside a large yellow Chrysanthemum and inspects its layered petals."
    "The guide finishes his spiel about some other flower or something and leads the group further down the path. Mayu isn't paying attention and continues to look at the flowers."
    pf "Mayu!"
    hide mayu with dissolve
    "She begins to stir, and I wait for her to rejoin us, but to my surprise she steps off the path to examine another flower! She must not have heard me."
    
    menu:
        "She'll come back herself.":
            "I shrug it off and catch up with the group. Mayu won't stray far and she'll come back as soon as she's finished with whatever she's doing."
            scene black with fade
            jump E4D2S2
        
        "Go after her!":
            "She might get lost if I don't go after her!"
            show mayu neu at cc with dissolve:
                xzoom 0.75
                yzoom 0.75
            "I slip away from the group and jog up to Mayu. She's ventured into a patch of bright yellow Chrysanthemums. I'm a couple of steps behind her when I call out again."
            stop music fadeout 5
            pf "Mayu!"
            show exclamation:
                xoffset 800
                yoffset 135
                xzoom .5
                yzoom .5
            show mayu sur
            voice "audio/voice/E4/Mayu/D2/Mayu D2-04.ogg"
            ma "Ah!"
            "She jumps in surprise and whirls around to face me. Unfortunately, she trips over her own feet and is precariously close to falling on her face!"
    
            if MCStory == 1:
                show mayu sur b1 at cc with dissolve:
                    xzoom 1
                    yzoom 1
                "Instinctively, I step in and catch her in my arms."
                jump E4D2MA_Win
            
            else:
                # QTE
                $ qtebase = 3
                $ qtetotal = qteath + qtebase
                $ t_var = qtetotal
                show screen timer_scr(place="E4D2MA_Freeze")
                
                menu:
                    "Catch!":
                        $ renpy.hide_screen ("timer_scr")
                        show mayu sur b1 at cc with dissolve:
                            xzoom 1
                            yzoom 1
                        "Instinctively, I step in and catch her in my arms."
                        jump E4D2MA_Win
                    
                    "Freeze...":
                        label E4D2MA_Freeze:
                            $ renpy.hide_screen ("timer_scr")
                            "I'm too slow to react and watch as Mayu catches herself with her hands."
                            jump E4D2MA_Fail
                    
                    "Watch...":
                        $ renpy.hide_screen ("timer_scr")
                        "I watch as Mayu catches herself with her hands."
                        jump E4D2MA_Fail
            
            label E4D2MA_Fail:
                play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 5
                show mayu wor b1 at cc with dissolve:
                    xzoom 1
                    yzoom 1
                "Mayu's face is bright red as I help her to her feet. She brushes yellow pollen and petals off of her clothes."
                pf "Are you okay?"
                show mayu ner b1
                voice "audio/voice/E4/Mayu/D2/Mayu D2-05.ogg"
                ma "Yeah, s-sorry…"
                "She looks helplessly at the small patch of crushed flowers."
                show panic:
                    xoffset 720
                    yoffset 135
                    xzoom .75
                    yzoom .75
                show mayu wor b1
                voice "audio/voice/E4/Mayu/D2/Mayu D2-06.ogg"
                ma "Oh no! Do you think anyone will notice?"
                pf "Uhhh…"
                "It looks like a bald spot on a blonde head."
                pf "Let's go with no... but we might want to go back now."
                show mayu ner b1
                "She nods and I offer her my hand. She blushes, but takes it and we quickly return to the group."
                scene black with fade
                jump E4D2S2
            
            label E4D2MA_Win:
                play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 5
                show dots:
                    xoffset 720
                    yoffset 135
                    xzoom .75
                    yzoom .75
                show mayu sur b2
                "Mayu looks up at me with wide eyes then quickly looks away as her cheeks burn red."
                show mayu ner b2
                voice "audio/voice/E4/Mayu/D2/Mayu D2-07.ogg"
                ma "Thank you."
                "I help steady her on her feet."
                pf "No problem. Are you okay?"
                show mayu smi b2
                "She nods, then looks back up at me, her eyes glittering."
                voice "audio/voice/E4/Mayu/D2/Mayu D2-08.ogg"
                ma "Y-You saved me!"
                pf "Oh, uh, I'm not sure I would go that far."
                show mayu hap b2
                voice "audio/voice/E4/Mayu/D2/Mayu D2-09.ogg"
                ma "No, you did!"
                "She seems pretty adamant."
                pf "Umm... okay."
                show mayu smi b2
                voice "audio/voice/E4/Mayu/D2/Mayu D2-10.ogg"
                ma "A-And in the books, the hero always gets a reward…"
                pf "Uh..."
                show regBlush:
                    xoffset 720
                    yoffset 135
                    xzoom .75
                    yzoom .75
                "Mayu quickly gets up on her toes and pecks me on the lips. I blink in surprise. Her face is bright red but she wears a small smile."
                "I can't help but grin and pull her into a hug."
                pf "I'll have to save you more often."
                #black screen
                scene black with fade
                "We spent some time together before rejoining the group."
                
                jump E4D2S2
