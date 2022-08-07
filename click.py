import threading
import pyautogui

def click1(num):
    for i in range(20):
        pyautogui.click()
  
def click2(num):
    for i in range(20):
        pyautogui.click()

def click3(num):
    for i in range(20):
        pyautogui.click()
 
def click4(num):
    for i in range(20):
        pyautogui.click()

def click5(num):
    for i in range(20):
        pyautogui.click()

def click6(num):
    for i in range(20):
        pyautogui.click()

def click7(num):
    for i in range(20):
        pyautogui.click()


i = int(input("pressione 1 para start"))

if (i==1):
    if __name__ == "__main__":
        while(True):
        # creating thread
            t1 = threading.Thread(target=click1, args=(20,))
            t2 = threading.Thread(target=click2, args=(20,))
            t3 = threading.Thread(target=click3, args=(20,))  
            t4 = threading.Thread(target=click4, args=(20,)) 
            t5 = threading.Thread(target=click5, args=(20,)) 
            t6 = threading.Thread(target=click6, args=(20,)) 
            t7 = threading.Thread(target=click7, args=(20,)) 


            t1.start()
            t2.start()
            t3.start()
            t4.start()
            t5.start()
            t6.start()
            t7.start()

            t1.join()
            t2.join()
            t3.join()
            t4.join()
            t5.join()
            t6.join()
            t7.join()
  
    # both threads completely executed
    print("Done!")