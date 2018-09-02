#
label E2YMS2:
    
    #Event 2 - Afternoon Choice (>50 Points)
    
    "I dial Yuuna's number and wait for her to answer."
    play sound "audio/sfx/Technology/Phone Dial.ogg"
    $renpy.pause(2.5)
    play sound2 "audio/sfx/Technology/Phone Answer.ogg"
    voice "audio/voice/E2/Free/YM/S2/1.ogg"
    ym "Hello?"
    pf "Hey Yuuna! It's [pfirst]. I was wondering if you've got some time to hang out. Maybe we can have another tennis match?"
    voice "audio/voice/E2/Free/YM/S2/2.ogg"
    ym "I'd love to, but I've got a class in about half an hour. I was about to stop and grab a coffee. Would you like to join me?"
    pf "Yeah, that sounds great. I'll meet you in the cafe."
    voice "audio/voice/E2/Free/YM/S2/3.ogg"
    ym "Okay, see you soon."
    play sound2 "audio/sfx/Technology/Phone Answer.ogg"
    stop music fadeout 3
    scene black with fade
    stop ambient fadeout 3
    "We hang up, and I walk to the cafe."
    $renpy.pause(1)
    play ambient "audio/ambience/Desert Maid Cafe.ogg" fadein 5
    scene bg campus cafe day with fade
    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 3
    
    $ yuuOut = "sUniform"
    
    "Yuuna is already there by the time I arrive. She sits at a table near the window. After ordering myself a coffee, I join her. {w}She smiles in acknowledgement as I sit down."
    show yuuna smi at cc with dissolve
    pf "So, what class do you have next?"
    voice "audio/voice/E2/Free/YM/S2/4.ogg"
    ym "Just one of my PHPT degree requirement classes. It's not one of the more interesting ones so I'm not too excited about going."
    show yuuna cur at cc
    voice "audio/voice/E2/Free/YM/S2/5.ogg"
    ym "Do you have any more classes today?"
    pf "Nope, all done for the day."
    show yuuna hap at cc
    voice "audio/voice/E2/Free/YM/S2/6.ogg"
    ym "That must be nice."
    "Her eyes sparkle as she sips her coffee."
    
    show yuuna smi at cc
    voice "audio/voice/E2/Free/YM/S2/7.ogg"
    ym "So, how are you spending your free time between classes? Anything fun?"
    pf "Hm, it varies. I'll go to the library to study or chill in the Pilot's Lounge. Generally, I like to spend some quality time with my GEAR."
    voice "audio/voice/E2/Free/YM/S2/8.ogg"
    ym "Ah…"
    show yuuna neu at cc
    "She glances at the teal stripes on my uniform as she takes a sip of her coffee."
    voice "audio/voice/E2/Free/YM/S2/9.ogg"
    ym "What made you decide to be a pilot?"
    pf "Well, my dad was an engineer and I grew up building mechs with him. He and I actually built Eagle together."
    show yuuna smi at cc
    voice "audio/voice/E2/Free/YM/S2/10.ogg"
    ym "Eagle must be really special to you then."
    pf "Yeah."
    show yuuna cur at cc
    voice "audio/voice/E2/Free/YM/S2/11.ogg"
    ym "So why didn't you go into engineering?"
    show yuuna neu at cc
    pf "My dad always wanted to be pilot, but he was colour blind so could never become one. He always encouraged me to be a pilot instead. I never even considered doing anything else."
    pf "Don't get me wrong, I'm not just doing it because my dad wanted me to. {w}I love piloting. It's just something I always knew I wanted to do."
    pf "What about you?"
    show yuuna hap at cc
    voice "audio/voice/E2/Free/YM/S2/12.ogg"
    ym "I actually almost joined the pilot program."
    pf "Really? What changed your mind?"
    show dots:
        xoffset 720
        yoffset 100
        xzoom .75
        yzoom .75
    show yuuna thi at cc
    "She hesitates. The words are on her lips, but she's debating whether or not to say them."
    voice "audio/voice/E2/Free/YM/S2/13.ogg"
    ym "There were a lot of factors, but the biggest reason I chose to study PHPT is because pilot health and safety is frequently overlooked."
    show yuuna neu at cc
    voice "audio/voice/E2/Free/YM/S2/14.ogg"
    ym "Pilots go through a rigorous training process and people don't consider the long term effects that training has on a person. Especially when you're talking about g-force training and the like."
    show yuuna smi at cc
    voice "audio/voice/E2/Free/YM/S2/15.ogg"
    ym "Being a pilot can take more of a toll on your body than you know."
    
    menu:
        "You're scaring me now…":
            pf "Okay, I'm going to admit you're making me a little bit nervous."
            show yuuna ner at cc
            "She flushes and waves her words away in apology."
            show panic:
                xoffset 720
                yoffset 100
                xzoom .75
                yzoom .75
            voice "audio/voice/E2/Free/YM/S2/16.ogg"
            ym "Sorry! That wasn't my intention!"
            show yuuna smi at cc
            voice "audio/voice/E2/Free/YM/S2/17.ogg"
            ym "I think piloting is great and I'm not trying to discourage you."
    
        "You can check my health any day.":
            pf "I feel safer just knowing you're here to look out for me."
            show regBlush:
                xoffset 720
                yoffset 100
                xzoom .75
                yzoom .75
            show yuuna cur b1 at cc with dissolve
            "She blushes."
            show yuuna smi b1 at cc
            voice "audio/voice/E2/Free/YM/S2/18.ogg"
            ym "I'll try my best."
    
        "Geez, lighten up, Negative Nancy.":
            pf "I'm sure it's not as bad as you think it is."
            show yuuna sad at cc
            "She frowns slightly."
            voice "audio/voice/E2/Free/YM/S2/19.ogg"
            ym "That's what most people think, and that's exactly the type of attitude I'm hoping to extinguish."
            
    stop music fadeout 5
    pf "So, pilot health and physiotherapy… does that encompass mental health as well as physical?"
    show yuuna smi at cc with dissolve
    play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 5
    voice "audio/voice/E2/Free/YM/S2/20.ogg"
    ym "Yes, definitely. Most people tend to forget that a healthy mind is just as important as a healthy body, but an unhealthy mind can be just as destructive--if not more so--than an unhealthy body."
    
    menu:
        "Ask more about pilot mental health.":
            pf "I'll admit I'm a little guilty of forgetting that myself. Is there currently a large emphasis on mental health screenings for pilots or is this an ever evolving process?"
            show yuuna neu at cc
            voice "audio/voice/E2/Free/YM/S2/21.ogg"
            ym "It's an ever evolving process, and unfortunately, it usually takes a tragedy before people realise there's a flaw in the system."
            pf "Really?"
            show yuuna smi at cc
            "She nods."
            voice "audio/voice/E2/Free/YM/S2/22.ogg"
            ym "Obviously, a pilot has to pass a mental evaluation before he can earn his license, but that screening needs to be more rigorous and more frequent."
            pf "What do you mean?"
            show yuuna thi at cc
            voice "audio/voice/E2/Free/YM/S2/23.ogg"
            ym "Some mental illnesses are easily diagnosed, but some are more tricky, and some can disappear and reappear--like depression or addictions."
            show yuuna neu at cc
            voice "audio/voice/E2/Free/YM/S2/24.ogg"
            ym "Those are hard conditions to spot because for the most part, they must be self-reported. But if a pilot knows that he may lose his license because he has this condition, he may not report it. It could reach a level where he would not only endanger himself, but those around him."
            #voice "audio/voice/E2/Free/YM/S2/25.ogg"
            #ym "For example, a pilot suffers from depression and decides to act upon his suicidal thoughts. Maybe in the middle of a battle he decides to exit his GEAR. If anyone else leaves their robot to assist him, then he's just put someone else in danger."
            pf "Shouldn't his colleagues or teammates report him if they notice the pilot's changed behaviour?"
            show yuuna sad at cc
            voice "audio/voice/E2/Free/YM/S2/26.ogg"
            ym "They absolutely should, but the way the current system works, the responsibility falls on the pilot himself and not his peers."
            show yuuna neu at cc
            voice "audio/voice/E2/Free/YM/S2/27.ogg"
            ym "Pilots who are on anxiety or depression medication can also be disqualified from earning their license just because of the medication use alone."
            pf "Isn't that kind of like punishing the pilot for treating his condition?"
            show yuuna thi at cc
            voice "audio/voice/E2/Free/YM/S2/28.ogg"
            ym "There are arguments for both sides. The pilot is being punished for treating his condition, and because he uses the medication he should be considered to be in sound mind."
            show yuuna neu at cc
            voice "audio/voice/E2/Free/YM/S2/29.ogg"
            ym "On the other hand, someone who is using the medication has a greater potential for significant underlying psychiatric or psychological problems and the side effects of medication is always unpredictable, so they're considered a risk."
            pf "Huh… I guess both sides make sense. Which side are you on?"
            show yuuna sur at cc
            "Yuuna's eyes flash."
            show yuuna ang at cc
            voice "audio/voice/E2/Free/YM/S2/30.ogg"
            ym "I'm a strong advocate for reform! We need pilots to understand the severity of these conditions and we can't encourage an environment of secrecy because that is what puts lives at risk!"
            show yuuna ner at cc with dissolve
            "She pauses, then her cheeks flush."
            show drop:
                xoffset 720
                yoffset 100
                xzoom .75
                yzoom .75
            show yuuna wor b1 at cc with dissolve
            voice "audio/voice/E2/Free/YM/S2/31.ogg"
            ym "Sorry, I didn't mean to yell at you."
            pf "It's okay, I'm just glad someone like you is here to fight for what's best for us pilots!"
    
        "Ask more about pilot physical health.":
            pf "While that may be true, aren't the physical qualifications for earning your pilot's license very rigorous?"
            show yuuna neu at cc
            "Yuuna nods."
            voice "audio/voice/E2/Free/YM/S2/32.ogg"
            ym "Yes, the pilot must pass a physical, and that includes your past medical history and family history screening."
            pf "That's a little unfair, isn't it? I mean, it's not my fault if my grandmother had diabetes or if my father had high blood pressure."
            show yuuna smi at cc
            voice "audio/voice/E2/Free/YM/S2/33.ogg"
            ym "No, it's not your fault, and generally speaking a person isn't disqualified based on a potential. It's still good to be aware, though, so you can take preventative measure if need be."
            pf "I suppose that's true."
            voice "audio/voice/E2/Free/YM/S2/34.ogg"
            ym "Besides, those screenings are more to spot if you have anything that could cause a sudden disabling condition, such as a heart arrhythmia."
            show yuuna mis at cc
            voice "audio/voice/E2/Free/YM/S2/35.ogg"
            ym "You can be disqualified if you don't reach the minimum height requirement, too."
            "I smirk."
            pf "I think I'm good on that."
            show yuuna hap at cc
            "Yuuna giggles."
            pf "I didn't know that they enforced it so strictly though."
            show yuuna smi at cc
            #voice "audio/voice/E2/Free/YM/S2/36.ogg"
            #ym "Of course."
            #voice "audio/voice/E2/Free/YM/S2/37.ogg"
            #ym "A pilot needs to be able to comfortably reach all the controls in the cockpit. That's why the minimum age to begin GEAR training is 16, when most people have gone through their growth spurt."
            pf "But can't you just purchase a frame with a the cockpit seat for your height?"
            show yuuna thi at cc
            voice "audio/voice/E2/Free/YM/S2/38.ogg"
            ym "Sort of. Companies can manufacture cockpit seats to accommodate a smaller person."
            pf "So there's no issue!"
            show yuuna neu at cc
            voice "audio/voice/E2/Free/YM/S2/39.ogg"
            ym "Well, these smaller seat configurations aren't approved by the United Cenorobotics Committee yet. While the manufacturers are pushing to remove the minimum height requirement, the UCC won't approve it until they are provided enough conclusive data which proves safety isn't compromised."
            pf "Then it falls on the manufacturers to collect that data."
            show yuuna smi at cc
            voice "audio/voice/E2/Free/YM/S2/40.ogg"
            ym "Yes, that's the work in progress right now."
            show dots:
                xoffset 720
                yoffset 100
                xzoom .75
                yzoom .75
            show yuuna thi at cc
            "She looks thoughtful."
            voice "audio/voice/E2/Free/YM/S2/41.ogg"
            ym "Although, I've heard the UCC is being particularly resistant to amending the minimum height rule. They keep requesting more and more data even though what has been presented technically passes their current standards."
            pf "Hmm, what's your thought on this?"
            show yuuna neu at cc
            voice "audio/voice/E2/Free/YM/S2/42.ogg"
            ym "I think that the UCC has all the right to be stringent in their process. There can be no compromises when it comes to pilot safety."
            show yuuna smi at cc
            voice "audio/voice/E2/Free/YM/S2/43.ogg"
            ym "Besides, the UCC isn't against changing the rule, they just want enough comprehensive data to make a well informed decision."
            
    show yuuna cur at cc with dissolve
    "Yuuna checks the time."
    show yuuna smi at cc
    voice "audio/voice/E2/Free/YM/S2/44.ogg"
    ym "Ah! I need to get going. Sorry for lecturing you."
    pf "No, don't be. I think it's great that you're so passionate about this. Passion is what creates change."
    show yuuna hap at cc
    "She smiles brightly."
    show note:
        xoffset 720
        yoffset 100
        xzoom .75
        yzoom .75
    voice "audio/voice/E2/Free/YM/S2/45.ogg"
    ym "I'll see you later, okay?"
    pf "Yeah, see you."
    hide yuuna with dissolve
    stop music fadeout 5
    scene black with fade
    "She gathers her things and leaves. I finish up my coffee, then follow her out of the cafe."
    stop ambient fadeout 3
    $renpy.pause(1)
    $ E2YMS2_Completed = 1
    #end

