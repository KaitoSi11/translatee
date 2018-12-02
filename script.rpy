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

    ym = Character("Юна Мисаки", color="#58D3F7")
    
    ki = Character("Каори Итами", color="#FA5858")
    
    ss = Character("Сё Синдзиро", color="#01DF3A")
    
    ma = Character("Маю Акеми", color="#00FFBF")
    
    hk = Character("Кайто Хикари", color="#FF8000")
    
    hy = Character("Юки Хикари")
    
    am = Character("Акира Масато", color="#CCCCCC")
    
    vb = Character("Валерия Бель", color="#FFFF00")
    
    ms = Character("Мэй Сатоми", color="#835930")
    
    GEARpf = Character("Орёл", color="#4D94FF")
    
    mv = Character("Дядя Мигель")
    
    ky = Character("Кен \"Йен\" Кокан")
    
    acc = Character("Брий Алиев")
    
    don = Character("Донни Рус")
    
    dfirst = "James"
    dfull = dfirst+" "+plast
    dad = DynamicCharacter("dfull", color="#FFD640")
    
    e = Character("Eileen")
    
    
    aks = Character("Акио Синдзиро")
    kt = Character("Кен Такео")
    tk = Character("Тацуо Кимура")
    gua = Character("Охранник")
    an = Character("Диктор")
    eng1 = Character("Инженер")
    eng1m = Character("Инженер мужчина")
    fk = Character("Arcade Gosu")
    rn = Character("Tech Gosu")
    dr = Character("Водитель")
    iceman = Character("Мороженщик")
    ez = Character("Ex Zee")
    rec1 = Character("Регистратор общежития")
    dormf1 = Character("Студентка ACE")
    hito = Character("Хитоми")
    wait = Character("Официант")
    oldman = Character("Старик")
    alm = Character("Алудийский конгрессмен")
    
    rc1m = Character("Male Administrator")
    rc2f = Character("Female Receptionist")
    rc3f = Character("Female Receptionist")
    
    profm = Character("Профессор - Piloting 101")
    prof1m = Character("Профессор - Арсенал GEAR 201")
    prof2f = Character("Профессор - История GEAR 201")
    prof3f = Character("Профессор - International Bridging")
    prof4m = Character("Профессор - Physical Education")
    sprof1 = Character("Владелец клуба")
    
    mec1m = Character("Мужчина механик")
    mech1 = Character("Механик")
    photo1 = Character("Фотограф")
    aeng = Character("Алудийский инженер")
    
    pres1m = Character("Мистер Такеда")
    
    stu1f = Character("Студентка")
    stu3f = Character("Студентка")
    stu4f = Character("Студентка")
    stu9f = Character("Студентка")
    
    stu2m = Character("Студент")
    stu5m = Character("Студент")
    stu6m = Character("Студент")
    stu7m = Character("Студент")
    stu8m = Character("Студент")
    
    fbro1 = Character("Frat Bro")
    fbro2 = Character("Frat Bro")
    fbro3 = Character("Frat Bro")
    fbro4 = Character("Frat Bro")
    fbro5 = Character("Frat Bro")
    fbra1f = Character("Frat Bra")
    fbra2f = Character("Frat Bra")
    
    hstu1f = Character("Старшеклассница")
    hstu2m = Character("Старшеклассник")
    hstu3f = Character("Старшеклассница")
    
    barm = Character("Мужчина бармен")
    
    Bully1 = Character("Goon")
    Bully2 = Character("Goon")
    
    dass1 = Character("Dasshu Coordinator")
    
    bh = Character("Билл Хэнг")
    tj = Character("Саймон Квелл")
    
    sl  = Character("SLASHER")
    mk  = Character("Мицуки Оширо")
    
    hotm1  = Character("Привлекательный мужчина 1")
    hotm2  = Character("Привлекательный мужчина 2")
    hotm3  = Character("Привлекательный мужчина 3")
    hotm4  = Character("Привлекательный мужчина 4")
    hotm4  = Character("Привлекательный мужчина 4")
    girl1 = Character("Фанатка 1")
    girl2 = Character("Фанатка 2")
    team1m = Character("Teammate")
    
    ip  = Character("Иван Поддубный")
    
    flirtyg1 = Character("Привлекательная женщина 1")
    flirtyg2 = Character("Привлекательная женщина 2")
    
    tc = Character("Tennis Captain Райома Эчизан")
    ei = Character("Эйто Иваса")
    
    dk = Character("Dishu Khan")
    ama = Character("АмаЛи")
    recep = Character("Receptionist")
    
    cafec1 = Character("Посетитель 1")
    cafec2 = Character("Посетитель 2")
    
    hstuf1 = Character("Подруга Никки 1")
    
    hstuf3 = Character("Подруга Никки 2")
    
    hstu1f = Character("Подруга Никки 1")
    
    hstu3f = Character("Подруга Никки 2")
    
    creep = Character("\"Этот\" парень")
    
    vg = Character("Продавец")
    
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
    
    "Добро пожаловать в {i}Академию ACE{/i}!"
    
    "Давайте настроим кое-что..."
    #label rollbackchoice:
    #    "{i}{b}Функция отката{/b}{/i}{p}This feature allows you to scroll back and re-pick options within a certain period of time. {w}Configuration will not impact the story in any way... pick to your preference!"
    #    "Would you like to enable {i}{b}Rollback Function{/b}{/i}?"
    #    menu:
    #        "Да.":
    #            $ config.rollback_enabled = True
    #            "{i}{b}Rollback Function{/b}{/i} enabled! Please use your mousewheel to access this function."
    #
    #        "Нет!":
    #            $ config.rollback_enabled = False
    #            "{i}{b}Rollback Function{/b}{/i} disabled!"



    label naming:
        $ pfirst = renpy.input("Введите имя персонажа:")
        $ pfirst = pfirst.strip()
        if pfirst == "":
            $ pfirst = "Tristan"

        $ plast = renpy.input("Введите фамилию персонажа:")
        $ plast = plast.strip()
        if plast == "":
            $ plast = "Spade"

        "Продолжить как {color=#FFBF00}[pfirst] [plast]{/color}?"


        menu:
            "Да.":
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
            "Нет, я передумал":
                jump naming


    "Пожалуйста, выберите {color=#FFBF00}[pfirst]'s{/color} характеристику:"

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
            "Сила":
                $ MCStory = 1
                hide intelimage
                hide intuitiveimage
                with dissolve

            "Интеллект":
                $ MCStory = 2
                hide athleticimage
                hide intuitiveimage
                with dissolve

            "Интуиция":
                $ MCStory = 3
                hide athleticimage
                hide intelimage
                with dissolve


    $renpy.pause(.75)
    hide athleticimage
    hide intelimage
    hide intuitiveimage
    with dissolve
    "Вот и всё.{w} Удачи вам в  {i}Академии ACE{/i}!"

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
