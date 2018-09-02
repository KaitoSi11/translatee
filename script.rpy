###################################################################### ~ Characters


define pfirst = DynamicCharacter("pfirst")
define plast = DynamicCharacter("plast")
define pf = DynamicCharacter('pfull')

define sfirst = DynamicCharacter('Nikki')
define sf = DynamicCharacter('sfull')

init python:

    pfirst = "Tristan"
    plast = "Spade"
    pfull = pfirst+" "+plast
    pf = DynamicCharacter("pfull", color="#FFBF00")
    
    sfirst = "Nikki"
    sfull = sfirst+" "+plast
    sf = DynamicCharacter("sfull", color="#FFD633")

    ym = Character("Yuuna Misaki", color="#58D3F7")
    
    ki = Character("Kaori Itami", color="#FA5858")
    
    ss = Character("Shou Shinjirou", color="#01DF3A")
    
    ma = Character("Mayu Akemi", color="#00FFBF")
    
    hk = Character("Kaito Hikari", color="#FF8000")
    
    hy = Character("Yuki Hikari")
    
    am = Character("Akira Masato", color="#CCCCCC")
    
    vb = Character("Valerie Belle", color="#FFFF00")
    
    ms = Character("Mei Satomi", color="#835930")
    
    GEARpf = Character("Eagle", color="#4D94FF")
    
    mv = Character("Uncle Miguel")
    
    ky = Character("Ken \"Yen\" Kokan")
    
    acc = Character("Yuri Aliyev")
    
    don = Character("Donnie Roos")
    
    dfirst = "James"
    dfull = dfirst+" "+plast
    dad = DynamicCharacter("dfull", color="#FFD640")
    
    e = Character("Eileen")
    
    
    aks = Character("Akio Shinjirou")
    kt = Character("Ken Takeo")
    tk = Character("Tatsuo Kimura")
    gua = Character("Guard")
    an = Character("Announcer")
    eng1 = Character("Engineer")
    eng1m = Character("Male Engineer")
    fk = Character("Arcade Gosu")
    rn = Character("Tech Gosu")
    dr = Character("Driver")
    iceman = Character("Ice Cream Man")
    ez = Character("Ex Zee")
    rec1 = Character("Dorm Receptionist")
    dormf1 = Character("Female ACE Student")
    hito = Character("Hitomi")
    wait = Character("Waiter")
    oldman = Character("Old Man")
    alm = Character("Aludian Rep")
    
    rc1m = Character("Male Administrator")
    rc2f = Character("Female Receptionist")
    rc3f = Character("Female Receptionist")
    
    profm = Character("Professor - Piloting 101")
    prof1m = Character("Professor - GEAR Arsenal 201")
    prof2f = Character("Professor - GEAR History 201")
    prof3f = Character("Professor - International Bridging")
    prof4m = Character("Professor - Physical Education")
    sprof1 = Character("Club Host")
    
    mec1m = Character("Male Mechanic")
    mech1 = Character("Mechanic")
    photo1 = Character("Photographer")
    aeng = Character("Aludian Engineer")
    
    pres1m = Character("Mr. Takeda")
    
    stu1f = Character("Female Student")
    stu3f = Character("Female Student")
    stu4f = Character("Female Student")
    stu9f = Character("Female Student")
    
    stu2m = Character("Male Student")
    stu5m = Character("Male Student")
    stu6m = Character("Male Student")
    stu7m = Character("Male Student")
    stu8m = Character("Male Student")
    
    fbro1 = Character("Frat Bro")
    fbro2 = Character("Frat Bro")
    fbro3 = Character("Frat Bro")
    fbro4 = Character("Frat Bro")
    fbro5 = Character("Frat Bro")
    fbra1f = Character("Frat Bra")
    fbra2f = Character("Frat Bra")
    
    hstu1f = Character("Female High School Student")
    hstu2m = Character("Male High School Student")
    hstu3f = Character("Female High School Student")
    
    barm = Character("Male Bartender")
    
    Bully1 = Character("Goon")
    Bully2 = Character("Goon")
    
    dass1 = Character("Dasshu Coordinator")
    
    bh = Character("Bill Hang")
    tj = Character("Simone Cuwell")
    
    sl  = Character("SLASHER")
    mk  = Character("Mitsuki Oshiro")
    
    hotm1  = Character("Attractive Male 1")
    hotm2  = Character("Attractive Male 2")
    hotm3  = Character("Attractive Male 3")
    hotm4  = Character("Attractive Male 4")
    hotm4  = Character("Attractive Male 4")
    girl1 = Character("Fan Girl 1")
    girl2 = Character("Fan Girl 2")
    team1m = Character("Teammate")
    
    ip  = Character("Ivan Poddubny")
    
    flirtyg1 = Character("Attractive Female 1")
    flirtyg2 = Character("Attractive Female 2")
    
    tc = Character("Tennis Captain Ryoma Echizan")
    ei = Character("Eito Iwasa")
    
    dk = Character("Dishu Khan")
    ama = Character("AmaLee")
    recep = Character("Receptionist")
    
    cafec1 = Character("Cafe Customer 1")
    cafec2 = Character("Cafe Customer 2")
    
    hstuf1 = Character("Nikki's Bestie 1")
    
    hstuf3 = Character("Nikki's Bestie 2")
    
    hstu1f = Character("Nikki's Bestie 1")
    
    hstu3f = Character("Nikki's Bestie 2")
    
    creep = Character("\"That\" Guy")
    
    vg = Character("Vendor")
    
    GuestM = Character("Panel Audience")
    
    GuestF = Character("Panel Audience")


