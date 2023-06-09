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
        print("Ghostface lost its patience and exploded your house!\n")
    if c2 == "2":
        print("You opened the door and went outside, but no one was there!")
        c3 = input("Someone calls you again. What do you do?\n1 Ignore it\n2 Answer it\n")
        if c3 == "1":
            print("Ghostface lost its patience and exploded your house\n!")
            print("You are dead now!\n")
        if c3 == "2":
            c4 = input("What is the name of the original killer from Friday the 13th?\n 1. Jason\n 2. Fred\n 3. Maureen\n")
            print("Ghostface entered your house when you opened the door and was just distracting you.\n")
            print("He pulls a knife and kills you!\n")

if c1 == "2":
    c5 = input("What is your favorite scary movie?\n1. Dont answer\n 2. Answer")
    if c5 == "1":
        print("Ghostface got angry because you didnt answer him, he pulls a knife and kills you!")
    if c5 == "2":
        print("Wrong answer. Ghostface pulls a knife and kills you!")
