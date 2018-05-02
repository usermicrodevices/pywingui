from time import sleep
from pywingui.winuser import *

# hwnd_desktop = GetDesktopWindow()
# SendMessage(hwnd_desktop, WM_KEYDOWN, VK_LWIN, 0)
# SendMessage(hwnd_desktop, WM_KEYDOWN, VK_E, 0)
# SendMessage(hwnd_desktop, WM_KEYUP, VK_E, 0)
# SendMessage(hwnd_desktop, WM_KEYUP, VK_LWIN, 0)
######################
# SendMessage(HWND_BROADCAST, WM_KEYDOWN, VK_LWIN|VK_E, 0)
# PostMessage(HWND_BROADCAST, WM_KEYDOWN, VK_LWIN|VK_E, 0)
# PostMessage(HWND_BROADCAST, WM_KEYDOWN, VK_RETURN, 0)
# PostMessage(hwnd_desktop, WM_CHAR, VK_E, 0)
# PostMessage(hwnd_desktop, WM_SYSKEYDOWN, VK_LWIN, 0)
# keybd_event(VK_CONTROL, MapVirtualKey(VK_CONTROL, 0), 0, 0);
######################
###OPEN EXPLORER
keybd_event(VK_LWIN, MapVirtualKey(VK_LWIN, 0), 0, 0)
press_key(VK_E)
keybd_event(VK_LWIN, MapVirtualKey(VK_LWIN, 0), KEYEVENTF_KEYUP, 0)
######################
sleep(1)
######################
###GO TO END
press_key(VK_END)
######################
###PRESS ENTER
press_key(VK_RETURN)
######################
###GO TO HOME
press_key(VK_HOME)
######################
sleep(1)
######################
###SELECT FIRST ITEM
press_key(VK_SPACE)
######################
sleep(1)
######################
###OPEN SYSTEM MENU
press_key(VK_APPS)
######################
###SELECT SEVEN ITEM
for i in range(8):
	press_key(VK_UP)
######################
###PRESS RIGHT
press_key(VK_RIGHT)
######################
###PRESS ENTER
press_key(VK_RETURN)
######################
sleep(2)
######################
###PRESS DELETE
for i in range(3):
	press_key(VK_DELETE)
######################
###PRESS RIGHT
for i in range(6):
	press_key(VK_RIGHT)
######################
###PRESS ENTER
press_key(VK_RETURN)
######################
###SELECT ALL
keybd_event(VK_CONTROL, MapVirtualKey(VK_CONTROL, 0), 0, 0)
press_key(VK_A)
keybd_event(VK_CONTROL, MapVirtualKey(VK_CONTROL, 0), KEYEVENTF_KEYUP, 0)
######################
###GO TO CENTER
keybd_event(VK_CONTROL, MapVirtualKey(VK_CONTROL, 0), 0, 0)
press_key(VK_E)
keybd_event(VK_CONTROL, MapVirtualKey(VK_CONTROL, 0), KEYEVENTF_KEYUP, 0)
######################
###INCREASE FONT SIZE - TODO, NOT WORKED YET
keybd_event(VK_CONTROL, MapVirtualKey(VK_CONTROL, 0), 0, 0)
keybd_event(VK_SHIFT, MapVirtualKey(VK_SHIFT, 0), 0, 0)
VKCODE = 0xBE#190 OEM specific, symbol '>', but not ord('>')
for i in range(9):
	press_key(VKCODE)
keybd_event(VK_CONTROL, MapVirtualKey(VK_CONTROL, 0), KEYEVENTF_KEYUP, 0)
keybd_event(VK_SHIFT, MapVirtualKey(VK_SHIFT, 0), KEYEVENTF_KEYUP, 0)
######################
sleep(1)
######################
###PRESS PRINT
keybd_event(VK_CONTROL, MapVirtualKey(VK_CONTROL, 0), 0, 0)
press_key(VK_P)
keybd_event(VK_CONTROL, MapVirtualKey(VK_CONTROL, 0), KEYEVENTF_KEYUP, 0)
######################
sleep(2)
######################
press_key(VK_ESCAPE)
######################
sleep(1)
######################
###CLOSE WINDOW
keybd_event(VK_MENU, MapVirtualKey(VK_MENU, 0), 0, 0)
press_key(VK_F4)
keybd_event(VK_MENU, MapVirtualKey(VK_MENU, 0), KEYEVENTF_KEYUP, 0)
######################
###PRESS RIGHT
press_key(VK_RIGHT)
######################
###PRESS BUTTON
press_key(VK_SPACE)
######################
sleep(1)
######################
###CLOSE WINDOW
keybd_event(VK_MENU, MapVirtualKey(VK_MENU, 0), 0, 0)
press_key(VK_F4)
keybd_event(VK_MENU, MapVirtualKey(VK_MENU, 0), KEYEVENTF_KEYUP, 0)
