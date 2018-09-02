#
label E3D7S4:
    
    # mayu confession another label?
    $ kaiOut = "sCasual"
    if mayrelatonship == 1:
        scene bg homekaito garage day with fade
        play music "audio/music/After a Long Day (GAME VERSION).ogg" fadein 3
        "I park my bike in the garage and fish in my pocket for my keys when my hand touches the envelope. I'd forgotten all about it during the concert, but the same trepidation from before rushes back."
        "Should I wait to read it? Nikki is probably waiting for me on the other side of that door. I remember Mayu's face as she shoved the letter into my hands. This must be important if she would subject herself to that kind of embarrassment."
        "I tear open the letter and read through."
    
        "{i}I tried so many times to write this but the words never come out right. I don't know how to tell you that in these past few months I feel closer to you than anyone else.{/i}"
        "{i}You've helped me grow as a person. Playing my music and forming our band was a dream I never thought would come true, but you made it happen. Talking to you about chess was the only time I wasn't embarrassed to admit I play it, and I was thrilled to find out we read the same books!{/i}"
        "{i}You always seem to say exactly what I need to hear. Yesterday was the first time in a long time that I felt like I could be myself around someone. You were helping me get over my fears, again, and I feel like when I'm with you I can be strong.{/i}"
    
        "{i}I had so much fun yesterday that I was sad to say goodbye. Nobody makes me feel the way I feel when I'm around you. I love the time we spend together and I want to have even more of those moments with you.{/i}"
    
        "I clutch the letter in my hands as I digest Mayu's words."
    
        menu:
            "I feel the same way.":
                "My hands shake as I reread the letter. I feel the same way when I'm around her too! I want to have more days like yesterday with her."
                "Pulling out my phone, I prepare to text her."
                "Is this really how I feel?"
    
                menu:
                    "Yes.":
                        "My thumbs type out a short response."
                        "{i}I feel the same way.{/i}"
                        "There's a pounding in my ears as I wait anxiously for her reply."
                        $renpy.pause(1.5)
                        play sound "audio/sfx/Technology/Phone Vibration Once.ogg"
                        "The seconds feel like an eternity before my phone vibrates."
                        "{i}You don't know how happy I am! I was so worried you wouldn't feel the same way.{/i}"
                        "{i}:){/i}"
                        "I catch myself grinning stupidly at nothing. Can this day get any better?"
                        "..."
                        "I've been sitting in the garage for a while now. I should probably head inside."
    
                    "No.":
                        "As I continue to think about it, I realise I don't quite share the same feelings as Mayu."
                        jump E3D7S4_MayuRejection
    
            "I don't feel the same.":
                label E3D7S4_MayuRejection:
                $ mayrelatonship = 0
                "My heart sinks. I thought she meant it when she said she liked Shou. Did I lead her on by offering to help yesterday? I need to tell her the truth."
                "I type out a short response."
                "{i}I'm sorry, but I think we are better as friends.{/i}"
                $renpy.pause(2)
                play sound "audio/sfx/Technology/Phone Vibration Once.ogg"
                "There is a long pause before Mayu replies."
                "{i}I understand. Thank you for being honest with me.{/i}"
                "I hope I didn't hurt her too badly."
                "..."
                "I've been sitting in the garage for a while now. I should probably head inside."
                
    stop music fadeout 3
    play ambient "audio/ambience/Night Crickets.ogg" fadein 3
    $renpy.pause(2.0)
    scene bg homekaito main night with fade
    "I'm barely through the door before Nikki bombards me."
    play music "audio/music/Isnt This Nice (GAME VERSION).ogg" fadein 5
    show nikki neu at cc with dissolve
    voice "audio/voice/E3/D7/S4/nikki/Nikki_6_001.ogg"
    sf "Hello!"
    pf "Uh, hi."
    "She eyes me up and down."
    show nikki smi
    voice "audio/voice/E3/D7/S4/nikki/Nikki_6_002.ogg"
    sf "Soooooo?"
    pf "\"So\" what?"
    show nikki hap
    voice "audio/voice/E3/D7/S4/nikki/Nikki_6_003.ogg"
    sf "Quit stalling! The autograph?"
    
    menu:
        "I got something even better.":
            pf "Forget the autograph. Check this out!"
            show nikki cur
            "Nikki's eyes widen with anticipation."
    
        "I completely forgot!":
            "I feign a look of dread."
            pf "Oh crap! I knew I forgot something!"
            show dots:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            "Nikki's face is frozen in place as if she can't understand my words."
            pf "I'm so sorry, sis!"
            show nikki ner
            "Gradually, as my words sink in, her face falls."
            show nikki wor
            voice "audio/voice/E3/D7/S4/nikki/Nikki_6_004.ogg"
            sf "B-B-B-But y-y-ou p-promised!"
            show nikki win
            "She tries to tether her sniffles but can't stop her lip from trembling as the tears well in her eyes."
            pf "Woah! Hey! Stop! I was just kidding."
            show crying:
                xoffset 720
                yoffset 160
                xzoom .75
                yzoom .75
            "The tears slip down her cheeks."
            pf "No, seriously, look!"
        
        "I didn't get an autograph.":
            pf "I didn't have any paper so couldn't get you an autograph."
            show nikki cur
            "Her eyes widen."
            show nikki wor
            voice "audio/voice/E3/D7/S4/nikki/Nikki_6_005.ogg"
            sf "You had one job! How could you have been so unprepared?"
            pf "Calm down! I didn't come home empty handed. Look."
    
    "I pull out the necklace."
    show nikki cur
    "She snatches it from my hand and examines it for a signature, but there isn't one."
    show nikki dis
    "She pouts."
    show storm:
        xoffset 720
        yoffset 160
        xzoom .75
        yzoom .75
    voice "audio/voice/E3/D7/S4/nikki/Nikki_6_006.ogg"
    sf "This is just an Ex Zee necklace. You can buy those at any souvenir stand. I wanted an autograph from him!"
    
    pf "No, Ex Zee himself gave this to me to give to you."
    show nikki ske
    "She crosses her arms and raises an eyebrow."
    voice "audio/voice/E3/D7/S4/nikki/Nikki_6_007.ogg"
    sf "Do you really think I'm that gullible?"
    "Okay, to be fair, even I wouldn't have believed that story."
    pf "I can prove it."
    show nikki cur
    "I pull out my phone and open up the selfie we took before the concert. The medallion is clearly around his neck. Then I flip to the photos during the concert where there is an obvious lack of a necklace."
    "Nikki grabs my phone and pinches in to zoom the images. She swipes back and forth between the photos... over and over and over..."
    "When suddenly she leaps up and down, still clutching my phone."
    show nikki sur
    voice "audio/voice/E3/D7/S4/nikki/Nikki_6_008.ogg"
    sf "OHMYGODYOUWERETELLINGTHETRUTHICAN'TBELIEVEIT!"
    pf "...What?"
    show nikki hap
    "Nikki throws her arms around my neck and squeezes me tightly."
    voice "audio/voice/E3/D7/S4/nikki/Nikki_6_009.ogg"
    sf "This is the best!"
    pf "The necklace or me?"
    show heart:
        xoffset 720
        yoffset 160
        xzoom .75
        yzoom .75
    "She plants a kiss on my cheeks before letting go, then slips the necklace over her head."
    show nikki smi
    voice "audio/voice/E3/D7/S4/nikki/Nikki_6_010.ogg"
    sf "I'm never taking this off."
    
    menu:
        "I'm happy for you.":
            pf "Glad you like it, sis."
            show nikki hap
            voice "audio/voice/E3/D7/S4/nikki/Nikki_6_011.ogg"
            sf "You're the best brother ever!"
            pf "Thanks!"
    
        "I bet I can change that!":
            pf "You know that was in my back pocket, right?"
            ### VOICE - needs editting
            voice "audio/voice/E3/D7/S4/nikki/Nikki_6_012.ogg"
            sf "Don't care."
            pf "And I sat on it."
            voice "audio/voice/E3/D7/S4/nikki/Nikki_6_012_01.ogg"
            sf "Don't care."
            pf "And I might have farted."
            voice "audio/voice/E3/D7/S4/nikki/Nikki_6_012_02.ogg"
            sf "Don't care."
            pf "And I also put it in--"
            show nikki dis
            voice "audio/voice/E3/D7/S4/nikki/Nikki_6_013.ogg"
            sf "Ok don't ruin this for me! Ugh, you are the suckiest best brother ever."
            pf "Thanks... I think."
    
        "That's gross.":
            pf "You know he sweat all over that thing, right?"
            show nikki ske
            voice "audio/voice/E3/D7/S4/nikki/Nikki_6_014.ogg"
            sf "Um, yeah, that's kind of the point."
            pf "I can't wait for the day when girls will cherish my sweat."
            show nikki hap
            voice "audio/voice/E3/D7/S4/nikki/Nikki_6_015.ogg"
            sf "I don't even care that you're being gross right now because this necklace is the best gift ever!"
            pf "Glad you like it."
            
    show nikki mis
    "She nods happily."
    voice "audio/voice/E3/D7/S4/nikki/Nikki_6_016.ogg"
    sf "I have to go tell my friends! They are going to flip!"
    stop music fadeout 5
    hide nikki with dissolve
    # speed increase on this sfx?
    play sound "audio/sfx/Human/Going Upstairs (wood).ogg" fadein 1
    $renpy.pause(1)
    "She dashes up the stairs two at a time."
    "That's the fastest she's ever tried to get away from me. I haven't seen her this happy in a long time! Thanks Ex Zee for making this happen."
    play sound "audio/sfx/Human/Stomach Grumble.ogg"
    "My grumbling stomach derails my train of thought."
    play music "audio/music/After a Long Day (GAME VERSION).ogg" fadein 3
    "I probably should have made better use of all the free food. {w}Oh well. Let's go see what we've got."
    "I make my way into the kitchen. Uncle Kaito's laptop and papers are spread across the kitchen table but he is nowhere in sight. He probably went to the washroom."
    
    "I'm about to open the fridge when a beeping from his computer distracts me. I glance over and see a new email has come in… but as my eye wanders over the sea of Japanese text, one English email draws my attention. Even more curiously, the words {i}New York{/i} are in the preview text."
    "New York? What could Uncle Kaito possibly be doing there? I try to resist the temptation, but as I read \"A private investigation firm based out of New York\" my curiosity gets the best of me and I click open the email."
    
    "Why would Uncle Kaito order investigative work in the States? And New York specifically? I read on."
    "{i}Mr. Kaito, we have begun our preliminary investigation into the case of Mr. and Mrs. [plast]--{/i}"
    stop music fadeout 3
    "The laptop is closed shut before I can finish. I look up sharply into Kaito's serious frown."
    show kaito dis at cc with dissolve
    play music "audio/music/A Bad Feeling (GAME VERSION).ogg" fadein 5
    voice "audio/voice/E3/D7/S4/kaito/10.ogg"
    hk "I thought you knew better than to snoop through other people's things."
    
    pf "I just saw an email from an investigation firm in New York."
    voice "audio/voice/E3/D7/S4/kaito/11.ogg"
    hk "Why were you looking through my email in the first place?"
    
    "I know I'm in the wrong for snooping, but I can't let him change the subject. Not when it involves my home… my family."
    
    pf "The email was talking about Mom and Dad."
    
    "Uncle Kaito remains stoic."
    voice "audio/voice/E3/D7/S4/kaito/12.ogg"
    hk "You misread it."
    
    pf "No!"
    
    "A growing anger bubbles in my chest."
    
    pf "I don't care if you have secrets. I even understood when you tried to hide the truth about Aunt Yuki, but I will {i}not{/i} allow you to keep secrets from me when it involves my parents!"
    
    "There is no trace of a smile on Uncle Kaito's face and his dark eyes are unusually grim. I search his face, looking for a spark of my goofy, mellow uncle, but he is a mask of stony silence."
    
    pf "What do you know? What aren't you telling me?"
    
    #stop music fadeout 5
    
    show dots:
        xoffset 720
        yoffset 5
        xzoom .75
        yzoom .75
    $renpy.pause(1)
    
    "After a long pause, he finally speaks."
    voice "audio/voice/E3/D7/S4/kaito/13.ogg"
    hk "There are some things you are better off not knowing."
    
    menu:
        "Try me.":
            jump E3_5S1
            #Black screen
            #scene black with fade
            #stop ambient fadeout 3
            
    #jump E3END
    jump E3_5S1