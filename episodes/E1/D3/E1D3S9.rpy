label E1D3S9:
    
    $renpy.pause(1)
    scene bg homekaito main dusk with fade
    "I enter the house and hear laughter coming from the kitchen."
    play ambient "audio/ambience/Kitchen Cooking.ogg" fadein 1
    "I drop my bag on the floor and follow the sounds of my family and the delicious smells of dinner."
    play music "audio/music/Hanging Out (GAME VERSION).ogg" fadein 1
    pf "Hey." 
    "I sit at the table and watch Nikki and Uncle Kaito move around the kitchen. They're wearing matching aprons." 
    pf "Looking good, Uncle! That apron really suits you. It brings out your eyes."
    hk "..."
    voice "audio/voice/E1/D3/S9/Kaito/6.ogg"
    hk "That's it! I'm done!" 
    "He tears off the apron and tosses it aside."
    show kaito dis at l2 with dissolve
    show storm:
        xoffset 365
        yoffset 5
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D3/S9/Kaito/7.ogg"
    hk "You said I'd look cool."
    "Nikki giggles and goes back to the food she's cooking."
    show nikki hap at r2 with dissolve:
        xzoom -1
    show note:
        xoffset 1050
        yoffset 160
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D3/S9/Nikki/1.ogg"
    sf "You did look cool! Every lady loves a man who can cook." 
    pf "And I love a lady who cooks for me!"
    show kaito hap at l2
    voice "audio/voice/E1/D3/S9/Kaito/8.ogg"
    hk "Amen!"
    show nikki dis at r2
    "Kaito sits beside me. We laugh as Nikki sticks her tongue out at us."
    voice "audio/voice/E1/D3/S9/Nikki/2.ogg"
    sf "Men!" 
    show kaito smi at l2
    pf "So what are we having?"
    show nikki smi at r2 with dissolve
    voice "audio/voice/E1/D3/S9/Nikki/3.ogg"
    sf "Guess!" 
    pf "Oh god, not this again."
    show kaito hap at l2
    "Kaito laughs."
    show nikki neu at r2
    voice "audio/voice/E1/D3/S9/Kaito/9.ogg"
    hk "How was your day, bud?" 
    pf "It was alright."
    show kaito mis at l2
    voice "audio/voice/E1/D3/S9/Kaito/10.ogg"
    hk "Yeah? What kind of shenanigans did you get up to?" 
    pf "Nothing major. Had class this morning, checked out my GEAR after."
    show kaito smi at l2
    
    if (E1D2S11_JoinedTheTeam == 0): #this means he joined the team today because if you joined yesterday, it be a 1 here
        pf "I did manage to join a team though."
        show nikki cur at r2
        "Nikki glances over her shoulder."
        voice "audio/voice/E1/D3/S9/Nikki/4.ogg"
        sf "You found one that would take you? Congrats, big bro!" 
        pf "Yeah, same team from yesterday. I had no luck finding any others, but luckily, Shou offered to take me again today." 
    
        if (E1D2S3_MetKaoriWasRudeNoHelmet == 1) or (E1D2S11_ComingCleanAboutRunningOverKaori == 1):
            show nikki ner at r2
            voice "audio/voice/E1/D3/S9/Nikki/5.ogg"
            sf "Hopefully that girl will be okay with it." 
            pf "Shou didn't sound worried."
            show kaito cur at l2
            show nikki neu at r2
            show question:
                xoffset 365
                yoffset 5
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D3/S9/Kaito/11.ogg"
            hk "Girl? I want to hear about this girl." 
            pf "She's just a team member."
            show kaito mis at l2
            show drooling:
                xoffset 365
                yoffset 5
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D3/S9/Kaito/12.ogg"
            hk "For now... close quarters working on a team together... things can get... {i}heated{/i}." 
            "With a fiery personality like Kaori's, I wouldn't be surprised if things got heated, although it wouldn't be in the way my uncle suggests."
            show kaito smi at l2
    
        elif (E1D2S9_AgreeJoinShouTeam == 0):
            show nikki ske at r2
            show question:
                xoffset 1050
                yoffset 160
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D3/S9/Nikki/6.ogg"
            sf "Isn't that the team you turned down?" 
            pf "Yeah, but I didn't have any other options. Besides, they've got a decent reputation. It's something to move forward for qualifiers at least."
            show nikki thi at r2
            voice "audio/voice/E1/D3/S9/Nikki/7.ogg"
            sf "Hmm." 
            "Nikki turns back to the stove while Kaito claps me on the back."
            show kaito hap at l2
            show nikki neu at r2
            voice "audio/voice/E1/D3/S9/Kaito/13.ogg"
            hk "Good job, kid! Who's on the team?" 
            pf "Shou, myself, and a couple of girls."
            show kaito cur at l2
            show question:
                xoffset 365
                yoffset 5
                xzoom .75
                yzoom .75
            voice "audio/voice/E1/D3/S9/Kaito/14.ogg"
            hk "Good looking girls?"
            show nikki ang at r2
            voice "audio/voice/E1/D3/S9/Nikki/8.ogg"
            sf "Uncle Kaito! Don't encourage him!"
            show nikki ann at r2
            "I shrug."
            show kaito mis at l2
            "Kaito winks at me."
            voice "audio/voice/E1/D3/S9/Kaito/15.ogg"
            hk "I knew you could make being here work for you."
            show nikki dis at r2
            pf "Thanks, I think."
            show kaito smi at l2
            show nikki neu at r2
    
    elif (E1D2S11_JoinedTheTeam == 1):
        pf "One of my teammates showed up and we had a practice simulation."
        show kaito hap at l2
        voice "audio/voice/E1/D3/S9/Kaito/16.ogg"
        hk "Sounds fun." 
        pf "It was. I think we'll make a good team."
        show kaito smi at l2
        voice "audio/voice/E1/D3/S9/Kaito/17.ogg"
        hk "Who else is on the team?" 
        pf "Shou, myself, and a couple girls."
        show kaito cur at l2
        show question:
            xoffset 365
            yoffset 5
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D3/S9/Kaito/18.ogg"
        hk "Good looking girls?" 
        "I shrug." 
        pf "Yeah, I guess."
        show kaito mis at l2
        "Kaito winks at me and I just shake my head."
    
    if (E1D3S1_BikeImpounded == 1):
        show nikki cur at r2
        voice "audio/voice/E1/D3/S9/Nikki/9.ogg"
        sf "And you got your bike back?" 
        pf "Yeah, thank god. At least I won't have to deal with the bus anymore."
        show nikki hap at r2
        show bulb:
            xoffset 1050
            yoffset 160
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D3/S9/Nikki/10.ogg"
        sf "Me too!" 
        pf "Keep dreaming."
        show kaito ske at l2
        show nikki neu at r2
        show exclamation:
            xoffset 365
            yoffset 5
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D3/S9/Kaito/19.ogg"
        hk "Whoa, whoa. What happened to your bike?"
        show nikki mis at r2
        voice "audio/voice/E1/D3/S9/Nikki/11.ogg"
        sf "He somehow managed to park it in the wrong place and got it impounded."
        show kaito cur at l2
        voice "audio/voice/E1/D3/S9/Kaito/20.ogg"
        hk "Really? How did you manage to do that?"
        pf "Eh... Long story."
        show nikki smi at r2
        voice "audio/voice/E1/D3/S9/Nikki/12.ogg"
        sf "Let's be honest, it was obvious you were going to do something dumb on your first day."
        pf "H-Hey!"
        show kaito hap at l2
        show nikki mis at r2
        "Uncle Kaito laughs. Nikki shoots me a playful smirk."
        
    show nikki neu at r2
    "Nikki places full plates in front of us, then removes her apron and join us at the table."
    show kaito neu at l2
    voice "audio/voice/E1/D3/S9/Kaito/21.ogg"
    hk "What else did you get up to today?" 
    
    if (E1D3S4_PlayedAnotherWithShou == 1):
        pf "Mostly just practiced with Shou, my new teammate."
        show kaito cur at l2
        voice "audio/voice/E1/D3/S9/Kaito/22.ogg"
        hk "Is he any good?" 
        pf "Yeah, I think we'll be a good fit, but I guess we'll find out tomorrow at the qualifiers if that's true."
    
    elif (E1D3S6_WentLibraryYuuna == 1):
        pf "I got some study time in the library and ran into one of my friends."
        show nikki mis at r2
        voice "audio/voice/E1/D3/S9/Nikki/13.ogg"
        sf "Ooooh, was it that giiiiiirl?" 
        pf "Shut up, Nikki! {w}How did you even know that?!"
        show nikki smi at r2
        voice "audio/voice/E1/D3/S9/Nikki/14.ogg"
        sf "I didn't, but thanks for sharing!"
        show kaito hap at l2
        voice "audio/voice/E1/D3/S9/Kaito/23.ogg"
        hk "Another girl? Sounds like you're getting all the ladies." 
        pf "It's not like that. She helped me out yesterday, that's all."
        show kaito mis at l2
        show drooling:
            xoffset 365
            yoffset 5
            xzoom .75
            yzoom .75
        voice "audio/voice/E1/D3/S9/Kaito/24.ogg"
        hk "Right, \"helped\"."
        show nikki mis at r2
        "Uncle Kaito and Nikki exchange a smile. {w}At least I know for sure these two are related." 
    
    elif (E1D3S6_WentLibraryStudied == 1):
        pf "I got a chance to catch up on some of my work, so that's good."
        show kaito smi at l2
        voice "audio/voice/E1/D3/S9/Kaito/25.ogg"
        hk "Proud of you, kid. Glad you're staying on top of your studies."
        show nikki hap at r2
        voice "audio/voice/E1/D3/S9/Nikki/15.ogg"
        sf "Are you going to be a teacher's pet with all your studying?" 
        pf "I'm sorry, who's in the top Cenorobotics school in Japan?"
        show nikki ske at r2
        voice "audio/voice/E1/D3/S9/Nikki/16.ogg"
        sf "Oh, now you're just gloating."
        show kaito hap at l2
        show nikki dis at r2
        "Kaito lets out a hearty laugh."
        voice "audio/voice/E1/D3/S9/Kaito/26.ogg"
        hk "He's got you there, kiddo."
        show nikki wor at r2
        voice "audio/voice/E1/D3/S9/Nikki/17.ogg"
        sf "No fair! You guys are ganging up on me."
    
    elif (E1D3S4_WentToThePilotsLounge == 1):
        pf "I hung out at the pilot's lounge for a bit."
        show kaito smi at l2
        voice "audio/voice/E1/D3/S9/Kaito/27.ogg"
        hk "That sounds cool." 
        pf "Yeah it was. I actually learned a lot about this guy named Akira. He's the top tier pilot in the program."
        show nikki sur at r2 with dissolve
        voice "audio/voice/E1/D3/S9/Nikki/18.ogg"
        sf "So he's your rival?"
        pf "Rival?"
        show nikki hap at r2
        voice "audio/voice/E1/D3/S9/Nikki/19.ogg"
        sf "Yeah, these types of stories always needs a villainous rival!"
        pf "Uhm, well, he's actually a pretty nice guy. Well-liked."
        show nikki mis at r2
        voice "audio/voice/E1/D3/S9/Nikki/20.ogg"
        sf "Really? Is he cute?" 
        pf "Uh, how should I know?"
        show nikki cur at r2
        voice "audio/voice/E1/D3/S9/Nikki/21.ogg"
        sf "Did the girls think he was cute?" 
        pf "... I guess so?"
        show nikki hap at r2
        "Nikki beams."
        show nikki mis at r2
        voice "audio/voice/E1/D3/S9/Nikki/22.ogg"
        sf "Accomplished, polite, and cute. You could learn a thing from him."
        pf "What's that suppose to mean?!"
        show nikki smi at r2
        voice "audio/voice/E1/D3/S9/Nikki/23.ogg"
        sf "Hehe! Nothing."
        
    $renpy.pause(1)
    stop ambient fadeout 3
    stop music fadeout 3
    scene black with fade
    $renpy.pause(2.5)
    play sound "audio/sfx/Human/Burp.ogg"
    scene bg homekaito main night with fade
    play music "audio/music/After a Long Day (GAME VERSION).ogg" fadein 1
    show kaito smi at l2 with dissolve
    show nikki cur at r2 with dissolve:
        xzoom -1
    "Kaito cleans his plate, then rests a hand on his stomach and lets out a loud belch. Nikki and I blink at him."
    show kaito mis at l2
    voice "audio/voice/E1/D3/S9/Kaito/28.ogg"
    hk "I was simply complimenting the chef!" 
    pf "I should do the same."
    show nikki win at r2
    "I open my mouth to burp, but Nikki squeals in protest." 
    show crying:
        xoffset 1050
        yoffset 160
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D3/S9/Nikki/24.ogg"
    sf "Please don't! I'd rather not have them."
    show kaito hap at l2
    show nikki neu at r2
    "Kaito and I laugh as Nikki clears the table. Then Kaito rests a hand on my shoulder."
    show kaito smi at l2
    voice "audio/voice/E1/D3/S9/Kaito/1.ogg"
    hk "Sounds like you’ve had quite the day, bud."
    pf "It'll get easier once I'm in the swing of things."
    voice "audio/voice/E1/D3/S9/Kaito/2.ogg"
    hk "Of course."
    show kaito hap at l2
    voice "audio/voice/E1/D3/S9/Kaito/2_1.ogg"
    hk "Want to watch a movie or something before you two head to bed?"
    show nikki hap at r2
    "I almost say yes, but a long yawn escapes my mouth." 
    pf "I'm pretty fried. I think I might go review some notes then get to bed early. I've got qualifiers tomorrow."
    show kaito smi at l2
    voice "audio/voice/E1/D3/S9/Kaito/3.ogg"
    hk "That's fair. Nikki?"
    show nikki neu at r2
    voice "audio/voice/E1/D3/S9/Nikki/25.ogg"
    sf "I'll join you once I'm done cleaning."
    show kaito hap at l2
    voice "audio/voice/E1/D3/S9/Kaito/4.ogg"
    hk "I'll help you."
    show nikki smi at r2
    voice "audio/voice/E1/D3/S9/Nikki/26.ogg"
    sf "Thanks!" 
    show kaito smi at l2
    "I stand up and Kaito and Nikki both wave."
    show kaito hap at l2
    show nikki hap at r2
    with dissolve
    show note:
        xoffset 1050
        yoffset 160
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D3/S9/Nikki/27.ogg"
    sf "Goodnight!"
    show note:
        xoffset 365
        yoffset 5
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D3/S9/Kaito/5.ogg"
    hk "Goodnight!"
    hide kaito
    hide nikki
    with dissolve
    play sound "audio/sfx/Human/Going Upstairs (wood).ogg" fadein 1 fadeout 1
    $renpy.pause(1)
    scene black with fade
    "I wave back and head to my room."
    $renpy.pause(1)
    scene bg homekaito myroom night with Dissolve(2.5)
    "In my room, I crawl into bed and grab my tablet to review my notes from today's class. {w}I'm only part way through when my eyes grow heavy and I can't read any longer. {w}I flick off the light and close my eyes."
    stop music fadeout 3
    scene black with fade
    "As I drift to sleep, I dream of tomorrow's qualifiers." 
    
    
    jump E1D4S1