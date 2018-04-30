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
keybd_event(VK_E, MapVirtualKey(VK_E, 0), 0, 0)
keybd_event(VK_E, 0, KEYEVENTF_KEYUP, 0)
keybd_event(VK_LWIN, MapVirtualKey(VK_LWIN, 0), KEYEVENTF_KEYUP, 0)
######################
sleep(1)
######################
###GO TO END
keybd_event(VK_END, MapVirtualKey(VK_END, 0), 0, 0)
keybd_event(VK_END, 0, KEYEVENTF_KEYUP, 0)
######################
###PRESS ENTER
keybd_event(VK_RETURN, MapVirtualKey(VK_RETURN, 0), 0, 0)
keybd_event(VK_RETURN, 0, KEYEVENTF_KEYUP, 0)
######################
###GO TO HOME
keybd_event(VK_HOME, MapVirtualKey(VK_HOME, 0), 0, 0)
keybd_event(VK_HOME, 0, KEYEVENTF_KEYUP, 0)
######################
sleep(1)
######################
###SELECT FIRST ITEM
keybd_event(VK_SPACE, MapVirtualKey(VK_SPACE, 0), 0, 0)
keybd_event(VK_SPACE, 0, KEYEVENTF_KEYUP, 0)
######################
sleep(1)
######################
###OPEN SYSTEM MENU
keybd_event(VK_APPS, MapVirtualKey(VK_APPS, 0), 0, 0)
keybd_event(VK_APPS, 0, KEYEVENTF_KEYUP, 0)
######################
###SELECT SEVEN ITEM
for i in range(8):
	keybd_event(VK_UP, MapVirtualKey(VK_UP, 0), 0, 0)
	keybd_event(VK_UP, 0, KEYEVENTF_KEYUP, 0)
######################
###PRESS RIGHT
keybd_event(VK_RIGHT, MapVirtualKey(VK_RIGHT, 0), 0, 0)
keybd_event(VK_RIGHT, 0, KEYEVENTF_KEYUP, 0)
######################
###PRESS ENTER
keybd_event(VK_RETURN, MapVirtualKey(VK_RETURN, 0), 0, 0)
keybd_event(VK_RETURN, 0, KEYEVENTF_KEYUP, 0)
######################
sleep(2)
######################
###PRESS DELETE
for i in range(3):
	keybd_event(VK_DELETE, MapVirtualKey(VK_DELETE, 0), 0, 0)
	keybd_event(VK_DELETE, 0, KEYEVENTF_KEYUP, 0)
######################
###PRESS RIGHT
for i in range(6):
	keybd_event(VK_RIGHT, MapVirtualKey(VK_RIGHT, 0), 0, 0)
	keybd_event(VK_RIGHT, 0, KEYEVENTF_KEYUP, 0)
######################
###PRESS ENTER
keybd_event(VK_RETURN, MapVirtualKey(VK_RETURN, 0), 0, 0)
keybd_event(VK_RETURN, 0, KEYEVENTF_KEYUP, 0)
######################
###SELECT ALL
keybd_event(VK_CONTROL, MapVirtualKey(VK_CONTROL, 0), 0, 0)
keybd_event(VK_A, MapVirtualKey(VK_A, 0), 0, 0)
keybd_event(VK_A, 0, KEYEVENTF_KEYUP, 0)
keybd_event(VK_CONTROL, MapVirtualKey(VK_CONTROL, 0), KEYEVENTF_KEYUP, 0)
######################
###GO TO CENTER
keybd_event(VK_CONTROL, MapVirtualKey(VK_CONTROL, 0), 0, 0)
keybd_event(VK_E, MapVirtualKey(VK_E, 0), 0, 0)
keybd_event(VK_E, 0, KEYEVENTF_KEYUP, 0)
keybd_event(VK_CONTROL, MapVirtualKey(VK_CONTROL, 0), KEYEVENTF_KEYUP, 0)
######################
###INCREASE FONT SIZE
# VKCS = VK_CONTROL|VK_SHIFT
keybd_event(VK_CONTROL, MapVirtualKey(VK_CONTROL, 0), 0, 0)
sleep(0.5)
keybd_event(VK_SHIFT, MapVirtualKey(VK_SHIFT, 0), 0, 0)
sleep(0.5)
VKCODE = ord('>')
for i in range(9):
	keybd_event(VKCODE, MapVirtualKey(VKCODE, 0), 0, 0)
	keybd_event(VKCODE, 0, KEYEVENTF_KEYUP, 0)
	sleep(0.5)
keybd_event(VK_CONTROL, MapVirtualKey(VK_CONTROL, 0), KEYEVENTF_KEYUP, 0)
keybd_event(VK_SHIFT, MapVirtualKey(VK_SHIFT, 0), KEYEVENTF_KEYUP, 0)
######################
sleep(1)
######################
###PRESS PRINT
keybd_event(VK_CONTROL, MapVirtualKey(VK_CONTROL, 0), 0, 0)
keybd_event(VK_P, MapVirtualKey(VK_P, 0), 0, 0)
keybd_event(VK_P, 0, KEYEVENTF_KEYUP, 0)
keybd_event(VK_CONTROL, MapVirtualKey(VK_CONTROL, 0), KEYEVENTF_KEYUP, 0)
######################
sleep(2)
######################
keybd_event(VK_ESCAPE, MapVirtualKey(VK_ESCAPE, 0), 0, 0)
keybd_event(VK_ESCAPE, 0, KEYEVENTF_KEYUP, 0)
######################
sleep(1)
######################
###CLOSE WINDOW
keybd_event(VK_MENU, MapVirtualKey(VK_MENU, 0), 0, 0)
keybd_event(VK_F4, MapVirtualKey(VK_F4, 0), 0, 0)
keybd_event(VK_F4, 0, KEYEVENTF_KEYUP, 0)
keybd_event(VK_MENU, MapVirtualKey(VK_MENU, 0), KEYEVENTF_KEYUP, 0)
######################
###PRESS RIGHT
keybd_event(VK_RIGHT, MapVirtualKey(VK_RIGHT, 0), 0, 0)
keybd_event(VK_RIGHT, 0, KEYEVENTF_KEYUP, 0)
######################
###PRESS BUTTON
keybd_event(VK_SPACE, MapVirtualKey(VK_SPACE, 0), 0, 0)
keybd_event(VK_SPACE, 0, KEYEVENTF_KEYUP, 0)
######################
sleep(1)
######################
###CLOSE WINDOW
keybd_event(VK_MENU, MapVirtualKey(VK_MENU, 0), 0, 0)
keybd_event(VK_F4, MapVirtualKey(VK_F4, 0), 0, 0)
keybd_event(VK_F4, 0, KEYEVENTF_KEYUP, 0)
keybd_event(VK_MENU, MapVirtualKey(VK_MENU, 0), KEYEVENTF_KEYUP, 0)
