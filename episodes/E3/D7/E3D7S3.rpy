#
label E3D7S3:
    
    scene bg nightclub with fade
    
    show kaori smi at l1:
        xoffset 75
        xzoom 0.75
        yzoom 0.75
    show mayu smi b1 at l3:
        xoffset -200
        xzoom 0.75
        yzoom 0.75
    show shou smi at l2:
        xoffset -50
        xzoom 0.75
        yzoom 0.75
    with dissolve
    
    show valerie smi at r1:
        xoffset -150
        xzoom 0.75
        yzoom 0.75
    with dissolve
    
    
    show yuuna smi at r2:
        xoffset -50
        xzoom 0.75
        yzoom 0.75
    with dissolve
    voice "audio/voice/E3/D7/S3/shou/33.ogg"
    ss "What do you guys want to do now?"
    
    # voice for this?
    show exclamation:
        xoffset 850
        yoffset 125
        xzoom .5
        yzoom .5
    show valerie sur
    "Valerie lets out a loud squeal."
    voice "audio/voice/E3/D7/S3/valerie/E3D7L22.ogg"
    vb "Look!"
    
    "She points to none other than Ex Zee... who is steadily walking towards us!"
    play music "audio/music/Bring It On! [INSTRUMENTAL].ogg" fadein 5
    $renpy.pause(.75)
    show xz smi at r3 with dissolve:
        xoffset 200
        xzoom -0.75
        yzoom 0.75
    "He's a lot taller in person, and a lot cooler. I have to admit, Nikki was right. He is more attractive in person."
    show kaori cur
    show mayu cur
    show shou cur
    show valerie cur b1
    show yuuna cur
    voice "audio/voice/E3/D7/S3/valerie/E3D7L23.ogg"
    vb "Ex Zee!"
    voice "audio/voice/E3/D7/S3/ez/1.ogg"
    ez "That would be me."
    show xz mis
    "He grins charmingly."
    voice "audio/voice/E3/D7/S3/ez/2.ogg"
    ez "I don't believe we've met. Are you new? I doubt I would have forgotten such stunning visions such as yourselves."
    show kaori neu b2
    show mayu ner b2
    with dissolve
    show shou hap
    show valerie ner b2
    with dissolve
    show yuuna ner b2
    with dissolve
    "Each girl turns a bright shade of red, including Kaori. They shoot him nervous glances of elation and awe. Even Valerie has lost her cool. {w}With all of them speechless, Ex Zee looks at Shou, who's equally smitten."
    show xz smi
    "Ex Zee grins understandingly. Of course, he must be used to this. {w}Finally, his gaze lands on me."
    pf "Oh, uh, hi. We're from ACE Academy. Dasshu is sponsoring our team."
    show xz cur
    voice "audio/voice/E3/D7/S3/ez/3.ogg"
    ez "ACE Academy? That means you guys are pilots!"
    "His face lights up and he seems genuinely impressed."
    show kaori neu b1
    show mayu neu b1
    show shou smi
    show xz neu
    "I motion to myself, Shou, Mayu, and Kaori."
    pf "We are."
    show yuuna neu b1
    "I point to Yuuna."
    pf "She's the team manager."
    show valerie neu b1
    "Then I point to Valerie."
    pf "And she's our engineer."
    show xz mis
    "Ex Zee winks and gives us a thumbs up."
    show note:
        xoffset 1500
        yoffset 5
        xzoom .5
        yzoom .5
    voice "audio/voice/E3/D7/S3/ez/4.ogg"
    ez "That's hardcore, man."
    show xz smi
    voice "audio/voice/E3/D7/S3/ez/5.ogg"
    ez "I always wanted to be a pilot. What a cool job!"
    show drop:
        xoffset 315
        yoffset 20
        xzoom .75
        yzoom .75
    show shou hap
    voice "audio/voice/E3/D7/S3/shou/34.ogg"
    ss "Umm, excuse me, Ex Zee-senpai."
    show xz mis
    "Ex Zee laughs."
    voice "audio/voice/E3/D7/S3/ez/6.ogg"
    ez "Just Ex is fine."
    show shou smi
    voice "audio/voice/E3/D7/S3/shou/35.ogg"
    ss "O-Oh, okay. Uhh, e-excuse me Ex-Senpai, do you think we can get a photo... please?"
    show valerie hap
    voice "audio/voice/E3/D7/S3/valerie/E3D7L24.ogg"
    vb "Yeah! Me too!"
    show xz smi
    "Ex Zee nods."
    show valerie smi
    voice "audio/voice/E3/D7/S3/ez/7.ogg"
    ez "Sure! Why don't we do a group photo?"
    show yuuna smi
    voice "audio/voice/E3/D7/S3/yuuna/28.ogg"
    ym "Good idea!"
    show mayu smi
    voice "audio/voice/E3/D7/S3/mayu/Mayu Day 7-18.ogg"
    ma "Count me in."
    show kaori smi
    "Kaori nods with a smile."
    #voice "audio/voice/E3/D7/S3/kaori/e3d7_Kaori_22.ogg"
    #ki "Okay."
    "Ex motions to a nearby Dasshu employee. As we get into place (each of us surreptitiously trying to stand right beside Ex Zee), the photographer comes out from behind the curtains, his camera at the ready."
    voice "audio/voice/E3/D7/S3/photo1/18.ogg"
    photo1 "Everyone say \"Zee!\""
    show kaori hap
    show mayu hap
    show shou hap
    show valerie hap
    show yuuna hap
    show xz hap
    "We say \"Zee\" in unison and have a good laugh as the photo is taken."
    show kaori smi
    show mayu smi
    show shou smi
    show valerie smi
    show yuuna smi
    show xz smi
    voice "audio/voice/E3/D7/S3/photo1/19.ogg"
    photo1 "Excellent! I'll make sure to have these emailed to you all."
    voice "audio/voice/E3/D7/S3/yuuna/29.ogg"
    ym "Thank you."
    show yuuna hap
    voice "audio/voice/E3/D7/S3/yuuna/30.ogg"
    ym "And thank you, Mr. Zee."
    show xz mis
    "Ex smiles."
    show yuuna smi
    voice "audio/voice/E3/D7/S3/ez/8.ogg"
    ez "You guys are too formal. Kick back and have some fun! We're going to be rocking out soon enough!"
    show note:
        xoffset 315
        yoffset 20
        xzoom .5
        yzoom .5
    show shou hap
    voice "audio/voice/E3/D7/S3/shou/36.ogg"
    ss "Haha, that's right!"
    show xz neu
    "A man in a suit comes over and whispers in Ex Zee's ear."
    show shou smi
    voice "audio/voice/E3/D7/S3/ez/9.ogg"
    ez "Time for warm ups and stage prep. You're coming to the show, right?"
    pf "Of course!"
    show heart:
        xoffset 850
        yoffset 125
        xzoom .5
        yzoom .5
    show valerie hap
    voice "audio/voice/E3/D7/S3/valerie/E3D7L25.ogg"
    vb "I wouldn't miss it for the world!"
    show xz hap
    voice "audio/voice/E3/D7/S3/ez/10.ogg"
    ez "Good! I'll be looking for you."
    stop music fadeout 5
    hide xz with dissolve
    "After flashing us one last thumbs up, he walks towards his manager."
    "We're all still giddy from our encounter with him."
    voice "audio/voice/E3/D7/S3/kaori/e3d7_Kaori_23.ogg"
    ki "He's nice."
    show mayu hap
    voice "audio/voice/E3/D7/S3/mayu/Mayu Day 7-19.ogg"
    ma "Yeah!"
    show valerie smi
    "Valerie sighs dreamily and Yuuna nods."
    show shou mis
    voice "audio/voice/E3/D7/S3/shou/37.ogg"
    ss "I don't know about you guys, but all this excitement has made me hungry. We can't leave this event until we've checked out the buffet!"
    show mayu smi
    "Shou eyes the majestic spread as the team murmurs their agreement."
    pf "You guys go ahead. I'll catch up to you in just a sec."
    stop music fadeout 3
    hide kaori
    hide mayu
    hide shou
    hide valerie
    hide yuuna
    with dissolve
    "I rush after Ex Zee, my promise to Nikki at the front of my mind." 
    play music "audio/music/Bright New Day (GAME VERSION).ogg" fadein 3
    pf "Excuse me, Ex Zee?"
    show xz smi at cc with dissolve
    "He turns and smiles when he sees me."
    voice "audio/voice/E3/D7/S3/ez/11.ogg"
    ez "Hey, man! What's up?"
    
    pf "I was wondering if I could get an autograph..."
    show xz hap
    voice "audio/voice/E3/D7/S3/ez/12.ogg"
    ez "Of course!"
    "He waits with an expectant smile."
    
    "Right! Pen and paper..."
    "I pat down my pockets, but come back empty handed. {w}Oh crap! Don't tell me this is happening right now."
    "There isn't anything lying around I could use either..."
    voice "audio/voice/E3/D7/S3/dass1/3.ogg"
    dass1 "Zee! We need you!"
    show xz neu
    voice "audio/voice/E3/D7/S3/ez/13.ogg"
    ez "Sure."
    show drop:
        xoffset 720
        yoffset 5
        xzoom .75
        yzoom .75
    "He scratches the back of his head. I can't believe I'm going to fail like this."
    
    pf "I'm sorry, I don't have a pen or paper on me. You're busy and I don't want to keep you. I'm sure my sister will understand."
    show xz cur
    voice "audio/voice/E3/D7/S3/ez/14.ogg"
    ez "Sister?"
    pf "Yeah, my younger sister found out I was coming here and she asked me to get a signature."
    show xz neu
    "He nods knowingly."
    voice "audio/voice/E3/D7/S3/ez/15.ogg"
    ez "In that case..."
    # switch to no necklace base
    $ xzNecklace = 0
    show xz smi
    "Ex Zee takes off his necklace and offers it to me."
    
    menu:
        "There's no way I can accept this.":
            "I shake my head."
            pf "I can't take that from you!"
            voice "audio/voice/E3/D7/S3/ez/16.ogg"
            ez "It's no big deal."
            pf "Are you sure?"
            show xz hap
            voice "audio/voice/E3/D7/S3/ez/18.ogg"
            ez "I can't let you leave empty handed. Not when your sister is depending on you!"
            "It doesn't look like he'll take no for an answer."
            pf "Thanks a lot, really."
    
        "Thanks!":
            "I open my palm and he places it inside my hand."
            pf "Thanks a lot! I know she'll love this!"
    
        "Are you sure?":
            "I blink at him."
            pf "This is way more than just a signature. Are you sure this is okay?"
            show xz hap
            voice "audio/voice/E3/D7/S3/ez/19.ogg"
            ez "Yeah, don't worry about it."
            "I accept the offering."
            pf "Thank you."
            
    show xz mis
    "He smiles warmly."
    show note:
        xoffset 720
        yoffset 5
        xzoom .75
        yzoom .75
    voice "audio/voice/E3/D7/S3/ez/20.ogg"
    ez "The things we have to do for our baby sisters, right?"
    pf "You got that right!"
    hide xz with dissolve
    stop music fadeout 3
    "He gives me another a thumbs up before disappearing with his manager."
    
    "I look over his medallion before safely pocketing it, then head back to my friends."
    play music "audio/music/Evening Out (GAME VERSION).ogg" fadein 3
    
    # Mayu confession start label?
    if mayrelatonship == 1:
        $ persistent.gpix[42][0] = 1
        $ persistent.gpix[43][0] = 1
        $ persistent.gpix[44][0] = 1
        $ persistent.gpix[45][0] = 1
        $ persistent.gpix[46][0] = 1
        show cg mayu letter 1 with Dissolve(1):
            xzoom 0.5
            yzoom 0.5
        "Before I make it back to the group, I'm intercepted by Mayu."
        # exclamation maybe?
        voice "audio/voice/E3/D7/S3/mayu/Mayu Day 7-20.ogg"
        ma "W-Wait!"
        pf "Huh? Mayu? How come you aren't with the others?"
        show cg mayu letter 4 with dissolve:
            xzoom 0.5
            yzoom 0.5
        voice "audio/voice/E3/D7/S3/mayu/Mayu Day 7-21.ogg"
        ma "I… I wanted to give you something."
        pf "What is it?"
        show cg mayu letter 1 with dissolve:
            xzoom 0.5
            yzoom 0.5
        "She bites her lip and fidgets as if struggling through some inner dialogue."
        show cg mayu letter 2 with dissolve:
            xzoom 0.5
            yzoom 0.5
        "Suddenly, she thrusts an envelope into my hands."
        voice "audio/voice/E3/D7/S3/mayu/Mayu Day 7-22.ogg"
        ma "Don't read this until you get home!"
        pf "Wha--"
        show cg mayu letter 3 with dissolve:
            xzoom 0.5
            yzoom 0.5
        voice "audio/voice/E3/D7/S3/mayu/Mayu Day 7-23.ogg"
        ma "Promise you won't!"
        pf "I promise!"
        show cg mayu letter 5 with dissolve:
            xzoom 0.5
            yzoom 0.5
        "She nods. Her cheeks are tinged pink and she refuses to meet my eyes. {w}Just as abruptly as she arrived, she rushes back to the group."
        hide cg mayu letter 5 with dissolve
        "I flip over the nondescript envelope, wondering what it could say."
    
        if MCStory == 3:
            "My heart pounds in my chest. Maybe it has something to do with yesterday."
    
        "Still, I promised her I wouldn't read it, so with great reluctance, I put the letter in my pocket and rejoin the group."
    
    #Black screen
    scene black with fade
    stop ambient fadeout 3
    
    "After eating our fill from the buffet, we continue to mingle and meet other Dasshu sponsees. Everyone we spoke to was excited to hear that Dasshu was sponsoring an ACE team and wished us luck in our matches. {w}It felt really satisfying to be the center of attention, if only for a short moment."
    "Soon, it was time the for the concert. We file into the concert hall and towards the front of the stage where flashing lights introduce Ex Zee."
    
    if valrelatonship == 1:
        "Valerie sings along with Ex Zee. Even among the noise of the crowd, her voice rings strong and I'm impressed by how well she sings. When she notices me, she pulls me close to dance. My heart pounds in tune to the music as her hips sway alluringly."
    
    elif kaorelatonship == 1:
        "Kaori bobs her head in time with the music and sings along. To my surprise, she knows all the words! And she's actually pretty good. She blushes when she realises I can hear her and stops, but there's a smile on her lips."
    
    elif yuurelatonship == 1:
        "Yuuna jumps up and down with the beat and lets her long hair flow free. She sings loudly without abandon as she dances and flashes me excited grins."
        "I blush when her chest bumps against me, but Yuuna is too absorbed in the music and energy to notice. This is the first time I've seen her completely let loose!"
    
    elif mayrelatonship == 0 and E3MAS3_MockCompleted == 1:
        "Mayu sways to the music, a broad smile on her face. She sings quietly, but as the crowd gets riled up, she can't help but feed off of the energy around her. She boldly takes my hand in hers and we both dance to the beat."

    elif mayrelatonship == 0 and E3MAS3_RealCompleted == 1:
        "Mayu sways to the music, a broad smile on her face. She sings quietly, but as the crowd gets riled up, she can't help but feed off of the energy around her. She boldly takes my hand in hers and we both dance to the beat."
        
    elif mayrelatonship == 1:
        "Mayu sways to the music, a smile on her face. Every so often I catch her glancing at me, but she hurriedly looks away. A blush spreads across her cheeks whenever I catch her staring. As she gets into the music, she relaxes and I catch her singing along."
    
    else:
        "Shou and I jump in time to the music and high five whenever a girl bumps into us."
    
    "Ex Zee is the perfect combination of entertainment and talent, and my voice soon grows hoarse from singing along. {w}At one point he even saw us and winked!"
    stop music fadeout 2
    "Once the concert is over, we chat animatedly about how awesome it was before heading our separate ways and going home."
    
    jump E3D7S4
    
