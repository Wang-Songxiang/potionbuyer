import win32gui
import win32api
import win32con
import win32com.client
import time
import sys
import keyboard

with open("config.txt", "r", encoding="utf-8") as f:
    n = int(f.readline().strip("times:"))
    print(n)
    potion=f.readline()
    if potion[7]=="y":
        potion=1
    stone=f.readline()
    if stone[6]=="y":
        stone=1

titlename = "PrincessConnectReDive"
hwnd = win32gui.FindWindow(0, titlename)
left, top, right, bottom = win32gui.GetWindowRect(hwnd)
shell = win32com.client.Dispatch("WScript.Shell")
shell.SendKeys('%')
win32gui.BringWindowToTop(hwnd)
win32gui.SetForegroundWindow(hwnd)
# win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
print("这是一个自动买药的脚本")
print("请确保以管理员身份运行，并且游戏（dmm版）已打开在商店页面")
print("希望停下来时摁住s直到脚本关闭")

L=right-left
W=bottom-top
time.sleep(0.1)
i=0
x=0
p1y=top+int(W*(240/760))
p2y=bottom-int(W*(175/760))
p1x=left+int(L*(518/1280))
p2x=left+int(L*(750/1280))
p3x=left+int(L*(972/1280))
p4x=left+int(L*(1200/1280))
px=[p1x,p2x,p3x,p4x]
f=0
for i in range(n):
    if keyboard.is_pressed('s') or f==1:
        break
    time.sleep(1.5)
    if potion==1:
        for x in range(4):
            win32api.SetCursorPos((px[x],p1y))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            if keyboard.is_pressed('s'):
                f=1
                break
            time.sleep(0.1)
    if keyboard.is_pressed('s') or f==1:
        break
    if stone==1:
        for x in range(4):
            win32api.SetCursorPos((px[x],p2y))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            if keyboard.is_pressed('s'):
                f=1
                break
            time.sleep(0.1)
    if keyboard.is_pressed('s') or f==1:
        break
    time.sleep(0.1)
    win32api.SetCursorPos((right-int(L*(220/1280)),bottom-int(W*(135/760))))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    if keyboard.is_pressed('s') or f==1:
        break
    time.sleep(0.5)
    win32api.SetCursorPos((right-int(L*(500/1280)),bottom-int(W*(80/760))))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    if keyboard.is_pressed('s') or f==1:
        break
    time.sleep(2)
    win32api.SetCursorPos((right-int(L*(650/1280)),bottom-int(W*(80/760))))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    if keyboard.is_pressed('s') or f==1:
        break
    if i<n-1:
        time.sleep(1)
        win32api.SetCursorPos((right-int(L*(500/1280)),bottom-int(W*(140/760))))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        if keyboard.is_pressed('s') or f==1:
            break
        time.sleep(0.5)
        win32api.SetCursorPos((right-int(L*(500/1280)),bottom-int(W*(230/760))))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)