#
label E3_5S1:
    
    #CONTINUATION OF KAITO CONVERSATION (Episode 3)
    #scene black with fade
    #$renpy.pause(1)
    pf "I have a right to know what happened to my parents."
    #scene bg homekaito main night with fade
    show kaito dis at cc with dissolve
    "Uncle Kaito's expression doesn't change, but a faint line of worry creases his brow. I soften my tone."
    play music "audio/music/Next Time (GAME VERSION).ogg" fadein 5
    pf "I appreciate that you're trying to protect me, but whatever it says in that email, I can handle it."
    "He looks hard at me and I stay silent as he ponders my words. Finally, he sighs and opens the laptop. After he pulls up the email, he slides the computer towards me."
    show kaito ner
    "With bated breath, I read through the brief email."
    
    "{i}Mr. Kaito, we have begun our preliminary investigation into the case of Mr. and Mrs. [plast] and we have found that the witness statements released during the conclusion of the case contrasted greatly with the statements originally recorded by the investigating officers.{/i}"
    "{i}Further investigation will continue.{/i}"
    
    pf "That's it?"
    "I can't hide the confusion from my voice."
    show kaito neu
    voice "audio/voice/E4/Kaito/d00/(2).ogg"
    hk "For now."
    pf "I don't understand. It's common knowledge that witnesses are not always a reliable source. A lot of times they'll change their stories or misremember what they saw."
    voice "audio/voice/MISSING/BATCH4/Kaito_MissingLines-04.ogg"
    hk "It's not just the witness statements."
    show kaito ner
    voice "audio/voice/E4/Kaito/d00/(3).ogg"
    hk "Before the accident, your mom called me out of the blue with a very strange request. She wanted to make sure that if anything should happen to her or your dad that I'd take care of you kids."
    voice "audio/voice/E4/Kaito/d00/(4).ogg"
    hk "We'd talked about custody when your parents first created their will, and we'd already decided that should your parents pass away custody of you kids would go to me. I thought it was strange that she'd bring it up again, but I figured she might have gone in to update her will and felt a little insecure."
    voice "audio/voice/E4/Kaito/d00/(5).ogg"
    hk "Of course I assured her that I'd take care of you both."
    show kaito thi
    voice "audio/voice/E4/Kaito/d00/(6).ogg"
    hk "Then, a week later, your parents' accident happened…"
    pf "…"
    show kaito ner
    #voice "audio/voice/E4/Kaito/d00/(7).ogg"
    voice "audio/voice/MISSING/BATCH4/Kaito_MissingLines-02.ogg"
    hk "I tried to discreetly look into the accident on my own, but got nowhere. That's why I hired the private investigator."
    "I wrack my brain, trying to remember the last few days before Mom and Dad's accident. Were they acting any different than usual? {w}Dad was wrapping up the last few upgrades to my core… but we were both scrambling to finish updates on Eagle before school started…"
    pf "I understand why you wanted to keep this a secret."
    show kaito neu
    "Uncle Kaito looks relieved."
    pf "But now that I know about this investigation, I want to be kept in the loop."
    "He nods."
    voice "audio/voice/E4/Kaito/d00/(8).ogg"
    hk "I suppose that's fair."
    pf "Maybe I can help too. I mean, we did live in NYC and I still have some contacts from CINY."
    
    voice "audio/voice/E4/Kaito/d00/(9).ogg"
    hk "Let's see what the PI comes back with and we can go from there. If your parents were in danger, I don't want you to put your life at risk too."
    "I nod reluctantly."
    show kaito wor
    "Kaito suddenly looks uneasy."
    show drop:
        xoffset 720
        yoffset 5
        xzoom .75
        yzoom .75
    voice "audio/voice/E4/Kaito/d00/(10).ogg"
    hk "You aren't going to tell your sister about this, are you?"
    
    menu:
        "She should know.":
            pf "They were her parents too. I think Nikki deserves to know the truth."
            voice "audio/voice/E4/Kaito/d00/(11).ogg"
            hk "She had a harder time adjusting to the move than you did."
            pf "So?"
            show kaito ner
            voice "audio/voice/E4/Kaito/d00/(12).ogg"
            hk "She's finally started to move on and accept her new life… I don't want to ruin all of that for something we aren't even sure about."
            "It's true. Nikki seems a lot happier now than when we first arrived and I don't want to take that happiness away from her."
            pf "You're right. We shouldn't bring her into this before we have proof. But if we do find something concrete, we need to tell her the truth."
            show kaito neu
            "Uncle Kaito nods."
        
        "No, she has enough to worry about.":
            "I shake my head."
            pf "Our parents' death affected Nikki a lot more than it affected me. She puts on a smile and a brave face, but I can see when she's hurting inside."
            show kaito ner
            pf "She's made a lot of progress these past couple of months, and I think she's finally begun to move on and be happy. We shouldn't rock the boat until we know for certain what happened to Mom and Dad wasn't an accident."
            show kaito smi
            "Uncle Kaito grins in relief."
            voice "audio/voice/E4/Kaito/d00/(13).ogg"
            hk "I'm glad we're in agreement on this."
        
        "It's not my place to tell.":
            pf "It's not my place to decide what is or is not best for Nikki."
            voice "audio/voice/E4/Kaito/d00/(14).ogg"
            hk "I think we should wait to tell her."
            "I don't respond, but look at him questioningly."
            show kaito ner
            voice "audio/voice/E4/Kaito/d00/(15).ogg"
            hk "I don't want to open up old wounds or give her false hope after she's worked so hard to move on with her life. The less she knows, the better."
            pf "Sure, but if it turns out Mom and Dad's deaths weren't accidents we need to tell her the truth."
            show kaito neu
            voice "audio/voice/E4/Kaito/d00/(16).ogg"
            hk "When the time comes, we will."
            pf "Okay."
    
    "Uncle Kaito gently shuts his laptop."
    show kaito neu
    voice "audio/voice/E4/Kaito/d00/(17).ogg"
    hk "I think that's enough excitement for one day."
    #show note:
    #    xoffset 720
    #    yoffset 5
    #    xzoom .75
    #    yzoom .75
    show kaito smi
    "He grins jokingly at me."
    #show kaito smi
    voice "audio/voice/E4/Kaito/d00/(18).ogg"
    hk "I need to get some work done before you decide to snoop through even more of my emails."
    pf "That's my cue to head upstairs."
    stop music fadeout 3
    hide kaito with dissolve
    play sound "audio/sfx/Human/Going Upstairs (wood).ogg" fadein 1
    scene black with fade
    $renpy.pause(1)
    "As we part and I head into my room, I try to focus on my homework but my mind is filled with unanswered questions about Mom and Dad. If this wasn't an accident, then what really happened? Why would anyone want to hurt them?"
    stop ambient fadeout 3
    "Eventually, I get my work done and head to bed. Then I drift off into a fitful slumber."
    $renpy.pause(1)
    jump E3_5S2

