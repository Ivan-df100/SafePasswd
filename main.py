import os
import crypter
import database
import getpass
import hashlib
os.system("mode con cols=120 lines=50")

print("""
                         .--.,                   ,-.----.                                                         ,---, 
                       ,--.'  \                  \    /  \                                             .---.    ,---.'| 
  .--.--.              |  | /\/                  |   :    |              .--.--.    .--.--.           /. ./|    |   | : 
 /  /    '    ,--.--.  :  : :     ,---.          |   | .\ :  ,--.--.    /  /    '  /  /    '       .-'-. ' |    |   | | 
|  :  /`./   /       \ :  | |-,  /     \         .   : |: | /       \  |  :  /`./ |  :  /`./      /___/ \: |  ,--.__| | 
|  :  ;_    .--.  .-. ||  : :/| /    /  |        |   |  \ :.--.  .-. | |  :  ;_   |  :  ;_     .-'.. '   ' . /   ,'   | 
 \  \    `.  \__\/: . .|  |  .'.    ' / |        |   : .  | \__\/: . .  \  \    `. \  \    `. /___/ \:     '.   '  /  | 
  `----.   \ ," .--.; |'  : '  '   ;   /|        :     |`-' ," .--.; |   `----.   \ `----.   \.   \  ' .\   '   ; |:  | 
 /  /`--'  //  /  ,.  ||  | |  '   |  / |        :   : :   /  /  ,.  |  /  /`--'  //  /`--'  / \   \   ' \ ||   | '/  ' 
'--'.     /;  :   .'   \  : \  |   :    |        |   | :  ;  :   .'   \\'--'.     /'--'.     /   \   \  |--" |   :    :| 
  `--'---' |  ,     .-./  |,'@  \   \  /         `---'.|  |  ,     .-./  `--'---'   `--'---'     \   \ |     \   \  /   
            `--`---'   `--'      `----'            `---`   `--`---'                               '---"       `----'    
                                                     ,---,    ,----..       ,----..                                     
  ,---,                            ,---,  .--.,   ,`--.' |   /   /   \     /   /   \                                    
,---.'|                          ,---.'|,--.'  \ /    /  :  /   .     :   /   .     :                                   
|   | :                          |   | :|  | /\/:    |.' ' .   /   ;.  \ .   /   ;.  \                                  
:   : :         .--,             |   | |:  : :  `----':  |.   ;   /  ` ;.   ;   /  ` ;                                  
:     |,-.    /_ ./|           ,--.__| |:  | |-,   '   ' ;;   |  ; \ ; |;   |  ; \ ; |                                  
|   : '  | , ' , ' :          /   ,'   ||  : :/|   |   | ||   :  | ; | '|   :  | ; | '                                  
|   |  / :/___/ \: |         .   '  /  ||  |  .'   '   : ;.   |  ' ' ' :.   |  ' ' ' :                                  
'   : |: | .  \  ' |         '   ; |:  |'  : '     |   | ''   ;  \; /  |'   ;  \; /  |                                  
|   | '/ :  \  ;   :         |   | '/  '|  | |     '   : | \   \  ',  /  \   \  ',  /                                   
|   :    |   \  \  ;         |   :    :||  : \     ;   |.'  ;   :    /    ;   :    /                                    
/    \  /     :  \  \         \   \  /  |  |,'     '---'     \   \ .'      \   \ .'                                     
`-'----'       \  ' ;          `----'   `--'                  `---`         `---`                                       
                `--`                                                                                                    
""")

print()

if not os.path.exists(f"{os.getcwd()}/passwd"):
    print("Creating db..")
    db = database.Database("passwd")

    db.query("CREATE TABLE access (hash TEXT, help TEXT)")
    db.query("CREATE TABLE passwords (title TEXT, login TEXT, password TEXT)")
    password = getpass.getpass("Please, enter master-password: ")
    helpText = input("Please, enter help text. It helps you, if you lost your password: ")

    db.query("INSERT INTO access VALUES (?, ?)", [hashlib.md5(password.encode()).hexdigest(), helpText])
    input("Good, now, restart app.")
    exit()


db = database.Database("passwd")

passwordHash = db.query("SELECT hash FROM access")[0][0]

while True:
    password = getpass.getpass("Please, enter master-password: ")
    if hashlib.md5(password.encode()).hexdigest() == passwordHash:
        break
    print("ERR: PASSWORD INVALID")
c = crypter.Crypter(password)
print("Authorized!")



while True:
    passwords = db.query("SELECT * FROM passwords")

    for pas in passwords:
        print(f"{pas[0]} - {pas[1]}:{c.crypt(pas[2])}")

    choice = int( input("1 - new note. 2 - exit: ") )

    if choice == 1:
        name, login, passwd = input("Enter name for your note: "), input("Enter login: "), c.crypt(getpass.getpass("Enter password: "))

        db.query("INSERT INTO passwords VALUES (?, ?, ?)", [name, login, passwd])

    elif choice == 2:
        exit()