###################################################################### ~ Character Locations


init python:
    cc = Position(xalign = .50, yalign = .075)

    lc = Position(xalign = .40, yalign = .075)
    rc = Position(xalign = .60, yalign = .075)

    l1 = Position(xalign = .30, yalign = .075)
    l2 = Position(xalign = .15, yalign = .075)

    r1 = Position(xalign = .70, yalign = .075)
    r2 = Position(xalign = .85, yalign = .075)

    l3 = Position(xalign = .01, yalign = .075)
    r3 = Position(xalign = .99, yalign = .075)


###################################################################### ~ GEAR Locations

init python:
    br = Position(xalign = .999, yalign = .8)

    tr = Position(xalign = .700, yalign =  .001)

    mm = Position(xalign = .500, yalign = .8)

    tl = Position(xalign = .300, yalign = .001)

    bl = Position(xalign = .001, yalign = .8)

# REMEMBER TO ATL TRANSFORM "top" positions by using
#       yzoom .8



###################################################################### ~ Sprite Initialization

init python:
    
    yuuHairB = "default"
    yuuOut = "sUniform"
    yuuHairF = "default"
    yuuAccT = "emptyimage"
    yuuAccM = "emptyimage"
    yuuAccB = "emptyimage"
    
    yurGlasses = 1
    
    yukHairB = "default"
    yukOut = "coat"
    yukHairF = "default"
    yukAccT = "emptyimage"
    yukAccM = "emptyimage"
    yukAccB = "emptyimage"
    
    xzNecklace = 1
    
    valHairB = "default"
    valOut = "sUniform"
    valHairF = "default"
    valAccT = "emptyimage"
    valAccM = "emptyimage"
    valAccB = "emptyimage"
    
    shoHairB = "default"
    shoOut = "sUniform"
    shoHairF = "default"
    shoAccT = "emptyimage"
    shoAccM = "emptyimage"
    shoAccB = "emptyimage"
    
    nikHairB = "default"
    nikOut = "sCasual"
    nikHairF = "default"
    nikAccT = "emptyimage"
    nikAccM = "emptyimage"
    nikAccB = "emptyimage"
    
    migGlasses = 1
    
    meiHairB = "default"
    meiOut = "sUniform"
    meiHairF = "default"
    meiAccT = "emptyimage"
    meiAccM = "emptyimage"
    meiAccB = "emptyimage"
    
    mayHairB = "default"
    mayOut = "sUniform"
    mayHairF = "default"
    mayAccT = "emptyimage"
    mayAccM = "emptyimage"
    mayAccB = "emptyimage"
    
    kenDirt = 0
    kenOut = "default"
    
    kaoHairB = "default"
    kaoOut = "sUniform"
    kaoHairF = "default"
    kaoAccT = "emptyimage"
    kaoAccM = "emptyimage"
    kaoAccB = "emptyimage"
    
    kaiHairB = "default"
    kaiOut = "sWork"
    kaiHairF = "default"
    kaiAccT = "emptyimage"
    kaiAccM = "emptyimage"
    kaiAccB = "emptyimage"
    
    ivaHelmet = 1
    ivaOut = "default"
    
    donTie = 1
    donScanner = 0
    
    boyOut = "default"
    
    akiHairB = "default"
    akiOut = "sUniform"
    akiHairF = "default"
    akiAccT = "emptyimage"
    akiAccM = "emptyimage"
    akiAccB = "emptyimage"
    
    aksHairB = "default"
    aksOut = "default"
    aksHairF = "default"
    aksAccT = "Glasses"
    aksAccM = "emptyimage"
    aksAccB = "emptyimage"
    
    
