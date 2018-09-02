##
label E4MAS1:
    

    $ mayHairF = "default"
    $ mayHairB = mayHairF
    $ mayOut = "sCasual"
    
    "I wonder if Mayu is up to anything. As I'm debating whether or not to call her, a call comes in from her instead."
    pf "Hey, Mayu."
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-01.ogg"
    ma "Hi!"
    pf "What's up?"
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-02.ogg"
    ma "Um, I wanted to see if you'd like to go to the bookstore with me again."
    pf "Sure! I finished reading the manga I got last time."
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-03.ogg"
    ma "Me too! Actually, that's why I want to go back. I really liked it and want to get the second volume."
    pf "That's great!"
    pf "Are you ready to go now?"
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-04.ogg"
    ma "Yeah, if that's okay."
    pf "Sure, I'll meet you there."
    "After hanging up, I go and get ready."
    
    scene black with fade
    stop ambient fadeout 3
    stop music fadeout 3

    "I hop on my bike and drive to the bookstore."
    
    
    scene bg mall main day with fade
    
    "Since I'm the first to arrive, I decide to wait for Mayu inside. The same employee from before is at the counter and greets me warmly."
    play music "audio/music/Isokaze (GAME VERSION).ogg" fadein 5
    show studentM extra at cc with dissolve

    voice "audio/voice/E4/HOT MALE 4!!!/Mayu/1.ogg"
    hotm1 "Hey! Good to see you again. Welcome back."
    pf "Thanks."
    voice "audio/voice/E4/HOT MALE 4!!!/Mayu/2.ogg"
    hotm1 "Is Mayu not coming today?"
    pf "She is. We're coming separately."
    voice "audio/voice/E4/HOT MALE 4!!!/Mayu/3.ogg"
    hotm1 "Ah…"
    hide studentM extra with dissolve
    "I'm really surprised he remembers me considering I've only been here one other time. An employee smiles at me. She has flawless skin and legs that go on for days."
    "Then again, this store is atypical in basically every other way so maybe I shouldn't be surprised…"
    
    "The doors chime Mayu's arrival. She waves at me."
    show mayu smi at r3 with dissolve:
        xzoom -1
    
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-05.ogg"
    ma "I hope you weren't waiting long!"
    pf "Nope, not at all."
    pf "Let's go find your book."
    "She nods, and we head off into the shelves."
    hide mayu with dissolve
    "I browse for anything interesting, while Mayu goes straight for the series she wants. After making my selection, Mayu is still browsing the shelves."
    pf "Did you find what you're looking for?"
    show mayu thi at cc with dissolve
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-06.ogg"
    ma "Yeah, but then I also saw this manga which I think is interesting… or maybe this one…"
    "She trails off, lost in thought, holding an adventure series and a romance series."
    show mayu cur
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-07.ogg"
    ma "Which do you think I should get?"
    
    menu:
        "Adventure!":
            pf "Adventure stories have a little bit of everything. Can't go wrong with that."
            show mayu thi
            "She looks thoughtful."
        
        "Romance!":
            pf "I'm a sucker for a good romance."
            "She blinks."
            voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-08.ogg"
            ma "Really?"
            pf "But don't tell anyone I said that."
            "She looks thoughtful."
        
        "Why not both?":
            pf "Why don't you get both?"
            show mayu ner
            voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-09.ogg"
            ma "I don't want to get too many at once. I like to get more as I finish reading."
            pf "Hmm, well get whichever interests you more."
            voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-10.ogg"
            ma "Hmm…"
            "She stares hard in concentration."
    
    show mayu smi
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-11.ogg"
    ma "I'll just be another couple of minutes."
    pf "Okay, I'll meet you up front then."
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-12.ogg"
    ma "Okay."
    hide mayu with dissolve
    "When I return to the check-out counter, the clerk rings me up."
    show studentM extra at cc with dissolve
    voice "audio/voice/E4/HOT MALE 4!!!/Mayu/4.ogg"
    hotm1 "Did Mayu like the manga she got?"
    pf "Yup. She liked it so much she let me borrow it so I could read it too."
    "He seems intrigued."
    voice "audio/voice/E4/HOT MALE 4!!!/Mayu/5.ogg"
    hotm1 "Did you like it?"
    pf "It wasn't bad."
    voice "audio/voice/E4/HOT MALE 4!!!/Mayu/6.ogg"
    hotm1 "What did you think of the fanfic?"
    "I blink."
    pf "What fanfic?"
    "He seems surprised."
    voice "audio/voice/E4/HOT MALE 4!!!/Mayu/7.ogg"
    hotm1 "You don't know the fanfic?"
    #pf "Am I supposed to?"
    #"One of the store clerks overhears and chimes in excitedly."
    #hotm4 "You have to show him!"
    #"...Which attracts the attention of a few other people."
    #hotm2 "Are you guys talking about the fanfic? It's really good!"
    #hotm3 "It's only been up for a few days but it's already got a lot of views!"
    pf "Where can I find it?"
    "The first clerk takes a tablet out from behind the desk and pulls up the webpage."
    voice "audio/voice/E4/HOT MALE 4!!!/Mayu/8.ogg"
    hotm1 "Here you go."
    
    hide studentM extra with dissolve
    "I skim through the chapter note on the top of the page. The main character gives up her musical career and returns to her hometown to take care of her mother. She struggles to adapt to her new life, but is reunited with her childhood friend."
    "So far, this is staying true to the manga."
    
    if mayrelatonship == 0:
        "This chapter begins when she and her childhood friend are reconnecting, and she is beginning to develop feelings for him…"
    
    else:
        "Her childhood friend introduces her to a new guy in town, who is also a musician."
        "After a few months of hanging out, she realises she is developing feelings for him…"
    
    "{i}He grins at me and the heat flows in my face. I quickly look away. What is going on? I've seen that same smile a million times before. It doesn't mean anything.{/i}"
    "{i}Except that it means everything. Knowing that his attention is on me, no one else, makes my heart beat faster. There is an electricity swirling in currents around us, making the air thick.{/i}"
    "{i}\"Do you think we should invite the others?\", he asks, and my heart sinks. Why am I disappointed? After all, we're only friends…{/i}"
    "{i}I shake my head to clear my thoughts and he frowns in worry.{/i}"
    "{i}\"We don't have to invite them if you don't want!\"{/i}"
    "{i}I don't want to. I want to smile and tell him it'd be nice to spend time with just the two of us.{/i}"
    "{i}\"No, we should! I think they'd all enjoy it too.\" Why did I say that? He flashes me another warm smile, and my knees go weak. Oh, of course. That's why.{/i}"
    
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-13.ogg"
    ma "Hey, guys."
    show mayu smi at l3
    show studentM extra at r3
    with dissolve
    "I glance up as Mayu puts her books down."
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-14.ogg"
    ma "What are you reading?"
    pf "Just a fanfic."
    show mayu cur
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-15.ogg"
    ma "I didn't know you like fanfiction! Is it good?"
    
    $ E4MAS1_Fanfiction = "None"
    
    menu:
        "I'm already getting the feels.":
            $ E4MAS1_Fanfiction = "Feels"
            pf "Yeah! I've only read a little bit but I'm already starting to get invested in the characters and want to learn more. I'll probably finish reading it later."
        
        "LAWLS":
            $ E4MAS1_Fanfiction = "LAWLS"
            pf "Hahaha! This is the cheesiest thing I've ever read. It's like the long lost cousin of the \"Dusk\" series."
        
        "I'm indifferent.":
            $ E4MAS1_Fanfiction = "Indifferent"
            "I shrug."
            pf "It's alright, I guess? I don't usually read this stuff so wouldn't know what's considered good."
    
    show mayu thi
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-16.ogg"
    ma "Really?"
    pf "Here, let me read you a section."
    pf "{i}He grins at me and the heat flows in my face. I quickly look away. What is going on? I've seen that same smile a million times before. It doesn't mean anything.{/i}"
    show mayu cur
    pf "{i}Except that it means everything. Knowing that his attention is on me, no one else, makes my heart beat faster. There is an electricity swirling in currents around us, making the air thick.{/i}"
    show mayu ner b2 with dissolve
    "Mayu's face drains of colour, then turns bright red. I pause."
    pf "Have you read this before?"
    "The store clerk begins laughing as Mayu's blush deepens."
    "I look from one to the other. Uhh, this is strange…"
    pf "What's going on?"
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-17.ogg"
    ma "Um… well, actually…"
    "She looks away, seemingly too embarrassed to finish."
    voice "audio/voice/E4/HOT MALE 4!!!/Mayu/9.ogg"
    hotm1 "She wrote it!"
    pf "What?!"
    voice "audio/voice/E4/HOT MALE 4!!!/Mayu/10.ogg"
    hotm1 "Yeah, Mayu shared it with me which is why I was surprised you hadn't read it yet."
    
    if E4MAS1_Fanfiction == "Feels":
        "My eyes widen."
        
        if mayrelatonship == 0:
            pf "Wow, Mayu! That's awesome!"
            show mayu sur b2
            voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-18.ogg"
            ma "R-Really?"
            pf "Yeah! You're super talented! Have you written anything else?"
            
        else:
            pf "You are full of surprises. I'm so lucky to have such a talented girlfriend!"
            show mayu smi b2
            "She smiles."
            voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-19.ogg"
            ma "Do you really think it's good?"
            pf "Definitely! I can't wait to read more. Have you written anything else?"
            
        "She seems shy."
        show mayu ner b2
        voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-20.ogg"
        ma "The only other ones I've written I haven't posted."
        pf "You should post it. I bet they're just as good."
        voice "audio/voice/E4/HOT MALE 4!!!/Mayu/11.ogg"
        hotm1 "I agree, you've got a gift."
        voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-21.ogg"
        ma "M-Maybe…"
    
    elif E4MAS1_Fanfiction == "LAWLS":
        "Oh crap! {i}Mayu{/i} wrote this? {w}My face turns beet red."
        pf "O-Oh, well, I was just kidding earlier! \"Dusk\" was insanely popular and is the whole reason \"Fifty Shades of GEAR\" was written."
        "Mayu looks away."
        show mayu ner with dissolve
        voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-22.ogg"
        ma "N-No, it's okay, I know it's not that good."
        voice "audio/voice/E4/HOT MALE 4!!!/Mayu/12.ogg"
        hotm1 "No way, Mayu! We all loved it! You should write more."
        show mayu sad
        voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-23.ogg"
        ma "I don't know… I have a long way to go."
        #hotm2 "I'd definitely want to read whatever you write!"
        #hotm4 "Me too!"
        #hotm3 "Me three."
        #pf "Me four."
        
        if mayrelatonship == 1:
            "I pull her into a hug."
            show mayu cur b2 with dissolve
            pf "I'm sorry for being such a jerk. I'm proud to have such a talented girlfriend."
            "She smiles shyly."
            
        else:
            "Mayu glances at me."
            pf "I'm sorry for being such an idiot. It was a tasteless joke. You're really talented and you should be proud of your writing!"
            show mayu smi
            "She smiles."
            voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-24.ogg"
            ma "Thanks."
    
    else:
        pf "Really? That's pretty cool, Mayu!"
        show mayu smi b1
        "She blushes again."
        voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-25.ogg"
        ma "Y-You think so?"
        pf "Yeah! It seems like a lot of people like your work too so you should be proud."
        "She smiles."
        voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-26.ogg"
        ma "Thanks."
    
    hide mayu
    hide studentM Extra
    with dissolve
    "We continue to chat about Mayu's writing. The clerk gives her a discount on her purchases, which Mayu is thrilled about. After promising to return soon, I offer Mayu a ride back to campus."
    
    show mayu smi at cc with dissolve
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-27.ogg"
    ma "Thank you coming with me today."
    pf "No problem. I'll be looking out for your next chapter."
    show mayu ner b1 with dissolve
    "She blushes."
    
    voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-28.ogg"
    ma "Ah! Please don't tell the others though… I'm not sure they'd understand…"
    
    if mayrelatonship == 1:
        pf "Your secret is safe with me."
        show mayu smi b1
        "She smiles in appreciation, and an idea pops into my head…"
        pf "In fact, maybe I can help you with some new source material for your writing."
        "She blinks and furrows her brow in confusion."
        show mayu cur b1

        voice "audio/voice/MISSING/BATCH8/Missing Mayu-06.ogg"
        ma "What do you mean?"
        pf "Here's an example."
        "I scoop her into my arms and feeling bold, I plant a long kiss on her lips. At first she's surprised, but it doesn't take long before she melts into the kiss."
        show mayu smi b2 with dissolve
        "I gently pull away, and her cheeks are flushed. She glances away but smiles."

        voice "audio/voice/MISSING/BATCH8/Missing Mayu-07.ogg"
        ma "O-Oh, um, t-thanks. That will help a lot."
        "I grin."
        pf "Let me know if you need anymore help researching."
        "She blushes deeply, but nods."
        voice "audio/voice/MISSING/BATCH8/Missing Mayu-08.ogg"
        
        ma "I better get back..."
        pf "See you soon."
        
    else:
        pf "Not even Shou?"
        show mayu smi b1
        "She blushes."
        voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-29.ogg"
        ma "Actually, he already knows."
        pf "Really?"
        "I'm not sure why I'm so surprised. It makes sense that she would tell him."
        "She nods."
        voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-30.ogg"
        ma "He normally doesn't read that kind of stuff, but he read everything that I wrote and said he loved it."
        "I'm glad Shou is finally being more receptive to Mayu's interests and hobbies. He just may have found a new interest too."
        pf "Well, I promise I won't say anything."
        voice "audio/voice/E4/Mayu/Mayu Arc/Mayu Arc-31.ogg"
        ma "Thanks."
    
    
    hide mayu with dissolve
    "She smiles and waves goodbye. Who knew Mayu was so creative? Not only does she play an instrument, but she also writes. I wonder if she can draw too..."
    scene black with fade
    "Mulling over the thought, I head out."
    
    
    stop music fadeout 3
    stop ambient fadeout 3
    $renpy.pause(2.5)
    
    $ E4MAS1_Completed = 1
