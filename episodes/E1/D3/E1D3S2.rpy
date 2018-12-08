label E1D3S2:
    scene bg isokaze neighborhood day with fade
    stop ambient fadeout 3
    "По крайней мере, это хороший день, чтобы подождать автобус."
    play ambient "audio/ambience/Bus Stop.ogg" fadein 1
    "Остановка была немного переполнена. Я прислонился к павильону, ожидая."
    play sound "audio/sfx/Vehicles/Bus Door Open.ogg" fadein 1 fadeout 1
    "Автобус остановился через несколько минут после моего прибытия."
    scene bg travel bus day with fade
    stop ambient fadeout 3
    play sound [ "audio/sfx/Technology/ID Tap.ogg", "audio/sfx/Technology/ID Tap Success.ogg" ]
    "Я последовал за другими пассажирами, приложил ID карту, и начал искать свободное место."
    play ambient "audio/ambience/Bus.ogg" fadein 1
    
    if (E1D2S2_talkwithyuunayes == 1):
        "К сожалению, Юну нигде не было видно."
    
    "Я сел на первое попавшееся место, и ворчал, как только большой человек сел рядом со мной, прижимая меня к окну." 
    "Я уже представил, насколько приятной будет эта поездка."
    scene black with fade
    $renpy.pause(2.5)
    play sound "audio/sfx/Vehicles/Bus Chime.ogg"
    scene bg travel bus day with fade
    "К счастью, это была недолгая поездка, и я был в школе, прежде чем начал слишком много жаловаться."
    stop ambient fadeout 3
    play sound "audio/sfx/Vehicles/Bus Door Open.ogg"
    scene bg campus main day with fade
    play ambient "audio/ambience/Campus.ogg" fadein 1
    jump E1D3S4