default invLoadout = "default"
default invStance = "default"
    
init python:
    
    mode = "default"
    enemy = "shou"
    context = "blank"
    finishFirst = 0
    mcEnergyMax = 200
    mcEnergy = 200
    enemyHPMax = 100
    enemyHP = 100
    # "survived" is now just combo score
    survived = 0
    # "combo" records the highest number for score
    ### NEED TO CHANGE for inventory system
    #$ combo = 0
    # score will be the replacement, but still needs implementation in scenes
    score = 0
    
    comradeAssist = 0
    comradeUsed = 0
    
    bloSound = renpy.random.choice([ 'audio/sfx/GEAR Combat/Block.ogg', 'audio/sfx/GEAR Combat/Block.ogg' ])
    dodSound = renpy.random.choice([ 'audio/sfx/GEAR Combat/Dodge.ogg', 'audio/sfx/GEAR Combat/Dodge.ogg' ])
    fistSound = renpy.random.choice([ 'audio/sfx/GEAR Combat/Power Fist Attack 1.ogg', 'audio/sfx/GEAR Combat/Power Fist Attack 2.ogg' ])
    hitSound = renpy.random.choice([ 'audio/sfx/GEAR Combat/Hit.ogg', 'audio/sfx/GEAR Combat/Hit.ogg' ])
    rifSound = renpy.random.choice([ 'audio/sfx/GEAR Combat/Rifle.ogg', 'audio/sfx/GEAR Combat/Rifle.ogg' ])
    smgSound = renpy.random.choice([ 'audio/sfx/GEAR Combat/SMG.ogg', 'audio/sfx/GEAR Combat/SMG.ogg' ])
    sniSound = renpy.random.choice([ 'audio/sfx/GEAR Combat/Sniper.ogg', 'audio/sfx/GEAR Combat/Sniper.ogg' ])
    sw1Sound = renpy.random.choice([ 'audio/sfx/GEAR Combat/Sword Single.ogg', 'audio/sfx/GEAR Combat/Sword Single.ogg' ])
    sw2Sound = renpy.random.choice([ 'audio/sfx/GEAR Combat/Sword Double.ogg', 'audio/sfx/GEAR Combat/Sword Double.ogg' ])
    
    meleeSound = "audio/sfx/GEAR Combat/Sword Single.ogg"
    rangeSound = "audio/sfx/GEAR Combat/Sniper.ogg"
    Depowered = "audio/sfx/GEAR Combat/Depower.ogg"

    retSound = renpy.random.choice([ 'dodSound', 'bloSound' ])
    attSound = "audio/sfx/GEAR Combat/Hit.ogg"
    
### Inventory Stats

