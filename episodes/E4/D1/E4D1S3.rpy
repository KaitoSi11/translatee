#
label E4D1S3:
    
    ### NOTE - check event transition when implemented
    scene black with fade
    play ambient "audio/ambience/Campus.ogg" fadein 3
    scene bg campus main day with fade
    $ E4SSS1_NOTDAY1 = 1
    $ shoOut = "sCasual"
    play sound "audio/sfx/Technology/Phone Vibration Once.ogg"
    "My phone vibrates in my pocket. When I go to answer, I see Shou is calling me."

        
    pf "Hey Shou."
    voice "audio/voice/E4/Shou/d1/48 Copy.ogg"
    ss "Broseph! I'm so glad you picked up. I need your help!"
    

    pf "Are you okay?"

        
    voice "audio/voice/E4/Shou/d1/49 Copy.ogg"
    ss "No! I'm in dire need of assistance!"
    pf "What's going on?"
    voice "audio/voice/E4/Shou/d1/50 Copy.ogg"
    ss "Do you have any experience buying a gift?... For a ladyfriend?"
    pf "Uhh…"
    
    if E3MAS3_RealCompleted == 1:
        "I know he's talking about Mayu. Even though they haven't officially announced it to the group, the two of them have become inseparable--even more so than before."
    
        menu:
            "Help him.":
                "I know I messed up my chance with Mayu, and at first seeing them together really stung. Now that I've had some time to process what happened, I realise that Mayu and Shou are really good together. They're both my friends and they deserve happiness."
                pf "I may know a thing or two."
            
            "Don't help him.":
                "I know I messed up my chance with Mayu, and that fact still stings. I still wonder how that date could have gone so wrong."
                "Seeing her smile at Shou… it reminds me that it should have been me."
                "I want to be happy for my friends, and I will, eventually. I just need a little more time."
                "Besides, the only time I tried to do something special for a \"ladyfriend\" I royally screwed it up. I doubt he'd want my help."
                pf "Sorry, bro, I can't help you there."
                voice "audio/voice/E4/Shou/d1/51 Copy.ogg"
                ss "Oh."
                "I feel a twinge of guilt at his disappointment."
                voice "audio/voice/E4/Shou/d1/52 Copy.ogg"
                ss "That's okay. I guess I'll ask… Kaori?"
                "I try to imagine what kind of gift Kaori would pick out for Mayu. Probably something really practical and not romantic at all."
                voice "audio/voice/E4/Shou/d1/53 Copy.ogg"
                ss "Actually, maybe Yuuna would have some ideas."
                "He must have had the same thought I had."
                pf "Yeah, I'd stick with Yuuna."
                voice "audio/voice/E4/Shou/d1/54 Copy.ogg"
                ss "Thanks for pointing me in the right direction at least!"
                pf "No problem. Good luck!"
                voice "audio/voice/E4/Shou/d1/55 Copy.ogg"
                ss "Thanks, I'll need it."
                "Shou says a hasty goodbye before hanging up. I feel a little bad letting him down like that. I hope he's not upset with me."
                jump E4D1S3_Converge
    
    elif mayrelatonship == 1:
        $ E4D1S3_Target = "Hitomi"
        pf "You're talking about Hitomi, right?"
        voice "audio/voice/E4/Shou/d1/56 Copy.ogg"
        ss "Yeah! I still can't believe she's into me."
        pf "Me neither."
        "Shou laughs."
        voice "audio/voice/E4/Shou/d1/57 Copy.ogg"
        ss "Thanks for the vote of confidence."
        pf "Anytime."
    
    else:
        $ E4D1S3_Target = "Mayu"
        pf "We all know your \"ladyfriend\" is Mayu."
        "There's no answer for just a second, then Shou speaks."
        voice "audio/voice/E4/Shou/d1/58 Copy.ogg"
        ss "It still feels kind of surreal."
        pf "I get it."
    
    voice "audio/voice/E4/Shou/d1/59 Copy.ogg"
    ss "So, does that mean you'll help?"
    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 5
    pf "I can't leave my bro hanging."
    "Shou sighs in relief."
    voice "audio/voice/E4/Shou/d1/60 Copy.ogg"
    ss "You are the best broseph a bro could have. Come meet me at the mall."
    pf "I'll be right there."
    scene black with fade
    stop ambient fadeout 3
    "I hang up the phone and head to my bike. Then I drive directly to the mall."
    $renpy.pause(1)
    play ambient "audio/ambience/Mall.ogg" fadein 3
    scene bg mall main day with fade
    "After I park, I see Shou waiting for me at the main entrance. He greets me with his usual goofy grin, but his hair is disheveled and there's worry in his eyes."
    show shou hap at cc with dissolve
    voice "audio/voice/E4/Shou/d1/61 Copy.ogg"
    ss "Thanks for meeting me. I don't even know where to start!"
    
    $ E4D1S3_Suggestion = "None"
    
    menu:
        "Suggest jewelry.":
            $ E4D1S3_Suggestion = "Jewelry"
            pf "Girls love expensive jewelry."
            show shou cur
            voice "audio/voice/E4/Shou/d1/62 Copy.ogg"
            ss "How expensive?"
            "Although he asks the question, he doesn't sound too worried over the cost."
            pf "The pricier the better."
            show shou thi
            voice "audio/voice/E4/Shou/d1/63 Copy.ogg"
            ss "I don't feel like she's that materialistic…"
            pf "It's not about being materialistic. It's more sentimental for her."
            # question
            show shou ske
            voice "audio/voice/E4/Shou/d1/64 Copy.ogg"
            ss "It is?"
            pf "Sure, not only does she get to feel beautiful by wearing an exquisite piece of jewelry, she'll also think you're really sweet for spending money on her."
            show shou neu
            voice "audio/voice/E4/Shou/d1/65 Copy.ogg"
            ss "Hmm… girls do like shiny things..."
            pf "...I wouldn't word it like that."
    
        "Suggest stuffed animals.":
            $ E4D1S3_Suggestion = "Animal"
            pf "Get her a cute, fuzzy, animal."
            
            # drop
            show shou thi
            
            if E4D1S3_Target == "Mayu":
                voice "audio/voice/E4/Shou/d1/66 Copy.ogg"
                ss "I'm pretty sure Mayu's dad would not approve of her devoting even less energy to her studies."
            else:
                voice "audio/voice/E4/Shou/d1/67 Copy.ogg"
                ss "I'm not sure Hitomi's allowed to have a pet in her dorm…"
            
            pf "Not a real animal--a toy one!"
            show shou neu
            "Shou looks thoughtful."
            voice "audio/voice/E4/Shou/d1/68 Copy.ogg"
            ss "You think she'd like that?"
            pf "Oh yeah. Trust me, Nikki's room is filled with them."
    
        "Suggest chocolate.":
            $ E4D1S3_Suggestion = "Chocolate"
            pf "Do you even have to ask? Get her chocolate!"
            show shou ske
            voice "audio/voice/E4/Shou/d1/69 Copy.ogg"
            ss "I don't know…"
            pf "Have you ever met a girl who wouldn't eat chocolate?"
            # dots
            show shou thi
            "Shou thinks hard about it."
            show shou neu
            voice "audio/voice/E4/Shou/d1/70 Copy.ogg"
            ss "No… No, I haven't…"
            pf "Exactly."
    
        "Suggest books." if E4D1S3_Target == "Mayu" and MCStory != 3:
            jump E4D1S3_Books
            
        "{color=#00ff00}{b}Suggest books.{/b}{/color}" if E4D1S3_Target == "Mayu" and MCStory == 3:
            label E4D1S3_Books:
                $ E4D1S3_Suggestion = "Books"
                pf "Mayu loves reading, right?"
                show shou ske
                voice "audio/voice/E4/Shou/d1/71 Copy.ogg"
                ss "Yeah… How did you know?"
                
                if E2D5MA_MayuScene == 1 or E3MAS2_Completed == 1:
                    pf "We've talked books in the past."
                    # heart
                    show shou hap
                    voice "audio/voice/E4/Shou/d1/72 Copy.ogg"
                    ss "She likes to tell me what she's currently reading. It's so cute how excited she gets over them!"
                    
                else:
                    pf "I always see her reading when she's waiting for our team meetings to start."
                    # heart
                    show shou hap
                    voice "audio/voice/E4/Shou/d1/73 Copy.ogg"
                    ss "Oh yeah, I guess she does do that."
                
                pf "You should get her a new book. Maybe something that's just come out? That way you know she hasn't read it yet."
                show shou cur
                voice "audio/voice/E4/Shou/d1/74 Copy.ogg"
                ss "I think she'd like that."
                
    show shou smi
    "Shou nods."

    voice "audio/voice/MISSING/BATCH2/13.ogg"
    ss "Good thinking, broseph! Let's go!"
    "He leads the way to the store."
    pf "What is this gift for anyway?"
    show shou hap
    voice "audio/voice/E4/Shou/d1/75 Copy.ogg"
    ss "It's our one month anniversary!"
    
    menu:
        "Wow, time sure flies by fast…":
            pf "Has it been a month already? I feel like it was just yesterday that we fought Mei's team."
            show shou mis
            voice "audio/voice/E4/Shou/d1/76 Copy.ogg"
            ss "I know. Me too. Time seems to pass in a click, doesn't it?"
            pf "...I've never heard that saying before..."
        
        "You're celebrating every month?":
            pf "Geez, that'll get expensive fast."
            show shou ske
            voice "audio/voice/E4/Shou/d1/77 Copy.ogg"
            ss "Huh?"
            pf "Well, if you have to celebrate each month of being together by buying each other a gift, that adds up really quickly."
            show shou mis
            voice "audio/voice/E4/Shou/d1/78 Copy.ogg"
            ss "We're not celebrating each month! That'd be crazy! Just the milestones, like three months and six months."
            pf "...Right… \"milestones\"…"
        
        "There's no such thing.":
            pf "You can't have a one month anniversary."
            show shou ske
            voice "audio/voice/E4/Shou/d1/79 Copy.ogg"
            ss "Why not?"
            pf "Because anniversary means one year."
            show shou mis
            voice "audio/voice/E4/Shou/d1/80 Copy.ogg"
            ss "Alright, then it's a month-a-versary!"
            pf "I guess that's technically better..."
    
    pf "Anyway, congrats on your one month!"
    # note
    show shou hap
    voice "audio/voice/E4/Shou/d1/81 Copy.ogg"
    ss "Thanks!"
    show shou smi
    voice "audio/voice/E4/Shou/d1/82 Copy.ogg"
    ss "I'm actually kind of surprised by how it happened."
    pf "How did it happen?"
    
    if E4D1S3_Target == "Mayu":
        show shou hap
        voice "audio/voice/E4/Shou/d1/83 Copy.ogg"
        ss "It came out of the blue! Mayu and I were hanging out as usual the Monday after our match with Onna-Bugeisha, and I could tell something was on her mind."
        show shou smi
        voice "audio/voice/E4/Shou/d1/84 Copy.ogg"
        ss "When I asked her what was wrong, she blurted out a question about feelings. It was so unlike her that I was too shocked to speak."
        voice "audio/voice/E4/Shou/d1/85 Copy.ogg"
        ss "Mayu didn't even hesitate and she started talking about how she's liked me since we were kids and she wanted to know if I felt the same way or if I was into someone else."
        show shou hap
        "Shou laughs."
        # drop
        voice "audio/voice/E4/Shou/d1/86 Copy.ogg"
        ss "I guess she saw me walking home with Hitomi and thought we were dating. Silly, right?"
        pf "Yeah…"
        
        if E3MAS3_MockCompleted == 1:
            "I guess she really did learn something from our \"date\". I'm glad she took my advice."
            
        show shou smi
        "Shou looks sheepish."
        voice "audio/voice/E4/Shou/d1/87 Copy.ogg"
        ss "I started laughing as soon as she said that, and I know that embarrassed her, but I couldn't help it. I just couldn't believe what I was hearing."
        voice "audio/voice/E4/Shou/d1/88 Copy.ogg"
        ss "As if I could ever like anyone else!"
        "I blink."
        pf "Really?"
        show shou 
        voice "audio/voice/E4/Shou/d1/89 Copy.ogg"
        ss "Well, yeah… Why do you sound so surprised?"
        pf "It was obvious how Mayu felt about you, but you never seemed to notice…"
        show shou ner b1
        "Shou's cheeks flush."
        voice "audio/voice/E4/Shou/d1/90 Copy.ogg"
        ss "I noticed. Of course, I noticed."
        pf "Then why…?"
        show shou thi b1
        voice "audio/voice/E4/Shou/d1/91 Copy.ogg"
        ss "She's so smart and pretty and awesome! She is way out of my league."
        pf "She was head over heels for you."
        show shou neu
        voice "audio/voice/E4/Shou/d1/92 Copy.ogg"
        ss "It's still hard for me to believe that."
        show shou ner
        voice "audio/voice/E4/Shou/d1/93 Copy.ogg"
        ss "That's why this gift is so important!"
        "No wonder he seems so agitated."
        pf "Mayu will love whatever you get her. The fact that you're buying her a present at all will make her happy."
        show shou smi
        "Shou smiles worriedly."
        voice "audio/voice/E4/Shou/d1/94 Copy.ogg"
        ss "You think?"
        pf "Of course."
        voice "audio/voice/E4/Shou/d1/95 Copy.ogg"
        ss "Still, it has to be perfect."
        "I nod."
    
    else:
        voice "audio/voice/E4/Shou/d1/96 Copy.ogg"
        ss "I kind of saw it coming, actually."
        # question
        show shou ske
        "I try to hold back my laugh, but a snort escapes. Shou looks curiously at me."
        pf "Sorry…"
        "It's just hard to believe he wasn't oblivious for once."
        show shou neu
        voice "audio/voice/E4/Shou/d1/97 Copy.ogg"
        ss "Well, it was the weekend after our victorious defeat of Onna-Bugeisha. Hitomi stopped me as I was heading home to congratulate me."

        voice "audio/voice/MISSING/BATCH2/14.ogg"
        ss "She brought me a cake and it said \"yes or no\"."
        pf "Yes or no what?"
        show shou mis
        voice "audio/voice/E4/Shou/d1/98 Copy.ogg"
        ss "That's what I asked her--or wanted to. Before I could speak she said, \"We should go on a date.\"."
        pf "So, she asked you?"
        show shou ner b1
        "His cheeks turn pink."
        voice "audio/voice/E4/Shou/d1/99 Copy.ogg"
        ss "Yeah…"
        pf "And you said yes."
        show shou thi b1
        voice "audio/voice/E4/Shou/d1/100 Copy.ogg"
        ss "Yeah… I mean, she's never been shy about her feelings. I could tell she was interested in me but I thought maybe it was because…"
        # dots
        "He trails off."
        pf "Because what?"
        
        if E3SSS3_Completed == 1:
            show shou neu
            voice "audio/voice/E4/Shou/d1/101 Copy.ogg"
            ss "My family."
            pf "Ah."
            pf "How would she have even known about your family anyway?"
            show shou smi
            voice "audio/voice/E4/Shou/d1/102 Copy.ogg"
            ss "She doesn't. That was very obvious after our first date."
            "I grin."
            pf "So you were worried about nothing?"
            show shou hap
            voice "audio/voice/E4/Shou/d1/103 Copy.ogg"
            ss "Yeah! She's so awesome! I can't believe she wants to be with me."
            
        else:
            show shou mis
            voice "audio/voice/E4/Shou/d1/104 Copy.ogg"
            ss "...Because she was hypnotised by my supreme gymnast body."
            "I facepalm while Shou laughs."
            pf "And here I was worried that it was something serious."
            show shou hap
            voice "audio/voice/E4/Shou/d1/105 Copy.ogg"
            ss "I couldn't resist! But seriously, I'm so lucky that she's into me. I don't want to screw this up."
            
        show shou smi
        voice "audio/voice/E4/Shou/d1/106 Copy.ogg"
        ss "That's why I want to make sure this present is special!"
        "I nod."
    
    pf "On that note, we better get back to searching."
    show shou mis
    voice "audio/voice/E4/Shou/d1/107 Copy.ogg"
    ss "Right!"
    #black screen
    scene black with fade
    "I help Shou pick out the perfect gift for his \"ladyfriend\"."
    
    if E4D1S3_Suggestion == "Jewelry":
        "He ended up going with my advice and buying her a gold chain with an amethyst pendant."
    
    elif E4D1S3_Suggestion == "Animal":
        "He ended up going with my advice and buying her a teddy bear."
    
    elif E4D1S3_Suggestion == "Chocolate":
        "He ended up going with my advice and buying her a box of gourmet chocolates."
    
    elif E4D1S3_Suggestion == "Books": 
        "He ended up going with my advice and buying Mayu the newest fantasy bestseller."
    
    "As we exit the store, Shou has a spring in his step, but he seems both nervous and hopeful. I hope she ends up liking her present!"
    
    "We say our goodbyes in the parking lot."
    
    label E4D1S3_Converge:
        stop ambient fadeout 3
        stop music fadeout 3
        scene black with fade
        $renpy.pause(1)
        play ambient "audio/ambience/Campus.ogg" fadein 3
        scene bg campus main dusk with fade
        play music "audio/music/Isokaze (GAME VERSION).ogg" fadein 3
        "Since I didn't have class today, I've got even more free time than usual. What do I feel like doing?"
    
    #Evening
    $ freeTime = "evening"
    
    call E4FreeTime from _call_E4FreeTime_4
    
    scene black with fade
    stop ambient fadeout 3
    stop music fadeout 3
    $renpy.pause(1)
    
    jump E4D1S4
