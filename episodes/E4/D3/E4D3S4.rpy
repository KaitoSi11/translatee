#
label E4D3S4:
    
    $ yukOut = renpy.random.choice(['sweater'])
    $ kaiOut = renpy.random.choice(['sCasual'])
    play ambient "audio/ambience/Kitchen Cooking.ogg" fadein 5
    scene bg homekaito main night with fade
    "After parking my bike, I let myself into the house. The living room is empty. {w}Where is everybody? {w}I hear voices in the kitchen and hurry over."
    
    show yuki hap at cc
    show nikki smi at r3:
        xzoom -1
    with dissolve
    show kaito ske at l3 with dissolve
    play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 3
    
    "I pause as soon as I push open the doors.{w} Nikki is bent over the table laughing. Aunt Yuki stands by the fridge laughing as hard as Nikki, while Uncle Kaito chugs water looking increasingly confused."
    pf "Oh, hi, Aunt Yuki. I didn't know you were here."
    show yuki smi
    "Aunt Yuki tries to compose herself when she sees me and rushes over to give me a hug."
    voice "audio/voice/E4/Yuuki/E4/D3/1.ogg"
    hy "Oh good, you're home!"
    show yuki cur
    voice "audio/voice/E4/Yuuki/E4/D3/2.ogg"
    hy "Oops, I got some flour on you."
    pf "That's okay."
    show yuki smi
    show exclamation:
        xoffset 230
        yoffset 5
        xzoom .75
        yzoom .75
    show kaito win
    "Uncle Kaito's eyes are watering as he lunges towards the fridge and pulls out a carton of milk."
    pf "Uh, are you okay, Uncle Kaito?"
    "He doesn't answer as he chugs a fresh glass of milk."
    show nikki neu
    "Nikki finally composes herself enough to answer."
    voice "audio/voice/E4/Nikki/Day 3/Nikki_04_301.ogg"
    sf "Aunt Yuki's making us Chinese food tonight and she ran one of the chilis around the rim of Uncle Kaito's glass when he wasn't looking."
    show nikki smi
    "She starts laughing again."
    show kaito thi
    voice "audio/voice/E4/Kaito/d03/(17).ogg"
    hk "It doesn't hit you at first, but once it does…"
    show kaito win
    "Uncle Kaito takes another swig of milk while Aunt Yuki giggles."
    show yuki hap
    voice "audio/voice/E4/Yuuki/E4/D3/3.ogg"
    hy "I'm sorry, I couldn't resist!"
    "Their laughter is infectious and I find myself laughing with them. It's good to see Aunt Yuki hasn't lost her sense of humour!"
    pf "Uncle Kaito, hasn't Aunt Yuki played this same prank on you before?"
    show yuki smi
    show nikki hap
    voice "audio/voice/E4/Nikki/Day 3/Nikki_04_302.ogg"
    sf "She has! That's what makes it so funny!"
    show drop:
        xoffset 230
        yoffset 5
        xzoom .75
        yzoom .75
    show kaito wor
    show nikki neu
    voice "audio/voice/E4/Kaito/d03/(18).ogg"
    hk "It's been awhile! Cut me some slack!"
    pf "You're losing your touch."
    voice "audio/voice/E4/Nikki/Day 3/Nikki_04_303.ogg"
    sf "Aunt Yuki's been away for too long!"
    show nikki thi
    "Nikki sighs."
    show yuki neu
    voice "audio/voice/E4/Nikki/Day 3/Nikki_04_304.ogg"
    sf "Do you really have to leave again, Aunt Yuki? It's so fun when you're around!"
    show kaito ske
    voice "audio/voice/E4/Kaito/d03/(19).ogg"
    hk "Hey, are you saying I'm not fun?"
    show nikki smi
    voice "audio/voice/E4/Nikki/Day 3/Nikki_04_305.ogg"
    sf "Noooo, you're fun too…"
    show kaito mis
    show yuki smi
    
    voice "audio/voice/E4/Kaito/d03/(1).ogg"
    hk "That sounded awfully like a pity compliment…"
    show note:
        xoffset 1175
        yoffset 160
        xzoom .75
        yzoom .75
    "Nikki giggles."
    #show yuki ner
    stop music fadeout 5
    stop ambient fadeout 5
    "Aunt Yuki fidgets with the corner of her apron."
    voice "audio/voice/E4/Yuuki/E4/D3/4.ogg"
    hy "Actually, you'll all be seeing a lot more of me."
    show kaito sur
    show nikki cur
    "Kaito looks at her in surprise."
    show question:
        xoffset 230
        yoffset 5
        xzoom .75
        yzoom .75
    voice "audio/voice/E4/Kaito/d03/(2).ogg"
    hk "Really?"
    show yuki neu
    #play music "audio/music/Tender Moments (GAME VERSION).ogg" fadein 5
    play music "audio/music/Yuuna Misaki (GAME VERSION).ogg" fadein 5
    "She meets his gaze and nods."
    voice "audio/voice/E4/Yuuki/E4/D3/4_01.ogg"
    hy "If that's alright with you."
    show kaito ner
    voice "audio/voice/E4/Kaito/d03/(3).ogg"
    hk "Of course--I just--does that mean you're really going to stay here?"
    show yuki ner
    voice "audio/voice/E4/Yuuki/E4/D3/5.ogg"
    hy "Yeah… unless there's a reason why I shouldn't…?"
    show kaito wor
    voice "audio/voice/E4/Kaito/d03/(4).ogg"
    hk "No! But..."
    show dots:
        xoffset 230
        yoffset 5
        xzoom .75
        yzoom .75
    show kaito thi
    "Kaito hesitates. Nikki watches with bated breath. Her eyes are wide with excitement and I can tell it's taking a lot of self-control for her to keep quiet. I'm unsure if I should even be witnessing this conversation."
    show yuki smi
    "Aunt Yuki seems to understand Uncle Kaito's unspoken question."
    voice "audio/voice/E4/Yuuki/E4/D3/6.ogg"
    hy "Watching you with the kids… you've changed..."
    show kaito ner
    voice "audio/voice/E4/Kaito/d03/(5).ogg"
    hk "Yuki--I--"
    show nikki sur
    "Nikki can't hold it in anymore and explodes."
    show heart:
        xoffset 1175
        yoffset 160
        xzoom .75
        yzoom .75
    show nikki hap
    voice "audio/voice/E4/Nikki/Day 3/Nikki_04_306.ogg"
    sf "Aunt Yuki belongs here, Uncle Kaito! Let her stay!"
    show kaito cur b2
    show yuki cur b2
    with dissolve
    "Both Yuki and Kaito blush deeply."
    pf "Nikki!"
    show nikki smi
    voice "audio/voice/E4/Nikki/Day 3/Nikki_04_307.ogg"
    sf "What? They clearly need my help!"
    pf "Let's give them some privacy."
    show nikki ner
    "I begin to push her out of the room."
    voice "audio/voice/E4/Nikki/Day 3/Nikki_04_308.ogg"
    sf "But--"
    stop music fadeout 5
    pf "No buts."
    hide kaito
    hide yuki
    with dissolve
    "Reluctantly, Nikki allows me to lead her out of the kitchen and into the living room. We both sit on the couch and I turn on the TV."
    play music "audio/music/After a Long Day (GAME VERSION).ogg" fadein 5
    show nikki ner at cc with dissolve:
        xzoom 1
    voice "audio/voice/E4/Nikki/Day 3/Nikki_04_309.ogg"
    sf "Do you think Aunt Yuki will really stay?"
    
    menu:
        "Of course.":
            pf "Yeah, she obviously still cares for Uncle Kaito and he still cares for her. I have a feeling that once she comes back, she won't be going anywhere."
            show nikki neu
            voice "audio/voice/E4/Nikki/Day 3/Nikki_04_310.ogg"
            sf "I hope so! Then we'll be a family again."
            "I glance at Nikki. She looks hopeful yet apprehensive."
            pf "Again? We've always been a family."
            show nikki smi
            voice "audio/voice/E4/Nikki/Day 3/Nikki_04_311.ogg"
            sf "I know, but it wasn't the same without Aunt Yuki around. It felt incomplete somehow, like Uncle Kaito was missing a part of himself."
            pf "It'll definitely be more interesting having her back."
        
        "Doubtful…":
            pf "I wouldn't get my hopes up."
            show nikki ske
            voice "audio/voice/E4/Nikki/Day 3/Nikki_04_312.ogg"
            sf "Why not? They were joking around with each other just like old times!"
            pf "There's a reason why they split up in the first place and it's going to take them a while to work through those issues."
            show nikki neu
            voice "audio/voice/E4/Nikki/Day 3/Nikki_04_313.ogg"
            sf "It's obvious they're both still in love with each other."
            pf "So?"
            show nikki hap
            voice "audio/voice/E4/Nikki/Day 3/Nikki_04_314.ogg"
            sf "Love conquers all!"
            "I raise an eyebrow. Nikki sighs."
            show storm:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            show nikki dis
            voice "audio/voice/E4/Nikki/Day 3/Nikki_04_315.ogg"
            sf "You are so unromantic."
            
            if kaorelatonship == 1 or mayrelatonship == 1 or valrelatonship == 1 or yuurelatonship == 1:
                show nikki ske
                voice "audio/voice/E4/Nikki/Day 3/Nikki_04_316.ogg"
                sf "How do you even have a girlfriend?"
                pf "Because I'm delightful."
                show nikki mis
                "Nikki laughs."
                pf "I'm going to ignore that."
                
            else:
                show nikki mis
                voice "audio/voice/E4/Nikki/Day 3/Nikki_04_317.ogg"
                sf "No wonder you don't have a girlfriend."
                pf "Hey! I resent that!"
        
        "It's hard to say.":
            pf "I hope so, but I'm not sure."
            show nikki hap
            voice "audio/voice/E4/Nikki/Day 3/Nikki_04_318.ogg"
            sf "That's exactly why they need my help!"
            pf "This is something they need to work out themselves."
            show nikki smi
            voice "audio/voice/E4/Nikki/Day 3/Nikki_04_319.ogg"
            sf "But they need someone to remind them of how good they are together!"
            pf "If it's meant to be, then it will be."
            show nikki ske
            "Nikki gives me a skeptical look."
            voice "audio/voice/E4/Nikki/Day 3/Nikki_04_320.ogg"
            sf "Which magazine did you read that in?"
            pf "How do you know I didn't come up with that myself?"
            show note:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            show nikki smi
            "She chuckles."
            voice "audio/voice/E4/Nikki/Day 3/Nikki_04_321.ogg"
            sf "Please, I wasn't born yesterday!"
            pf "..."
            
    show nikki thi
    "We wait in silence. Every so often Nikki would sneak glances at the door, but she doesn't move."
    play sound "audio/sfx/Human/Stomach Grumble.ogg"
    "I can't ignore the delicious smell of Kung Pao chicken wafting out of the kitchen and my stomach grumbles loudly."
    pf "I kind of wish they were having this conversation {i}after{/i} we'd already eaten."
    show nikki smi
    "Nikki giggles."
    voice "audio/voice/E4/Nikki/Day 3/Nikki_04_322.ogg"
    sf "Are you ever not hungry?"
    play sound "audio/sfx/Human/Stomach Grumble.ogg"
    show nikki cur b1 with dissolve
    show shoBlush:
        xoffset 720
        yoffset 160
        xzoom .75
        yzoom .75
        
    $renpy.pause(1)
    "Her eyes widen as her stomach grumbles just as loudly."
    "Now it's my turn to laugh."
    show yuki smi at r3 with dissolve:
        xzoom -1
    "Luckily, we don't have to wait much longer before Aunt Yuki pops her head out."
    voice "audio/voice/E4/Yuuki/E4/D3/7.ogg"
    hy "Are you kids hungry yet?"
    show nikki neu
    pf "Starving!"
    show yuki hap
    voice "audio/voice/E4/Yuuki/E4/D3/8.ogg"
    hy "Then I guess we better feed you! Dinner's ready."
    "I jump to my feet and race into the kitchen, but Nikki lingers beside Aunt Yuki."
    voice "audio/voice/E4/Nikki/Day 3/Nikki_04_323.ogg"
    sf "Does this mean you're staying?"
    show yuki mis
    voice "audio/voice/E4/Yuuki/E4/D3/9.ogg"
    hy "Of course I'm staying. There's no way I'm going to let Kaito keep you kids to himself!"
    show nikki hap
    "Nikki grins from ear to ear and hugs Yuki tightly."
    voice "audio/voice/E4/Nikki/Day 3/Nikki_04_324.ogg"
    sf "I'm so happy! There will finally be another woman in the house!"
    show note:
        xoffset 1175
        yoffset 100
        xzoom .75
        yzoom .75
    show yuki smi
    "Aunt Yuki laughs as the two of them join us at the table."
    voice "audio/voice/MISSING/BATCH6/Redo 4.ogg"
    hy "I don't know how you managed all by yourself."
    show nikki smi
    voice "audio/voice/E4/Nikki/Day 3/Nikki_04_325.ogg"
    sf "Me neither."
    stop music fadeout 5
    "Everyone is all smiles as we sit down to eat."
    
    stop ambient fadeout 3
    #timeskip
    scene black with fade
    play ambient "audio/ambience/Night Crickets.ogg" fadein 3
    scene bg homekaito main night with fade
    "After dinner, Nikki dragged Aunt Yuki upstairs to show her the new dress she bought last week. Uncle Kaito and I are watching TV."
    show kaito neu at cc with dissolve
    play sound "audio/sfx/Technology/ID Tap Success.ogg"
    "In the middle of our show, his phone dings with an email. As he opens the email, his jaw sets."
    pf "What is it?"
    play music "audio/music/Next Time (GAME VERSION).ogg" fadein 5
    voice "audio/voice/E4/Kaito/d03/(6).ogg"
    hk "It's an email from the PI."
    pf "What does it say?"
    "He holds the phone out for me to see and we review the email together. Again, the content does not share much, but stresses that the accident might have been more than just an accident. The other driver had been spotted talking to Dad right before the car crash."
    pf "Wait--someone wanted to hurt Dad on purpose?"
    "Kaito's voice is grim."
    show kaito thi
    voice "audio/voice/E4/Kaito/d03/(7).ogg"
    hk "That seems to be what the PI is implying."
    pf "Why would he want to hurt them?"
    show kaito neu
    voice "audio/voice/E4/Kaito/d03/(8).ogg"
    hk "I wish I knew. Wasn't the other driver someone your dad knew?"
    pf "Yeah, Ezra Wilson was Dad's colleague. They worked closely on projects together."
    show kaito ske
    voice "audio/voice/E4/Kaito/d03/(9).ogg"
    hk "Did something happen between them?"
    pf "Not that I know of… and we can't even ask him since he's still in a coma last I heard."
    show kaito neu
    "Kaito nods."
    voice "audio/voice/E4/Kaito/d03/(10).ogg"
    hk "Well, the PI is still investigating. I'm sure he'll have more information soon."
    "None of this is making any sense. Ezra and Dad worked on the same projects together for as long as I can remember and he always seemed like a nice guy. I can't imagine that he'd want to hurt Dad!"
    "Does this mean Dad knew this was coming too? But how could he? He only left because Nikki called him. And what about Mom?"
    "I let out a frustrated sigh."
    "I wish he could just tell me what happened!"
    "Wait a minute…"
    "Dad's research… {w}the strange encryption in my core..."
    show kaito ske
    "Uncle Kaito notices the change in my expression."
    show question:
        xoffset 720
        yoffset 5
        xzoom .75
        yzoom .75
    voice "audio/voice/E4/Kaito/d03/(11).ogg"
    hk "What is it?"
    pf "I wonder if this has something to do with my core..."
    show kaito cur
    voice "audio/voice/E4/Kaito/d03/(12).ogg"
    hk "Because of the weird thing it did during your first match?"
    pf "Maybe."
    show kaito neu
    voice "audio/voice/E4/Kaito/d03/(13).ogg"
    hk "If whoever wanted your Dad dead was after your core then you might be in danger. You probably shouldn't use Eagle again just to be safe."
    pf "I wouldn't go that far. All my core did was use extra energy packs--at least that's what my professors said. That's why the referees didn't disqualify me from the match."
    show kaito thi
    voice "audio/voice/E4/Kaito/d03/(14).ogg"
    hk "Hm, extra energy doesn't sound like something to kill over."
    pf "My thoughts exactly. I brought up my core for a different reason."
    pf "It might be nothing, but our team engineer found a weird encryption from Dad in my core. She didn't think it was anything important, but now I'm not sure…"
    show kaito ske
    voice "audio/voice/E4/Kaito/d03/(15).ogg"
    hk "What does it say?"
    pf "I don't know."
    show kaito neu
    "He nods."
    "I try to refocus on the TV show, but I can't stop thinking about the accident-on-purpose."
    pf "I think I'm just going to go to bed."
    show kaito smi
    voice "audio/voice/E4/Kaito/d03/(16).ogg"
    hk "Alright, try not to stress too much about this. I promise we'll find out what happened."
    "I smile weakly."
    pf "Thanks, Uncle Kaito."
    hide kaito with dissolve
    $renpy.pause(0.5)
    stop music fadeout 5
    scene black with fade
    "After saying goodnight, I get ready for bed then slip under the blankets. I close my eyes, trying to clear my mind, but end up running through every detail of the accident I remember hoping to find a clue. Eventually, I fall asleep out of pure exhaustion."
    stop ambient fadeout 3
    $renpy.pause(1)
    
    jump E4D4S1
    