default hp     = 100
default energy = 100
default damage = 10
default combo  = 10
default inv    = Inventory("name", 100)

###################################################################### ~ Game Start


label start:
    $ renpy.music.set_volume(.55, channel="ambient")
    $ renpy.music.set_volume(.55, channel="ambient2")
    $ renpy.music.set_volume(.55, channel="music")
    $ renpy.music.set_volume(.80, channel="sound")
    $ renpy.music.set_volume(.80, channel="sound2")
    $ renpy.music.set_volume(.80, channel="sound3")
    $ renpy.music.set_volume(1, channel="voice")
    
    scene bg title with Dissolve(2.0)
    $ config.rollback_enabled = True
    
    "Welcome to {i}ACE Academy{/i}!"
    
    "Let's get a few things set up for you..."
    #label rollbackchoice:
    #    "{i}{b}Rollback Function{/b}{/i}{p}This feature allows you to scroll back and re-pick options within a certain period of time. {w}Configuration will not impact the story in any way... pick to your preference!"
    #    "Would you like to enable {i}{b}Rollback Function{/b}{/i}?"
    #    menu:
    #        "Yes please.":
    #            $ config.rollback_enabled = True
    #            "{i}{b}Rollback Function{/b}{/i} enabled! Please use your mousewheel to access this function."
    #
    #        "No way!":
    #            $ config.rollback_enabled = False
    #            "{i}{b}Rollback Function{/b}{/i} disabled!"



    label naming:
        $ pfirst = renpy.input("Enter male MCs first name:")
        $ pfirst = pfirst.strip()
        if pfirst == "":
            $ pfirst = "Tristan"

        $ plast = renpy.input("Enter male MCs last name:")
        $ plast = plast.strip()
        if plast == "":
            $ plast = "Spade"

        "Proceed as {color=#FFBF00}[pfirst] [plast]{/color}?"


        menu:
            "Yes":
                #$ pfull = "[pfirst] [plast]"
                $ pfull = pfirst+" "+plast
                $ pf = DynamicCharacter("pfull", color="#FFBF00")
                
                $ sfirst = "Nikki"
                $ sfull = "[sfirst] [plast]"
                $ sf = DynamicCharacter("sfull", color="#FFD633")
                
                $ dfirst = "James"
                $ dfull = "[dfirst] [plast]"
                $ dad = DynamicCharacter("dfull", color="#FFD640")
                
                #$ pfull = pfirst+" "+plast
                #$ sfull = sfirst+" "+plast
            "Rename":
                jump naming


    "Please select {color=#FFBF00}[pfirst]'s{/color} main characteristic:"

    image athleticimage 1 = "i/Personalities/Athletic_idle.png"
    image intelimage 1 = "i/Personalities/Intelligent_idle.png"
    image intuitiveimage 1 = "i/Personalities/Intuitive_idle.png"


    show athleticimage 1
    show intelimage 1
    show intuitiveimage 1
    with dissolve

    $renpy.pause()

    label CharacterBackstory:
        menu:
            "Athletic":
                $ MCStory = 1
                hide intelimage
                hide intuitiveimage
                with dissolve

            "Intelligent":
                $ MCStory = 2
                hide athleticimage
                hide intuitiveimage
                with dissolve

            "Intuitive":
                $ MCStory = 3
                hide athleticimage
                hide intelimage
                with dissolve


    $renpy.pause(.75)
    hide athleticimage
    hide intelimage
    hide intuitiveimage
    with dissolve
    "That's it.{w} Good luck at {i}ACE Academy{/i}!"

    $ inv.add("defaultCore")
    $ inv.add("defaultFrame")
    $ inv.add("defaultThruster")
    $ inv.add("defaultBuster")
    $ inv.add("defaultRifle")
    
    $ inv.equip("defaultCore")
    $ inv.equip("defaultFrame")
    $ inv.equip("defaultThruster")
    $ inv.equip("defaultBuster")
    $ inv.equip("defaultRifle")
    

    jump E1D1S1
