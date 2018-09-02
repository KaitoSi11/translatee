#
label E4D7SS:
    $ shoOut = "sCasual"
    voice "audio/voice/E4/Shou/d7/1 Copy.ogg"
    ss "Broseph! How's it hanging?"
    
    if E4D6SS_Completed == 1:
        pf "Did I catch you at an okay time? I wasn't sure if I should call."
        voice "audio/voice/E4/Shou/d7/2 Copy.ogg"
        ss "Yeah, of course. I always have time for a friend."
        "He sounds just like his old self. I guess he must have done a lot of soul searching since I last saw him."
        
    pf "I just… do you think we could meet?"
    voice "audio/voice/E4/Shou/d7/3 Copy.ogg"
    ss "Oh, uh, sure."
    "He sounds surprised."
    voice "audio/voice/E4/Shou/d7/4 Copy.ogg"
    ss "Any place you have in mind?"
    pf "Where are you now? I can meet you."
    voice "audio/voice/E4/Shou/d7/5 Copy.ogg"
    ss "I'm just chilling in my room. Come on over."
    pf "Thanks, I'll see you soon."
    
    play sound "audio/sfx/Technology/Phone Answer.ogg"
    stop ambient fadeout 3
    scene black with fade
    #play music "audio/music/After a Long Day (GAME VERSION).ogg" fadein 5
    $renpy.pause(1.0)
    "We hang up the phone. As if in a daze, I make my way towards his dorm. Shou greets me with a wide smile, but it drops as soon as he sees my face. He quickly ushers me in. I half-heartedly greet any of his dorm mates we pass before we settle into Shou's room."
    scene bg campus dormroom night with fade
    "I sit at his desk while Shou flops onto his bed."
    play music "audio/music/Next Time (GAME VERSION).ogg" fadein 5
    show shou ske at cc with dissolve
    voice "audio/voice/E4/Shou/d7/6 Copy.ogg"
    ss "What's going on? You seem tense."
    
    
    if E4D7S2_CoreDestroyed == 1:
        pf "There's something I need to tell you."
        show shou neu
        voice "audio/voice/E4/Shou/d7/7 Copy.ogg"
        ss "Okay, I'm ready."
        pf "My core is gone."
        "Shou blinks."
        show question:
            xoffset 720
            yoffset 20
            xzoom .75
            yzoom .75
        voice "audio/voice/E4/Shou/d7/8 Copy.ogg"
        ss "Gone where?"
        pf "Nowhere, just gone."
        show shou ske
        voice "audio/voice/E4/Shou/d7/9 Copy.ogg"
        ss "Like into oblivion?"
        pf "Yeah."
        show shou neu
        "He blinks again before sitting straight up."
        show shocked:
            xoffset 720
            yoffset 20
            xzoom .75
            yzoom .75
        show shou sur
        voice "audio/voice/E4/Shou/d7/10 Copy.ogg"
        ss "Holy crap! Your core is gone?! That's so messed up! Who would do such a thing?"
        pf "I did."
        show shou ang
        voice "audio/voice/E4/Shou/d7/11 Copy.ogg"
        ss "This isn't time for jokes!"
        show shou neu
        pf "No, seriously, it was me. I destroyed it."
        "He continues to stare incredulously at me."
        voice "audio/voice/E4/Shou/d7/12 Copy.ogg"
        ss "Why?"
    
    else:
        "I unconsciously start to play with the drive in my hands."
        show shou neu
        voice "audio/voice/E4/Shou/d7/13 Copy.ogg"
        ss "What's that?"
        pf "It's my core."
        "He blinks, then laughs."
        show shou hap
        voice "audio/voice/E4/Shou/d7/14 Copy.ogg"
        ss "Very funny. But seriously, what is it?"
        pf "The data from my core."
        show shou ske
        "Shou frowns."
        voice "audio/voice/E4/Shou/d7/15 Copy.ogg"
        ss "What's it doing in there?"
        pf "I didn't know where else to put it."
        show drop:
            xoffset 720
            yoffset 20
            xzoom .75
            yzoom .75
        voice "audio/voice/E4/Shou/d7/16 Copy.ogg"
        ss "...You could have left it in Eagle…?"
    
    "I sigh and share with Shou all that I've learned. My story comes out in pieces and Shou continually asks questions to help him understand the order of events. Eventually, I finish my story."
    show shou thi
    voice "audio/voice/E4/Shou/d7/17 Copy.ogg"
    ss "Damn, that's intense."

    pf "I know."
    
    if E4D6SS_Completed == 1:
        show shou thi
        voice "audio/voice/E4/Shou/d7/18 Copy.ogg"
        ss "I guess this is the weekend we all learn about our family secrets."
        "I nod."
        
    pf "I'm not sure if I did the right thing. I acted emotionally and maybe I should have taken the time to really think things through."

    show shou neu
    voice "audio/voice/E4/Shou/d7/19 Copy.ogg"
    ss "No way. You were right to do what you did."
    pf "You think so?"

    show shou neu
    voice "audio/voice/E4/Shou/d7/20 Copy.ogg"
    ss "Without a doubt!"
    "I let out the breath I hadn't realised I'd been holding. A huge weight lifts off my shoulder. I hadn't realised how anxious I was about this decision until someone else validated my choice."
    show shou neu
    voice "audio/voice/E4/Shou/d7/21 Copy.ogg"
    ss "Your dad might not have been able to make the decision himself, but he was right to trust you. You're like the most logical guy I know!"
    "I grin weakly."
    pf "Considering your version of logic, that's not too difficult to achieve."
    show shou smi
    voice "audio/voice/E4/Shou/d7/22 Copy.ogg"
    ss "Hey!"
    "He matches my grin."
    show shou neu

    voice "audio/voice/MISSING/BATCH2/18.ogg"
    ss "How are you doing otherwise?"
    
    if E4D6SS_Completed == 1:
        "I shrug."
        pf "It sucks. {w}I just keep thinking about what if I'd known ahead of time. Maybe things would be different."
        show shou neu
        voice "audio/voice/E4/Shou/d7/23 Copy.ogg"
        ss "I get what you mean. After I found out about Akio, I felt so guilty for the way I treated him and the way I treated my parents."
        show shou sad
        voice "audio/voice/E4/Shou/d7/24 Copy.ogg"
        ss "And… I was angry too. I mean, how could they keep something so important from me?"
        voice "audio/voice/E4/Shou/d7/25 Copy.ogg"
        ss "Maybe if I'd known we could've had more time."
        show shou thi
        "Shou suddenly looks tired. I guess he's not as recovered as I thought he was."
        voice "audio/voice/E4/Shou/d7/26 Copy.ogg"
        ss "But you know what I realised?"
        pf "What?"
        show shou neu
        voice "audio/voice/E4/Shou/d7/27 Copy.ogg"
        ss "It doesn't matter."
        voice "audio/voice/E4/Shou/d7/28 Copy.ogg"
        ss "Who knows what would have happened if they'd told me, but the fact of the matter is that they didn't tell me."
        show shou ske
        voice "audio/voice/E4/Shou/d7/29 Copy.ogg"
        ss "That's my reality, and if I get lost in those thoughts I might lose my only chance to spend time with my brother."
        show shou neu
        "He looks at me and his face is serious."
        stop music fadeout 4
        voice "audio/voice/E4/Shou/d7/30 Copy.ogg"
        ss "You can't let those thoughts take over. You'll never know how things might have been if your dad had told you because that's not your reality. This is."
        "Shou's right. Wondering about the impossible will only bring more heartache. I need to accept what's happened, take what I've learned, and move on."
        pf "Thanks, Shou. That was actually very insightful."
        show shou hap
        "He grins again."
        
        voice "audio/voice/E4/Shou/d7/31 Copy.ogg"
        ss "I know, right? Took me all night to come up with that."
        "The one thing I can count on with Shou is that he'll always try to find a way to smile. Even when he's feeling as low as can be, he can see the spark of light in the darkness. That's a rare quality to have, and I'm glad to see that even after discovering the news about his brother he still hasn't lost it."
        "I know that if I ever teeter too close to the edge of losing myself, Shou will be there to pull me back."
        $ renpy.music.set_volume(1.0, channel="music")
        play music "audio/music/Timeless.ogg" fadein 2       
        "In this moment, I have clarity.{w} I don't need to focus on the past because my future is worth exploring, and my friends will be with me every step of the way."
        
    
    else:
        pf "It still sucks. I keep wondering about what could have happened."
        voice "audio/voice/E4/Shou/d7/32 Copy.ogg"
        ss "I know it's easier said than done, but you've got to let it go."
        show shou neu
        voice "audio/voice/E4/Shou/d7/33 Copy.ogg"
        ss "Once you give in to the \"what if\"s, it's really hard to pull yourself back out."
        
        if MCStory == 3:
            "Shou's expression saddens. I wonder if he's talking from experience."
            
        voice "audio/voice/E4/Shou/d7/34 Copy.ogg"
        ss "You end up obsessed. You don't even realise what you're doing until it's too late and life passes you by."
        show shou thi
        "He shakes his head."
        voice "audio/voice/E4/Shou/d7/35 Copy.ogg"
        ss "Then you would have just wasted the life your father fought so hard to give you."
        show shou neu
        "He's right. Wondering about the impossible will only bring more heartache. I need to accept what's happened, take what I've learned, and move on."
        stop music fadeout 4
        "I nod."
        pf "You're right. I can't let what I've learned bring me down."
        show shou smi
        
        "I'm lucky to have a friend who'll always have my back."
        $ renpy.music.set_volume(1.0, channel="music")
        play music "audio/music/Timeless.ogg" fadein 2
        "In this moment, I have clarity.{w} I don't need to focus on the past because my future is worth exploring, and my friends will be with me every step of the way."
        

    jump E4Epilogue
