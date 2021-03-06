#
label E3D4S1:
    
    $ kaoHairF = "default"
    $ kaoHairB = kaoHairF
    $ kaoOut = "sUniform"
    
    $ mayHairF = "default"
    $ mayHairB = mayHairF
    $ mayOut = "sUniform"
    
    $ nikHairF = "default"
    $ nikHairB = nikHairF
    $ nikOut = "sUniform"
    
    $ shoHairF = "default"
    $ shoHairB = shoHairF
    $ shoOut = "sUniform"
    
    $ valHairF = "default"
    $ valHairB = valHairF
    $ valOut = "sUniform"
    
    $ yuuHairF = "default"
    $ yuuHairB = yuuHairF
    $ yuuOut = "sUniform"
    
    $ meiHairB = "default"
    $ meiOut = "sUniform"
    $ meiHairF = "default"
    
    $ day = 4
    $ timeSpent = "none"
    $renpy.pause(1)
    play ambient "audio/ambience/Morning.ogg" fadein 1
    $renpy.pause(1)
    #beep beep beep
    play sound [ "audio/sfx/Technology/Phone Alarm.ogg", "audio/sfx/Technology/Phone Alarm.ogg", "audio/sfx/Technology/Phone Alarm.ogg" ]
    $renpy.pause(2.5)
    stop sound
    scene bg homekaito myroom day with fade
    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 3
    
    "I wake up energized and throw off the blankets. Today is our match against Onna-Bugeisha and I'm looking forward to it. {w}I run through my morning routine, thinking up strategies in my head. Then try to refocus as I finish my breakfast. I still have a class to attend before my match." 

    stop ambient fadeout 3
    scene black with fade
    "I grab my bag and hop on my bike. {w}There is an unexpectedly heavy amount of traffic this morning and I rush into class right on time."
    play ambient "audio/ambience/Ace Academy Library.ogg" fadein 3
    scene bg campus auditorium day with fade
    "That was a little too close for comfort. {w}As I settle into my seat, the professor clears his throat, beginning the lesson."
    
    show professorM extra at cc with dissolve
    voice "audio/voice/E3/D4/S1/prof1m/1.ogg"
    prof1m "Good morning, class. For today's lesson, we will discuss the differences between energy and kinetic weapons."
    
    menu:
        "Sounds interesting!":
            voice "audio/voice/E3/D4/S1/prof1m/2.ogg"
            prof1m "Let's first review the two defensive mechanisms of a GEAR: the shield and hull."
            ### VOICE - missing line?
            prof1m "The hull is the physical GEAR."
            voice "audio/voice/E3/D4/S1/prof1m/3.ogg"
            prof1m "The shield is a virtually invisible barrier generated by using the core's energy. The strength of the shield varies greatly depending on the core, shield generator, and power allocation settings."
            voice "audio/voice/E3/D4/S1/prof1m/4.ogg"
            prof1m "Energy and kinetic weapons are meant to target opposite defenses. Energy based arsenals are effective against shields as they quickly drain shield energy, but because of that they are weak at penetrating the hull."
            voice "audio/voice/E3/D4/S1/prof1m/5.ogg"
            prof1m "Alternatively, kinetic weaponry is designed to puncture the armor, but they're weak against shields as the kinetic energy gets dispersed over a large surface area... the entire shield."
            voice "audio/voice/E3/D4/S1/prof1m/6.ogg"
            prof1m "For the purpose of wargames and recreational use, only energy weapons are permitted. A GEAR is considered destroyed when it is depowered. Of course, outside of recreational combat this rule does not apply."
            "A student raises his hand."
            voice "audio/voice/E3/D4/S1/stu2m/1.ogg"
            stu2m "What about hybrid weapons?"
            voice "audio/voice/E3/D4/S1/prof1m/7.ogg"
            prof1m "Ah, yes. Hybrid weapons are able to equally damage both the shield and hull. However, their damage strength is not as effective as a singular purpose weapon."
            "The student nods in acknowledgement."
            voice "audio/voice/E3/D4/S1/prof1m/8.ogg"
            prof1m "Please turn to page 233 and let's take a look at the different types of energy weapons..."
            "I flip to the page the professor mentioned and continue listening to the lesson."
    
    
        "Skip.":
            if MCStory == 2:
                "I already know this material. I can probably work on some other assignments during this time."
            else:
                "What an excellent opportunity for a power nap!"
    
            "I settle into my business and class passes by in a blur."
    
    stop music fadeout 5
    scene black with fade
    $renpy.pause(1)
    scene bg campus auditorium day with fade
    show professorM extra at cc with dissolve
    voice "audio/voice/E3/D4/S1/prof1m/9.ogg"
    prof1m "That's all for today. Please make sure you have all completed your weblink assignments for next class."
    play sound "audio/sfx/Human/Class End.ogg"
    "I pack my things and head to the Hangar to meet up with my team. Our match is scheduled earlier than usual and we need to rethink our strategy."
    "The plans we'd discussed had all revolved around our match against StrikeX, but now that they're disqualified, we have to come up with new ones against our new opponent."
    stop ambient fadeout 3
    #Black screen into hangar BG
    scene black with fade
    play ambient "audio/ambience/Hangar.ogg" fadein 3
    scene bg campus hangar day with fade
    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 5
    "I enter the Hangar and look for Aura. {w}When I arrive, everyone is already there. Shou waves."
    show kaori neu at r3:
        xzoom -1
    show mayu neu at l3
    show shou smi at cc
    with dissolve
    voice "audio/voice/E3/D4/S1/shou/1.ogg"
    ss "Broseph!"
    pf "Hey."
    show mayu smi
    voice "audio/voice/E3/D4/S1/mayu/Mayu-01.ogg"
    ma "Hi."
    
    show kaori smi
    "Kaori greets me with a nod."
    voice "audio/voice/E3/D4/S1/kaori/e3d4_Kao_01.ogg"
    ki "Good, we're all here. Let's head to the pre-combat room and start planning out strategies--"
    
    $ meiOut = "sUniform"
    show kaori cur
    show mayu neu
    show shou cur
    voice "audio/voice/E3/D4/S1/mei/MeiEp3_Line_15.ogg"
    ms "Hey!"
    show mei hap at r3:
        xoffset 200
        xzoom -1
    show kaori thi at r1:
        xzoom 1
    show shou neu at l1:
        xoffset -100
    show mayu neu at l3:
        xoffset -275
    with dissolve
    
    "We collectively turn at the sound of Mei's voice. She waves and beams at us as she runs closer."
    show question:
        xoffset 890
        yoffset 110
        xzoom .75
        yzoom .75
    show kaori ske
    voice "audio/voice/E3/D4/S1/kaori/e3d4_Kao_02.ogg"
    ki "What are you doing here, Mei?"
    show mei smi
    "Kaori sounds less than amused."
    show heart:
        xoffset 1375
        yoffset 100
        xzoom .75
        yzoom .75
    show mei hap
    ### VOICE - something's wrong with this line, it has like, a mis-take?
    voice "audio/voice/E3/D4/S1/mei/MeiEp3_Line_16.ogg"
    ms "I wanted to wish you all good luck! I'm so excited for our match!"
    show kaori dis
    show note:
        xoffset 415
        yoffset 20
        xzoom .75
        yzoom .75
    show shou hap
    voice "audio/voice/E3/D4/S1/shou/2.ogg"
    ss "Me too!"
    show mayu smi
    show mei smi
    "Mayu smiles and nods."
    
    menu:
        "Let's give it our best!":
            pf "Good luck to you guys too! We won't hold back."
            show mei mis
            show shou mis
            "Mei smiles."
            show note:
                xoffset 1375
                yoffset 100
                xzoom .75
                yzoom .75
            voice "audio/voice/E3/D4/S1/mei/MeiEp3_Line_17.ogg"
            ms "We won't either!"
    
        "Who needs luck when you're this good.":
            pf "Try and keep up. We wouldn't want a one sided match."
            show mei mis
            show shou mis
            "Mei grins."
            show note:
                xoffset 1375
                yoffset 100
                xzoom .75
                yzoom .75
            voice "audio/voice/E3/D4/S1/mei/MeiEp3_Line_18.ogg"
            ms "Don't underestimate us!"
    
        "Stay quiet.":
            show mei neu
            "I remain silent as does Kaori. Mei looks at the pair of us before shrugging."
            show drop:
                xoffset 1375
                yoffset 100
                xzoom .75
                yzoom .75
            show mei ske
            voice "audio/voice/E3/D4/S1/mei/MeiEp3_Line_19.ogg"
            ms "Okay... well... good luck again. I'll see you guys in the arena!"
            
    hide mei with dissolve
    "As quickly as she arrived, she's gone in a flash."
    show kaori neu at r3:
        xzoom -1
    show mayu smi at l3:
        xoffset 0
    show shou smi at cc:
        xoffset 0
    with dissolve
    voice "audio/voice/E3/D4/S1/shou/3.ogg"
    ss "She's so nice! I'm totally feeding off her enthusiasm. I'm getting a better vibe off of this match than the one off of StrikeX."
    show exclamation:
        xoffset 1175
        yoffset 110
        xzoom .75
        yzoom .75
    stop music fadeout 2
    show kaori ang
    voice "audio/voice/E3/D4/S1/kaori/e3d4_Kao_03.ogg"
    ki "No!"
    show kaori ann
    show mayu cur
    show shou cur
    "Shou blinks at Kaori's outburst."
    show question:
        xoffset 720
        yoffset 20
        xzoom .75
        yzoom .75
    show shou sad
    voice "audio/voice/E3/D4/S1/shou/4.ogg"
    ss "No?"
    show kaori ang
    show mayu neu
    play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 3
    voice "audio/voice/E3/D4/S1/kaori/e3d4_Kao_04.ogg"
    ki "She's just putting on an act. She was trying to psych us out. Don't fall for it!"
    show kaori ann
    show drop:
        xoffset 230
        yoffset 135
        xzoom .75
        yzoom .75
    show mayu thi
    show shou ske
    voice "audio/voice/E3/D4/S1/mayu/Mayu-02.ogg"
    ma "I don't think that was her goal..."
    show mayu neu
    show shou neu
    voice "audio/voice/E3/D4/S1/kaori/e3d4_Kao_05.ogg"
    ki "You guys don't know her like I do. You can't trust her... {i}especially{/i} when she's acting all friendly like that."
    
    if MCStory == 3:
        "I remember the heated conversation I overheard between Kaori and Mei. This must be related."
    
    else:
        "Kaori's been acting strange... more so than usual when Mei is involved."
        
    show kaori thi
    voice "audio/voice/E3/D4/S1/kaori/e3d4_Kao_06.ogg"
    ki "Anyways, let's go strategize while we still have time!"
    hide kaori with dissolve
    "She doesn't wait for us to answer and begins power walking towards the pre-combat rooms."
    show panic:
        xoffset 720
        yoffset 20
        xzoom .75
        yzoom .75
    show shou wor
    voice "audio/voice/E3/D4/S1/shou/5.ogg"
    ss "Hey! Wait for us!"
    hide mayu
    hide shou
    with dissolve
    stop music fadeout 3
    "We jog to catch up and follow her."
    stop ambient fadeout 3
    scene black with fade
    "After a quick change into our pilot suits, we meet at the holodesk."
    $renpy.pause(1.0)
    $ shoOut = "Pilot"
    $ mayOut = "Pilot"
    $ kaoOut = "Pilot"
    scene bg campus battleroom day
    play music "audio/music/Light Tension (GAME VERSION).ogg" fadein 5
    with dissolve
    
    show kaori neu at cc:
        xoffset 200
    with dissolve
    show mayu neu at r3:
        xoffset 200
        xzoom -1
    with dissolve
    show shou neu at l3:
        xoffset -150
    with dissolve
    "Kaori sets up the match. A few minutes later, the holodesk projects the arena and the GEARs involved in the fight."
    voice "audio/voice/E3/D4/S1/shou/6.ogg"
    ss "Alright, so what's the deal?"
    voice "audio/voice/E3/D4/S1/kaori/e3d4_Kao_07.ogg"
    ki "Onna-Bugeisha is a melee-only team. It will be important to pay attention to our positioning and maintain a safe distance."
    
    pf "We've had close combat teams in the past. Claw of the Wild comes to mind from a few weeks ago."
    #show shou cur
    #voice "audio/voice/E3/D4/S1/shou/7.ogg"
    #ss "Isn't that similar to our last match?"
    show mayu dis
    "Mayu is focused on the holodesk and takes a serious tone."
    show shou neu
    voice "audio/voice/E3/D4/S1/mayu/Mayu-03.ogg"
    ma "Claw of the Wild was a melee centric team but their GEARs were kitted to perform a hybrid role. Based on Onna-Bugeisha's data, their GEARs are all custom-tailored for high bursts of speed and close combat engagements."
    show mayu neu
    voice "audio/voice/E3/D4/S1/mayu/Mayu-04.ogg"
    ma "We would benefit greatly from keeping a distance. If we play defensively, it will force them to chase us and we can wear them down before going on the offense."
    show shou ske
    voice "audio/voice/E3/D4/S1/shou/8.ogg"
    ss "What do you think broseph?"
    
    $ E3D4S1_Brawl = 0
    
    menu:
        "Agreed, range is key.":
            pf "If they have no ranged weaponry, we should do as much damage from afar as we can. Whittling them down before fully engaging will give us the advantage."
            show shou smi
            voice "audio/voice/E3/D4/S1/shou/9.ogg"
            ss "Sounds good to me."
            show mayu smi
            "Mayu and Kaori both nod."
    
        "Let's go for a super smash melee brawl!":
            $ E3D4S1_Brawl = 1
            pf "I say we swap out our equipment and go full close quarters too. The true victors will be decided by steel!"
            show shiny:
                xoffset 80
                yoffset 20
                xzoom .75
                yzoom .75
            show shou mis
            voice "audio/voice/E3/D4/S1/shou/10.ogg"
            ss "Yeah! A battle of strength like true warriors!"
            show kaori dis
            show panic:
                xoffset 1375
                yoffset 135
                xzoom .75
                yzoom .75
            show mayu wor
            voice "audio/voice/E3/D4/S1/mayu/Mayu-05.ogg"
            ma "Um, Shou, you know Emerald is not really fit to handle melee weapons…"
            show shou thi
            "Shou scratches his head."
            voice "audio/voice/E3/D4/S1/shou/11.ogg"
            ss "Oh, yeah."
            show mayu ner
            show shou neu
            voice "audio/voice/E3/D4/S1/shou/12.ogg"
            ss "Sorry broseph, no can do."
            show kaori ann
            voice "audio/voice/E3/D4/S1/kaori/e3d4_Kao_08.ogg"
            ki "Why were you all \"Yeah!\" then?"
            show shou smi
            voice "audio/voice/E3/D4/S1/shou/13.ogg"
            ss "Can't you feel the passion flowing out of him? I got swept up in the hype."
            show drop:
                xoffset 920
                yoffset 110
                xzoom .75
                yzoom .75
            show kaori ske
            "Kaori raises an eyebrow."
            show storm:
                xoffset 1375
                yoffset 135
                xzoom .75
                yzoom .75
            show mayu thi
            show shou neu
            voice "audio/voice/E3/D4/S1/mayu/Mayu-06.ogg"
            ma "I can change my loadout for close combat engagements... but I still think we should use our tactical advantage of being ranged..."
            show kaori neu
            voice "audio/voice/E3/D4/S1/kaori/e3d4_Kao_09.ogg"
            ki "Mayu is right. We have to play our advantage and keep our distance. Besides, their entire team may only focus on melee engagements but we've been competing as a balanced setup."
            show kaori thi
            show mayu neu
            voice "audio/voice/E3/D4/S1/kaori/e3d4_Kao_10.ogg"
            ki "It would be stupid to try to brute force it and play out of our element."
    
    pf "Okay, well, we can all go range, but Aura can't..."
    "The team looks at Kaori."
    voice "audio/voice/E3/D4/S1/kaori/e3d4_Kao_11.ogg"
    ki "I'll engage Mei head on and keep her out of the fight."
    
    if E3D4S1_Brawl == 1:
        pf "Didn't we just decide going full force is a bad idea?"
    
    else:
        pf "That kind of goes against our plan."
    
    show kaori dis
    "To my surprise, Kaori grits her teeth and bites back a retort. She studies the holodesk for a little too long, then sighs."
    show storm:
        xoffset 920
        yoffset 110
        xzoom .75
        yzoom .75
    voice "audio/voice/E3/D4/S1/kaori/e3d4_Kao_12.ogg"
    ki "I guess I don't have much choice. I'll hang back with you guys and intercept if one of the enemy GEARs manages to break through."
    show mayu smi
    "Mayu nods."
    voice "audio/voice/E3/D4/S1/mayu/Mayu-07.ogg"
    ma "I think that would be best."
    show kaori neu
    voice "audio/voice/E3/D4/S1/kaori/e3d4_Kao_13.ogg"
    ki "Okay, let's recap:"
    show mayu neu
    voice "audio/voice/E3/D4/S1/kaori/e3d4_Kao_14.ogg"
    ki "We'll play it from a distance and keep baiting their team. Since Mayu is our best shot, we'll keep her well protected and follow her lead."
    show kaori dis
    "Kaori looks right at me. She finally looks more focused than I've seen her all week."
    voice "audio/voice/E3/D4/S1/kaori/e3d4_Kao_15.ogg"
    ki "You and Shou can play aggressively if we take the lead. I will intercept whoever reaches Mayu... if they even manage to."
    show kaori neu
    voice "audio/voice/E3/D4/S1/kaori/e3d4_Kao_16.ogg"
    ki "Got it?"
    
    "We all nod. The tension is palpable. Even though Kaori is always serious, her tone is more aggressive than usual."
    voice "audio/voice/E3/D4/S1/kaori/e3d4_Kao_17.ogg"
    ki "We have a rare opportunity to really boost our MMR and we can't throw this chance away."
    show kaori ann
    voice "audio/voice/E3/D4/S1/kaori/e3d4_Kao_18.ogg"
    ki "There's absolutely no way we can lose to Mei!"
    show dots:
        xoffset 1375
        yoffset 135
        xzoom .75
        yzoom .75
    show mayu ner
    show dots2:
        xoffset 80
        yoffset 20
        xzoom .75
        yzoom .75
    show shou thi
    "That almost sounded like a threat. I nod a little uneasily and glance at Shou and Mayu whose faces mirror my thoughts."
    show kaori neu
    "Kaori turns back to the holodesk and uploads our plans as we wait in silence."
    
    "A loud beep announces the match. I mutter under my breath."
    pf "Saved by the beep."
    show mayu neu
    show shou neu
    "Shou and Mayu seem equally relieved."
    show kaori ann
    voice "audio/voice/E3/D4/S1/kaori/e3d4_Kao_19.ogg"
    ki "Just make sure you guys stay focused."
    show shou hap
    voice "audio/voice/E3/D4/S1/shou/14.ogg"
    ss "Of course!"
    "Shou forces enthusiasm into his voice, attempting to raise our morale. Kaori ignores him and Shou deflates."
    show kaori dis
    show shou ner
    stop music fadeout 5
    voice "audio/voice/E3/D4/S1/kaori/e3d4_Kao_20.ogg"
    ki "Let's go."
    hide kaori with dissolve
    hide mayu
    hide shou
    with dissolve
    scene black with fade
    
    jump E3D4S2

