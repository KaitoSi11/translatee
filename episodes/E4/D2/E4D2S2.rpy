#
label E4D2S2:
    
    stop music fadeout 5
    "The tour was very beautiful and I enjoyed the leisurely pace we took around the gardens. Although, I did learn a lot more about plants than I ever wanted to know."
    scene bg vacation nature day with fade
    play music "audio/music/Day Out (GAME VERSION).ogg" fadein 5
    "Once the tour was over, we regrouped back outside the hotel."
    show yuuna neu at l3 with dissolve:
        xoffset -200
        xzoom 0.75
        yzoom 0.75
    show mayu neu at l2 behind yuuna  with dissolve:
        xoffset -50
        xzoom 0.75
        yzoom 0.75
    show valerie neu at l1 with dissolve:
        xoffset 75
        xzoom 0.75
        yzoom 0.75
    show kaori neu at r1 behind shou with dissolve:
        xoffset -75
        xzoom -0.75
        yzoom 0.75
    show shou neu at r3 with dissolve:
        xoffset 100
        xzoom -0.75
        yzoom 0.75
    pf "How did everyone enjoy the tour?"
    show mayu smi
    "Mayu sighs dreamily."
    voice "audio/voice/E4/Mayu/D2/Mayu D2-11.ogg"
    ma "The flowers were so beautiful. I felt like I was walking through a fairy tale."
    show yuuna smi
    voice "audio/voice/E4/Yuuna/E4/D2/10.ogg"
    ym "I'm glad you had fun, Mayu. I thought it was really pretty too, but I found the history of the place to be the most interesting part."
    "Kaori shrugs."
    voice "audio/voice/E4/Kaori/D2/Kaori_27_d1.ogg"
    ki "Yeah, it was alright."
    show valerie smi
    voice "audio/voice/E4/Valerie/ValE4D2/ValE4D2L12.ogg"
    vb "It reminded me a little bit of home. On the outskirts of town there was a cute little museum which also included a garden walk."
    show yuuna hap
    voice "audio/voice/E4/Yuuna/E4/D2/11.ogg"
    ym "That sounds really nice."
    show valerie hap
    voice "audio/voice/E4/Valerie/ValE4D2/ValE4D2L13.ogg"
    vb "It was!"
    show shou smi
    voice "audio/voice/MISSING/BATCH2/15.ogg"
    ss "I thought it was good, but I could have used less of all that flower talk."
    show valerie smi
    pf "You aren't the only one."
    show mayu ner
    voice "audio/voice/E4/Mayu/D2/Mayu D2-12.ogg"
    ma "I thought it was informative."
    show shou smi
    voice "audio/voice/E4/Shou/d2/51 Copy.ogg"
    ss "But enough of that. It's now time for the main event… hot springs!"
    show heart:
        xoffset 590
        yoffset 125
        xzoom .5
        yzoom .5
    show valerie hap
    voice "audio/voice/E4/Valerie/ValE4D2/ValE4D2L14.ogg"
    vb "Yay! I cannot wait to soak in that glorious water."
    show yuuna hap
    voice "audio/voice/E4/Yuuna/E4/D2/12.ogg"
    ym "Same here!"
    show kaori smi
    show mayu smi
    "Mayu grins and even Kaori cracks a smile."
    stop ambient fadeout 3
    stop music fadeout 5
    scene black with fade
    "We eagerly follow Shou into the hotel where he presents our tickets. We had to wait what felt like a couple hours at least while they prepped the place."
    "Afterwards, an attendant leads Shou and I to the male changing room while another attendant leads the girls away."
    
    $ akiOut = "hotspring"
    
    $ kaoHairF = "hotspring"
    $ kaoHairB = "tied"
    $ kaoOut = "hotspring"
    
    $ mayHairF = "hotspring"
    $ mayHairB = mayHairF
    $ mayOut = "hotspring"
    
    $ meiHairF = "hotspring"
    $ meiHairB = meiHairF
    $ meiOut = "hotspring"
    
    $ shoHairF = "default"
    $ shoHairB = shoHairF
    $ shoOut = "hotspring"
    
    $ valHairF = "pony"
    $ valHairB = valHairF
    $ valOut = "hotspring"
    
    $ yuuHairF = "hotspring"
    $ yuuHairB = yuuHairF
    $ yuuOut = "hotspring"
    
    
    #play ambient "audio/ambience/Night Crickets.ogg" fadein 3
    $renpy.pause(0.5)
    scene bg vacation hotspring boy with Dissolve(2)
    play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 5
    #play music "audio/music/Evening Out (GAME VERSION).ogg" fadein 5
    "As is customary, we strip down and rinse ourselves thoroughly before entering the adjoining hot spring. I can feel the difference in temperature as soon as I step out of the room. There are a few other men spread out in the pool. They all look to be young and close to my age."
    "Shou and I slowly wade into the hot spring. I dip my feet in and my toes tingle from the rush of heat. Carefully, I lower the rest of me into the water and instantly relax in the warmth."
    show shou smi b1 at r2 with dissolve:
        xzoom -1
    "Shou lets out a contented sigh."
    voice "audio/voice/E4/Shou/d2/52 Copy.ogg"
    ss "Ahh… This is the life."
    "I nod and close my eyes."
    "I listen to the soft sounds of nature mixed with the low murmur of voices from other patrons. The waters are mostly still, only rippling when someone enters or leaves the spring. The water gently eases out any remaining tension in my muscles, and as I let out a deep breath, I wish this moment can last forever."
    voice "audio/voice/E4/Akira/D2/1.ogg"
    am "Hey guys."
    show shou cur b1
    voice "audio/voice/E4/Shou/d2/53 Copy.ogg"
    ss "Akira?"
    show akira smi b1 at l2 with dissolve
    "I blink my eyes open at the sound of a familiar voice. Akira has a small towel resting on his head."
    voice "audio/voice/E4/Akira/D2/2.ogg"
    am "Fancy seeing you here."
    show shou neu b1
    pf "I was just about to say that to you. What are you doing here?"
    voice "audio/voice/E4/Akira/D2/3.ogg"
    am "We can't stay on campus today, so instead of practicing, my team and I decided to do the next best thing--heal in the hot springs!"
    "I squint at the other men in the spring. No wonder they all look my age."
    show exclamation:
        xoffset 1040
        yoffset 20
        xzoom .75
        yzoom .75
    show shou sur b1
    voice "audio/voice/E4/Shou/d2/54 Copy.ogg"
    ss "That's why everyone looks so familiar!"
    pf "I'm surprised we didn't recognise you guys."
    show shou neu b1
    show akira hap b1
    "Akira smiles."
    voice "audio/voice/E4/Akira/D2/4.ogg"
    am "We look different without our uniforms. It took me a few minutes before I recognised you two."
    show akira neu b1
    stop music fadeout 5
    "In the distance, I hear a high-pitched squeal."
    pf "Was that the girls?"
    voice "audio/voice/E4/Shou/d2/55 Copy.ogg"
    ss "I think so."
    show akira thi b1
    voice "audio/voice/E4/Akira/D2/5.ogg"
    am "Their spring is right next to ours."
    show shou cur b1
    "Shou perks up."
    show question:
        xoffset 1040
        yoffset 20
        xzoom .75
        yzoom .75
    voice "audio/voice/E4/Shou/d2/56 Copy.ogg"
    ss "Really?"
    #play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 3
    show akira neu b1
    voice "audio/voice/E4/Akira/D2/6.ogg"
    am "Yeah."
    pf "I wonder what they're talking about."
    show shou hap b1
    voice "audio/voice/E4/Shou/d2/57 Copy.ogg"
    ss "Let's find out!"
    play music "audio/music/Sneaking About (GAME VERSION).ogg" fadein 7
    pf "You mean eavesdrop?"
    show shou mis b1
    voice "audio/voice/E4/Shou/d2/58 Copy.ogg"
    ss "It's not eavesdropping if we're just checking on their well-being."
    
    $ E4D2S2_Minds = 0
    
    menu:
        "This can only end poorly.":
            pf "I don't know. I've seen enough anime to know how this ends."
            show shou hap b1
            "Shou laughs."
            show note:
                xoffset 1040
                yoffset 20
                xzoom .75
                yzoom .75
            voice "audio/voice/E4/Shou/d2/59 Copy.ogg"
            ss "Lucky for us, we aren't in an anime! We'll be fine."
            pf "...That doesn't make me feel any more confident about this decision."
        
        "Great minds think alike.":
            $ E4D2S2_Minds = 1
            pf "There is only one thing wrong with your idea."
            show shou ske b1
            voice "audio/voice/E4/Shou/d2/60 Copy.ogg"
            ss "What?"
            pf "The fact that you said it instead of me."
            show shou hap b1
            "Shou grins."
            show note:
                xoffset 1040
                yoffset 20
                xzoom .75
                yzoom .75
            voice "audio/voice/E4/Shou/d2/61 Copy.ogg"
            ss "You've got to be quick. That's how you don't get caught."
            "I nod."
        
        "But I'm so comfortable.":
            pf "You guys go on without me. I'm too relaxed to care."
            show shou ske b1
            voice "audio/voice/E4/Shou/d2/62 Copy.ogg"
            ss "You do know that you can't sit in here for too long, right?"
            pf "Huh?"
            show shou neu b1
            voice "audio/voice/E4/Shou/d2/63 Copy.ogg"
            ss "It's dangerous for your health."
            pf "But the hot springs are supposed to be full of healing minerals!"
            show akira wor b1
            voice "audio/voice/E4/Akira/D2/7.ogg"
            am "It is, but staying too long in the hot water can make you feel dizzy."
            "I sigh."
            pf "Alright, fine, if I have to leave anyway I guess I'll go with you."
            show akira neu b1
            show shou hap b1
            "Shou grins."
    
    "Akira climbs out of the water."
    show akira smi b1
    voice "audio/voice/E4/Akira/D2/8.ogg"
    am "I know a way we can slip in unseen."
    show shou cur b1
    pf "How exactly do you know this?"
    show note:
        xoffset 365
        yoffset 20
        xzoom .75
        yzoom .75
    show akira mis b1
    voice "audio/voice/E4/Akira/D2/9.ogg"
    am "I can't give away my sources."
    show shou neu b1
    stop music fadeout 7
    "Shou and I look at each other then shrug. I might have expected this type of behaviour from Shou, but definitely not Akira!"
    scene black with fade
    #play music "audio/music/Sneaking About (GAME VERSION).ogg" fadein 5
    "We follow him out of the pool and into the changing room where we each grab towels. Then Akira leads us through an employee entrance and into a tunneled hallway. The hallway opens up right beside a large rock enclave surrounding the women's hot spring, which keeps us perfectly out of site."
    scene bg vacation hotspring girl with Dissolve(2)
    play music "audio/music/Day Out (GAME VERSION).ogg" fadein 10
    "Giggles float around us as we peek over the rocks. Just our luck! Valerie, Yuuna, Mayu, Kaori, and Mei are right in front of us. Shou and I share a look as if to silently ask: {i}Mei's here too?{/i} Then we shrug. If Akira's here, it only makes sense that Mei would be here too."
    show yuuna smi b1 at l3 with dissolve:
        xoffset -100
        xzoom 0.75
        yzoom 0.75
    show mayu neu b1 at l2 behind yuuna with dissolve:
        xoffset 50
        xzoom 0.75
        yzoom 0.75
    show mei smi b1 at cc with dissolve:
        xoffset -50
        xzoom 0.75
        yzoom 0.75
    show kaori neu b1 at r2 with dissolve:
        xoffset -50
        xzoom -0.75
        yzoom 0.75
    show valerie smi b1 at r3 with dissolve:
        xoffset 100
        xzoom -0.75
        yzoom 0.75
    voice "audio/voice/E4/Yuuna/E4/D2/13.ogg"
    ym "It's your turn, Valerie."
    voice "audio/voice/E4/Valerie/ValE4D2/ValE4D2L15.ogg"
    vb "Okay."
    show yuuna mis b1
    voice "audio/voice/E4/Yuuna/E4/D2/14.ogg"
    ym "Truth or dare?"
    show valerie mis b1
    voice "audio/voice/E4/Valerie/ValE4D2/ValE4D2L16.ogg"
    vb "Dare!"
    show mei mis b1
    voice "audio/voice/E4/Mei/Mei_Ep4D2_Line1.ogg"
    ms "Okay, truth."
    show drop:
        xoffset 1475
        yoffset 125
        xzoom .5
        yzoom .5
    show valerie ner b1
    voice "audio/voice/E4/Valerie/ValE4D2/ValE4D2L17.ogg"
    vb "What? No, I picked dare."
    voice "audio/voice/E4/Mei/Mei_Ep4D2_Line2.ogg"
    ms "Right, truth."
    show mei smi b1
    show yuuna smi b1
    show valerie dis b1
    "Mei turns to the rest of the girls."
    voice "audio/voice/E4/Mei/Mei_Ep4D2_Line3.ogg"
    ms "What should we ask her?"
    show mayu wor b2
    "Mayu blushes."
    voice "audio/voice/E4/Mayu/D2/Mayu D2-13.ogg"
    ma "Um, what is it like being with a boy?"
    show kaori cur b2
    show mayu ner b3
    show valerie ske b1
    "Everyone stares at her with wide eyes, and Mayu's face turns even redder."
    voice "audio/voice/E4/Valerie/ValE4D2/ValE4D2L18.ogg"
    vb "Why would you ask {i}me{/i} that?"
    show kaori ner b2
    voice "audio/voice/MISSING/BATCH5/k_redo_14.ogg"
    ki "Because... you know..."
    show kaori thi b2
    "Even Kaori's cheeks are pink, but I can't tell whether it's from the question or the heat of the water."
    show valerie cur b2
    show mayu neu b2
    "Valerie blinks."
    show exclamation:
        xoffset 1475
        yoffset 125
        xzoom .5
        yzoom .5
    voice "audio/voice/E4/Valerie/ValE4D2/ValE4D2L19.ogg"
    vb "Oh! Right, um, okay. You see…"
    show valerie thi b2
    show kaori neu b2
    show yuuna neu b1
    "Her voice trails off and my breath catches in my throat. Is this really happening right now? Shou and Akira both focus intently on the conversation."
    
    voice "audio/voice/E4/Valerie/ValE4D2/ValE4D2L20.ogg"
    vb "...How do I put this..."
    show dots:
        xoffset 1475
        yoffset 125
        xzoom .5
        yzoom .5
    "She pauses again as she thinks."
    show valerie wor b2
    voice "audio/voice/E4/Valerie/ValE4D2/ValE4D2L21.ogg"
    vb "Okay, basically, imagine you have a motherboard. On the different sockets, you have to add the different components. So first you put in the CPU and then the RAM, a graphics card, some sort of storage drive..."
    show valerie cur b2
    voice "audio/voice/E4/Valerie/ValE4D2/ValE4D2L22.ogg"
    vb "Oh and the power supply! You can't forget the power supply. That is what... supplies power..."
    show valerie neu b2
    show mei ske b1
    voice "audio/voice/E4/Valerie/ValE4D2/ValE4D2L23.ogg"
    vb "And once all those pieces are ready, then it's time to make sure all the wires are connected. Some graphics cards require a 6 pin connector while others need an 8 pin. Some also require two sets of connectors depending on the power draw requirements."
    show valerie smi b2
    voice "audio/voice/E4/Valerie/ValE4D2/ValE4D2L24.ogg"
    vb "It's also important to pick a good case because you want to make sure everything is well protected but still has strong air flow. Having a strong cooling system is important when things heat up!"
    show kaori neu b2
    show mayu wor b2
    show yuuna ske b1
    with dissolve
    "As Valerie continues with her explanation, the girls struggle to follow along. Mayu's brows are furrowed but she nods every so often, listening closely to Valerie's words."
    "Yuuna just seems plain confused although she's trying her best to follow along. Kaori frowns thoughtfully, and I can almost see the gears in her brain trying to piece together the image Valerie is describing."
    "Only Mei sits with her eyebrow raised and her arms across her chest."
    voice "audio/voice/E4/Mei/Mei_Ep4D2_Line4.ogg"
    ms "None of this makes sense."
    show valerie ner b2
    "Valerie freezes and looks a little panicked."
    show panic:
        xoffset 1475
        yoffset 125
        xzoom .5
        yzoom .5
    voice "audio/voice/E4/Valerie/ValE4D2/ValE4D2L25.ogg"
    vb "W-What?"
    show mei mis b1
    "Mei studies Valeries expression and discomfort. Then she smiles triumphantly, as if she's solved a puzzle."
    voice "audio/voice/E4/Mei/Mei_Ep4D2_Line5.ogg"
    ms "Ohhhh, you've never actually been with--"
    show valerie hap b2
    "Valerie laughs loudly over Mei's voice."
    voice "audio/voice/E4/Valerie/ValE4D2/ValE4D2L26.ogg"
    vb "Haha! You're so silly, Mei! What are you even talking about?"
    show mei hap b1
    show valerie sur b2
    voice "audio/voice/E4/Mei/Mei_Ep4D2_Line6.ogg"
    ms "Your \"analogy\" doesn't describe {i}it{/i} at all!!"
    show kaori ske b2
    "Kaori crosses her arms."
    voice "audio/voice/E4/Kaori/D2/Kaori_28_d1.ogg"
    ki "If she's not right, then what's it {i}supposed{/i} to be?"
    show mei mis b1
    show valerie cur b2
    "Mei grins mischievously."
    voice "audio/voice/E4/Mei/Mei_Ep4D2_Line7.ogg"
    ms "Well, when a man and a woman love each other very much--"
    stop music fadeout 1.5
    # sfx ? something dropping in water
    show kaori cur b2
    show mayu cur b2
    with dissolve
    
    show mei cur b1
    show valerie cur b2
    show yuuna cur b1
    with dissolve
    "{i}Plop!{/i}"

    
    "I look over at Shou. He had leaned too far forward and accidentally wobbled an unstable pebble which rolled into the spring."
    show kaori ske b3
    show mayu sur b3
    show mei sur b2
    show valerie sur b3
    show yuuna sur b2
    #play music "audio/music/A Bad Feeling (GAME VERSION).ogg" fadein 3
    "As one, the girls look over in our direction, then shriek!"
    voice "audio/voice/E4/Akira/D2/10.ogg"
    am "Run!"
    scene black with fade
    "We scramble into the safety of the hallway and head back into the men's changing room."
    scene bg vacation hotspring boy with fade
    show akira dis at l2
    show shou ner at r2:
        xzoom -1
    with dissolve
    play music "audio/music/Sneaking About (GAME VERSION).ogg" fadein 5
    voice "audio/voice/E4/Shou/d2/64 Copy.ogg"
    ss "Do you think they saw us?"
    pf "They probably saw {i}you{/i}."
    show shou wor
    "The blood leaves shou's face."
    show panic:
        xoffset 1040
        yoffset 20
        xzoom .75
        yzoom .75
    voice "audio/voice/E4/Shou/d2/65 Copy.ogg"
    ss "No! Akira, please tell me otherwise..."
    show drop:
        xoffset 365
        yoffset 20
        xzoom .75
        yzoom .75
    show akira wor
    voice "audio/voice/E4/Akira/D2/11.ogg"
    am "It was pretty dark… Maybe they just saw a silhouette?"
    pf "For your sake, I hope that's all they saw."
    show shou ner
    voice "audio/voice/E4/Shou/d2/66 Copy.ogg"
    ss "If I fall, I'm dragging you down with me."
    pf "Me? I was in the men's hot springs the entire time. Isn't that right, Akira?"
    show akira neu
    voice "audio/voice/E4/Akira/D2/12.ogg"
    am "Of course."
    show frightful:
        xoffset 1040
        yoffset 20
        xzoom .75
        yzoom .75
    show shou wor
    voice "audio/voice/E4/Shou/d2/67 Copy.ogg"
    ss "YOU GUYS."
    #black screen
    stop music fadeout 3
    scene black with fade
    "Once our pounding hearts subside, we return to the men's hot spring as if nothing happened. {w}As soon as our time was up, we left with the rest of the group. This way, it could have been anyone who disturbed the girls!"
    
    jump E4D2S3
