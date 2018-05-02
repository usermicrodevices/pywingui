from pywingui.winuser import *

mouse_event(MOUSEEVENTF_ABSOLUTE | MOUSEEVENTF_MOVE, 0, 0, 0, 0)
mouse_event(MOUSEEVENTF_MOVE, 200, 200, 0, 0)
mouse_event(MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
mouse_event(MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
# mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
# mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
