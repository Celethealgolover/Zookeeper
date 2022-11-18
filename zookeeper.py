p=input("Welcome to the Zookeeper's room!Here you can take a look to the animals in my zoo by choosing the animal's name.Would you like to try?yes or no")
if p=="yes":
    s = ""
    while s != "exit":
        s = input("Please enter the name of the animal you would like to view:")
        if s == 'camel':
            print(r"""
    Switching on the camera in the camel habitat...
     ___.-''''-.
    /___  @    |
    ',,,,.     |         _.'''''''._
         '     |        /           \
         |     \    _.-'             \
         |      '.-'                  '-.
         |                               ',
         |                                '',
          ',,-,                           ':;
               ',,| ;,,                 ,' ;;
                  ! ; !'',,,',',,,,'!  ;   ;:
                 : ;  ! !       ! ! ;  ;   :;
                 ; ;   ! !      ! !  ; ;   ;,
                ; ;    ! !     ! !   ; ;
                ; ;    ! !    ! !     ; ;
               ;,,      !,!   !,!     ;,;
               /_I      L_I   L_I     /_I
    Look at that! Our little camel is sunbathing!""")
        elif s == 'lion':
            print(r"""
    Switching on the camera in the lion habitat...
                                                   ,w.
                                                 ,YWMMw  ,M  ,
                            _.---.._   __..---._.'MMMMMw,wMWmW,
                       _.-""        '''           YP"WMMMMMMMMMb,
                    .-' __.'                   .'     MMMMW^WMMMM;
        _,        .'.-'"; `,       /`     .--""      :MMM[==MWMW^;
     ,mM^"     ,-'.'   /   ;      ;      /   ,       MMMMb_wMW"  @\
    ,MM:.    .'.-'   .'     ;     `\    ;     `,     MMMMMMMW `"=./`-,
    WMMm__,-'.'     /      _.\      F'''-+,,   ;_,_.dMMMMMMMM[,_ / `=_}
    "^MP__.-'    ,-' _.--""   `-,   ;       \  ; ;MMMMMMMMMMW^``; __|
               /   .'            ; ;         )  )`{  \ `"^W^`,   \  :
              /  .'             /  (       .'  /     Ww._     `.  `"
             /  Y,              `,  `-,=,_{   ;      MMMP`""-,  `-._.-,
            (--, )                `,_ / `) \/"")      ^"      `-, -;"\:
    The lion is roaring!""")
        elif s == 'deer':
            print(r"""
    Switching on the camera in the deer habitat...
       /|       |\
    `__\\       //__'
       ||      ||
     \__`\     |'__/
       `_\\   //_'
       _.,:---;,._
       \_:     :_/
         |@. .@|
         |     |
         ,\.-./ \
         ;;`-'   `---__________-----.-.
         ;;;                         \_\
         ';;;                         |
          ;    |                      ;
           \   \     \        |      /
            \_, \    /        \     |\
              |';|  |,,,,,,,,/ \    \ \_
              |  |  |           \   /   |
              \  \  |           |  / \  |
               | || |           | |   | |
               | || |           | |   | |
               | || |           | |   | |
               |_||_|           |_|   |_|
              /_//_/           /_/   /_/
    Our 'Bambi' looks hungry. Let's go to feed it!""")
        elif s == 'goose':
            print(r"""
    Switching on the camera in the goose habitat...

                                        _
                                    ,-"" "".
                                  ,'  ____  `.
                                ,'  ,'    `.  `._
       (`.         _..--.._   ,'  ,'        \    \
      (`-.\    .-""        ""'   /          (  d _b
     (`._  `-"" ,._             (            `-(   \
     <_  `     (  <`<            \              `-._\
      <`-       (__< <           :
       (__        (_<_<          ;
        `------------------------------------------
    The goose is staring intently at you... Maybe it's time to change the channel?""")
        elif s == 'bat':
            print(r"""
    Switching on the camera in the bat habitat...
    _________________               _________________
     ~-.              \  |\___/|  /              .-~
         ~-.           \ / o o \ /           .-~
            >           \\  W  //           <
           /             /~---~\             \
          /_            |       |            _\
             ~-.        |       |        .-~
                ;        \     /        i
               /___      /\   /\      ___\
                    ~-. /  \_/  \ .-~
                       V         V
    This bat looks like it's doing fine.""")
        elif s == 'rabbit':
            print(r"""
    Switching on the camera in the rabbit habitat...
             ,
            /|      __
           / |   ,-~ /
          Y :|  //  /
          | jj /( .^
          >-"~"-v"
         /       Y
        jo  o    |
       ( ~T~     j
        >._-' _./
       /   "~"  |
      Y     _,  |
     /| ;-"~ _  l
    / l/ ,-"~    \
    \//\/      .- \
     Y        /    Y
     l       I     !
     ]\      _\    /"\
    (" ~----( ~   Y.  )
    It looks like we will soon have more rabbits!""")
        elif s == 'exit':
            print("Thanks for your time!Hope you enjoyed")
else:
    print("Your loss..")