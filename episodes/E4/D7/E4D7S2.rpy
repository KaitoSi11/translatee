#
label E4D7S2:
    
    scene bg campus cafe night with fade
    "Nikki and I sit with Ken as we wait for his brother to arrive. Nikki fusses over Ken and he lets her. As I watch the two of them, I pay close attention to Ken. He's calm, respectful, and polite… but most importantly, he makes Nikki smile."
     
    menu:
        "Let Ken know you approve.":
            stop music fadeout 3
            pf "Hey Ken, can I talk to you for a second?"
            show ken cur at cc with dissolve
            "He looks up at me with wide eyes--the very same expression that he wore the first time I met him."
            voice "audio/voice/E4/Ken/E4/D7/14.ogg"
            ky "S-Sure."
            show ken neu
            play music "audio/music/After a Long Day (GAME VERSION).ogg" fadein 5
            "Amused, I lead him to a quiet area behind the shelves."
            pf "I'm trusting you to take care of her."
            show dots:
                xoffset 720
                yoffset 100
                xzoom .75
                yzoom .75
            $renpy.pause(2.5)
            show ken sur b2 with dissolve
            "He blinks blankly before his eyes open wide again. As his face goes pink, he bows at a perfect 90 degree angle."
            voice "audio/voice/E4/Ken/E4/D7/15.ogg"
            ky "Of course! Thank you for your trust."
            pf "...You don't have to bow."
            show ken cur b1
            "He returns to an upright position."
            voice "audio/voice/E4/Ken/E4/D7/16.ogg"
            ky "Sorry."
            pf "Don't apologise."
            show ken ner
            voice "audio/voice/E4/Ken/E4/D7/17.ogg"
            ky "...Sorry--"
            "I glare at him and he shuts up. {w}Heh, this is kind of fun. I think I may actually enjoy this turn of events!"
            pf "Okay, let's go back."
            hide ken with dissolve
            "Nikki bombards us with questions as we return."
            show nikki ske at l2
            show ken neu at r2:
                xzoom -1
            with dissolve
            
            voice "audio/voice/E4/Nikki/Day 6/Nikki_04_627.ogg"
            sf "What was that all about? Why wasn't I invited? Why did Ken bow?"
            pf "Yeah, Ken, why did you bow?"
            "I grin devilishly at him, daring him to answer."
            show ken wor
            voice "audio/voice/E4/Ken/E4/D7/18.ogg"
            ky "O-Oh! It's... uhhh… b-because...he's..."
            show ken thi
            voice "audio/voice/E4/Ken/E4/D7/18_01.ogg"            
            ky "...My senpai?"
            show dots:
                xoffset 365
                yoffset 160
                xzoom .75
                yzoom .75
            "Nikki stares at him blankly, then shifts her attention to me."
            voice "audio/voice/E4/Nikki/Day 6/Nikki_04_628.ogg"
            sf "What did you do?"
            pf "Nothing at all. {w}Isn't that right, Ken?"
            show note:
                xoffset 1040
                yoffset 100
                xzoom .75
                yzoom .75
            show ken smi
            voice "audio/voice/E4/Ken/E4/D7/19.ogg"
            ky "Of course!"
            show nikki thi
            "Nikki pouts, but I can see the trace of a smile. I guess she's glad we're finally getting along."
            hide nikki
            hide ken
            with dissolve
            "A few minutes later, Ken's brother shows up. He convinces Ken to go to the hospital and thanks us for our help. With Ken safe, we head home."
        
        "I'm not convinced.":
            "Just because Ken has top grades, an impeccable work ethic and sense of responsibility, and more discipline than guys my age, doesn't mean he's right for Nikki." 
            "He'll have to do more than that to impress me."
            "We wait a little while until Ken's brother shows up. He convinces Ken to go to the hospital and thanks us for our help. With Ken safe, we head home."
            
    stop music fadeout 3
    play ambient "audio/ambience/Night Crickets.ogg" fadein 3
    scene black with fade
    scene bg homekaito main night with fade
    show nikki dis at cc with dissolve
    "Nikki lets out a huge breath when we step into the living room. Her face is unusually serious. She hangs her head and stares at her feet."
    voice "audio/voice/E4/Nikki/Day 6/Nikki_04_630.ogg"
    sf "I'm so sorry."
    pf "Why?"
    show nikki sad
    voice "audio/voice/E4/Nikki/Day 6/Nikki_04_631.ogg"
    sf "If I hadn't gone to visit Ken I wouldn't have lost track of time and stayed out so late and then I wouldn't have gotten into this mess and made everyone worry--"
    pf "Nikki, what happened wasn't your fault."
    show nikki wor
    "She glances up at me."
    voice "audio/voice/E4/Nikki/Day 6/Nikki_04_632.ogg"
    sf "But if I--"
    pf "No. None of this is your fault."
    show nikki dis
    pf "What happened is the fault of those guys, and if I ever find out who they are I'm going to finish what Ken started."
    show nikki neu
    "Nikki smiles weakly and nods."
    show nikki neu
    voice "audio/voice/E4/Nikki/Day 6/Nikki_04_633.ogg"
    sf "I think I'll go take a shower."
    pf "Sure."
    hide nikki with dissolve
    stop music fadeout 5
    "As soon as Nikki goes upstairs, Kaito pops his head out of the kitchen."
    show kaito neu at cc with dissolve
    voice "audio/voice/E4/Kaito/d07/(2).ogg"
    hk "Is Nikki gone?"
    pf "Yeah."
    "He pauses and gives me another look."
    show kaito ske
    voice "audio/voice/E4/Kaito/d07/(3).ogg"
    hk "Did something happen?"
    "I debate telling Kaito about the incident, but I don't want him to needlessly worry. He looks like he has something else on his mind."
    pf "It's fine. What's up?"
    show kaito neu
    play music "audio/music/Stress (GAME VERSION).ogg" fadein 5
    voice "audio/voice/E4/Kaito/d07/(4).ogg"
    hk "I heard back from the PI."
    pf "What did he say?"
    voice "audio/voice/E4/Kaito/d07/(5).ogg"
    hk "Ezra Wilson."
    pf "The drunk driver?"
    voice "audio/voice/E4/Kaito/d07/(6).ogg"
    hk "Yeah… What do you really know about him?"
    pf "He and Dad used to work together at Midori Energy. They were on every project together and he used to come to the house all the time while we were growing up. I thought he and Dad were friends..." 
    "My voice trails off."
    "His blood alcohol was far over the legal limit. It's not like the cops could ask him about it due to his coma, nor was there any evidence which indicated this was more than a cut and dry drunk driving accident. There was no incentive to investigate further so that was all that was listed in the report."
    show kaito thi
    voice "audio/voice/E4/Kaito/d07/(7).ogg"
    hk "Well, it turns out Ezra was stalking your father."
    "I frown. That doesn't make sense. They saw each other every day at work."
    pf "Why?"
    show kaito neu
    voice "audio/voice/E4/Kaito/d07/(8).ogg"
    hk "The PI read about a huge fire at Midori Energy the week before your parents' accident. He spoke to a few people and found out that the fire destroyed important documents which contained all the research for Midori's latest project."
    "I wrack my brain."
    pf "I think I might remember hearing something about that fire..."
    voice "audio/voice/E4/Kaito/d07/(9).ogg"
    hk "The documents which were destroyed was your father's and Ezra's research."
    "Dad's research? I try to recall Dad right before the accident. He seemed a little more worried than usual, but otherwise didn't give any indication that something was amiss. {w}Shouldn't he have been devastated by something like losing years of research?"
    "Was he trying to protect me or was something else going on…?"
    show kaito ner
    voice "audio/voice/E4/Kaito/d07/(10).ogg"
    hk "Ezra didn't take the loss well. Right after the fire, Ezra accused your father of purposely sabotaging him by setting their research on fire."
    pf "Dad wouldn't do that! It was his research too!"
    voice "audio/voice/E4/Kaito/d07/(11).ogg"
    hk "Right. It didn't make sense. Nobody believed him and they chalked up his breakdown to stress."
    show kaito neu
    voice "audio/voice/E4/Kaito/d07/(12).ogg"
    hk "But he wouldn't let it go."
    voice "audio/voice/E4/Kaito/d07/(13).ogg"
    hk "He accosted your father many times at work demanding answers. It got so bad that he was assigned a leave of absence by the company."
    voice "audio/voice/E4/Kaito/d07/(14).ogg"
    hk "On the day of the accident, your parents had lunch at a cafe. Nikki called them asking for a ride."
    pf "Yeah, I remember."
    voice "audio/voice/E4/Kaito/d07/(15).ogg"
    hk "The PI asked the waitstaff if they remembered seeing your parents there and they did… Ezra too." 
    pf "He was there?"
    show kaito ner
    voice "audio/voice/E4/Kaito/d07/(16).ogg"
    hk "Yeah. He'd followed them there and was already clearly intoxicated. He demanded that they pay him all the money he would have made upon completion of the project. He said your father owed him."
    voice "audio/voice/E4/Kaito/d07/(17).ogg"
    hk "Obviously, your father refused and continually maintained his innocence. Ezra became so disruptive the manager had to forcibly remove him from the cafe. Your parents seemed shaken but tried to finish their meals as if nothing happened."
    show kaito neu
    voice "audio/voice/E4/Kaito/d07/(18).ogg"
    hk "That's when they received the call from Nikki."
    pf "And I guess Ezra tried to tail them but ended up running them off the road…"
    "Kaito nods, looking more grim than ever."
    "Something doesn't add up. What research is important enough to kill over? And if Ezra was driven to madness after losing his life's work, why was Dad barely affected?"
    "Then there's the convenient timing of Akira's copycat core…"
    "How much time has passed since the accident? {w}Since the fire? {w}Enough for the company to piece together just enough of the research to turn a profit."
    pf "Uncle Kaito."
    "He looks at me."
    pf "I think the research that killed Dad has to do with my core."
    show kaito ner
    "He hesitates, then nods slowly."
    voice "audio/voice/E4/Kaito/d07/(19).ogg"
    hk "You might be right."
    "Wasn't there an encrypted piece that Valerie wasn't able to unlock? Maybe that can help make sense of all of this. I need to take another look at it."
    pf "I need to go look at my core."
    "Uncle Kaito doesn't try to stop me."
    show kaito neu
    voice "audio/voice/E4/Kaito/d07/(1).ogg"
    hk "You do what you need to do. Just be safe."
    pf "Thanks, Uncle Kaito."
    stop music fadeout 3
    scene black with fade
    stop ambient fadeout 5
    "For the second time today, I race to the garage and hop back on my bike. Then I drive to ACE."
    $renpy.pause(1)
    play ambient "audio/ambience/Hangar.ogg" fadein 3
    scene bg campus hangar day with fade
    "The campus feels even more empty than usual. Even though it's after hours, I have no trouble swiping into the Hangar. All is quiet except for the sound of my footsteps."
    #play sound "audio/sfx/GEAR/GEAR Cockpit Open.ogg"
    #scene cg GEAR cockpit first1 with fade
    #$renpy.pause(1)
    #stop ambient fadeout 5
    #play sound2 "audio/sfx/GEAR/GEAR Cockpit Close.ogg"
    "I cannot get to Eagle fast enough. As soon as I do, I plop down at the terminal and boot up the computer."
    #play sound "audio/sfx/GEAR/GEAR Boot Up 1.ogg"
    #play ambient "audio/ambience/GEAR Cockpit.ogg" fadein 5
    #scene bg GEAR cockpit first2 with fade
    "I follow the instructions Valerie left for me and I'm greeted by the password prompting screen she showed me earlier. She said there was a hint here. Let's see what it says..."
    "The screen is a scrambled mess of words with no rhyme or reason to them. I read through a couple of times, making sure my eyes don't skip any words."
    "Most of these words mean nothing to me, but a select few stand out."
    "{i}Cricket… Moo… Sir Hopsalot…{/i}"
    "Those were childhood nicknames Dad gave me. Each one of them has a story, but none of them were very long lived."
    "The ultimate nickname that stuck with me for an embarrassingly long time was \"Meatball\", because when I was born my cheeks were big and round like meatballs. {w}Dad's favourite story to tell was the time I started school."
    "The teacher called \"[pfirst]\" for roll call and I stayed silent so she marked me absent. After she'd gone through the list of names, I said she didn't call mine. She asked if my name was [pfirst] and I responded with \"no, my name is Meatball\"."
    "I'd been called Meatball at home for so long that I didn't even know my real name!"
    "That must be the answer. {w}I apprehensively type in \"Meatball\" into the password prompt. My finger hovers over the enter key before pressing it."
    play music "audio/music/Slow Day (GAME VERSION).ogg" fadein 5
    stop ambient fadeout 5
    $ dfirst = "James"
    $ dfull = "[dfirst] [plast]"
    $ dad = DynamicCharacter("dfull", color="#FFD640")
    "The prompt disappears and a video pops up on the screen. My breath catches in my throat as Dad looks straight into the camera. There are dark circles under his eyes and worry lines around his mouth. His hair sticks up at odd angles and his clothes are smudged with dirt and oil."
    "He notices the recording light is on and tries to fix himself up a bit before giving me a weak smile."
    
    voice "audio/voice/E4/Dad/D7/(2).ogg"
    dad "The fact that you are watching this now means something must have gone wrong."
    "He sighs, and his voice grows thick."
    voice "audio/voice/E4/Dad/D7/(3).ogg"
    dad "I'm sorry."
    "I try to swallow the lump in my throat and ignore the sting of tears in my eyes. This isn't the dad I remember. The dad I remember had a booming laugh which took up the room. He was sure of himself and never had regrets."
    voice "audio/voice/E4/Dad/D7/(4).ogg"
    dad "By putting this technology in Eagle, I have potentially endangered you… but I… I don't know where else I can keep it safe."
    voice "audio/voice/E4/Dad/D7/(5).ogg"
    dad "Midori Energy doesn't fully understand the scope of this research. They're willing to sell it to anyone without considering the consequences."
    voice "audio/voice/E4/Dad/D7/(6).ogg"
    dad "Companies which would weaponise this technology will cause irreparable damage. They could create energy explosions thirteen times the force of a nuclear bomb!"
    "He sets his jaw and lifts his gaze back towards the camera. His eyes are unusually steely and cold."
    stop music fadeout 25
    
    voice "audio/voice/E4/Dad/D7/(7).ogg"
    dad "That's why I caused the fire. I burned all copies of my research to prevent it from falling into the wrong hands… but…"
    "Dad runs his hands through his hair--a gesture he would do whenever he was stressed or worried."
    voice "audio/voice/E4/Dad/D7/(8).ogg"
    dad "...It's hard to completely destroy twenty years of research. Especially when this technology could bring so much {i}good{/i}!"
    voice "audio/voice/E4/Dad/D7/(9).ogg"
    dad "The possibilities would have been endless. This new format of energy may function similarly to existing methods, but the fundamental principles are vastly different and have far wider scalability implications."
    "A shadow of his old self returns while he talks and I catch a glimpse of a genuine smile. Dad was always a bit of a dreamer."
    "Then his face becomes grim."
    voice "audio/voice/E4/Dad/D7/(10).ogg"
    dad "And that is why this core is sitting in Eagle now."
    "His piercing gaze stares straight into my soul."
    play ambient "audio/ambience/Hangar.ogg" fadein 10
    voice "audio/voice/E4/Dad/D7/(12).ogg"
    dad "I'm sorry for getting you involved. I'm sorry I couldn't follow through with what I started."
    voice "audio/voice/E4/Dad/D7/(13).ogg"
    dad "But most of all, I'm sorry I wasn't able to tell you this in person."
    "His eyes look glassy and glitter too much beneath the light."
    voice "audio/voice/E4/Dad/D7/(14).ogg"
    dad "I probably don't say this enough, but I'm so proud of who you've grown up to be."
    voice "audio/voice/E4/Dad/D7/(15).ogg"
    dad "I know if you're watching this that I've put a heavy burden on your shoulders, but I trust you will make the right decision."
    voice "audio/voice/E4/Dad/D7/(16).ogg"
    dad "My only hope is that you can find it in your heart to forgive me."
    "Dad glances behind him. Something must have spooked him because when he faces the camera again he smiles feebly and his voice is quiet."
    voice "audio/voice/E4/Dad/D7/(17).ogg"
    dad "Take care of your sister."
    voice "audio/voice/E4/Dad/D7/(1).ogg"
    dad "Goodbye, son."
    "The video cuts off abruptly."
    
    "At first, I'm too stunned to move. The image of Dad is seared into my eyes. He was the same, yet so unfamiliar."
    "As his face slowly fades away, I'm surprised to feel wetness on my cheeks."
    "He knew. {w}He knew exactly what he was doing when he hid this technology inside of Eagle. And now I understand why I wasn't allowed to help program the core. I understand why Dad seemed almost obsessive about completing Eagle."
    "It also makes sense why I never noticed a difference between this core and any other core. Dad never matured the technology."
    "But he must have set up the overdrive configuration probably not long before he..."
    "..."
    "He set the overdrive to only happen once so I'd begin to search for answers."
    "His last words ring in my mind."
    "{i}Goodbye, son.{/i}"
    "He knew the implications of his research and entrusted it all to me through the GEAR we built together."
    show cg GEAR hangar first with Dissolve(2.0):
        xzoom 1.5
        yzoom 1.5
        yoffset -500
        linear 5.0 yoffset 0
    "I glance over at Eagle, partially obscured by shadows. The darkened blue no longer seems warm and inviting like the salty spray of the ocean, but feels dangerous and cold like a winter sky."
    "I try to bring up the video once more so I can hear his voice one more time. See his face--even though it's the not the one I want to remember. But I can't. It was a one-time initiation."
    "As I try to process the situation, I don't know what to feel."
    "I recall Dad's hollow cheeks and the shadow of pain in his eyes… of one thing I am certain--I cannot keep using the core knowing all this."
    "But what will I do about the research?"
    
    $ E4D7S2_CoreDestroyed = 0
    
    menu:
        "Destroy it all.":
            $ E4D7S2_CoreDestroyed = 1
            "I stare at Eagle and a gathering flame burns away the pain in my chest."
            "This technology has already destroyed my family. Dad would still be alive. Mom would still be alive. Nikki would be happy finishing up school with her childhood friends."
            "It's amazing how this one device could wipe all of that away in an instant."
            "I don't even want to imagine what would happen if it fell into the wrong hands…"
            scene black with fade
            stop ambient fadeout 5
            play sound "audio/sfx/GEAR/GEAR Cockpit Open.ogg"
            #Rscene cg GEAR cockpit first1 with fade
            $renpy.pause(1)
            play sound2 "audio/sfx/GEAR/GEAR Cockpit Close.ogg"
            "Crawling up the ladder beside Eagle, I open up the cockpit and key in the sequence to access my core."
            play sound "audio/sfx/GEAR/GEAR Boot Up 1.ogg"
            "The heat bubbling in my chest rises when I see it. Like a beating heart, it gives off a faint pulse of energy."
            "I open the terminal screen in my cockpit and find the source information for my core."
            "After wiping all the data, I set an impossible run instance. The low glow continues to brighten more and more. After a zapping noise, it becomes an opaque object."
            "As far as anyone would know, the core short circuited."
            stop ambient fadeout 3
            play sound "audio/sfx/GEAR/GEAR Cockpit Open.ogg"
            "After closing the core access panel and exiting the cockpit, I climb back down the ladder."
            play ambient "audio/ambience/Hangar.ogg" fadein 3
        
        "Keep it protected.":
            "Sometimes Dad thought too much about the big picture and forgot about the details. He wanted to create a better future for us and was willing to die to make his dreams a reality."
            "If only he could have seen that the future we wanted was one with him in it."
            "I don't want Dad's sacrifice to have been in vain. I want him to achieve his dream."
            play sound "audio/sfx/GEAR/GEAR Cockpit Open.ogg"
            stop ambient fadeout 5
            scene black with fade
            $renpy.pause(1)
            play sound2 "audio/sfx/GEAR/GEAR Cockpit Close.ogg"
            "I climb up the ladder beside Eagle and open the cockpit. Then I key in the sequence which unlocks the panel protecting my core."
            play sound "audio/sfx/GEAR/GEAR Boot Up 1.ogg"

            "Like a beating heart, it gives off a faint pulse of energy."
            "I open the terminal screen in my cockpit and find the source information for my core."
            "After collecting all the schematics and data into a drive, I set an impossible run instance. The low glow continues to brighten more and more. After a zapping noise, it becomes an opaque object."
            "As far as anyone would know, the core short circuited."
            play sound "audio/sfx/GEAR/GEAR Cockpit Open.ogg"
            scene black with fade
            "This technology belongs with a company who will utilise it properly. Until I know who that is, I'll keep it safe with me and not bring any more attention to it."
            play ambient "audio/ambience/Hangar.ogg" fadein 3
            "After learning all that I have, I can't keep using it as a leg-up against the competition. Eagle will use a regular core from now on."
           

          
    
    
    
    
    scene bg campus hangar day with fade
    $renpy.pause(1.0)
    "As I stand there, I suddenly feel so tired and so lost. {w}Without thinking, I pull out my phone and dial the first name that comes to mind."
    play sound "audio/sfx/Technology/Phone Dial.ogg"
    $renpy.pause(2.5)
    play sound2 "audio/sfx/Technology/Phone Answer.ogg"
    
    $renpy.pause(1.25)
    
    if valrelatonship == 1:
        jump E4D7VB
    elif yuurelatonship == 1:
        jump E4D7YM
    elif kaorelatonship == 1:
        jump E4D7KI
    elif mayrelatonship == 1:
        jump E4D7MA
    else:
        jump E4D7SS
