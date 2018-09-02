#
label E3D4KI:
    
    $ E3D4KI_Embraced = 1
    $ kaorelatonship = 1
    pf "Kaori..."
    show exclamation:
        xoffset 720
        yoffset 110
        xzoom .75
        yzoom .75
    show kaori cur b1
    "She's startled by my presence and jumps to her feet."
    show kaori sur b1
    voice "audio/voice/E3/D4/KI/kaori/e3d4_Kao_79.ogg"
    ki "I--I wasn't--"
    show kaori ner b1
    "She grabs at her bag but misses."
    voice "audio/voice/E3/D4/KI/kaori/e3d4_Kao_80.ogg"
    ki "I have to go."

    scene black with fade
    play music "audio/music/Slow Day (GAME VERSION).ogg" fadein 5
    "I grab her hand as she turns away from me and pull her into my chest. She freezes as I wrap my arms around her."
    $ persistent.gpix[29][0] = 1
    $ persistent.gpix[30][0] = 1
    $ persistent.gpix[31][0] = 1
    $ persistent.gpix[32][0] = 1
    show cg kaori hug 1 with Dissolve(2.5):
        xzoom 0.5
        yzoom 0.5
    "At first, she doesn't move, then she begins to squirm but I refuse to let go."
    pf "It's okay, Kaori. I'm here. You're not alone."
    show cg kaori hug 2 with Dissolve(1.5):
        xzoom 0.5
        yzoom 0.5
    $renpy.pause(0.5)
    "Slowly, her body relaxes but her breathing is uneven. Tiny droplets of moisture drip onto my shoulder."
    show cg kaori hug 3 with Dissolve(1.25):
        xzoom 0.5
        yzoom 0.5
    $renpy.pause(0.5)
    "I pull her closer and let her cry for as long as she needs. She returns my embrace and leans her head on my shoulder."
    show cg kaori hug 4 with dissolve:
        xzoom 0.5
        yzoom 0.5
    $renpy.pause(0.5)
    "I don't know how long we stayed like this before Kaori calms down. {w}As her breathing steadies, I gently pull away. Kaori's hands linger on me before they drop to her side. She sits back down on the bench and I sit beside her."
    
    scene bg campus main night with fade
    show kaori smi b2 at cc with dissolve
    pf "Are you okay, Kaori?"
    "She nods as her gaze locks onto mine."
    
    show kaori sad b2
    voice "audio/voice/E3/D4/KI/kaori/e3d4_Kao_81.ogg"
    ki "I was being pretty stupid, wasn't I?"
    show kaori ner b2
    voice "audio/voice/E3/D4/KI/kaori/e3d4_Kao_82.ogg"
    ki "Shou was trying to tell me I was wrong..."
    show kaori wor b2
    voice "audio/voice/E3/D4/KI/kaori/e3d4_Kao_83.ogg"
    ki "Even Mayu was upset."
    show kaori sad b1 with dissolve
    "She sighs."
    voice "audio/voice/E3/D4/KI/kaori/e3d4_Kao_84.ogg"
    ki "And the worst part is that they have every right to be mad at me."
    voice "audio/voice/E3/D4/KI/kaori/e3d4_Kao_85.ogg"
    ki "I... I know I'm not the easiest person to be around... and you've all been so patient with me..."
    show kaori wor b1
    voice "audio/voice/E3/D4/KI/kaori/e3d4_Kao_86.ogg"
    ki "Just knowing that you guys are upset--that it was {i}me{/i} who hurt my friends... I..."
    show kaori win b1
    "She chokes up."
    
    menu:
        "Friends fight all the time.":
            pf "Hey, stop thinking like that."
            show kaori wor b1
            "Kaori wipes roughly at her eyes."
            pf "Being friends mean that we forgive each other."
            pf "And believe me, they've already forgiven you."
    
        "You're only human.":
            pf "It's okay to make mistakes."
            show kaori wor b1
            "Kaori looks down."
            pf "We learn through our errors and that's what makes us better people."
    
        "You have to move on.":
            show kaori sad b1
            pf "Things like this will happen. That's just how life is."
            pf "You can't take things so hard. You have to keep going forward."
            
    show kaori cur b1
    "Kaori looks up at me."
    voice "audio/voice/E3/D4/KI/kaori/e3d4_Kao_87.ogg"
    ki "You think so?"
    pf "I know so."
    show kaori neu b1
    "Kaori wipes away her remaining tears and takes a deep breath."
    voice "audio/voice/E3/D4/KI/kaori/e3d4_Kao_88.ogg"
    ki "It wasn't just the match."
    pf "What do you mean?"
    show kaori ner b1
    voice "audio/voice/E3/D4/KI/kaori/e3d4_Kao_89.ogg"
    ki "It's just been a really stressful week, and I guess it finally got to me."
    "She plays with the sleeve of her blazer."
    voice "audio/voice/E3/D4/KI/kaori/e3d4_Kao_90.ogg"
    ki "I've been putting in a lot of hours at the daycare and midterms are coming up. I need to maintain my marks to keep my scholarships and it's all so overwhelming."
    show kaori sad b1
    voice "audio/voice/E3/D4/KI/kaori/e3d4_Kao_91.ogg"
    ki "And to add to all that, we had to go against {i}Mei{/i}."
    "Speaking of which..."
    pf "What's the history between you and Mei?"
    show dots:
        xoffset 720
        yoffset 110
        xzoom .75
        yzoom .75
    "She's quiet and I wonder if she'll answer."
    show kaori ner b1
    voice "audio/voice/E3/D4/KI/kaori/e3d4_Kao_92.ogg"
    ki "She and I were best friends until she betrayed me."
    pf "What did she do?"
    show kaori neu b1
    "Kaori sighs."
    voice "audio/voice/E3/D4/KI/kaori/e3d4_Kao_93.ogg"
    ki "It was back in middle school. I told her a secret crush I had and she went and blurted it out to him."
    pf "You mean Ryouta?"
    show kaori cur b1
    "She glances sharply at me."
    show kaori neu b1
    voice "audio/voice/E3/D4/KI/kaori/e3d4_Kao_94.ogg"
    ki "I forgot you knew. Yeah, Ryouta."
    show kaori neu b1
    voice "audio/voice/E3/D4/KI/kaori/e3d4_Kao_95.ogg"
    ki "Long story short, that ruined my friendship with both him and Mei."
    pf "Are you sure about that? Mei still treats you like you're best friends."
    show storm:
        xoffset 720
        yoffset 110
        xzoom .75
        yzoom .75
    voice "audio/voice/E3/D4/KI/kaori/e3d4_Kao_96.ogg"
    ki "I know, and that annoys me even more."
    show kaori ner b1
    voice "audio/voice/E3/D4/KI/kaori/e3d4_Kao_97.ogg"
    ki "It's as if she doesn't believe she did anything wrong. She doesn't believe it's her fault that I lost both of my best friends."
    "Ryouta was her best friend? For some reason that leaves a bad taste in my mouth."
    pf "I didn't know you were that close with Ryouta…"
    "It was a long time ago, though. It shouldn't matter now."
    show kaori ske b1
    "Kaori looks questioning at me."
    voice "audio/voice/E3/D4/KI/kaori/e3d4_Kao_98.ogg"
    ki "Well, yeah. The three of us were inseparable."
    show kaori thi b1
    voice "audio/voice/E3/D4/KI/kaori/e3d4_Kao_99.ogg"
    ki "That's why I can't forgive Mei."
    pf "I don't think that's why she acts like nothing happened."
    show kaori neu b1
    pf "I think she's trying to reach out and make amends. I think the reason she pretends nothing happened is because she misses you."
    show kaori cur b1
    voice "audio/voice/E3/D4/KI/kaori/e3d4_Kao_100.ogg"
    ki "Really?"
    show kaori ner b1
    "She speaks softly, and although she tries to play it cool, I can tell she's thinking about my words."
    pf "Yeah."
    show kaori neu b1
    "She falls silent. I enjoy the silence with her. {w}A soft breeze rustles the leaves in the trees and feels cool on my skin. I listen to the hum of nature and let the tranquility wash over me. Kaori stirs beside me. I think I see a blush in her cheeks."
    show kaori smi b1
    voice "audio/voice/E3/D4/KI/kaori/e3d4_Kao_101.ogg"
    ki "Thanks."
    
    menu:
        "For what?":
            pf "For?"
            show drop:
                xoffset 720
                yoffset 110
                xzoom .75
                yzoom .75
            "Kaori sighs."
            voice "audio/voice/E3/D4/KI/kaori/e3d4_Kao_102.ogg"
            ki "You're really dense sometimes."
            pf "I guess you rubbed off on me."
            show kaori mis b2
            "She hits my arm, but smiles."
            voice "audio/voice/E3/D4/KI/kaori/e3d4_Kao_103.ogg"
            ki "Meanie."
            "I grin at her."
    
        "Anytime.":
            pf "What are friends for?"
            show kaori mis b1
            "Kaori smiles."
            voice "audio/voice/E3/D4/KI/kaori/e3d4_Kao_104.ogg"
            ki "You better not tell anyone about this."
            pf "It's our secret."
            show kaori smi b2 with dissolve
            "Her blush deepens."
    
        "Where's my reward, Kaori!":
            pf "What, that's all I get?"
            show kaori cur b1
            voice "audio/voice/E3/D4/KI/kaori/e3d4_Kao_105.ogg"
            ki "Hm?"
            pf "All I get is a {i}thank you{/i}?"
            show kaori ske b1
            "Kaori tilts her head."
            voice "audio/voice/E3/D4/KI/kaori/e3d4_Kao_106.ogg"
            ki "Were you expecting something else?"
            pf "Well, usually the hero gets a {i}reward{/i}."
            show kaori cur b1 with dissolve
            show bulb:
                xoffset 720
                yoffset 110
                xzoom .75
                yzoom .75
            $renpy.pause(.75)
            "Kaori blinks, then nods."
            #play sound "audio/sfx/UI or Plot Element/Lightbulb.ogg"
            voice "audio/voice/E3/D4/KI/kaori/e3d4_Kao_107.ogg"
            ki "Okay, I get it."
            show kaori smi b1
            voice "audio/voice/E3/D4/KI/kaori/e3d4_Kao_108.ogg"
            ki "Close your eyes."
            scene black with fade
            "Woah! Did that actually work? I close my eyes and my cheeks flush as I anticipate what's coming next."
            "Hueheuhue."
            play sound "audio/sfx/Human/Poke_1.ogg"
            $renpy.pause(0.5)
            scene bg campus main night with fade
            show kaori smi b2 at cc with dissolve
            "Instead, I receive a sharp flick to my forehead. I blink open my eyes and see Kaori holding back a smile."
            voice "audio/voice/E3/D4/KI/kaori/e3d4_Kao_109.ogg"
            ki "Pervert."
            "I rub my forehead."
            pf "What do you mean pervert?"
            show kaori ske b2
            voice "audio/voice/E3/D4/KI/kaori/e3d4_Kao_110.ogg"
            ki "Your stupid grin couldn't have been anymore obvious. You were thinking about something weird."
            pf "Would that be so bad?"
            show kaori cur b3 with dissolve
            "To my surprise, she blushes."
            show tsuBlush:
                xoffset 720
                yoffset 110
                xzoom .75
                yzoom .75
            show kaori thi b3
            voice "audio/voice/E3/D4/KI/kaori/e3d4_Kao_111.ogg"
            ki "O-Of course it would be bad! Idiot."
            
    show kaori smi b2 with dissolve
    voice "audio/voice/E3/D4/KI/kaori/e3d4_Kao_112.ogg"
    ki "Anyways, it's starting to get late. I'm going to head home."
    "I nod."
    pf "Want me to walk back with you?"
    voice "audio/voice/E3/D4/KI/kaori/e3d4_Kao_113.ogg"
    ki "No, it's okay. You've already done a lot for me."
    pf "Are you sure?"
    show heart:
        xoffset 720
        yoffset 110
        xzoom .75
        yzoom .75
    "She nods."
    pf "Alright."
    "She stands up and picks up her bag."
    voice "audio/voice/E3/D4/KI/kaori/e3d4_Kao_114.ogg"
    ki "Thanks again. Umm... I'll see you tomorrow."
    "I smile."
    pf "See you then."
    hide kaori with dissolve
    "When she disappears around the corner, I head back to my bike."
    stop ambient fadeout 5
    stop music fadeout 5
    scene black with fade
    $renpy.pause(2.0)
    "I replay Kaori and my conversation in the quad as I drive myself home. My thoughts always slip back to that one moment when her arms wrap around my back..."
    play ambient "audio/ambience/Night Crickets.ogg" fadein 3
    scene bg homekaito main night with fade
    "The house is quiet when I arrive home. I'm a little relieved as I'm exhausted, so I head straight to bed and fall fast asleep."
    stop ambient fadeout 5
    scene black with fade
    $renpy.pause(1.0)
    jump E3D5S1

