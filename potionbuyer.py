import win32gui
import win32api
import win32con
import win32com.client
import time
import sys

with open("times.txt", "r") as f:
    n = int(f.read())

titlename = "PrincessConnectReDive"
hwnd = win32gui.FindWindow(0, titlename)
left, top, right, bottom = win32gui.GetWindowRect(hwnd)
shell = win32com.client.Dispatch("WScript.Shell")
shell.SendKeys('%')
win32gui.BringWindowToTop(hwnd)
win32gui.SetForegroundWindow(hwnd)
# win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
print(left)
print(top)
print(right)
print(bottom)
L=right-left
W=bottom-top
print(L)
print(W)
print(int(L*(518/1280)))
print(int(W*(240/760)))
time.sleep(0.1)
i=0
for i in range(n):
    time.sleep(1.5)
    win32api.SetCursorPos((left+int(L*(518/1280)),top+int(W*(240/760))))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(0.1)
    win32api.SetCursorPos((left+int(L*(750/1280)),top+int(W*(240/760))))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(0.1)
    win32api.SetCursorPos((left+int(L*(972/1280)),top+int(W*(240/760))))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(0.1)
    win32api.SetCursorPos((left+int(L*(1200/1280)),top+int(W*(240/760))))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)

    time.sleep(0.1)
    win32api.SetCursorPos((left+int(L*(518/1280)),bottom-int(W*(175/760))))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(0.1)
    win32api.SetCursorPos((left+int(L*(750/1280)),bottom-int(W*(175/760))))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(0.1)
    win32api.SetCursorPos((left+int(L*(972/1280)),bottom-int(W*(175/760))))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(0.1)
    win32api.SetCursorPos((left+int(L*(1200/1280)),bottom-int(W*(175/760))))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)

    time.sleep(0.1)
    win32api.SetCursorPos((right-int(L*(220/1280)),bottom-int(W*(135/760))))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)

    time.sleep(0.5)
    win32api.SetCursorPos((right-int(L*(500/1280)),bottom-int(W*(80/760))))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(2)
    win32api.SetCursorPos((right-int(L*(650/1280)),bottom-int(W*(80/760))))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    if i<n-1:
        time.sleep(1)
        win32api.SetCursorPos((right-int(L*(500/1280)),bottom-int(W*(140/760))))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        time.sleep(0.5)
        win32api.SetCursorPos((right-int(L*(500/1280)),bottom-int(W*(230/760))))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)