label E1D3S3:
    
    scene bg isokaze highschool day with fade
    stop ambient fadeout 3
    "Я остановился возле школы Никки и снял шлем."
    play ambient "audio/ambience/Campus.ogg" fadein 1
    pf "Мы на месте!"
    show nikki hap at cc with dissolve
    "Никки спрыгнула с мотоцикла и усмехнулась, протягивая мне второй шлем." 
    voice "audio/voice/E1/D3/S3/Nikki/1.ogg"
    sf "Спасибо."
    show nikki neu at cc
    "Я заметил, как несколько студентов смотрело в нашу сторону; одна девушка подошла к нам."
    show highschoolgirl extra at l3 with dissolve
    hstu1f "Привет, Никки."
    show nikki smi at cc
    voice "audio/voice/E1/D3/S3/Nikki/2.ogg"
    sf "Привет!" 
    hstu1f "Кто это?"
    show nikki hap at cc
    voice "audio/voice/E1/D3/S3/Nikki/3.ogg"
    sf "Мой брат! Он учится в ACE."
    # shiny eyes for girl
    show heart:
        xoffset 230
        yoffset 160
        xzoom .75
        yzoom .75
    hstu1f "Ого, тиановые полосы на его форме! Это восхитительно! Я понятия не имела, что тя связана с пилотом ACE. Это такая сложная программа."
    show nikki neu at cc
    "Она помахала молодому студенту парню."
    show studentM extra at r3 with dissolve
    hstu1f "Смотри! Старший брат Никки пилот в ACE."
    # more shiny eyes?
    show heart:
        xoffset 1175
        yoffset 160
        xzoom .75
        yzoom .75
    hstu2m "Правда что ли?"
    show nikki smi at cc
    "Несколько других студентов собрались вокруг нас, охали и задыхалмсь от сложности пилотной программы и комментируя, насколько я впечатляющ. Всё время Никки гордо сияла."  
    pf "Ну, я должен ехать в школу. Хорошего дня, Никки."
    show nikki hap at cc
    show heart:
        xoffset 720
        yoffset 160
        xzoom .75
        yzoom .75
    voice "audio/voice/E1/D3/S3/Nikki/4.ogg"
    sf "Пока! Ещё раз спасибо за поездку."
    hide nikki
    hide studentM extra
    hide highschoolgirl extra
    with dissolve
    stop ambient fadeout 3
    play sound "audio/sfx/Vehicles/Bike driving off.ogg" fadein 1 fadeout 1
    "Она помахала и я уехал."
    play ambient "audio/ambience/Open Road Helmet.ogg" fadein 1
    play sound "audio/sfx/Vehicles/Bike Accelerate.ogg" fadein 1 fadeout 1
    scene bg campus intersection day with fade
    "Я рад, что впечатлил друзей Никки. Если у нее были какие-то трудности с новыми друзьями, то сейчас, конечно, их не будет."
    $renpy.pause(1)
    scene black with fade
    $renpy.pause(1)
    stop ambient fadeout 3
    $renpy.pause(1)
    stop music fadeout 3
    play ambient "audio/ambience/Campus.ogg" fadein 1
    scene bg campus main day with fade
    
    jump E1D3S4
