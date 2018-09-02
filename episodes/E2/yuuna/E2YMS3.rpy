#
label E2YMS3:
    
    #Event 3 - Afternoon Choice (>65 Points)
    
    "I'm on my way to grab something to eat when I pass by the campus bookstore. I have a lot of CINY swag at home, but I don't have anything from ACE yet. It wouldn't hurt to take a look and see what they have."
    
    if E1D3S1_BusRide == 0:
        "Plus, remembering how impressed Nikki's friends were when they found out I went to ACE, I bet Nikki would love to have some ACE Academy swag."
    
    else:
        "Maybe Nikki would like something from here too."
        
    stop ambient fadeout 2
    stop music fadeout 2
    scene black with fade
    #play ambient "audio/ambience/Campus Office.ogg" fadein 3
    scene bg campus office day with fade
    "I walk in. The cashier counters are right by the entrance. As I go further inside, I can turn either into the clothing section or the book section."
    
    menu:
        "Check out the books.":
            $ E2YMS3_CheckBooks = 1
            "The books are organized by class and take up two levels in the store. I'm a little surprised they still offer hard copies of all the class texts since most people just purchase the electronic versions now. There's an option to rent the books for the school year too. {w}Not too many students are browsing in this area. I already have all the texts I need so I move on."
            "Next to the books are miscellaneous school supplies. {w}There's a pink planner with the ACE Academy logo I think Nikki will really like."
            "I grab the planner for Nikki and a notebook for myself, then stand in line to check-out."
    
        "Check out the clothing.":
            $ E2YMS3_CheckBooks = 0
            "There are racks of T-shirts, sweaters, hoodies, etc., all in different sizes with the ACE Academy school name and logo on them. There are even ACE Academy baby clothes!"
            "I browse the T-shirt section and and spot one I like. It's got the ACE logo in the center and teal stripes around the edges, kind of like our uniforms."
            "Next I check out the hoodies and immediately spot the perfect one for Nikki. It's pink and has the ACE logo in the top corner."
            "I grab the hoodie for Nikki and the T-shirt for me, then stand in line to check-out."
    
    "I'm zoning out while waiting for my turn in line, when a familiar voice interrupts me."
    play music "audio/music/Day Out (GAME VERSION).ogg" fadein 5
    voice "audio/voice/E2/Free/YM/S3/1.ogg"
    ym "Hey there."
    show yuuna smi at cc with dissolve
    "I spin around and see Yuuna's smiling face standing in line behind me. {w}She glances at my items and holds back a laugh."
    
    if E2YMS3_CheckBooks == 1:
        show heart:
            xoffset 720
            yoffset 100
            xzoom .75
            yzoom .75
        show yuuna hap at cc
        voice "audio/voice/E2/Free/YM/S3/2.ogg"
        ym "That's a pretty planner you chose."
        "She has the same one in her hand."
        show yuuna mis at cc
        voice "audio/voice/E2/Free/YM/S3/3.ogg"
        ym "You must have good taste."
    
    else:
        show heart:
            xoffset 720
            yoffset 100
            xzoom .75
            yzoom .75
        show yuuna hap at cc
        voice "audio/voice/E2/Free/YM/S3/4.ogg"
        ym "That's a pretty hoodie you have there."
        "She's holding the same one."
        show yuuna mis at cc
        voice "audio/voice/E2/Free/YM/S3/5.ogg"
        ym "But I think you might need a bigger size."
        
    show yuuna smi at cc
    "I laugh and Yuuna lets out a giggle."
    pf "No, this isn't for me. It's for my sister."
    "I hold up the item I bought for myself."
    pf "This is for me."
    show yuuna hap at cc
    voice "audio/voice/E2/Free/YM/S3/6.ogg"
    ym "Ohhh, well I think she'll like it."
    show yuuna smi at cc
    voice "audio/voice/E2/Free/YM/S3/7.ogg"
    ym "Is your sister younger than you?"
    pf "Yeah, she's in her last year of high school."
    show yuuna smi at cc
    voice "audio/voice/E2/Free/YM/S3/8.ogg"
    ym "It seems like you two are close."
    pf "Really? What makes you say that?"
    show yuuna thi at cc
    voice "audio/voice/E2/Free/YM/S3/9.ogg"
    ym "Well, teenagers usually go through a phase where they fight with their sibling all the time, but since you're buying her a gift, it seems like you two must get along."
    pf "Ah, yeah, we do."
    show yuuna smi at cc
    "Yuuna smiles warmly."
    voice "audio/voice/E2/Free/YM/S3/10.ogg"
    ym "That must be really nice."
    stop music fadeout 5.0
    pf "Yeah. How about you? Do you have any siblings?"
    show yuuna cur at cc with dissolve
    show dots:
        xoffset 720
        yoffset 100
        xzoom .75
        yzoom .75
    $renpy.pause(.5)
    show yuuna neu at cc with dissolve
    $renpy.pause(.5)
    "Yuuna hesitates, and shifts her items from one hand to the other. Finally, she shakes her head."
    voice "audio/voice/E2/Free/YM/S3/11.ogg"
    ym "No."
    "She breaks eye contact and looks down."
    
    if MCStory == 3:
        "Before she looked away, I noticed a sadness in her eyes. There's something she's not telling me, but I can tell that it hurts her deeply to talk about it. {w}I should respect her feelings and leave it be. I shouldn't pry."
    
    else:
        "It feels like there's something she's not telling me…"
    
    menu:
        "{color=#00ff00}{b}Don't ask her about it.{/b}{/color}" if MCStory == 3:
            "Yuuna seems really uncomfortable by this topic. I shouldn't force her to talk about it."
            pf "I'm sorry, we don't have to talk about this."
            show yuuna smi at cc
            "She gives me a grateful smile."
            voice "audio/voice/E2/Free/YM/S3/12.ogg"
            ym "It's okay."
            "Glancing at her hands, I see her carrying the book {i}Hamlette{/i}."
            play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 3.0
            pf "{i}\"To bee or not to bee, that is the question.\"{/i}"
            show question:
                xoffset 720
                yoffset 100
                xzoom .75
                yzoom .75
            show yuuna cur at cc
            voice "audio/voice/E2/Free/YM/S3/13.ogg"
            ym "Huh?"
            pf "Your book."
            show yuuna hap at cc
            "She glances at her hands, and chuckles."
            voice "audio/voice/E2/Free/YM/S3/14.ogg"
            ym "Oh, right. It's for one of my classes."
            pf "Ah yeah. I bought the e-versions of my texts."
            show yuuna smi at cc
            "Yuuna nods."
            voice "audio/voice/E2/Free/YM/S3/15.ogg"
            ym "I did too for most of them, but I find it's easier for me to take notes when I have a physical copy of the text in front of me."
            "She opens the book and flips through it."
            pf "Hey, that's in English!"
            show yuuna cur at cc
            "She blinks at me."
            voice "audio/voice/E2/Free/YM/S3/16.ogg"
            ym "Yeah, it's for my English Literature class."
            "I switch to speaking English."
            pf "{b}I didn't know you can speak English.{/b}"
            show yuuna smi at cc
            voice "audio/voice/E2/Free/YM/S3/17.ogg"
            ym "{b}Not very well.{/b}"
            "She answers in English. Her accent is good, but she speaks with the confidence of someone who's not used to conversing with a native speaker."
            "I switch back to Japanese to make her more comfortable."
            pf "It seems good to me!"
            show yuuna hap at cc
            voice "audio/voice/E2/Free/YM/S3/18.ogg"
            ym "Thanks, but I know I still have a lot to work on."
            pf "Well, if you ever want to practice I'll be happy to help."
            show regBlush:
                xoffset 720
                yoffset 100
                xzoom .75
                yzoom .75
            show yuuna smi b1 at cc with dissolve
            voice "audio/voice/E2/Free/YM/S3/19.ogg"
            ym "Okay, thanks!"
            
            voice "audio/voice/E2/Free/YM/S1/stu8m/3.ogg"
            rc1m "Next in line."
            pf "Ah! That's me. We'll catch up next time, okay?"
            show yuuna hap b1 at cc
            "She smiles."
            voice "audio/voice/E2/Free/YM/S3/20.ogg"
            ym "Of course."
            hide yuuna with dissolve
            stop music fadeout 5
            scene black with fade
            "I go up to the counter and pay for my items. Then wave goodbye to Yuuna as I head out of the store."
            stop ambient fadeout 3
            $renpy.pause(1)
            $ E2YMS3_Completed = 1
            #end
    
        "Don't ask her about it." if MCStory != 3:
            "Yuuna seems really uncomfortable by this topic. I shouldn't force her to talk about it."
            pf "I'm sorry, we don't have to talk about this."
            show yuuna smi at cc
            "She gives me a grateful smile."
            voice "audio/voice/E2/Free/YM/S3/12.ogg"
            ym "It's okay."
            "Glancing at her hands, I see her carrying the book {i}Hamlette{/i}."
            play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 3.0
            pf "{i}\"To bee or not to bee, that is the question.\"{/i}"
            show question:
                xoffset 720
                yoffset 100
                xzoom .75
                yzoom .75
            show yuuna cur at cc
            voice "audio/voice/E2/Free/YM/S3/13.ogg"
            ym "Huh?"
            pf "Your book."
            show yuuna hap at cc
            "She glances at her hands, and chuckles."
            voice "audio/voice/E2/Free/YM/S3/14.ogg"
            ym "Oh, right. It's for one of my classes."
            pf "Ah yeah. I bought the e-versions of my texts."
            show yuuna smi at cc
            "Yuuna nods."
            voice "audio/voice/E2/Free/YM/S3/15.ogg"
            ym "I did too for most of them, but I find it's easier for me to take notes when I have a physical copy of the text in front of me."
            "She opens the book and flips through it."
            pf "Hey, that's in English!"
            show yuuna cur at cc
            "She blinks at me."
            voice "audio/voice/E2/Free/YM/S3/16.ogg"
            ym "Yeah, it's for my English Literature class."
            "I switch to speaking English."
            pf "{b}I didn't know you can speak English.{/b}"
            show yuuna smi at cc
            voice "audio/voice/E2/Free/YM/S3/17.ogg"
            ym "{b}Not very well.{/b}"
            "She answers in English. Her accent is good, but she speaks with the confidence of someone who's not used to conversing with a native speaker."
            "I switch back to Japanese to make her more comfortable."
            pf "It seems good to me!"
            show yuuna hap at cc
            voice "audio/voice/E2/Free/YM/S3/18.ogg"
            ym "Thanks, but I know I still have a lot to work on."
            pf "Well, if you ever want to practice I'll be happy to help."
            show regBlush:
                xoffset 720
                yoffset 100
                xzoom .75
                yzoom .75
            show yuuna smi b1 at cc with dissolve
            voice "audio/voice/E2/Free/YM/S3/19.ogg"
            ym "Okay, thanks!"
            
            rc1m "Next in line."
            pf "Ah! That's me. We'll catch up next time, okay?"
            show yuuna hap b1 at cc
            "She smiles."
            voice "audio/voice/E2/Free/YM/S3/20.ogg"
            ym "Of course."
            hide yuuna with dissolve
            stop music fadeout 5
            scene black with fade
            "I go up to the counter and pay for my items. Then wave goodbye to Yuuna as I head out of the store."
            stop ambient fadeout 3
            $renpy.pause(1)
            $ E2YMS3_Completed = 1
            #end
    
        "Ask her about it.":
            pf "Are you okay? I'm sorry if I offended you."
            show yuuna hap at cc
            "Yuuna looks back at me with a smile that's too cheerful."
            voice "audio/voice/E2/Free/YM/S3/21.ogg"
            ym "Yes, I'm fine. Please don't worry about me."
            pf "Okay… {w}Does that mean you'll tell me what's going on?"
            show yuuna cur at cc
            voice "audio/voice/E2/Free/YM/S3/22.ogg"
            ym "What do you mean?"
            pf "I don't know… I get the feeling you're hiding something from me."
            stop music fadeout 5
            show yuuna neu at cc
            "Yuuna is silent. Then she points to the empty lane beside us."
            voice "audio/voice/E2/Free/YM/S3/23.ogg"
            ym "I'm actually in a bit of a hurry so I'm going to ring up my items in that empty lane over there."
            pf "Yuuna--"
            show yuuna hap at cc
            voice "audio/voice/E2/Free/YM/S3/24.ogg"
            ym "I'll catch you later, okay?"
            pf "Okay…"
            hide yuuna with dissolve
            "Still wearing her forced smile, she goes into the next lane, pays, and then hurries out of the store."
            "I hope I didn't offend her."
            scene black with fade
            stop ambient fadeout 3
            "Once it's my turn, I pay for my items and leave."
            $renpy.pause(1)
            $ E2YMS3_Completed = 1
            #end

