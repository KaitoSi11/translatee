#
label E3KIS2:
    
    #Evening (only possible evening = Day 3)
    
    $ kaoOut = "sUniform"
    
    "The match against Onna-Bugeisha lingers in my mind. I've watched some replays of their past matches and they are predominantly a melee oriented team. My best practice against them would be to practice with Kaori in Aura."
    play sound "audio/sfx/Technology/Phone Dial.ogg"
    scene black with fade
    stop ambient fadeout 3
    $renpy.pause(2)
    "She doesn't answer when I call, but I make my way to the Hangar anyway. When I arrive, I see Kaori is already in a simulation match. No wonder she's not answering her phone. {w}After grabbing her attention, she agrees to play against me. I boot up Eagle and enter into a simulation with Aura." 
    
    #timeskip?
    $renpy.pause(1)
    "..."
    play music "audio/music/Rivals (GAME VERSION).ogg" fadein 5
    "...."
    scene bg battleground day with fade
    show kaori mech at br
    show mc mech at bl:
        xzoom -1
    with dissolve
    voice "audio/voice/E3/Free/KI/S2/kaori/Date_Kaori_55.ogg"
    ki "Hyaaah!"
    show kaori att with dissolve
    "Aura thrusts forward with an aggressive stab!"
    
    #QTE
    $ qtebase = 3
    $ qtetotal = qteath + qtebase
    $ t_var = qtetotal
    show screen timer_scr(place="E3KIS2_Juke")
    
    menu:
        "Dodge Easily!":
            jump E3KIS2_Juke
        "Move out of the way!":
            jump E3KIS2_Juke
        "Thrust backward!":
            jump E3KIS2_Juke
        "Juke City!":
            label E3KIS2_Juke:
                $ renpy.hide_screen ("timer_scr")
                "I easily dodge her attack. Her GEAR loses balance and stumbles forward."
    
    menu:
        "Counter-attack!":
            show mc ready with dissolve
            "Eagle uses counter-attack."
            
    show kaori att at mm, Shake(None, .25, dist=15) with Dissolve(.25)
    play sound "audio/sfx/GEAR Combat/Depower.ogg"
    show kaori mech at mm, Shake(None, .25, dist=15) with Dissolve(.25)
    $renpy.pause(0.5)
    "It's super effective!"
    hide kaori with dissolve
    "Aura has fainted."
    "...I mean, has been depowered."
    stop music fadeout 3
    voice "audio/voice/E3/Free/KI/S2/kaori/Date_Kaori_56.ogg"
    ki "Again?!"
    play ambient "audio/ambience/GEAR Cockpit.ogg" fadein 3
    show cg GEAR cockpit first3 with dissolve:
        xzoom 0.5
        yzoom 0.5
    "Kaori's frustration is audible through the comm. This marks her fourth consecutive loss. She's playing too aggressively and not planning out any tactics."
    pf "Let's take a break."
    voice "audio/voice/E3/Free/KI/S2/kaori/Date_Kaori_57.ogg"
    ki "No, we need to keep practicing."
    
    menu:
        "I'd like to take a break for a minute.":
            pf "I need to get a drink. We can continue after."
            voice "audio/voice/E3/Free/KI/S2/kaori/Date_Kaori_58.ogg"
            ki "...Fine."
    
        "This isn't really {i}practice{/i} for me.":
            pf "Yeah, I don't know if these duels can really be considered training."
            voice "audio/voice/E3/Free/KI/S2/kaori/Date_Kaori_59.ogg"
            ki "What's that suppose to mean?"
            pf "Look at the scoreboard and you tell me."
            ki "..."
            pf "Anyways, I didn't say I wouldn't do more matches. Let's just take a small break to recharge and we'll continue."
            voice "audio/voice/E3/Free/KI/S2/kaori/Date_Kaori_60.ogg"
            ki "Okay, fine."
    
        "No, you are sucking too much.":
            pf "Yeah, forget that. I'm going to go play AI's. At least they'll pose a challenge."
            voice "audio/voice/E3/Free/KI/S2/kaori/Date_Kaori_61.ogg"
            ki "W-What did you say?!"
            pf "You heard me."
            voice "audio/voice/E3/Free/KI/S2/kaori/Date_Kaori_62.ogg"
            ki "You are being a serious ass right now."
            pf "And you are wasting both of our time. So either take a break or I'll go practice against AIs."
            voice "audio/voice/E3/Free/KI/S2/kaori/Date_Kaori_63.ogg"
            ki "Fine, we'll take a stupid break then."
            
    scene black with fade
    stop ambient fadeout 3
    "Aura disconnects from our virtual simulation. I do the same, then hop out of my cockpit and reconvene with Kaori at her GEAR."
    
    play ambient "audio/ambience/Hangar.ogg" fadein 3
    scene bg campus hangar day with fade
    show kaori dis at cc with dissolve
    play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 3
    "Her arms are crossed and she has a sour look on her face."
    pf "Kaori."
    show kaori cur
    "She looks up at me."
    
    if E2KIS4_Completed == 1:
        pf "Hi."
        show dots:
            xoffset 720
            yoffset 110
            xzoom .75
            yzoom .75
        show kaori neu
        "She blinks at me rapidly before her arms fall her side and she sighs."
        show kaori thi
        voice "audio/voice/E3/Free/KI/S2/kaori/Date_Kaori_64.ogg"
        ki "...Hi."
        pf "I know better than to ask if you're okay... but..."
        show kaori neu
        voice "audio/voice/E3/Free/KI/S2/kaori/Date_Kaori_65.ogg"
        ki "Yes, I am. Sorry about earlier."
        pf "No, it's okay."
        show kaori smi
        if MCStory == 3:
            "Her body relaxes and she takes a more welcoming posture. I think she's pleased by how I brought that up."
    
    else:
        pf "I'm not sure what that was all about, but we can't have that happen in a real match."
        show kaori thi
        voice "audio/voice/E3/Free/KI/S2/kaori/Date_Kaori_66.ogg"
        ki "You think I don't know that?"
        "She looks annoyed, but sighs anyway."
        
    voice "audio/voice/E3/Free/KI/S2/kaori/Date_Kaori_67.ogg"
    ki "It's just, we absolutely can't lose to Onna-Bugeisha!"
    menu:
        "We won't.":
            pf "Don't worry. Let's not forget we are currently an undefeated team."
            show kaori neu
            "Kaori's nods slowly."
            ### VOICE - "newly found team"?
            voice "audio/voice/E3/Free/KI/S2/kaori/Date_Kaori_68.ogg"
            ki "As a newly formed team, I'm honestly a little surprised by our hot streak."
            pf "And we're keeping that streak going, right?"
            show note:
                xoffset 720
                yoffset 110
                xzoom .75
                yzoom .75
            show kaori mis
            voice "audio/voice/E3/Free/KI/S2/kaori/Date_Kaori_69.ogg"
            ki "Of course! Not even Mei can ruin this for us!"
            "I blink at her. Where did that come from? {w}Regardless, her mood certainly seems to be lifted."
    
        "What's the big deal anyway?":
            pf "What's so important about beating Mei's team?"
            show kaori ann
            voice "audio/voice/E3/Free/KI/S2/kaori/Date_Kaori_70.ogg"
            ki "It's nothing to do with Mei!"
            "I blink at her heated reaction."
            pf "Uh, I never said it did…"
            voice "audio/voice/E3/Free/KI/S2/kaori/Date_Kaori_71.ogg"
            ki "With StrikeX being disqualified from our original match, we have a rare chance to really jump our rating if we beat Onna-Bugeisha."
    
            if MCStory == 2:
                "That makes a lot of sense. Our MMR will get a hefty boost if we win."
    
            "I'm not fully convinced that's the only reason, but she does have a point!"
            pf "Then we'll give it our all!"
            show kaori smi
            "Kaori nods. Her spirits seem to be lifted."
    
        "Then get your head in the game.":
            pf "All we have to do is focus and formulate a solid plan like we always do."
            show kaori neu
            voice "audio/voice/E3/Free/KI/S2/kaori/Date_Kaori_72.ogg"
            ki "Agreed."
            pf "So it doesn't matter that it's Mei's team."
            show note:
                xoffset 720
                yoffset 110
                xzoom .75
                yzoom .75
            show kaori mis
            ### VOICE - missing line
            voice "audio/voice/MISSING/BATCH5/k_redo_04.ogg"
            ki "Agreed! Mei doesn't matter at all!"
            show kaori cur
            "I stare at her. She seems just as shocked as I am by her outburst."
            show dots:
                xoffset 720
                yoffset 110
                xzoom .75
                yzoom .75
            ki "..."
            show kaori neu
            pf "Okay, random outburst aside, that means no unnecessary aggressive play. When we practice, we treat it like it's the real deal."
            show kaori smi
            ### VOICE - missing line
            ki "...Agreed."
    
    pf "I'm glad we got that sorted out."
    show kaori neu
    "Kaori nods but can't quite hide her yawn. She covers her mouth and after taking another look at her, I notice bags under her eyes. It looks like she used makeup to cover it up so I wouldn't notice."
    
    menu:
        "Kaori wears make-up?!":
            pf "Wow, I can't believe I never noticed you wear make-up."
            show kaori ske b1
            "Kaori is caught off guard."
            voice "audio/voice/E3/Free/KI/S2/kaori/Date_Kaori_73.ogg"
            ki "W-Wha? Huh? Why does it even--why are you even bringing that up?!"
            pf "No don't get me wrong, you look great!"
            show kaori ann b1
            voice "audio/voice/E3/Free/KI/S2/kaori/Date_Kaori_74.ogg"
            ki "Stop looking at me like that!"
            pf "Like what?! My thoughts are innocent and pure!"
            show kaori ang b1
            voice "audio/voice/E3/Free/KI/S2/kaori/Date_Kaori_75.ogg"
            ki "Like hell they are!"
            # sfx
            # screen shake?
            show kaori ann b2
            "She slugs me in the arm. Her face is super red."
            pf "Ow! Why do you always resort to violence..."
            show tsuBlush:
                xoffset 720
                yoffset 110
                xzoom .75
                yzoom .75
            voice "audio/voice/E3/Free/KI/S2/kaori/Date_Kaori_76.ogg"
            ki "I have to with idiots like you."
            show kaori thi b1
            "She spins around before I can say anything else."
            voice "audio/voice/E3/Free/KI/S2/kaori/Date_Kaori_77.ogg"
            ki "A-Anyway, let's go back to practicing."
            pf "Okay..."
    
        "Someone stayed up all night!":
            pf "I knew it! You're a closet party girl! We should hang out together if you want to do the nightlife scene."
            show kaori ske
            voice "audio/voice/E3/Free/KI/S2/kaori/Date_Kaori_78.ogg"
            ki "Seriously, how can you still be this dumb after all this time?"
            pf "Don't lie. I can see the bags under your eyes."
            show vein:
                xoffset 720
                yoffset 110
                xzoom .75
                yzoom .75
            show kaori ang
            voice "audio/voice/E3/Free/KI/S2/kaori/Date_Kaori_79.ogg"
            ki "What bags?!"
            show kaori ann
            pf "Someone's not been getting their beauty sleep. Actually, now that I think about it, that explains why you're cranky all the time too--"
            # sfx
            # screen shake?
            "{i}WHAM{/i}!"
            "I rub my fresh bruise, already used to her doing this."
            pf "I thought you were tired. Where did all that energy come from?"
            show kaori dis
            voice "audio/voice/E3/Free/KI/S2/kaori/Date_Kaori_80.ogg"
            ki "Let's get back to practicing."
            pf "You're the boss!"
    
        "I'm worried about you." if E2KIS4_Completed == 1:
            pf "We've been over this Kaori. You have to take care of yourself or you'll get sick."
            show kaori ske
            voice "audio/voice/MISSING/BATCH5/k_redo_06.ogg"
            ki "What are you talking about?"
            pf "The yawn, the bags under your eyes..."
            show kaori dis
            "Kaori shakes her head."
            voice "audio/voice/E3/Free/KI/S2/kaori/Date_Kaori_81.ogg"
            ki "I'm fine."
            "I cross my arms and look at her sternly."
            show dots:
                xoffset 720
                yoffset 110
                xzoom .75
                yzoom .75
            ki "..."
            "My look doesn't change."
            show kaori thi
            voice "audio/voice/E3/Free/KI/S2/kaori/Date_Kaori_82.ogg"
            ki "Okay, maybe I spent a little extra time at the daycare this week. And brought some marking work home."
            pf "And how long did you stay up doing that?"
            show kaori neu
            voice "audio/voice/E3/Free/KI/S2/kaori/Date_Kaori_83.ogg"
            ki "Just until like 2:00AM. It really wasn't that bad."
            pf "2:00AM?!"
            show kaori ske
            voice "audio/voice/E3/Free/KI/S2/kaori/Date_Kaori_84.ogg"
            ki "I don't know why you're making this into such a big deal! Stop worrying about me!"
            pf "I can't stop worrying about you!"
            show kaori cur b1
            "Kaori blinks. I just realise how that sounded."
    
            menu:
                "I mean as my teammate.":
                    pf "I-I mean as my teammate, because, you know, you are on the starting 4 on the team and we don't have a backup."
                    show kaori neu b1
                    "Kaori nods rapidly."
                    voice "audio/voice/E3/Free/KI/S2/kaori/Date_Kaori_85.ogg"
                    ki "Y-Yes, I see what you are saying. You are correct. That would be, um, bad. I will look into... rectifying my situation."
                    pf "Good."
                    show kaori thi b1
                    voice "audio/voice/E3/Free/KI/S2/kaori/Date_Kaori_86.ogg"
                    ki "Good!"
                    "..."
                    "This is getting awkward..."
                    show kaori neu b1
                    voice "audio/voice/E3/Free/KI/S2/kaori/Date_Kaori_87.ogg"
                    ki "Let's get back to practicing!"
                    pf "Yes!"
    
                "That's exactly what I meant.":
                    "Kaori waits for me to correct myself, but I don't. She furrows her brow, and seems a little confused by how to respond."
                    show kaori thi b2
                    voice "audio/voice/E3/Free/KI/S2/kaori/Date_Kaori_88.ogg"
                    ki "If I do, will you stop... umm.."
                    show tsuBlush:
                        xoffset 720
                        yoffset 110
                        xzoom .75
                        yzoom .75
                    voice "audio/voice/E3/Free/KI/S2/kaori/Date_Kaori_89.ogg"
                    ki "{i}Annoying{/i} me so much about it?"
                    "She's starting to sound like herself again."
                    pf "Yes."
                    show kaori ske b2
                    voice "audio/voice/E3/Free/KI/S2/kaori/Date_Kaori_90.ogg"
                    ki "Okay, but I'd only be doing it so you stop pestering me!"
                    "I smile."
                    pf "Works for me. Should we get back to training?"
                    show kaori neu b1
                    voice "audio/voice/E3/Free/KI/S2/kaori/Date_Kaori_91.ogg"
                    ki "Yes, of course."
    
                "Don't comment.":
                    pf "Alright, let's get back to practicing."
                    show kaori neu b1
                    voice "audio/voice/E3/Free/KI/S2/kaori/Date_Kaori_92.ogg"
                    ki "Yeah..."
                    
    hide kaori with dissolve
    scene black with fade
    stop ambient fadeout 5
    "We head back into our GEARs and load up another simulation match. Kaori is more focused than before and no longer making such rash decisions. {w}Ultimately, we end up getting a solid training session from our duels."
    stop music fadeout 3
    "Before long, it becomes late and we say our goodbyes before heading home."
    
    # end
    $ E3KIS2_Completed = 1
    
