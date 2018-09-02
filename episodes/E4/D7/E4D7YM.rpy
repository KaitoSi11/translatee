#
label E4D7YM:
    
    $ yuuHairF = "default"
    $ yuuHairB = yuuHairF
    $ yuuOut = "Dog"

    voice "audio/voice/E4/Yuuna/E4/D7/1.ogg"
    ym "Hey! I didn't expect to hear from you so soon."
    pf "Yuuna, can we meet?"
    "Worry enters her voice."
    voice "audio/voice/E4/Yuuna/E4/D7/2.ogg"
    ym "Yes, of course. What's wrong?"
    pf "I--I just found out something huge and need to talk."
    voice "audio/voice/E4/Yuuna/E4/D7/3.ogg"
    ym "Okay, should I come over?"
    pf "No, I'm not at home. I can come to you if that's okay."
    voice "audio/voice/E4/Yuuna/E4/D7/4.ogg"
    ym "O-Oh! Um, sure."
    pf "Thanks, I'll be there soon."
    
    play sound "audio/sfx/Technology/Phone Answer.ogg"
    stop ambient fadeout 3
    scene black with fade
    #play music "audio/music/After a Long Day (GAME VERSION).ogg" fadein 5
    
    "We hang up, and as if in a daze, I make it to Yuuna's house."
    "I hear barking on the other side of her door, and Yuuna ushers me in before Mochi can escape."
    "As we settle on the couch, she frowns."
    scene bg campus dorm night with fade
    show yuuna neu at cc with dissolve
    voice "audio/voice/E4/Yuuna/E4/D7/5.ogg"
    ym "Are you okay?"
    "Mochi leaps onto the couch and places a paw on my leg. I absentmindedly pat his head."
    pf "I think so."
    "Looking around the familiar living room, I once again note the immaculate cleanliness of the place."
    pf "Are your parents back?"
    show yuuna smi
    "She shakes her head."
    voice "audio/voice/E4/Yuuna/E4/D7/6.ogg"
    ym "They're coming back tomorrow."
    pf "Right at the start of exams, huh?"
    show drop:
        xoffset 720
        yoffset 100
        xzoom .75
        yzoom .75
    show yuuna hap
    voice "audio/voice/E4/Yuuna/E4/D7/7.ogg"
    ym "As if I won't be stressed enough!"
    pf "I thought you didn't like being in this big house alone."
    show yuuna smi
    voice "audio/voice/E4/Yuuna/E4/D7/8.ogg"
    ym "Not usually, but now that I have Mochi…"
    "I feel a strong tug in my lap as Mochi bites my jacket."
    show yuuna sur
    voice "audio/voice/E4/Yuuna/E4/D7/9.ogg"
    ym "Mochi! No!"
    show yuuna ner
    "Yuuna scoops up the wriggling puppy and puts him on the floor. He whines then scampers under the couch when Yuuna continues to chastise him."
   
    
    if E4D7S2_CoreDestroyed == 1:
        play music "audio/music/Next Time (GAME VERSION).ogg" fadein 5
        pf "Yuuna, I have to tell you something."
        show yuuna neu
        voice "audio/voice/E4/Yuuna/E4/D7/10.ogg"
        ym "Hm?"
        "She answers absentmindedly as she tries to coax Mochi out from under the couch."
        pf "My core is gone."
        show yuuna sur
        "She shoots straight up, her eyes wide in alarm."
        show shocked:
            xoffset 720
            yoffset 100
            xzoom .75
            yzoom .75
        voice "audio/voice/E4/Yuuna/E4/D7/11.ogg"
        ym "Did someone attack your GEAR?"
        pf "No, nothing like that."
        show yuuna wor
        voice "audio/voice/E4/Yuuna/E4/D7/12.ogg"
        ym "Then what happened?"
        "I fill her in on everything I'd learned. She listens attentively to my jumbled mess of a story and only speaks once I'm finished."
        show yuuna neu
        voice "audio/voice/E4/Yuuna/E4/D7/13.ogg"
        ym "So you did this?"
        pf "...Yeah."
    
    else:
        "When he disappears, Yuuna peers at my clenched hand."
        show yuuna cur
        
        voice "audio/voice/E4/Yuuna/E4/D7/14.ogg"
        ym "What's that?"
        play music "audio/music/Next Time (GAME VERSION).ogg" fadein 5
        "I hadn't realised I'd brought this in with me. I open my hand to reveal the drive."
        show question:
            xoffset 720
            yoffset 100
            xzoom .75
            yzoom .75
        show yuuna cur
        "Yuuna cocks her head to the side and gives me a questioning look."
        pf "It's the data to my core."
        voice "audio/voice/E4/Yuuna/E4/D7/15.ogg"
        ym "Did something happen to your core?"
        pf "Not exactly."
        show yuuna ske
        voice "audio/voice/E4/Yuuna/E4/D7/16.ogg"
        ym "Then why is the data in a drive?"
        pf "I downloaded it."
        show yuuna neu
        "She pauses and fixes her big, blue eyes on me."
        "I fill her in on everything I'd learned. She listens attentively to my jumbled mess of a story and only speaks once I've finished."
        voice "audio/voice/E4/Yuuna/E4/D7/17.ogg"
        ym "I see."
        
    #stop music fadeout 3
    show yuuna smi
    "Suddenly, her arms wrap around me."
    pf "What--"
    #play music "audio/music/You and I (GAME VERSION).ogg" fadein 3
    "She squeezes me even tighter and lays her head on my chest. {w}Her touch dissolves the dam holding back my emotions, and all the pain and fear and confusion threatens to burst."
    
    menu:
        "Hold her back.":
            "As my thoughts and emotions swirl without abandon, I cling onto my only thread of stability and hold Yuuna just as tightly."
            "We stay this way until I've had a chance to calm down and regain control of my emotions. Then Yuuna gently pulls away."
        
        "Pull away.":
            show yuuna neu
            "It's too much to bear and I gently pull away as I regain control. Yuuna lets me go, but the worry doesn't disappear from her eyes."
    
    pf "Sorry, I guess I'm not that fun to be around right now."
    show yuuna sad
    voice "audio/voice/E4/Yuuna/E4/D7/18.ogg"
    ym "You have a lot on your mind."
    pf "Yeah."
    show yuuna neu
    voice "audio/voice/E4/Yuuna/E4/D7/19.ogg"
    ym "From what I've heard, you two are a lot alike."
    "I blink."
    pf "What?"
    show yuuna neu
    voice "audio/voice/E4/Yuuna/E4/D7/20.ogg"
    ym "You and your father. From what you've described, he's confident and headstrong but has an immense heart. He was always looking out for those he cared about."
    show yuuna smi
    show note:
        xoffset 720
        yoffset 100
        xzoom .75
        yzoom .75
    voice "audio/voice/E4/Yuuna/E4/D7/21.ogg"
    ym "Sounds familiar, doesn't it?"
    show yuuna smi
    "She smiles."
    voice "audio/voice/E4/Yuuna/E4/D7/22.ogg"
    ym "I know this must be confusing for you. It sounds like your dad kept a lot of secrets and you keep wondering \"what if\"..."
    voice "audio/voice/E4/Yuuna/E4/D7/23.ogg"
    ym "...wondering how you couldn't see this coming sooner."
    "It's like she can see directly into my brain."
    show yuuna dis
    "She looks into my eyes."
    voice "audio/voice/E4/Yuuna/E4/D7/24.ogg"
    ym "You can't go down that rabbit hole. It will consume you."
    
    if MCStory == 3:
        "Is she talking from experience?"
        
    show yuuna neu
    voice "audio/voice/E4/Yuuna/E4/D7/25.ogg"
    ym "You couldn't see it because your dad didn't want you to see it. He was trying to protect you."
    voice "audio/voice/E4/Yuuna/E4/D7/26.ogg"
    ym "The same way you haven't told Nikki because you're trying to protect her."
    pf "How did you know that?"
    show yuuna neu
    "Yuuna's look softens."
    voice "audio/voice/E4/Yuuna/E4/D7/27.ogg"
    ym "Because I know you. Because I'd do the same thing."
    show yuuna sad
    "She looks away."
    voice "audio/voice/E4/Yuuna/E4/D7/28.ogg"
    ym "Because Yuudai did the same thing."
    "Of course Yuuna understands what I'm going through."
    pf "Yuuna…"
    show yuuna smi
    "She smiles and shakes her head slightly."
    voice "audio/voice/E4/Yuuna/E4/D7/29.ogg"
    ym "I drove myself crazy trying to imagine all the ways things could have been different."
    show yuuna neu
    voice "audio/voice/E4/Yuuna/E4/D7/30.ogg"
    ym "But in the end, it just made the grieving process that much harder. I wasn't able to move on until I learned to let go and accept what happened."
    "She leans against me and I let my head rest on top of hers."
    voice "audio/voice/E4/Yuuna/E4/D7/31.ogg"
    ym "We have to keep moving forward, but we don't have to forget our past."
    voice "audio/voice/E4/Yuuna/E4/D7/32.ogg"
    ym "Your dad loved you and that's why he entrusted your core's technology to you."
    "I pause."
    pf "Do you think I made the right choice?"
    stop music fadeout 5
    "She pushes herself up and looks me in the eyes."
    show yuuna smi
    voice "audio/voice/E4/Yuuna/E4/D7/33.ogg"
    ym "I know you did."
    "I let out the breath I hadn't realised I was holding. Yuuna's confidence in me is unwavering and her strength helps me find peace."
    "There's no use in living in the past. What's done is done and the only thing left to do is make sure I honor my father's final wishes."
    $ renpy.music.set_volume(1.0, channel="music")
    play music "audio/music/Timeless.ogg" fadein 2
    "She snuggles back into me and I hold her close. The silence isn't stifling or uncomfortable but a warm blanket of understanding and companionship."
    pf "Thank you."
    show yuuna cur b1 with dissolve
    "I lean in and our lips lock. We linger into the kiss and she melts into my embrace. As we slowly pull away, I gaze deeply into her eyes."
    show yuuna smi b2 with dissolve
    "In this moment, I have clarity. It rinses away all my stress and fears."
    "It's okay that I don't have all the answers now, because I'm looking at my future...{p}\n...and it is beautiful."
    
    jump E4Epilogue