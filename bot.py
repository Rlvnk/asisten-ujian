import time
from plyer import notification
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from gemini import Gemini
import keyboard

def readtxt(txt):
    try:
        with open(txt,'r') as file:
            isi_file = file.read()
        return isi_file
    except FileNotFoundError:
        print(f"file'{txt}' tidak ditemukan.")
        return None
    except Exception as e:
        print("terjadi kesalahan: {e}")
        return None
def end():
    print("program terhenti")
    browser.quit()
def triger():
    try:
        print('run')
        window_handles = browser.window_handles
        browser.switch_to.window(window_handles[1]) 
        soal = WebDriverWait(browser, 60).until(
        EC.presence_of_element_located((By.XPATH,readtxt('soal.txt')))
        )
    
        pila = WebDriverWait(browser, 60).until(
        EC.presence_of_element_located((By.XPATH,readtxt('a.txt')))
        )
        pilb = WebDriverWait(browser, 60).until(
        EC.presence_of_element_located((By.XPATH,readtxt('b.txt')))
        )
        pilc = WebDriverWait(browser, 60).until(
        EC.presence_of_element_located((By.XPATH,readtxt('c.txt')))
        )
        pild = WebDriverWait(browser, 60).until(
        EC.presence_of_element_located((By.XPATH,readtxt('d.txt')))
            )
        pile = WebDriverWait(browser, 60).until(
        EC.presence_of_element_located((By.XPATH,readtxt('e.txt')))
            )
        notification.notify(title="",message="generate",app_name="",timeout=1 );
        a=pila.text
        b=pilb.text
        c=pilc.text
        d=pild.text
        e=pile.text
        time.sleep(5)
        ask="tolong jawab dengan bahasa indonesia, soal : "+soal.text+'.Pilihan ganda : A. '+a+' B. '+b+' C. '+c+' D. '+d+' E. '+e+' . pilihlah jawaban yang paling sesuai dan tolong jawab dengan singkat + konsisten'
        response = client.generate_content(ask)
        answer=response.text
        answerl= answer.lower()
        pilal = "jawaban adalah adalah: **a. a. "+a.lower()+'**'+" **"+a.lower()+"**"+" **"+a.lower()+"**."
        pilbl = "jawaban adalah adalah: **b. b. "+b.lower()+'**'+" **"+b.lower()+"**"+" **"+b.lower()+"**."
        pilcl = "jawaban adalah adalah: **c. c. "+c.lower()+'**'+" **"+c.lower()+"**"+" **"+c.lower()+"**."
        pildl = "jawaban adalah adalah: **d. d. "+d.lower()+'**'+" **"+d.lower()+"**"+" **"+d.lower()+"**."
        pilel = "jawaban adalah adalah: **e. e. "+e.lower()+'**'+" **"+e.lower()+"**"+" **"+e.lower()+"**."
        answers = set(answerl.split())
        pilas = set(pilal.split())
        pilbs = set(pilbl.split())
        pilcs = set(pilcl.split())
        pilds = set(pildl.split())
        piles = set(pilel.split())

        kataA = answers.symmetric_difference(pilas)
        kataB = answers.symmetric_difference(pilbs)
        kataC = answers.symmetric_difference(pilcs)
        kataD = answers.symmetric_difference(pilds)
        kataE = answers.symmetric_difference(piles)

        # print(answer)
        if len(kataA) < len(kataB) and len(kataA) < len(kataC) and len(kataA) < len(kataD)and len(kataA) < len(kataE)   :  
            print("A")
            notification.notify(title="",message="Jawabannya A",app_name="",timeout=1 );     
            pila.click()
        elif len(kataB) < len(kataA) and len(kataB) < len(kataC) and len(kataB) < len(kataD)and len(kataB) < len(kataE)   :       
            print("B")
            pilb.click()
            notification.notify(title="",message="Jawabannya B",app_name="",timeout=1 );  
        elif len(kataC) < len(kataA) and len(kataC) < len(kataB) and len(kataC) < len(kataD) and len(kataC) < len(kataE)  :     
            print("C")
            pilc.click()
            notification.notify(title="",message="Jawabannya C",app_name="",timeout=1 );  
        elif len(kataD) < len(kataA) and len(kataD) < len(kataB) and len(kataD) < len(kataC) and len(kataD) < len(kataE) :
            print("D")
            pild.click()
            notification.notify(title="",message="Jawabannya D",app_name="",timeout=1 );  
        elif len(kataE) < len(kataA) and len(kataE) < len(kataB) and len(kataE) < len(kataC) and len(kataE) < len(kataD) :
            print("E")
            pile.click()
            notification.notify(title="",message="Jawabannya E",app_name="",timeout=1 );  
        else:
            notification.notify(title="",message="failed",app_name="",timeout=1 );
    except:
        notification.notify(title="",message="Not Found",app_name="",timeout=1 );
def main():
    keyboard.add_hotkey('/', triger)
    keyboard.wait('home')
    end()


try:
    cookies = {
    "__Secure-1PSIDCC" : "value",
    "__Secure-1PSID" : "value",
    "__Secure-1PSIDTS" : "value",
    "NID" : "value",
    # Cookies may vary by account or region. Consider sending the entire cookie file.
  }
    client  = Gemini(cookies=cookies)
except Exception as e:
    notification.notify(title="",message="cookie expired",app_name="",timeout=1 )
options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True )
options.add_experimental_option("excludeSwitches", ['enable-automation'])
options.add_experimental_option("useAutomationExtension", False)
browser = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()),options=options)
browser.get(readtxt('url.txt'))
main()

