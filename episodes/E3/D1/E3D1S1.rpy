#
label E3D1S1:
    
    play music "audio/music/Open Road (GAME VERSION).ogg" fadein 3
    scene bg travel openroad day with Dissolve(1.5)
    "Time passes in a blur, and suddenly it's been a month since Nikki and I moved to Isokaze and I started at ACE Academy."
    "My team and I are stronger than ever and our winning streak has not been broken. Kaori, Shou, Mayu and I spent many evenings practicing in the hangar, learning how to anticipate each other's needs on the field."
    scene bg campus main day with fade
    "Yuuna continues to manage our sponsorship from Dasshu, and she's become more comfortable with the team. {w}Valerie works hard behind the scenes to continually update our GEARs, and after all the tweaks she had given Eagle, I'm more confident than ever in my mech's abilities."
    
    # Dishu addition 2/25/2016
    "I've had a surprising number of companies reach out to me to partner and research my core, but I've declined each invitation. I don't feel comfortable having strangers poke and prod at my dad's legacy, especially when I don't understand what's going on myself." 
    
    #call SocialLink_Check
    
    if E2YMS4_Completed == 1:
        $ highSocialLink = "Yuuna"
        $ yuuOut = "sTennis"
        $ yuuHairF = "pony"
        $ yuuHairB = "pony"
        scene bg campus gym day with fade
        show yuuna hap at cc with dissolve
        "Aside from team stuff, Yuuna and I partner up to play tennis on a regular basis, but it wasn't until last week when I {i}finally{/i} won a match against her!"
        if MCStory != 1:
            "Although, I think she might have let me win..."
    
    elif E2KIS4_Completed == 1:
        $ highSocialLink = "Kaori"
        scene bg campus cafe day with fade
        show kaori smi at cc with dissolve
        "Aside from team stuff, Kaori and I will occasionally meet up for lunch, in which she berates my food choices and offers me healthy alternative recipes. I pass those on to Nikki who already loves Kaori even though they haven't met."
    
    elif E2VBS4_Completed == 1:
        $ highSocialLink = "Valerie"
        scene bg campus hangar day with fade
        show valerie hap at cc with dissolve
        "Aside from updating my GEAR, Valerie has spent a majority of her free time investigating my core--under supervision. She hasn't touched anything she shouldn't… I think."
        if MCStory == 3:
            "I'm a little surprised by her focus--when she puts her mind to something she will stop at nothing to get results."
    
    elif E2MAS4_Completed == 1:
        $ highSocialLink = "Mayu"
        scene bg campus library day with fade
        show mayu hap at cc with dissolve
        "Aside from team stuff, Mayu and I have doubled up to create our band. She's no longer afraid to play her music in front of me, and we practice different music genres and experiment with styles."
        if MCStory == 2 and E2D5MA_MayuScene == 1:
            "Because of our shared love of books, she's recommend a few novels to me too. They're actually pretty good."
    
    elif E2SSS4_Completed == 1:
        $ highSocialLink = "Shou"
        $ shoOut = "sCasual"
        scene bg campus dorm day with fade
        show shou hap at cc with dissolve
        "Aside from team stuff, Shou and I have hung out at his dorm so often that I've become an honorary roommate. Although I've always been Shou's broseph, his roommates have started to call me their \"broseph\" too."
        
    scene bg homekaito main night with fade
    "On the homefront, Uncle Kaito is still as busy as ever now that his newly opened cafe has become insanely popular. {w}Nikki spends most of her time at her school's cooking club, which has gained a lot of traction among the students."
    
    stop music fadeout 5
    "Sadly, that means I've had to fend for myself when it comes to food…"
    
    
    $ kaoHairF = "default"
    $ kaoHairB = kaoHairF
    $ kaoOut = "sUniform"
    
    $ mayHairF = "default"
    $ mayHairB = mayHairF
    $ mayOut = "sUniform"
    
    $ nikHairF = "default"
    $ nikHairB = nikHairF
    $ nikOut = "sUniform"
    
    $ shoHairF = "default"
    $ shoHairB = shoHairF
    $ shoOut = "sUniform"
    
    $ valHairF = "default"
    $ valHairB = valHairF
    $ valOut = "sUniform"
    
    $ yuuHairF = "default"
    $ yuuHairB = yuuHairF
    $ yuuOut = "sUniform"
    
    $ day = 1
    $ timeSpent = "none"
    
    
    #blackscreen
    scene black with fade
    $renpy.pause(1)
    play ambient "audio/ambience/Morning.ogg" fadein 1
    $renpy.pause(1.5)
    play sound [ "audio/sfx/Technology/Phone Alarm.ogg", "audio/sfx/Technology/Phone Alarm.ogg", "audio/sfx/Technology/Phone Alarm.ogg" ]
    $renpy.pause(1)
    scene bg homekaito myroom day with fade
    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 1
    stop sound fadeout 1
    
    "I wake up at the sound of my alarm, then begin my morning routine."
    scene bg homekaito main day with fade
    
    "When I enter the kitchen, I make myself a bowl of cereal. Nikki's already left for school. {w}Lately, she's been leaving early almost every day. It barely phases me anymore… especially after I found cereal in the grocery store. The most expensive box of Tiger Flakes I've ever bought…"
    
    stop ambient fadeout 3
    scene black with fade
    "Finishing up breakfast, I hop on my bike and head to school."
    scene bg campus auditorium day with fade
    play ambient "audio/ambience/Ace Academy Library.ogg" fadein 3
    show valerie smi at cc with dissolve
    "Valerie is already waiting for me and waves me over as soon as I enter the classroom."
    voice "audio/voice/E3/D1/S1/valerie/E3D1L1.ogg"
    vb "I have news for you!"
    pf "Good news or bad news?"
    show valerie hap at cc
    "She pauses, then grins playfully."
    voice "audio/voice/E3/D1/S1/valerie/E3D1L2.ogg"
    vb "Come with me to the Hangar after class and I'll show you."
    pf "The Hangar? So it's something to do with my core?"
    show valerie neu at cc
    voice "audio/voice/E3/D1/S1/valerie/E3D1L3.ogg"
    vb "What else would it be about?"
    
    menu:
        "You do spend a lot of time there.":
            pf "Good point. You spend so much time at the Hangar sometimes I wonder if that's where you sleep."
            show valerie thi at cc
            voice "audio/voice/E3/D1/S1/valerie/E3D1L4.ogg"
            vb "I'm not sure \"sleep\" is the term I'd use."
            pf "Uh..."
            show valerie hap at cc
            voice "audio/voice/E3/D1/S1/valerie/E3D1L5.ogg"
            vb "More like an \"extended rest\"."
            "She smiles sweetly."
            pf "Right…"
    
        "Take your pick!":
            pf "My powerful thrusters, strong and sturdy exterior, or lightning quick agility to name a few."
            show valerie mis at cc
            voice "audio/voice/E3/D1/S1/valerie/E3D1L6.ogg"
            vb "If you're so \"lightning quick\" how come EAGLE gets so beat up during matches?"
    
            if E2D5S4_Victory == 0:
                "I think about what Eagle looks like before our sponsors fix it up."
                pf "So about my core…"
                show valerie hap at cc
                "Valerie just laughs."
            
            else:
                pf "I don't know which matches you've been watching, but clearly they aren't mine."
                show valerie smi at cc
                voice "audio/voice/E3/D1/S1/valerie/E3D1L7.ogg"
                vb "Pretty sure they are."
                pf "Then you have a strange definition of \"so beat up\" considering the most Eagle ever gets is a few scratches on his armour."
                show valerie mis at cc
                "Valerie smirks."
                voice "audio/voice/E3/D1/S1/valerie/E3D1L8.ogg"
                vb "I've seen some dents in there too."
                pf "Sure, from blocking!"
                show valerie hap at cc
                voice "audio/voice/E3/D1/S1/valerie/E3D1L9.ogg"
                vb "Mmhm."
    
        "Nothing.":
            "I shrug."
            pf "With the amount of time you've spent researching my core, nothing, I guess."
            show valerie hap at cc
            voice "audio/voice/E3/D1/S1/valerie/E3D1L10.ogg"
            vb "Don't worry, I'm taking good care of it."
            pf "I should hope so."
            
    show valerie neu at cc
    "Valerie waits expectantly."
    voice "audio/voice/E3/D1/S1/valerie/E3D1L11.ogg"
    vb "Sooooo?"
    pf "So what?"
    show valerie smi at cc
    voice "audio/voice/E3/D1/S1/valerie/E3D1L12.ogg"
    vb "You haven't said \"yes\" yet. Will you come with me to the Hangar?"
    pf "Yeah, I'll go with you."
    show note:
        xoffset 720
        yoffset 125
        xzoom .75
        yzoom .75
    show valerie mis at cc
    voice "audio/voice/E3/D1/S1/valerie/E3D1L13.ogg"
    vb "Good! I was starting to think maybe you didn't want to be alone with me."
    hide valerie with dissolve
    "Before I can respond, the professor raises her voice over the chatter."
    show professorF extra at cc with dissolve
    voice "audio/voice/E3/D1/S1/prof3f/1.ogg"
    prof3f "Good morning, everyone! In today's lesson we will cover…"
    
    stop ambient fadeout 2.0
    stop music fadeout 5
    #fade black
    scene black with fade
    $renpy.pause(1)
    scene bg campus auditorium day with fade
    show professorF extra at cc with dissolve
    voice "audio/voice/E3/D1/S1/prof3f/2.ogg"
    prof3f "That's all for today. Have a great rest of your day!"
    hide professorF with dissolve
    play sound "audio/sfx/Human/Class End.ogg" fadein 1
    $renpy.pause(1)
    "Just as I've finished packing up my things, Valerie grabs my hand and pulls me towards the door."
    show valerie smi at cc with dissolve
    voice "audio/voice/E3/D1/S1/valerie/E3D1L14.ogg"
    vb "Let's go!"
    pf "Sure, just give me a min--"
    stop ambient fadeout 5
    hide valerie with dissolve
    "But she's already started walking with me in tow. I hastily grab my bag."
    pf "Or we can go now."
    
    scene black with fade
    stop music fadeout 3
    $renpy.pause(1)
    play ambient "audio/ambience/Hangar.ogg" fadein 3
    scene bg campus hangar day with fade
    play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 5
    "We cut across campus and enter the Hangar through the main entrance instead of the Pilot's Lounge. {w}Inside the Hangar, Valerie rushes straight to Eagle's terminal, shooting impatient glances at me as I follow behind."
    play sound "audio/sfx/Technology/Phone Projection.ogg"
    "She sets herself in front of my terminal, and after typing in a sequence, she proudly points at the screen."
    show valerie smi at cc with dissolve
    voice "audio/voice/E3/D1/S1/valerie/E3D1L15.ogg"
    vb "Check it out!"
    
    menu:
        "Cool, numbers!":
            "I glance at the screen and see a continuous string of numbers. Valerie is trying to hold back a smile, waiting for my reaction. I'm not sure what I'm looking at but I don't want to disappoint her."
            pf "This is really cool!"
            show valerie hap at cc
            voice "audio/voice/E3/D1/S1/valerie/E3D1L16.ogg"
            vb "I know! It took me forever to find it but I think this is the big breakthrough we've been waiting for."
            pf "Really? What does it say?"
            show exclamation:
                xoffset 720
                yoffset 125
                xzoom .75
                yzoom .75
            show valerie cur at cc with dissolve
            $renpy.pause(.5)
            show valerie neu at cc with dissolve
            "She pauses, then smiles coyly."
            show valerie mis at cc
            voice "audio/voice/E3/D1/S1/valerie/E3D1L17.ogg"
            vb "You have no idea what this code is, do you?"
            pf "No... That last question gave me away, didn't it?"
            show valerie smi at cc
            voice "audio/voice/E3/D1/S1/valerie/E3D1L18.ogg"
            vb "Yup."
    
        "I'd rather be checking you out.":
            "My gaze slides across the continuous string of numbers on the terminal to rest on Valerie. I drink in the curve of her waist and how her skirt accentuates the outline of her hips. {w}She's holding back a smile, which she releases when she notices my stare."
            show regBlush:
                xoffset 720
                yoffset 125
                xzoom .75
                yzoom .75
            show valerie hap b1 at cc with dissolve
            voice "audio/voice/E3/D1/S1/valerie/E3D1L19.ogg"
            vb "Although I'm relieved I can hold your attention better than this terminal can, you might want to hold that thought and focus on the screen."
            pf "Mm, no, I'm happy with my choice."
            show valerie mis b1 at cc
            voice "audio/voice/E3/D1/S1/valerie/E3D1L20.ogg"
            vb "Then let me fix that."
            "Valerie stands behind the monitor and laughs at my disappointment. {w}With a sigh, I refocus my attention to the screen."
            show valerie smi at cc with dissolve
            pf "Okay, so what are these numbers?"
    
        "Stare silently.":
            "I stare at the continuous string of numbers on the screen. After a moment, Valerie waves her hand in my face."
            show question:
                xoffset 720
                yoffset 125
                xzoom .75
                yzoom .75
            show valerie cur at cc
            voice "audio/voice/E3/D1/S1/valerie/E3D1L21.ogg"
            vb "Hello? Anybody there?"
            "I snap back to reality."
            pf "What are you doing?"
            show valerie neu at cc
            voice "audio/voice/E3/D1/S1/valerie/E3D1L22.ogg"
            vb "Just making sure you're still there. You spaced out on me."
            pf "No, I was checking out the numbers."
            show valerie hap at cc
            voice "audio/voice/E3/D1/S1/valerie/E3D1L23.ogg"
            vb "Pretty cool, right?"
            pf "It might be if I knew what it was."
    
    show valerie thi at cc
    voice "audio/voice/E3/D1/S1/valerie/E3D1L24.ogg"
    vb "Well, you know how all the system scans we've been doing haven't shown anything new?"
    pf "Yeah."
    show valerie neu at cc
    voice "audio/voice/E3/D1/S1/valerie/E3D1L25.ogg"
    vb "Our approach was the mistake! I was thinking... if I wanted to leave a secret message on a system, I would embed it into existing code and spoof the service identity so that it would remain inconspicuous during scans."
    
    if MCStory == 2:
        pf "That makes sense."
    
    else:
        pf "What."
        
    show valerie smi at cc
    voice "audio/voice/E3/D1/S1/valerie/E3D1L26.ogg"
    vb "Well, I was doing a manual evaluation through listed services during the last week and noticed a discrepancy here. When I tried to execute it, it came back with this screen."
    
    "Her voice grows with excitement."
    show valerie smi at cc
    voice "audio/voice/E3/D1/S1/valerie/E3D1L27.ogg"
    vb "I'm positive there's something behind this code!"
    pf "Really? Then let's find out what that is!"
    show valerie hap at cc
    voice "audio/voice/E3/D1/S1/valerie/E3D1L28.ogg"
    vb "I was hoping you'd say that! Tell me how to decrypt it and we'll find out in a second."
    pf "Uh, what makes you think I know how to do that?"
    show valerie cur at cc
    "She raises an eyebrow."
    
    if MCStory == 2:
        show drop:
            xoffset 720
            yoffset 125
            xzoom .75
            yzoom .75
        show valerie ske at cc
        voice "audio/voice/E3/D1/S1/valerie/E3D1L29.ogg"
        vb "Doesn't any of this look familiar?"
        "I squint at the screen and scroll through the code."
        pf "No. Although Dad and I worked together to build Eagle, he didn't let me touch the programming for the core..."
        show valerie neu at cc
        pf "Would you be able to hack it?"
    
    else:
        pf "I wouldn't even know where to begin. {w}Would you be able to hack it?"
        
    show valerie thi at cc
    show dots:
        xoffset 720
        yoffset 125
        xzoom .75
        yzoom .75
    "Valerie bites her lip as she thinks."
    voice "audio/voice/E3/D1/S1/valerie/E3D1L30.ogg"
    vb "Mm, yeah, but it might take a few days."
    pf "That's probably still faster than it would take me to figure it out."
    show valerie smi at cc
    "She grins."
    voice "audio/voice/E3/D1/S1/valerie/E3D1L31.ogg"
    vb "I won't argue with that. Okay, I'll do it."
    show heart:
        xoffset 720
        yoffset 125
        xzoom .75
        yzoom .75
    show valerie mis at cc
    voice "audio/voice/E3/D1/S1/valerie/E3D1L32.ogg"
    vb "But only because you're cute."
    hide valerie with dissolve
    "She winks at me then turns towards the terminal."
    pf "Thanks?"
    "Already engrossed in the code, Valerie gives me a short wave of dismissal."
    
    stop ambient fadeout 3
    scene black with fade
    stop music fadeout 3
    $renpy.pause(1)
    play ambient "audio/ambience/Pilot Lounge.ogg" fadein 3
    scene bg campus lounge day with fade
    
    play sound "audio/sfx/Technology/Payment Beep Success.ogg"
    "As I find my way out of the Hanger, my phone dings with an email from the school administration. I scan through the contents."
    
    "Huh. Due to the disqualification of team StrikeX, my team will now face Onna-Bugeisha in this week's match. {w}I wonder what StrikeX did to get themselves disqualified."
    "..."
    play sound "audio/sfx/Technology/Phone Vibration Once.ogg"
    "My phone vibrates with a group chat from Shou."
    "S: {i}You guys get that email?{/i}"
    "I type out my response."
    "Me: {i}Yeah… wonder what StrikeX did...{/i}"
    "S: {i}Probably lied about something important. That's one reason why I left.{/i}"
    "Wait… StrikeX was Shou and Kaori's old team?"
    
    if MCStory == 3:
        "I consider asking Shou to talk more about what happened with him and StrikeX but decide against it. I'm still curious, but this isn't the time to go into it."
        play sound "audio/sfx/Technology/Phone Vibration Once.ogg"
        "While I was thinking, a text from Mayu comes in."
        
    else:
        play sound "audio/sfx/Technology/Phone Vibration Once.ogg"
        "As I'm typing out a question for Shou about what happened with him and StrikeX, a text from Mayu comes in."
    
    "M: {i}Looks like we'll go against Onna-Bugeisha instead.{/i}"
    "Onna-Bugeisha does sound familiar, but I can't recall which team they are…"
    "Me: {i}Who are they again?{/i}"
    "K: {i}A TEAM WE MUST DEMOLISH{/i}"
    "Of course Kaori would write in all caps."
    "S: {i}Whoa that's even more aggressive than usual{/i}"
    "K: {i}Shut up Shou!!{/i}"
    "M: {i}Please don't be upset Kaori…{/i}"
    "K: {i}I'm fine.{/i}"
    "While the texts come in, I wrack my brain trying to recall how I know that name…"
    "Oh right!"
    "Me: {i}Nvm, they're that all girls team right?{/i}"
    "S: {i}Yeah{/i}"
    "M: {i}They're supposed to be pretty good.{/i}"
    "K: {i}Who cares! I won't let them beat us!{/i}"
    stop music fadeout 5
    "The texts cease after that. {w}Probably for the best."
    
    stop ambient fadeout 3
    scene black with fade
    $renpy.pause(1)
    play ambient "audio/ambience/Campus.ogg" fadein 3
    scene bg campus main day with fade
    
    "What do I feel like doing now?"
    
    #Afternoon choice NO VALERIE
    $ freeTime = "afternoon"
    call E3FreeTime from _call_E3FreeTime_2
    
    jump E3D1S2

