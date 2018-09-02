#
label E2YMS4:
    
    #Weekend
    
    "Yuuna has really come through for me this past week and I feel like I should do something nice to thank her. Maybe she's free for lunch. {w}I dial her number and wait for her to answer."
    play sound "audio/sfx/Technology/Phone Dial.ogg"
    $renpy.pause(1)
    stop sound
    play sound2 "audio/sfx/Technology/Phone Answer.ogg"
    $renpy.pause(1)
    
    
    voice "audio/voice/E2/Free/YM/S4/1.ogg"
    ym "Hello?"
    pf "Hey, Yuuna. Have you eaten yet?"
    "She seems a little surprised."
    voice "audio/voice/E2/Free/YM/S4/2.ogg"
    ym "Oh, uh, no, not yet."
    pf "Great, let me treat you to lunch. {w}If it weren't for you, we never would have found a sponsor, and this is my way of saying thank you."
    pf "The team and I are really grateful for your help."
    voice "audio/voice/E2/Free/YM/S4/3.ogg"
    ym "You don't have to do that! Really it was no trouble at all."
    pf "Please, I insist."
    voice "audio/voice/E2/Free/YM/S4/4.ogg"
    ym "In that case, sure, I'd love to."
    voice "audio/voice/E2/Free/YM/S4/5.ogg"
    ym "Do you have a place in mind?"
    
    menu:
        "You can choose.":
            pf "We can go wherever you'd like to go."
            voice "audio/voice/E2/Free/YM/S4/6.ogg"
            ym "Since you've already offered to pay, I think we should go where you'd like to go."
            pf "Okay… hmm…"
            "Suddenly, I remember a past conversation with Uncle Kaito."
            pf "How do you feel about western cuisine?"
            voice "audio/voice/E2/Free/YM/S4/7.ogg"
            ym "I love it!"
            pf "I've heard there's a good western restaurant near the park."
            voice "audio/voice/E2/Free/YM/S4/8.ogg"
            ym "Oh! I think I know which place you're talking about. I haven't been before but have been meaning to try it."
    
        "Actually, I do!":
            "Kaito's restaurant immediately springs to mind."
            pf "I heard there's a popular western style restaurant which is pretty good."
            voice "audio/voice/E2/Free/YM/S4/9.ogg"
            ym "Oh! The place near the park?"
            pf "Yeah! Have you been there before?"
            voice "audio/voice/E2/Free/YM/S4/10.ogg"
            ym "No, but I've been meaning to try it! I mean, I've heard it's good too."
    
        "I don't care.":
            pf "It doesn't matter to me where we go."
            voice "audio/voice/E2/Free/YM/S4/11.ogg"
            ym "Oh, okay, well what type of food do you like?"
            pf "Anything. I'm not picky."
            voice "audio/voice/E2/Free/YM/S4/12.ogg"
            ym "Hm…"
            pf "What kind of food do you like?"
            voice "audio/voice/E2/Free/YM/S4/13.ogg"
            ym "Oh, um… well, actually… I like western cuisine."
            pf "Really?"
            voice "audio/voice/E2/Free/YM/S4/14.ogg"
            ym "Yeah, but I'm sure you don't want to eat that--"
            pf "No, let's do that."
            "I remember Uncle Kaito mentioning a place…"
            pf "I know of a restaurant next to the park that's supposed to be good."
            voice "audio/voice/E2/Free/YM/S4/15.ogg"
            ym "I know the place you're talking about. I've heard it's good too, but haven't been before."
    
    pf "Perfect, I'll meet you there."
    voice "audio/voice/E2/Free/YM/S4/16.ogg"
    ym "See you soon!"
    
    #day 6
    jump E2D6S1_Nikki
    
    label E2YMS4_Continued:
        
        $ yuuOut = "sCute"
        $ yuuHairF = renpy.random.choice([ 'bun', 'braided', 'extensions', 'pony' ])
        $ yuuHairB = yuuHairF
    
        play ambient "audio/ambience/Desert Maid Cafe.ogg" fadein 3
        scene bg campus cafe day with fade
        play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 3
        "The restaurant calls itself a diner, but has a more upscale atmosphere. The tables all have fresh tablecloths and a small vase with a flower. The ambiance is calmer than a diner but still family friendly."
        "Yuuna is waiting for me by the hostess stand when I arrive. That was pretty fast."
        show yuuna smi at cc with dissolve
        pf "Were you waiting long? I figured the bus would take a little more time than that."
        show yuuna hap at cc
        "Yuuna giggles and shakes her head."
        show yuuna mis at cc
        voice "audio/voice/E2/Free/YM/S4/17.ogg"
        ym "You're right, the bus would take more time. That's why I walked over."
        
        if E1D5S3_HelpedYuuna == 1:
            show yuuna smi at cc
            "Ah, that's right. Yuuna lives on the other side of the park. It's not too bad of a walk on a good day like today, but I certainly wouldn't want to walk it in bad weather."
        
        else:
            show yuuna smi at cc
            voice "audio/voice/E2/Free/YM/S4/18.ogg"
            ym "I only live about 20 minutes away. It's an easy walk."
        
        pf "Ah, well, I'm sure I've made you wait long enough. Let's go get seated."
        show yuuna cur at cc
        "Her brows furrow."
        show question:
            xoffset 720
            yoffset 100
            xzoom .75
            yzoom .75
        voice "audio/voice/E2/Free/YM/S4/19.ogg"
        ym "Shouldn't we wait for the others?"
        pf "...Others?"
        show yuuna neu at cc
        voice "audio/voice/E2/Free/YM/S4/20.ogg"
        ym "The rest of the team."
        "..."
        show yuuna ner b1 at cc with dissolve
        voice "audio/voice/E2/Free/YM/S4/21.ogg"
        ym "Oh."
        pf "I could call them--"
        show yuuna smi b1 at cc
        voice "audio/voice/E2/Free/YM/S4/22.ogg"
        ym "No, it's okay. Let's get seated."
        hide yuuna with dissolve
        "She grabs the hostess's attention, who leads us to a table. {w}We sit down and Yuuna buries her face in the menu."
        pf "Maybe I should call them. I know they'd want to thank you too."
        show yuuna ner at cc with dissolve
        "Yuuna makes eye contact for the first time since the misunderstanding, and her expression softens."
        show yuuna smi b1 at cc
        voice "audio/voice/E2/Free/YM/S4/23.ogg"
        ym "I'm sorry, I was just surprised. I don't mind hanging out just the two of us."
        show regBlush:
            xoffset 720
            yoffset 100
            xzoom .75
            yzoom .75
        "She blushes as she says that. {w}I grin."
        pf "Okay."
        hide yuuna with dissolve
        stop music fadeout 5
        "We both stare into our menus again. {w}I'm a little surprised by how extensive the menu is. They offer breakfast, lunch, dinner, and even a brunch on weekends."
        
        "..."
        play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 5
        pf "What are you going to order?"
        show yuuna smi at cc with dissolve
        voice "audio/voice/E2/Free/YM/S4/24.ogg"
        ym "Hmm… I think I will go with the burger."
        pf "You like American food?"
        show heart:
            xoffset 720
            yoffset 100
            xzoom .75
            yzoom .75
        show yuuna hap at cc
        voice "audio/voice/E2/Free/YM/S4/25.ogg"
        ym "Yes! The burger is my favourite but I also like hot dogs and pizza too."
        show yuuna smi at cc
        voice "audio/voice/E2/Free/YM/S4/26.ogg"
        ym "What will you get?"
        
        menu:
            "Choose something healthy.":
                pf "Hmm…"
                "I look at the salad section. They offer three types of salad."
        
                menu:
                    "Pick caesar salad.":
                        $ E2YMS4_Food = "Caesar"
                        "Let's play it safe and see if this tastes the same as back home."
                        pf "I will go with the caesar salad."
        
                    "Pick nicoise salad.":
                        $ E2YMS4_Food = "Nicoise"
                        "I always like to have a little protein with my salad."
                        pf "I'll go with the nicoise salad."
        
                    "Pick mushroom and lentil salad.":
                        $ E2YMS4_Food = "Lentil"
                        "This sounds really weird, but they're all veggies, so how bad can it be?"
                        pf "I'll go with mushroom and lentil salad."
        
                show yuuna cur at cc
                voice "audio/voice/E2/Free/YM/S4/27.ogg"
                ym "I didn't know you like to eat salad. Do you always try to eat healthy?"
                pf "I usually do."
                show yuuna hap at cc
                "She grins."
                voice "audio/voice/E2/Free/YM/S4/28.ogg"
                ym "As someone who cares about pilot health, I think that's great!"
                show yuuna smi at cc
        
            "Choose something adventurous!":
                "There are some items on here that would never exist outside of Japanese creativity… I need to try it!"
        
                menu:
                    "Cucumber and seaweed sandwich.":
                        $ E2YMS4_Food = "Sandwich"
                        "It has cucumber, seaweed, and sesame sauce. {w}It kind of reminds me of a sushi in a sandwich."
                        pf "I'm going to get the cucumber and seaweed sandwich."
        
                    "Avocado and honey toast.":
                        $ E2YMS4_Food = "Toast"
                        "It has avocado, honey, lime, and chili peppers. All these flavours will be like a party in my mouth!"
                        pf "I'm going to try the avocado and honey toast."
        
                    "German hot dog.":
                        $ E2YMS4_Food = "Dog"
                        "It's a bratwurst in a baguette with bacon, a sunny-side-up egg, hot sauce, and sauerkraut. {w}This one actually doesn't sound too weird at all considering all the \"gourmet\" hot dogs that have cropped up in the States."
                        pf "I'll go for the German hot dog."
        
                show yuuna sur at cc
                voice "audio/voice/E2/Free/YM/S4/29.ogg"
                ym "Ah! Is this typically what you will have back home?"
                pf "Not quite… We have toast, sandwiches, and hot dogs, but the fillings are different."
                show yuuna cur at cc
                voice "audio/voice/E2/Free/YM/S4/30.ogg"
                ym "Oh, well, it's true that our Japanese version of western food is not always accurate."
                pf "Yeah, but that's true of any other cuisine in a foreign country. I'm sure the Japanese food in the States tastes more American than Japanese."
                show yuuna smi at cc
                "Yuuna nods."
                voice "audio/voice/E2/Free/YM/S4/31.ogg"
                ym "I suppose you're right."
        
            "Choose something familiar.":
                "I'm missing my food from back home, but I spot a few of my favourites on the menu."
        
                menu:
                    "Burger and fries.":
                        $ E2YMS4_Food = "Burger"
                        pf "I'll also get the burger."
                        show note:
                            xoffset 720
                            yoffset 100
                            xzoom .75
                            yzoom .75
                        show yuuna hap at cc
                        "Yuuna beams."
        
                    "Steak.":
                        $ E2YMS4_Food = "Steak"
                        pf "I think I'll try the steak."
        
                    "B.L.T.":
                        $ E2YMS4_Food = "BLT"
                        pf "I'll get the bacon, lettuce, and tomato."
        
                pf "I hope it tastes similar to what I'm used to."
                show yuuna cur at cc
                voice "audio/voice/E2/Free/YM/S4/32.ogg"
                ym "Do you eat this a lot?"
                pf "I don't know if I'd say \"a lot\" but it's definitely something I would eat if I were back home."
                show yuuna smi at cc
                "Yuuna looks interested."
                voice "audio/voice/E2/Free/YM/S4/33.ogg"
                ym "You will have to tell me if it tastes the same."
                
        stop music fadeout 3
        "The waiter comes by and takes our order, complimenting us on our choices. Yuuna and I share an amused smile."
        pf "So, again, I want to thank you for working so hard to get us a sponsor, especially after that disaster of an interview."
        play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 5
        show yuuna dis at cc with dissolve
        "Yuuna's face clouds at the mention of the interview."
        show storm:
            xoffset 720
            yoffset 100
            xzoom .75
            yzoom .75
        voice "audio/voice/E2/Free/YM/S4/34.ogg"
        ym "That guy wouldn't have been good for you anyway. He couldn't see past his own ego to notice how strong of a team you guys are!"
        "I stare at her in surprise. She's usually so calm and positive..."
        show yuuna neu at cc
        voice "audio/voice/E2/Free/YM/S4/35.ogg"
        ym "What?"
        
        menu:
            "That's a little harsh.":
                pf "I understand where you're coming from, but I don't blame them for their decision."
                show yuuna wor at cc
                voice "audio/voice/E2/Free/YM/S4/36.ogg"
                ym "Aren't you even a little annoyed that they wouldn't give you a chance?"
                pf "I'm disappointed, but I get it."
                show yuuna dis at cc
                voice "audio/voice/E2/Free/YM/S4/37.ogg"
                ym "Well, their reasoning was not okay."
        
            "You tell 'em!":
                pf "You should give them a piece of your mind!"
                show vein:
                    xoffset 720
                    yoffset 100
                    xzoom .75
                    yzoom .75
                show yuuna ang at cc
                voice "audio/voice/E2/Free/YM/S4/38.ogg"
                ym "A part of me wants to!"
                show yuuna ann at cc
                pf "Ha, I like this fiery side of you."
                show yuuna wor b1 at cc with dissolve
                "Yuuna blushes."
                voice "audio/voice/E2/Free/YM/S4/39.ogg"
                ym "It's just… I don't like the way they treated you."
                show yuuna neu at cc with dissolve
        
            "I'm a little surprised.":
                pf "Nothing! I just didn't expect to hear that from you…"
                show yuuna mis at cc
                "She looks amused."
                voice "audio/voice/E2/Free/YM/S4/40.ogg"
                ym "I only say it because it's true."
        
        pf "Still, even after that experience, it's pretty amazing that you managed to get us such a great sponsor! You and the SBA are lifesavers!"
        stop music fadeout 5
        show yuuna thi at cc with dissolve
        "Yuuna fidgets in her seat."
        voice "audio/voice/E2/Free/YM/S4/41.ogg"
        ym "Oh, actually, I quit the SBA."
        play music "audio/music/Next Time (GAME VERSION).ogg" fadein 5
        pf "What?"
        show yuuna ann at cc
        voice "audio/voice/E2/Free/YM/S4/42.ogg"
        ym "I couldn't stay after what happened at the interview! The organisation has changed from what it used to be and has strayed too far from its mission."
        pf "Isn't the whole point of the SBA to help teams find sponsors? Does the organisation no longer do that?"
        show yuuna dis at cc
        voice "audio/voice/E2/Free/YM/S4/43.ogg"
        ym "The SBA was originally founded to help {i}all{/i} teams get matched up with a sponsor. But now, the only teams they care about are the top tier teams who don't really need the association's help because their stats speak for themselves."
        show yuuna ann at cc
        voice "audio/voice/E2/Free/YM/S4/44.ogg"
        ym "The people who really need their help get turned away or pushed aside, and I just don't agree with that."
        pf "Well, technically it was the company who turned us down, not the SBA."
        show yuuna dis at cc
        voice "audio/voice/E2/Free/YM/S4/45.ogg"
        ym "That's the problem--the only companies within the SBA network are those who feel the same as Warptech. I can't tell you how many calls I made only to get turned down once they knew your ranking."
        show yuuna ann at cc
        voice "audio/voice/E2/Free/YM/S4/46.ogg"
        ym "But the worst part is when my colleagues noticed me struggling, instead of offering to help, they encouraged me to give up because I was bringing down the association's statistics!"
        show yuuna ang at cc
        voice "audio/voice/E2/Free/YM/S4/47.ogg"
        ym "How can they call themselves a \"bridging\" association when they are so discriminatory? A bridge doesn't pick and choose who goes across it!"
        show yuuna ann at cc
        "As Yuuna speaks, she wears that same passionate look she wore after the interview."
        pf "I had no idea... {w}At least they had {i}one{/i} good company within their network, right? Otherwise we never would have found a sponsor."
        show yuuna cur at cc with dissolve
        $renpy.pause(.5)
        show yuuna thi at cc with dissolve
        "She blinks, then looks away."
        show drop:
            xoffset 720
            yoffset 100
            xzoom .75
            yzoom .75
        voice "audio/voice/E2/Free/YM/S4/48.ogg"
        ym "Oh, um…that's actually a bit of a different situation…"
        stop music fadeout 3
        "Her voice trails off. {w}Before I can ask what she means by that, our food arrives."
        $renpy.pause(1.33)
        "A few awkward seconds go by..."
        
        play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 5
        if E2YMS4_Food == "Burger":
            "I pick up my burger, and I'm about to take a bite when I notice Yuuna."
        
        show yuuna mis at cc with dissolve
        "Yuuna picks up her fork and knife and cuts into her burger, then eats the piece off of her fork."
        pf "Do you always eat your burgers with a fork and knife?"
        show exclamation:
            xoffset 720
            yoffset 100
            xzoom .75
            yzoom .75
        show yuuna cur at cc
        "She blinks in surprise."
        voice "audio/voice/E2/Free/YM/S4/49.ogg"
        ym "Yeah…"
        pf "How come?"
        show question:
            xoffset 720
            yoffset 100
            xzoom .75
            yzoom .75
        voice "audio/voice/E2/Free/YM/S4/50.ogg"
        ym "Isn't that how you eat western food?"
        pf "For some foods, yeah, but burgers are easier to eat when you pick it up."
        pf "Have you {i}never{/i} picked up a burger before?"
        show yuuna ner at cc
        "Yuuna shakes her head."
        pf "Not even if you get fast food?"
        show yuuna thi at cc
        "She wrinkles her nose."
        voice "audio/voice/E2/Free/YM/S4/51.ogg"
        ym "No, but I'm not a fan of fast food anyway."
        show yuuna ske at cc
        
        if E2YMS4_Food == "Burger":
            "She glances at the burger in my hands."
        
        voice "audio/voice/E2/Free/YM/S4/52.ogg"
        ym "Isn't it messy if you eat with your hands?"
        
        menu:
            "Not always.":
                pf "That depends on how full the burger is. This one shouldn't be messy."
                show yuuna ner at cc
                voice "audio/voice/E2/Free/YM/S4/53.ogg"
                ym "But isn't it rude to eat with your hands?"
                pf "Not when it's between friends!"
        
                if E2YMS4_Food == "Burger":
                    show yuuna cur at cc
                    "I take a big bite."
                    pf "See? Nothing fell out."
                    show yuuna ner at cc
                    "I take another bite. {w}Yuuna watches me, then carefully holds her burger with her fingertips and takes a dainty bite."
        
                else:
                    show yuuna cur with dissolve
                    "Yuuna bites her lip uncertainly, then gingerly holds her burger with her fingertips and takes a dainty bite."
        
                "There's a spot of ketchup on her cheek when she puts her burger back down. I stifle a laugh."
                pf "You have a little something on your cheek…"
                show yuuna sur at cc
                "Her eyes grow wide. She snatches the napkin from her lap and dabs at her face."
                voice "audio/voice/E2/Free/YM/S4/54.ogg"
                ym "Did I get it?"
                show yuuna ner at cc
                pf "No…"
        
                ### NOTE Points - "IF high points with Yuuna:"
                # temporarily set to 0
                if yuuromance > 0:
                    show yuuna sur at cc
                    "I lean over and wipe the ketchup off with a napkin."
                    show yuuna sur b1 at cc with dissolve
                    "Yuuna gasps at my touch, and her face turns pink."
                    show regBlush:
                        xoffset 720
                        yoffset 100
                        xzoom .75
                        yzoom .75
                    show yuuna smi b1 at cc
                    voice "audio/voice/E2/Free/YM/S4/55.ogg"
                    ym "Oh! Um, thank you."
                    pf "No problem."
        
                else:
                    "She wipes her face again with the napkin."
                    voice "audio/voice/E2/Free/YM/S4/56.ogg"
                    ym "How about now?"
                    pf "Yup."
                    show yuuna smi at cc
        
                pf "Well, what do you think?"
                show yuuna hap at cc with dissolve
                "Yuuna grins, then picks up her burger and takes another bite. {w}I smile back."
        
            "That's what your napkin is for!":
                pf "So what if it is? There's a reason people put a napkin on their lap."
                show yuuna ner at cc
                voice "audio/voice/E2/Free/YM/S4/57.ogg"
                ym "I think I'll stick with the fork and knife."
                pf "You're missing out! Half the fun of eating a burger is feeling the juices drip down your chin."
                show yuuna sur at cc
                "Yuuna's eyes grow wide."
                show panic:
                    xoffset 720
                    yoffset 100
                    xzoom .75
                    yzoom .75
                voice "audio/voice/E2/Free/YM/S4/58.ogg"
                ym "I-I couldn't! I'd be too embarrassed."
        
                if E2YMS4_Food == "Burger":
                    "I take a bite out of my burger and some ketchup drips onto my plate."
                    pf "See? Not bad, right?"
                    show yuuna smi at cc
                    "Yuuna giggles."
                    voice "audio/voice/E2/Free/YM/S4/59.ogg"
                    ym "There's a little something on your cheek…"
                    "I stick out my tongue and lick around my cheek."
                    pf "Did I get it?"
                    show yuuna mis at cc
                    voice "audio/voice/E2/Free/YM/S4/60.ogg"
                    ym "No…"
        
                    ### NOTE Points - "IF high points with Yuuna:"
                    # temporarily set to 0
                    if yuuromance > 0:
                        voice "audio/voice/E2/Free/YM/S4/61.ogg"
                        ym "It's right there…"
                        "She points at my cheek. I use my hand to wipe at the spot, and Yuuna giggles again."
                        show yuuna hap at cc
                        voice "audio/voice/E2/Free/YM/S4/62.ogg"
                        ym "No, it's… here."
                        show yuuna smi b2 at cc with dissolve
                        "Grabbing her napkin, she dabs at a spot on my face. As she leans back in her chair, her face turns bright pink."
                        pf "Thanks."
        
                    else:
                        show yuuna smi at cc
                        "She points to the same spot on her own cheek."
                        voice "audio/voice/E2/Free/YM/S4/63.ogg"
                        ym "It's right here."
                        "I grab my napkin and dab at my face."
                        pf "Did I get it?"
                        show yuuna hap at cc
                        voice "audio/voice/E2/Free/YM/S4/64.ogg"
                        ym "Yup!"
        
                    pf "Okay, point taken."
                    
                else:
                    pf "You don't have to be embarrassed. If you're worried about getting messy we can ask for more napkins."
                    show yuuna smi with dissolve
                    voice "audio/voice/E2/Free/YM/S4/65.ogg"
                    ym "That's okay."
                    "I shrug."
        
        
            "Do what you like.":
                pf "Sometimes, but if you'd rather use a fork and knife then you can do that. It doesn't matter."
                show yuuna ner at cc
                "Yuuna hesitates."
                voice "audio/voice/E2/Free/YM/S4/66.ogg"
                ym "What do they do in the States?"
                pf "We use our hands."
        
                ### NOTE Points - "IF high points with Yuuna:"
                # temporarily set to 0
                if yuuromance > 0:
                    show yuuna cur at cc
                    "She gingerly picks up her burger and takes a dainty bite."
                    voice "audio/voice/E2/Free/YM/S4/67.ogg"
                    ym "Like that?"
                    "I grin."
                    pf "Yeah, now you look like a native."
                    show yuuna smi b1 at cc with dissolve
                    "She blushes, and takes another bite."
        
                else:
                    show yuuna cur b1 at cc with dissolve
                    "She stares at her burger and her face turns pink. Then she shakes her head."
                    show yuuna ner b1 at cc
                    voice "audio/voice/E2/Free/YM/S4/68.ogg"
                    ym "I can't get the image of everything falling out of the burger and into my lap out of my head."
                    pf "It's okay. Just keep doing what you're doing."
                    show yuuna smi b1 at cc
                    "She smiles gratefully, and nods."
                    
        hide yuuna with dissolve
        "We fall silent as we dig into our meals. {w}After a while, I start to fidget from the quiet."
        pf "So, now that you've quit the SBA, are you planning on joining any other clubs?"
        show yuuna neu at cc with dissolve
        "She pauses."
        show yuuna thi at cc
        voice "audio/voice/E2/Free/YM/S4/69.ogg"
        ym "I hadn't thought about it…"
        pf "What about tennis? Maybe now you'll have time to compete."
        show yuuna hap at cc
        "She laughs lightly."
        voice "audio/voice/E2/Free/YM/S4/70.ogg"
        ym "Maybe. That's still a pretty big commitment--bigger than the SBA!"
        pf "I'll help you practice."
        show yuuna smi at cc
        "She grins."
        voice "audio/voice/E2/Free/YM/S4/71.ogg"
        ym "How can I say no to an offer like that?"
        pf "And I promise I'll win this time!"
        show yuuna mis at cc
        voice "audio/voice/E2/Free/YM/S4/72.ogg"
        ym "Alright, I'll go easy on you then."
        pf "Wait, what?"
        show note:
            xoffset 720
            yoffset 100
            xzoom .75
            yzoom .75
        show yuuna smi at cc
        "Yuuna just smiles and hides a laugh."
        
        show yuuna cur at cc
        "She glances at my nearly empty plate."
        voice "audio/voice/E2/Free/YM/S4/73.ogg"
        ym "How is your food?"
        
        menu:
            "Like heaven in my mouth!":
                show yuuna smi at cc
                pf "This is great!"
        
                if E2YMS4_Food != "Burger":
                    pf "Do you want to try it?"
        
                    ### NOTE Points - "IF high points with Yuuna:"
                    # temporarily set to 0
                    if yuuromance > 0:
                        show yuuna cur at cc
                        voice "audio/voice/E2/Free/YM/S4/74.ogg"
                        ym "Oh! Okay!"
                        show yuuna neu at cc
                        voice "audio/voice/E2/Free/YM/S4/75.ogg"
                        ym "Hold on, let me just grab my fork…"
                        "She reaches for her fork, but I spear a piece of my food onto my fork and offer it to her."
                        pf "Here, have a bite."
                        show yuuna ner at cc
                        voice "audio/voice/E2/Free/YM/S4/76.ogg"
                        ym "Oh… um…"
                        "She hesitates, then gently leans over and puts her mouth over the fork. {w}Her cheeks flush as she chews."
                        show yuuna smi b1 at cc with dissolve
                        voice "audio/voice/E2/Free/YM/S4/77.ogg"
                        ym "It's good!"
                        pf "I told you!"
        
                    else:
                        show yuuna hap at cc
                        voice "audio/voice/E2/Free/YM/S4/78.ogg"
                        ym "Thank you, but I couldn't! I'm so full. Maybe next time I'll get that."
                        pf "You should. I highly recommend it."
                        show yuuna smi at cc
                        
                else:
                    pf "If I didn't know any better, I'd think it was made by an American."
                    show yuuna sur at cc
                    "Yuuna's face lights up."
                    show shiny:
                        xoffset 720
                        yoffset 100
                        xzoom .75
                        yzoom .75
                    voice "audio/voice/E2/Free/YM/S4/79.ogg"
                    ym "Ooh, really? So this is what an authentic burger tastes like…"
        
            "I'd rate it a solid C.":
                pf "It's not the best thing that I've had, but it's not the worst either."
                show yuuna mis at cc
                "Her face is a mixture of amusement and confusion."
                voice "audio/voice/E2/Free/YM/S4/80.ogg"
                ym "So, would you get it again?"
                pf "Ehh… I'd probably try something else first."
        
            "I've made a terrible mistake.":
                pf "Not something fit for human consumption."
                show yuuna cur at cc
                "She furrows her brow in concern."
                voice "audio/voice/E2/Free/YM/S4/81.ogg"
                ym "That sounds serious! And you ate so much of it."
                pf "...I was hungry."
        
        pf "How was your meal?"
        show yuuna smi at cc
        "Yuuna's already polished her plate, so I can guess what the answer is."
        show heart:
            xoffset 720
            yoffset 100
            xzoom .75
            yzoom .75
        show yuuna hap at cc
        voice "audio/voice/E2/Free/YM/S4/82.ogg"
        ym "I loved it! This was one of the best burgers I've had in Isokaze."
        hide yuuna with dissolve
        stop music fadeout 5
        "I grin. I'll have to pass the compliment on to Uncle Kaito."
        stop ambient fadeout 5
        "Once I close out the check, Yuuna and I pause right outside the restaurant."
        play ambient "audio/ambience/Campus Road.ogg" fadein 3
        scene bg campus intersection day with fade
        play music "audio/music/Day Out (GAME VERSION).ogg" fadein 5
        show yuuna hap at cc with dissolve
        voice "audio/voice/E2/Free/YM/S4/83.ogg"
        ym "Thank you for a really lovely meal."
        pf "It was my pleasure."
        show yuuna smi at cc
        voice "audio/voice/E2/Free/YM/S4/84.ogg"
        ym "I better get going."
        pf "Can I offer you a ride home?"
        "She smiles."
        show yuuna hap at cc
        voice "audio/voice/E2/Free/YM/S4/85.ogg"
        ym "Thank you, but I can walk." 
        
        menu:
            "But what about the hooligans?":
                pf "Are you sure it's safe for you to walk alone? I've heard that some kids like to hang around the park and cause trouble."
                show yuuna smi at cc
                "She smiles."
                voice "audio/voice/E2/Free/YM/S4/86.ogg"
                ym "Don't worry, it's a bright, sunny day outside. I'll be fine."
        
            "I'm open to a little exercise with you.":
                pf "I like going on long walks too… especially with such lovely company."
                show regBlush:
                    xoffset 720
                    yoffset 100
                    xzoom .75
                    yzoom .75
                show yuuna smi b1 at cc with dissolve
                "Yuuna blushes."
                voice "audio/voice/E2/Free/YM/S4/87.ogg"
                ym "It's not that long. Really, I'll be fine going on my own."
        
            "Don't argue with her.":
                "I nod. {w}She already made the walk over here by herself. I'm sure she'll be able to handle the walk home alone too."
                show yuuna smi at cc
                pf "Alright, if you're sure."
        
            "I know where you live." if E1D5S3_HelpedYuuna == 1:
                pf "I already know where you live if that's what you're worried about."
                show yuuna mis at cc
                voice "audio/voice/E2/Free/YM/S4/88.ogg"
                ym "Well, I guess that means it's time for me to move!"
                show yuuna smi at cc
                "I blink, but Yuuna wears a playful smile."
                
        show yuuna thi at cc
        voice "audio/voice/E2/Free/YM/S4/89.ogg"
        ym "I have to run some errands before my parents come home anyway."
        "Weren't her parents away last time too?"
        pf "Are your parents gone a lot?"
        show yuuna neu at cc
        voice "audio/voice/E2/Free/YM/S4/90.ogg"
        ym "Yeah…"
        voice "audio/voice/E2/Free/YM/S4/91.ogg"
        ym "They split their time between the house here and our house in the country. Right now they're in the country, but they'll be back tomorrow for a few days so I want to have the house tidied up before they arrive."
        pf "A house in the country?"
        show yuuna smi at cc
        voice "audio/voice/E2/Free/YM/S4/92.ogg"
        ym "That's where I grew up! My family moved here to be closer to ACE Academy, but they aren't quite ready to give up our old house yet."
        pf "But if your family isn't around, how come you didn't choose to stay in the dorms? It would be an easier commute to school."
        show yuuna thi at cc
        voice "audio/voice/E2/Free/YM/S4/93.ogg"
        ym "I thought about it… but…"
        show dots:
            xoffset 720
            yoffset 100
            xzoom .75
            yzoom .75
        "She hesitates."
        show yuuna neu at cc
        voice "audio/voice/E2/Free/YM/S4/94.ogg"
        ym "After everything that's happened, it doesn't feel right to leave my family alone. My parents do stay here for extended periods of time--like months at a time! It's just hard to predict {i}when{/i} they'll be here."
        
        if MCStory == 3:
            "This is exactly how I feel about Nikki and why I left CINY. I wonder if Yuuna lost someone in her family too…"
        
        else:
            "I wonder what her family went through…"
            
        show yuuna smi at cc
        voice "audio/voice/E2/Free/YM/S4/95.ogg"
        ym "Anyway, I really should get going."
        "I nod."
        pf "Same here, I'll see you later then."
        hide yuuna with dissolve
        stop music fadeout 5
        scene black with fade
        "She waves, then starts to walk. {w}Once she's out of view, I drive off and head home."
        stop ambient fadeout 3
        $renpy.pause(1)
        $ E2YMS4_Completed = 1
        jump E2D6S2
