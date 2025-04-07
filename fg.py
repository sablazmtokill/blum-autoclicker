import pyautogui 
import time 
import keyboard
import win32api, win32con
import threading


def maindef():
    print("Press alt + s to start")
    print("Press q to stop autoclicking")
    print("Press w to stop autorestarting and exit")

    def click(x,y) :
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

    while keyboard.is_pressed("Alt + s") == False:
        a = 0
        a += 1

    while keyboard.is_pressed("q") == False :

        scrnsht = pyautogui.screenshot(region=(1229, 175, 393, 623)) 

        # coordinates of left top corner is x 1229 y 200

        width, height = scrnsht.size

        for x in range(0, width, 5) :
            for y in range(0, height, 5) :

                r,g,b = scrnsht.getpixel((x,y))

                if (r in range(200, 223)) and (g in range(219, 240)) and (b in range(0, 100)) :
                    click(x + 1229, y + 200)
                    time.sleep(0.02) # here we can edit speed
                    break

def restart_def():
    while keyboard.is_pressed("w") == False:
        try:
            bttn = pyautogui.locateOnScreen("imgs/button.png", confidence=0.4, region=(1240, 764, 358, 66))
            pyautogui.click(bttn)
        except pyautogui.ImageNotFoundException:
            pass
        except NotImplementedError:
            pass
        time.sleep(1)       

if __name__ == '__main__':
    threading.Thread(target=maindef).start()
    threading.Thread(target=restart_def).start()