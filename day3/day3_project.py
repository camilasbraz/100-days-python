print('''

                                                                ⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠋⠉⠁⠄⠄⠈⠙⠻⣿⣿⣿⣿
                                                                ⣿⣿⣿⣿⣿⣿⠟⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⢿⣿
                                                                ⣿⣿⣿⣿⡿⠃⠄⠄⠄⢀⣀⣀⡀⠄⠄⠄⠄⠄⠄⠄⠈⢿
                                                                ⣿⣿⣿⡟⠄⠄⠄⠄⠐⢻⣿⣿⣿⣷⡄⠄⠄⠄⠄⠄⠄⠈
                                                                ⣿⣿⣿⠃⠄⠄⠄⢀⠴⠛⠙⣿⣿⡿⣿⣦⠄⠄⠄⠄⠄⠄
                                                                ⣿⣿⠃⠄⢠⡖⠉⠄⠄⠄⣠⣿⡏⠄⢹⣿⠄⠄⠄⠄⠄⢠
                                                                ⣿⠃⠄⠄⢸⣧⣤⣤⣤⢾⣿⣿⡇⠄⠈⢻⡆⠄⠄⠄⠄⣾
                                                                ⠁⠄⠄⠄⠈⠉⠛⢿⡟⠉⠉⣿⣷⣀⠄⠄⣿⡆⠄⠄⢠⣿
                                                                ⠄⠄⠄⠄⠄⠄⢠⡿⠿⢿⣷⣿⣿⣿⣿⣿⠿⠃⠄⠄⣸⣿
                                                                ⠄⠄⠄⠄⠄⢀⡞⠄⠄⠄⠈⣿⣿⣿⡟⠁⠄⠄⠄⠄⣿⣿
                                                                ⠄⠄⠄⠄⠄⢸⠄⠄⠄⠄⢀⣿⣿⡟⠄⠄⠄⠄⠄⢠⣿⣿
                                                                ⠄⠄⠄⠄⠄⠘⠄⠄⠄⢀⡼⠛⠉⠄⠄⠄⠄⠄⠄⣼⣿⣿
                                                                ⠄⠄⠄⠄⠄⡇⠄⠄⢀⠎⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⢿⣿
                                                                ⠄⠄⠄⠄⢰⠃⠄⢀⠎⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄ ⠙

 _    _  _____ _   _ _    ______  __   _______ _   _   _     _____ _   __ _____   _____ _____  ______ _       _____   __   ___    _____   ___  ___  ___ _____ ___  
| |  | ||  _  | | | | |   |  _  \ \ \ / /  _  | | | | | |   |_   _| | / /|  ___| |_   _|  _  | | ___ \ |     / _ \ \ / /  / _ \  |  __ \ / _ \ |  \/  ||  ___|__ \ 
| |  | || | | | | | | |   | | | |  \ V /| | | | | | | | |     | | | |/ / | |__     | | | | | | | |_/ / |    / /_\ \ V /  / /_\ \ | |  \// /_\ \| .  . || |__    ) |
| |/\| || | | | | | | |   | | | |   \ / | | | | | | | | |     | | |    \ |  __|    | | | | | | |  __/| |    |  _  |\ /   |  _  | | | __ |  _  || |\/| ||  __|  / / 
\  /\  /\ \_/ / |_| | |___| |/ /    | | \ \_/ / |_| | | |_____| |_| |\  \| |___    | | \ \_/ / | |   | |____| | | || |   | | | | | |_\ \| | | || |  | || |___ |_|  
 \/  \/  \___/ \___/\_____/___/     \_/  \___/ \___/  \_____/\___/\_| \_/\____/    \_/  \___/  \_|   \_____/\_| |_/\_/   \_| |_/  \____/\_| |_/\_|  |_/\____/ (_)                                                      
''')
print("Your mission is to survive Ghostface.\n") 

c1 = input("You are watching TV and the phone rings. What do you do?\n1 Ignore it\n2 Answer it\n")

if c1 == "1":
    print("You scapped so far, but you ignored Ghostface and made him angry. Watch out")
    c2 = input("The doorbell rings. What do you do?\n1 Ignore it\n2 Answer it\n")
    if c2 == "1":
        print("")
        c2 = input("\n")

    if c2 == "2":
        print("You opened the door and went outside, but no one was there!")
        c3 = input("Someone calls you again. What do you do?\n1 Ignore it\n2 Answer it\n")

if c1 == "2":
    c2 = input("What is your favorite scary movie?\n1. Scream\n 2. ")