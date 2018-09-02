label E1D2S10:
    
    
    #  The previous programming is so silly. They separated going alone or with shou even though it is the same scene and location. 
    #  I think I figured out a clean way to merge S10 and S11 but still keep them separate for voice files.
    
    if (E1D2S9_AgreeJoinShouTeam == 1):
        jump E1D2S11
        
    elif (E1D2S9_AgreeJoinShouTeam == 0):
        jump E1D2S10_WentSolo
    
    
    label E1D2S10_WentSolo:
        scene black with fade:
        "I grab the handle and push my way inside."
        play ambient "audio/ambience/Pilot Lounge.ogg" fadein 1
        scene bg campus lounge day with fade
        "Groups of students fill the lounge, all of them wearing similar striped teal uniforms. I take a few steps, then pause, trying to decide how to handle the situation."
        $ E1S2D10_AskedOtherTeams = 1
        menu: 
            "I’ll just be honest about my situation.":
                play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 1
                "There has to be at least one or two teams looking for a new member."
                "I set my sights on a small group of people closest to me, who are speaking animatedly amongst themselves. They seem friendly enough." 
                pf "Hey! How's it going?"
                show studentM extra at l2
                show studentM2 extra at r2
                with dissolve
                "They all turn and look at me. A girl closest to me gives me a once over." 
                voice "audio/voice/E1/D2/S10/stu7m/2.ogg"
                stu7m "Uh… Hi. Can we help you with something?"
                "The guy beside her speaks up before I can answer."
                voice "audio/voice/E1/D2/S10/stu2m/1.ogg"
                stu2m "Hey, you're new right? I saw you around campus today. You certainly stick out."
                "He glances at my blond hair."
                pf "I guess I do look a little different."
                voice "audio/voice/E1/D2/S10/stu7m/3.ogg"
                stu7m "Did you just transfer here?"
                pf "Yeah, from CINY in the States."
                voice "audio/voice/E1/D2/S10/stu7m/4.ogg"
                stu7m "Bit late in the year to transfer, isn't it?" 
                "Is it? The year just started. But they all nod, agreeing with one another." 
                voice "audio/voice/E1/D2/S10/stu2m/2.ogg"
                stu2m "Yeah, teams usually get picked in the summer before classes begin. Who are you teamed up with?"
                pf "Yeah, that's sort of my problem. I was hoping that someone in the lounge could help me out. You wouldn't happen to need another pilot, would you?" 
                "The second student shakes his head." 
                voice "audio/voice/E1/D2/S10/stu2m/3.ogg"
                stu2m "No, we're all filled up. At least in pilot positions." 
                pf "Just my luck. Any chance you know of anyone looking?" 
                "The group exchanges glances before the first student speaks again."
                voice "audio/voice/E1/D2/S10/stu7m/5.ogg"
                stu7m "Shinjirou and Itami were looking for another pilot weren't they?" 
                voice "audio/voice/E1/D2/S10/stu2m/4.ogg"
                stu2m "Oh yeah. If I were you, I'd talk to them. Last I heard, their team wasn't full. You'll probably learn a lot from them too. They were both top pilots in their first year." 
                "Shinjirou? Is that the guy who approached me before? I didn't get the impression that he was a top pilot. Maybe there's more to that guy than I thought." 
                pf "Well, thanks. I appreciate the help."
                hide studentM extra
                hide studentM2 extra
                with dissolve
                "I smile and turn away from the group. Guess I'm back where I started." 
        
            "I'm a smooth operator.":
                "I put on my most charming smile and glance around the room, looking for an appropriate target."
                "I catch the eyes of a pretty girl across the lounge and stride towards her."
                show studentF2 extra at r2 with dissolve
                pf "Hi, I'm [pfirst]."
                show bully2 extra at l2 with dissolve
                play music "audio/music/Stress (GAME VERSION).ogg" fadein 1
                "Before she can answer, a tall guy steps towards us and looks at me coldly." 
                voice "audio/voice/E1/D2/S10/stu2m/5.ogg"
                stu2m "What do you want?" 
                pf "Since you asked, I was just hoping to learn the name of this lovely lady."
                "She blinks in surprise, and tries to hide the growing blush in her cheeks. He becomes even more flustered by her response."
                voice "audio/voice/E1/D2/S10/stu2m/6.ogg"
                stu2m "She doesn't want to know yours!"
                pf "Are you sure about that?"
                voice "audio/voice/E1/D2/S10/stu2m/7.ogg"
                stu2m "Huh?"
                pf "Did you ask her?"
                voice "audio/voice/E1/D2/S10/stu2m/8.ogg"
                stu2m "Well, no."
                pf "Then how do you know she isn't as curious about me as I am about her?"
                "Without waiting for him to sputter out a response, I turn to the girl."
                pf "As I said before we were so rudely interrupted, I'm [pfirst], and you are?"
                "She smiles shyly."
                stu9f "Mitsuki."
                "The guy's face is bright red as he steps between us, and turns towards her."
                voice "audio/voice/E1/D2/S10/stu2m/9.ogg"
                stu2m "Why would you tell this asshole your name?"
                stu9f "I can tell my name to anyone I want."
                voice "audio/voice/E1/D2/S10/stu2m/10.ogg"
                stu2m "But this guy? No way!"
                hide studentF2 extra
                hide bully2 extra
                with dissolve
                stop music fadeout 3
                "I back away as the couple continue to argue. Even if they have an opening on their team, it probably wouldn't work out."
                "I catch her gazing at me from the corner of my eye as her boyfriend continues to lecture her. Heh, still got it!"
                "As I search for another team, I spot a group of giggling girls watching me intensely... {w}Bullseye. I head towards them."
                play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 1
                show studentF2 extra at l3
                show studentF extra at r3
                show highschoolgirl2 extra at cc
                with dissolve
                pf "Hello ladies." 
                "One of them smiles." 
                voice "audio/voice/E1/D2/S10/stu1f/stu1f_01.ogg"
                stu1f "Having some trouble?" 
                pf "Me? Never! But I guess not everyone appreciates my charm." 
                voice "audio/voice/E1/D2/S10/stu1f/stu1f_02.ogg"
                stu1f "Maybe you just aren't very good at picking who you speak to. I know I certainly wouldn't say no."
                "I grin."
                pf "Oh yeah? And why's that?"
                voice "audio/voice/E1/D2/S10/stu1f/stu1f_03.ogg"
                stu1f "You look just like a young Ceonardo DiLaprio!"
                voice "audio/voice/E1/D2/S10/stu4f/stu4f_01.ogg"
                stu4f "Ooh, Ceonardo DiLaprio!"
                voice "audio/voice/E1/D2/S10/stu3f/Alexandria Bearden_stu3f_1.ogg"
                stu3f "Wait, which one's Ceonardo DiLaprio?"
                voice "audio/voice/E1/D2/S10/stu1f/stu1f_04.ogg"
                stu1f "You know--Ceonardo DiLaprio."
                voice "audio/voice/E1/D2/S10/stu4f/stu4f_02.ogg"
                stu4f "Ceonardo DiLaprio, he was in {i}Jomeo and Ruliet{/i}."
                voice "audio/voice/E1/D2/S10/stu3f/Alexandria Bearden_stu3f_2.ogg"
                stu3f "Ohhhh, Ceonardo DiLaprio! I guess he does look like him."
                pf "Great, I'm glad we got that established."
                voice "audio/voice/E1/D2/S10/stu4f/stu4f_03.ogg"
                stu4f "Who are you anyway?" 
                pf "I'm a transfer student from CINY." 
                voice "audio/voice/E1/D2/S10/stu1f/stu1f_05.ogg"
                stu1f "You're from the States?" 
                pf "Yeah. Just transferred into the second year pilot program." 
                "One of the girls nudges her friend. She leans in close and whispers something, then tries to hide her smile." 
                voice "audio/voice/E1/D2/S10/stu1f/stu1f_06.ogg"
                stu1f "What is it?" 
                voice "audio/voice/E1/D2/S10/stu3f/Alexandria Bearden_stu3f_3.ogg"
                stu3f "… He's from the States." 
                voice "audio/voice/E1/D2/S10/stu1f/stu1f_07.ogg"
                stu1f "So?" 
                voice "audio/voice/E1/D2/S10/stu4f/stu4f_04.ogg"
                stu4f "Sooo, remember that old GEAR in the hangar? It came from the States." 
                voice "audio/voice/E1/D2/S10/stu1f/stu1f_08.ogg"
                stu1f "Is that GEAR yours?" 
                pf "Uh… Maybe." 
                voice "audio/voice/E1/D2/S10/stu3f/Alexandria Bearden_stu3f_4.ogg"
                stu3f "Hm… I didn't realise America was so far behind Japan when it comes to GEAR." 
                "My smile melts away."
                pf "It's always worked fine for me." 
                "My GEAR is important to me. Does everyone think it's junk?" 
                voice "audio/voice/E1/D2/S10/stu1f/stu1f_09.ogg"
                stu1f "What team was willing to have you join them?" 
                pf "No one yet. That's what I'm looking for." 
                "She exchanges looks with her friends then turns back to me and shakes her head." 
                voice "audio/voice/E1/D2/S10/stu1f/stu1f_10.ogg"
                stu1f "Well, good luck. I don't think any team will take you on with GEAR like that." 
                hide studentF2 extra
                hide studentF extra
                hide highschoolgirl2 extra
                with dissolve
                "She and the rest of her friends turn away from me and I'm left awkwardly staring at their backs."
                "I guess my GEAR is everyone's first impression of me."
        
            "I should probably target groups of 3":
                play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 1
                "Since teams function as groups of at least 4 pilots, my best bet is to assume that any group of three is still looking for a fourth member. {w}My eyes fall on a group of three students sitting at the far end of the room. There's an extra chair next to them, so I saunter over and take a seat."
                show studentM extra at l3
                show studentM2 extra at l1
                show studentF2 extra at r1
                with dissolve
                pf "Hey, you guys look like you're missing a pilot." 
                voice "audio/voice/E1/D2/S10/stu7m/6.ogg"
                stu7m "And who are you exactly?"
                pf "Transfer student from CINY. Best in my class back home and looking for a team that needs a skilled member." 
                "The group of three exchange looks with each other." 
                voice "audio/voice/E1/D2/S10/stu2m/11.ogg"
                stu2m "Transfer? I heard the exam was pretty tough." 
                pf "I managed." 
                voice "audio/voice/E1/D2/S10/stu7m/7.ogg"
                stu7m "Right, well we're actually not looking." 
                "She smiles politely and waves over another pilot."
                show studentF extra at r3 with dissolve
                voice "audio/voice/E1/D2/S10/stu7m/8.ogg"
                stu7m "This is our fourth member, sorry." 
                "She looks at me, like he's expecting me to move from his seat. I don't."
                pf "Any idea who is looking?" 
                voice "audio/voice/E1/D2/S10/stu2m/12.ogg"
                stu2m "We don't keep tabs on all the other teams and their needs. As far as I know, all teams were formed over the summer, but you can keep asking around to see if anyone's missing a member."
                pf "Well, thanks anyway."
                hide studentF2 extra
                hide studentF extra
                hide studentM extra
                hide studentM2 extra
                with dissolve
                "I stand and walk away from the group. Scanning the room again, I see there are no other groups of three. Everyone seems to have a group of pilots they work with already."  
                "So much for trying to find a team this way." 
    
    "Should I see if Shou will still take me or just head home and try again tomorrow?"
    stop music fadeout 3
    menu:
            "Maybe Shou will give me another chance.":
                jump E1D2S11
    
            "I've had enough rejection for one day.":
                $ E1D2S10_EnoughRejection = 1
                jump E1D2S12
    

