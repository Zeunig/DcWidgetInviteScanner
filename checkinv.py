from selenium import webdriver
from discord_webhook import DiscordWebhook, DiscordEmbed
from colorama import Fore, Style, init
import time
import os
init(convert=True)
os.system("mode con cols=150 lines=50")
os.system('color 2')
PATH = 'D:\chromedriver.exe'
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/909207631804129312/ZISomNtygU4mCte_EAs6S_YOslfPt2u3yf_ZfI9EKX4ZpnnV-Ntx2CYjEDnG5h7SZTa3"
driver = webdriver.Chrome(PATH) 
driver.maximize_window()
driver.get('https://discord.com/widget?id=601496163023323137&theme=dark')
q = "https://discord.com/invite/9vDrQg7K?utm_source=Discord%20Widget&utm_medium=Connect"
print("\033[2J\033[1;1f")
print('''
$$\                                     $$\                           $$\                           
\__|                                    $$ |                          $$ |                          
$$\ $$$$$$$\ $$\    $$\        $$$$$$$\ $$$$$$$\   $$$$$$\   $$$$$$$\ $$ |  $$\  $$$$$$\   $$$$$$\  
$$ |$$  __$$\\$$\  $$  |      $$  _____|$$  __$$\ $$  __$$\ $$  _____|$$ | $$  |$$  __$$\ $$  __$$\ 
$$ |$$ |  $$ |\$$\$$  /       $$ /      $$ |  $$ |$$$$$$$$ |$$ /      $$$$$$  / $$$$$$$$ |$$ |  \__|
$$ |$$ |  $$ | \$$$  /        $$ |      $$ |  $$ |$$   ____|$$ |      $$  _$$<  $$   ____|$$ |      
$$ |$$ |  $$ |  \$  /         \$$$$$$$\ $$ |  $$ |\$$$$$$$\ \$$$$$$$\ $$ | \$$\ \$$$$$$$\ $$ |      
\__|\__|  \__|   \_/           \_______|\__|  \__| \_______| \_______|\__|  \__| \_______|\__|  
\n\n\n
''')
TIME = int(input("Milyen gyorsasággal nézze az inviteokat (másodpercben, egész számmal)?: "))
while True:
    try:
        f = driver.find_element_by_class_name('widgetBtnConnect-2fvtGa').get_attribute('href')
        if f == q:
            print(Fore.RED + "Semmi se változott (",f,")")
        else:
            print(Fore.GREEN + "Brékó brékó új inviteot találtam!")
            g = "Új inviteot találtam a büdös pedofiltól: ",f
            webhook = DiscordWebhook(url=DISCORD_WEBHOOK_URL)
            embed = DiscordEmbed(title='ÚJ INV', description=str(g))
            webhook.add_embed(embed)
            response = webhook.execute()
    except:
        print("valami gond van gec na mind1")
    time.sleep(TIME)
    q = f


# https://zeunig.hu