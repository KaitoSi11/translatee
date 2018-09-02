#
label E3D1S2:
    
    stop music fadeout 3
    stop ambient fadeout 3
    
    $renpy.pause(1)
    play ambient "audio/ambience/Pilot Lounge.ogg" fadein 3
    scene bg campus lounge day with fade
    play music "audio/music/Idle Conversation (GAME VERSION).ogg" fadein 3
    
    "I'm in the Pilot's Lounge watching the Japan vs. China GEAR playoff match. The Lounge is packed with students as this is a highly anticipated game."
    "Many shout at the TV, but I watch in silence, sipping my drink and enjoying the ambiance."
    voice "audio/voice/E3/D1/S2/akira/1.ogg"
    am "Exciting game, right?"
    show akira hap at cc with dissolve
    "I glance up in surprise, but nod. Akira grins and sits down in the seat across from me. {w}Although he seems like a nice guy, we don't talk very often so it's unusual he'd approach me. I suppose I do have a really good view of the TV, though."
    show akira neu at cc
    "A string of boos and yells fill the room as China takes out one of Japan's GEARs."
    pf "People are really getting into it this time."
    show akira thi at cc
    voice "audio/voice/E3/D1/S2/akira/2.ogg"
    am "Yeah. It was predicted that this year China was going to be a strong opponent for Japan, and it looks like that's coming true."
    pf "Is that why there's such a big turn out?"
    show akira smi at cc
    "I gesture to the crowded room. Akira nods."
    voice "audio/voice/E3/D1/S2/akira/3.ogg"
    am "This is the first year that China's even made it this far in the playoffs. Everyone's watching to see who'll come out on top."
    pf "Who do you think will win?"
    "He doesn't even hesitate."
    show akira hap at cc
    voice "audio/voice/E3/D1/S2/akira/4.ogg"
    am "Japan."
    voice "audio/voice/E3/D1/S2/akira/5.ogg"
    am "What do you think?"
    show akira smi at cc
    
    menu:
        "Japan.":
            pf "Definitely Japan. China might be catching up, but their technology hasn't reached the same innovative standards as Japan's."
            pf "Plus, this year's lineup is a completely new team so they don't have the same player advantage as Japan's seasoned team."
            show akira thi at cc
            voice "audio/voice/E3/D1/S2/akira/6.ogg"
            am "I agree."
            "He gives me a long look. I wonder what he's thinking."
    
        "China.":
            pf "I wouldn't rule out China just yet. Even though their technology isn't as advanced as Japan's, and China's a completely new team, their chaos has actually been their advantage."
            pf "They've been doing a better job reacting to their opponent."
            show akira hap at cc
            "Akira grins."
            voice "audio/voice/E3/D1/S2/akira/7.ogg"
            am "Sounds like you've got a soft spot for the underdogs."
            "I return the smile."
            pf "I wouldn't underestimate a rising team."
            show akira mis at cc
            "His eyes seem to stare deep within me."
            voice "audio/voice/E3/D1/S2/akira/8.ogg"
            am "Neither would I."
            "For a second, I wonder if we're still talking about the ongoing match…"
    
        "I don't care.":
            pf "The only team I follow is the United States, so I don't care either way."
            show akira hap at cc
            "Akira nods."
            voice "audio/voice/E3/D1/S2/akira/9.ogg"
            am "Ah, of course you'd root for your home team."
            
    show akira smi at cc
    voice "audio/voice/E3/D1/S2/akira/10.ogg"
    am "Speaking of matches, I believe congratulations are in order for you and your team."
    pf "Me? Your team is still holding the number one spot on the leaderboards."
    show akira neu at cc
    voice "audio/voice/E3/D1/S2/akira/11.ogg"
    am "Sure, but you guys are quickly catching up. You started out at rank 21 but you've already made it to rank 11."
    pf "Yeah… It's kind of weird to think about it. And we're going against an even better team this week since StrikeX got disqualified."
    show akira thi at cc
    voice "audio/voice/E3/D1/S2/akira/12.ogg"
    am "Yeah, the school is taking no chances with them."
    pf "What do you mean?"
    show akira cur at cc
    "Akira blinks."
    show question:
        xoffset 720
        yoffset 5
        xzoom .75
        yzoom .75
    voice "audio/voice/E3/D1/S2/akira/13.ogg"
    am "You didn't hear?"
    pf "No…"
    show akira ske at cc
    voice "audio/voice/E3/D1/S2/akira/14.ogg"
    am "The team lead and one of his starting pilots got into a huge fight, and they did not hold back. I mean, there were some serious injuries so both members obviously couldn't compete."
    pf "Why did they fight?"
    show akira neu at cc
    voice "audio/voice/E3/D1/S2/akira/15.ogg"
    am "The leader decided to sideline his starting pilot and his pilot didn't like that."
    pf "They're on the same team. Couldn't they just talk it out? I'm sure the leader had a reason."
    show akira thi at cc
    "Akira shrugged."
    voice "audio/voice/E3/D1/S2/akira/16.ogg"
    am "I don't know all the details, but my guess is that there probably wasn't a good reason to sideline the pilot. Either way, because the fight escalated to the degree in which ACE had to get involved, the school is currently investigating the team."
    pf "That's crazy stuff."
    show akira ner at cc
    voice "audio/voice/E3/D1/S2/akira/17.ogg"
    am "Yeah. Who are you going against now?"
    pf "Onna-Bugeisha."
    show exclamation:
        xoffset 720
        yoffset 5
        xzoom .75
        yzoom .75
    show akira sur at cc
    voice "audio/voice/E3/D1/S2/akira/18.ogg"
    am "Oh, Mei's team!"
    pf "Yeah. I hear they're strong."
    show akira smi at cc
    "Akira nods."
    voice "audio/voice/E3/D1/S2/akira/19.ogg"
    am "They are, but so are you. In fact, I'm really looking forward to my match with you."
    pf "That might still be a while considering my team's rank."
    show akira ske at cc
    voice "audio/voice/E3/D1/S2/akira/20.ogg"
    am "Right, but you guys have been on a winning streak, haven't you?"
    pf "Yeah."
    show akira smi at cc
    voice "audio/voice/E3/D1/S2/akira/21.ogg"
    am "Because of that, your match-making rating, or MMR, is actually higher than your earned rank. That tends to happen with outliers like being an undefeated team."
    "What he says makes sense. Plus, I'm not going to question {i}Akira{/i} about how being undefeated works."
    show akira mis at cc
    voice "audio/voice/E3/D1/S2/akira/22.ogg"
    am "I have a feeling that if you beat Onna-Bugeisha, it won't be long before we face each other on the field."
    
    menu:
        "Don't jinx us!":
            pf "I appreciate the confidence, but we've got to beat Onna-Bugeisha first before considering anyone else."
            show akira smi at cc
            voice "audio/voice/E3/D1/S2/akira/23.ogg"
            am "It'll be a tough match. I'm interested to see the outcome."
            "Akira is a hard person to read."
    
        "We won't go easy on you.":
            pf "Don't get too comfortable in that number one spot!"
            show akira hap at cc
            "Akira merely smiles."
    
        "It is what it is.":
            "I shrug."
            pf "One match at a time."
            show akira hap at cc
            "Akira nods."
    
    hide akira with dissolve
    "We continue to watch the game in silence. {w}After a while, Akira stands."
    show akira hap at cc with dissolve
    voice "audio/voice/E3/D1/S2/akira/24.ogg"
    am "I wish I could watch the end of this match, but I've got to head to class. I'll see you later."
    "I nod."
    hide akira with dissolve
    "After Akira leaves, I check my phone and notice a text from Shou."
    "{i}Don't forget tomorrow we'll be getting our game on at the beach! Meet there at 11{/i}"
    "As if I could forget that! {w}I shove my phone back into my pocket and watch the rest of the game."
    
    #black screen
    stop music fadeout 3
    scene black with fade
    stop ambient fadeout 3
    "In the end, Japan won with just one GEAR left standing."
    
    #fade in
    play ambient "audio/ambience/Campus.ogg" fadein 3
    scene bg campus main day with fade
    
    "I've still got some time before I head home tonight..."
    
    #Evening Choice
    $ freeTime = "evening"
    call E3FreeTime from _call_E3FreeTime
    
    jump E3D1S3

