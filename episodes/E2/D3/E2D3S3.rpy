#
label E2D3S3:
    
    #Evening choice end
    
    scene black with fade
    stop ambient fadeout 3
    stop music fadeout 3
    $renpy.pause(2.5)
    play ambient "audio/ambience/Night Crickets.ogg" fadein 1
    scene bg homekaito main night with fade
    # no music for this first part ?
    
    "I'm in a happier mood when I arrive home."
    pf "Hey guys, I'm home--"
    voice "audio/voice/E2/D3/S3/Kaito/1.ogg"
    hk "You can't just decide that without telling me!"
    "Uncle Kaito's voice stops me. I can see him pacing back and forth in the kitchen."
    voice "audio/voice/E2/D3/S3/Kaito/2.ogg"
    hk "So cut it short!"
    voice "audio/voice/E2/D3/S3/Kaito/3.ogg"
    hk "This is the opening day of my new restaurant! They'll expect me to be there and they'll expect you there too."
    "As I get closer to the kitchen, I can hear a woman's voice on the other end of the line."
    voice "audio/voice/E2/D3/S3/Kaito/4.ogg"
    hk "I really don't care. Part of our arrangement was that we'd consult each other {i}before{/i} making a decision, and you didn't. So how you're supposed to be in two places at once really isn't my problem."
    "A flurry of muffled words on the line has Kaito frowning deeper and deeper."
    voice "audio/voice/E2/D3/S3/Kaito/5.ogg"
    hk "Don't forget, we are {i}still{/i} married. We promised to do whatever it took to make sure nothing interfered with our careers. Well, if you don't show up, then that will certainly interfere with my career!"
    "Married? Is he talking to Aunt Yuki?"
    "There's a pause. I think I hear her say, \"I'll see what I can do\" and hang up."
    # phone hang up / slam sfx?
    show kaito dis at cc with dissolve
    "Uncle Kaito slams the phone onto the table, then falls into a chair and holds his head in his hands."
    pf "Hey, Uncle Kaito."
    play music "audio/music/After a Long Day (GAME VERSION).ogg" fadein 3
    show exclamation:
        xoffset 720
        yoffset 5
        xzoom .75
        yzoom .75
    show kaito cur at cc with dissolve
    show kaito mis at cc with dissolve
    "He glances up and gives me a weak smile."
    voice "audio/voice/E2/D3/S3/Kaito/6.ogg"
    hk "You're back. How was school today?"
    pf "Good..."
    show kaito neu at cc
    "I sit beside him."
    pf "I wasn't trying to eavesdrop, but I heard you talking to Aunt Yuki just now."
    show kaito ner at cc
    "He looks a little uneasy, but waits for me to finish."
    pf "What did you mean by \"still married\"? Isn't Aunt Yuki just away on business?"
    voice "audio/voice/E2/D3/S3/Kaito/7.ogg"
    hk "Sort of."
    show kaito neu at cc
    "Kaito sighs wearily and rubs his temples."
    voice "audio/voice/E2/D3/S3/Kaito/8.ogg"
    hk "I suppose you're old enough to know the truth. Your aunt and I are separated. We have been for the last six months."
    "The last {i}six{/i} months?"
    pf "But you aren't divorced?"
    voice "audio/voice/E2/D3/S3/Kaito/9.ogg"
    hk "No."
    pf "How come we didn't know? We're your family."
    show kaito ner at cc
    voice "audio/voice/E2/D3/S3/Kaito/10.ogg"
    hk "We had to keep this quiet. Divorce is viewed differently here in Japan. It's not as common as in the States, and Yuki and I don't want our personal issues to interfere with our careers."
    "I remember the stories Mom told me about how difficult it was when she and Dad first got married. She couldn't have stayed in Japan even if she wanted to."
    pf "If you two are just separated, does that mean Aunt Yuki is here in Isokaze?"
    show kaito neu at cc
    voice "audio/voice/E2/D3/S3/Kaito/11.ogg"
    hk "Yes."
    
    menu:
        "You shouldn't have lied.":
            pf "How long were you planning on keeping up this charade before telling us?"
            show kaito wor at cc
            "He hesitates."
            show kaito ner at cc
            hk "As long as possible, I suppose."
            voice "audio/voice/E2/D3/S3/Kaito/12.ogg"
            pf "We live with you now and would have found out sooner rather than later. Aunt Yuki can only be \"away on business\" for so long before it gets suspicious."
            show kaito mis at cc
            voice "audio/voice/E2/D3/S3/Kaito/13.ogg"
            hk "Well, I would have had her stop by and live here a few days before taking off again."
            "I raise a brow."
            pf "Because a marriage where you see each other once every few weeks is normal."
            show kaito neu at cc
            "He sighs."
            show kaito sad at cc
            voice "audio/voice/E2/D3/S3/Kaito/14.ogg"
            hk "Yeah, it's inevitable that you would have started asking questions. I'm sorry I didn't tell you when you kids first got here."
            "I feel a pang of guilt. {w}I shouldn't be so hard on him. After all, he meant well."
            pf "It's okay. We were busy getting adjusted anyway."
        
        "Does this mean I can see her?":
            "Aunt Yuki was always the fun aunt. Not to say Uncle Kaito isn't fun, but she used to help us play tricks on the \"grown-ups\" when we were little. Sometimes she'd even help us prank Uncle Kaito. He never got angry, but would laugh instead."
            "They seemed so happy together."
            show question:
                xoffset 720
                yoffset 5
                xzoom .75
                yzoom .75
            show kaito ske at cc
            voice "audio/voice/E2/D3/S3/Kaito/15.ogg"
            hk "Hey, you okay there?"
            "I snap back to reality."
            pf "We can still see her, right? Even though you two are separated."
            show kaito cur at cc
            "He's taken aback."
            show kaito neu at cc
            voice "audio/voice/E2/D3/S3/Kaito/16.ogg"
            hk "Of course. She's still your family."
        
        "I get it.":
            pf "I know Japan has stricter rules on family and what's proper, so I don't blame you for keeping this a secret from us."
            show kaito smi at cc
            "Kaito grins in relief."
            voice "audio/voice/E2/D3/S3/Kaito/17.ogg"
            hk "You don't know how much that means to me, kid."
            pf "Are you going to tell Nikki?"
            show dots:
                xoffset 720
                yoffset 5
                xzoom .75
                yzoom .75
            show kaito neu at cc
            "He thinks before responding."
            voice "audio/voice/E2/D3/S3/Kaito/18.ogg"
            hk "Yes, I will."
            pf "Do you think she'll be angry you lied?"
            "Nikki has always been more sensitive than I."
            "He shrugs."
            show kaito smi at cc
            ### VOICE - Last half of that line isn't voiced
            voice "audio/voice/E2/D3/S3/Kaito/19.ogg"
            hk "Maybe, but I think she's mature enough to understand why we did it."  #Plus, it'll be nice to have this out in the open."
            pf "Yeah, it must be exhausting hiding it from everyone."
            show kaito mis at cc
            voice "audio/voice/E2/D3/S3/Kaito/20.ogg"
            hk "It has been."
    
    pf "What did Aunt Yuki say when you told her we were living with you?"
    show drop:
        xoffset 720
        yoffset 5
        xzoom .75
        yzoom .75
    show kaito thi at cc
    voice "audio/voice/E2/D3/S3/Kaito/21.ogg"
    hk "Uh, well, about that…"
    "Kaito trails off and refuses to meet my eyes."
    pf "She doesn't know we're here?"
    show kaito neu at cc
    voice "audio/voice/E2/D3/S3/Kaito/22.ogg"
    hk "No."
    pf "Were you planning on telling her?"
    show kaito ner at cc
    voice "audio/voice/E2/D3/S3/Kaito/23.ogg"
    hk "Of course. I just haven't gotten around to it yet."
    "I nod. Uncle Kaito doesn't share any more, but I can't stop myself from asking."
    pf "Since we're talking about it now, what happened between you two?"
    show kaito wor at cc
    "He sighs."
    show kaito neu at cc
    voice "audio/voice/E2/D3/S3/Kaito/24.ogg"
    hk "Yuki was ready to have kids and I wasn't. We'd discussed the possibility of having children when we first got married, and I kept pushing it back. I wanted to focus on my career and for a while, so did she."
    show kaito ner at cc
    voice "audio/voice/E2/D3/S3/Kaito/25.ogg"
    hk "But you know how women are--at some point their biological clock starts ticking. She didn't want to wait anymore."
    pf "But you still weren't ready?"
    show kaito sad at cc
    ### VOICE - last sentence wasn't voiced
    voice "audio/voice/E2/D3/S3/Kaito/26.ogg"
    hk "No… After that huge argument, we started to drive each other crazy. I became acutely aware of all those small things Yuki did that I hated. We fought all the time, and at some point, we agreed that this wasn't working anymore." #We couldn't divorce--Yuki's in PR so a divorce would especially hurt her career--and we couldn't live together, so we separated."
    show kaito ner at cc
    voice "audio/voice/E2/D3/S3/Kaito/27.ogg"
    hk "And that's how it's been for the last six months until we can figure out a more permanent solution."
    pf "Heh. It's kind of funny that even though you weren't ready for kids you ended up with them anyway."
    show kaito smi at cc
    "He grins."
    voice "audio/voice/E2/D3/S3/Kaito/28.ogg"
    hk "Nah, you guys don't count. You practically take care of yourselves. I'm just here to provide the roof."
    pf "Gee, thanks. Maybe it's a good thing you didn't have kids…"
    show kaito hap at cc
    "He laughs."
    pf "So what was this phone call tonight about?"
    show kaito ner at cc
    "Kaito turns solemn again."
    ### VOICE - last two sentences weren't voiced
    voice "audio/voice/E2/D3/S3/Kaito/29.ogg"
    hk "Part of our agreement for our separation was that we will both do whatever it takes to keep up the pretense of marriage when it involves our careers." #I called her tonight to tell her about the new restaurant's grand opening. She's breaking her promise because she says she can't make it."
    pf "Oh… Why not?"
    show kaito neu at cc
    voice "audio/voice/E2/D3/S3/Kaito/30.ogg"
    hk "She's going on some sort of retreat with her girlfriend. Normally we consult with each other before booking any trips to prevent something like this from happening, but this time she didn't."
    show kaito ner at cc
    voice "audio/voice/E2/D3/S3/Kaito/31.ogg"
    hk "I really need her there."
    
    menu:
        "She'll be there.":
            pf "Don't worry, Aunt Yuki won't let you down."
            show kaito wor at cc
            voice "audio/voice/E2/D3/S3/Kaito/32.ogg"
            hk "I'm not so sure."
            pf "It sounds like you two had an amicable separation."
            show kaito neu at cc
            voice "audio/voice/E2/D3/S3/Kaito/33.ogg"
            hk "Yeah, that's true."
            pf "Then you've got nothing to worry about. She'll be there."
            show kaito ske at cc
            voice "audio/voice/E2/D3/S3/Kaito/34.ogg"
            hk "How can you be so sure?"
            pf "Because she still cares for you and wouldn't want to hurt you."
            show kaito mis at cc
            "Kaito grins."
            voice "audio/voice/E2/D3/S3/Kaito/35.ogg"
            hk "Who knew you were such a romantic?"
            pf "What? No! I wrestle bears and stuff!"
            show kaito hap at cc
            show note:
                xoffset 720
                yoffset 5
                xzoom .75
                yzoom .75
            "He laughs."
            voice "audio/voice/E2/D3/S3/Kaito/36.ogg"
            hk "I'm just teasing. Seriously, thanks."
        
        "Aunt Yuki and a girl?":
            pf "Did you say she's going on a retreat with her girlfriend?"
            show kaito cur at cc
            voice "audio/voice/E2/D3/S3/Kaito/37.ogg"
            hk "Yes, why?"
            pf "Her {i}girl{/i}friend?"
            show kaito ske at cc
            voice "audio/voice/E2/D3/S3/Kaito/38.ogg"
            hk "Yes…"
            pf "Uncle Kaito, I've discovered the reason why your marriage didn't work. {w}Aunt Yuki likes women."
            show dots:
                xoffset 720
                yoffset 5
                xzoom .75
                yzoom .75
            $renpy.pause(1)
            show kaito hap at cc with dissolve
            "He stares at me for a second, then bursts into laughter."
            show kaito smi at cc
            voice "audio/voice/E2/D3/S3/Kaito/39.ogg"
            hk "No, her friend who is a girl. Not her girlfriend."
            pf "Ohhh."
            show kaito hap at cc
            voice "audio/voice/E2/D3/S3/Kaito/40.ogg"
            hk "She is very much into men."
            pf "Okay."
            show kaito mis at cc
            voice "audio/voice/E2/D3/S3/Kaito/41.ogg"
            hk "I mean {i}very{/i} into men."
            pf "I believe you…"
            show kaito mis b1 at cc with dissolve
            voice "audio/voice/E2/D3/S3/Kaito/42.ogg"
            hk "Trust me, she's definitely a fan of the--."
            pf "Please stop."
    
        "Clearly this arrangement isn't working either.":
            pf "Maybe you guys should just get that divorce."
            "All traces of playfulness is gone from Kaito's face."
            voice "audio/voice/E2/D3/S3/Kaito/43.ogg"
            hk "Excuse me?"
            pf "Well, living together wasn't working and being separated doesn't seem to be working for you two either. {w}If she doesn't show up to the grand opening, how would that be any better than getting divorced?"
            show kaito dis at cc
            voice "audio/voice/E2/D3/S3/Kaito/44.ogg"
            hk "It's not the same. Missing one engagement can easily be excused. There's no turning back from divorce. Neither one of us can afford that."
            "I shrug."
            pf "If you say so."
            show kaito neu at cc
            voice "audio/voice/E2/D3/S3/Kaito/45.ogg"
            hk "I do."
        
    show dots:
        xoffset 720
        yoffset 5
        xzoom .75
        yzoom .75
    "Uncle Kaito glances at the clock and stands."
    show kaito mis at cc
    voice "audio/voice/E2/D3/S3/Kaito/46.ogg"
    hk "I didn't realise how late it's gotten. I have an early start tomorrow."
    pf "Don't you always have an early start? You get up before I do."
    show drop:
        xoffset 720
        yoffset 5
        xzoom .75
        yzoom .75
    voice "audio/voice/E2/D3/S3/Kaito/47.ogg"
    hk "True, but I have an even earlier start than usual."
    pf "Ick."
    hide kaito with dissolve
    stop music fadeout 3
    scene black with fade
    "We say goodnight and Kaito heads upstairs. {w}I go into the living room and turn on the TV."
    "After watching my shows and the news, I turn in for the night."
    
    jump E2D4S1
