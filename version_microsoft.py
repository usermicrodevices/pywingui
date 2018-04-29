# version_microsoft.py
'Microsoft products version constants'

from sys import getwindowsversion

# also can be used versionInfo struct from windows module
# analog is fields: dwMajorVersion, dwMinorVersion, dwBuildNumber, dwPlatformId, szCSDVersion
major, minor, build, platform, text = getwindowsversion()

# WINVER is used for many other constants
WINVER = 0x0300
if major < 5:
	WINVER = 0x0400 # _WIN32_WINNT_NT4
elif major == 5 and minor == 0:
	WINVER = 0x0500 # _WIN32_WINNT_WIN2K
elif major == 5 and minor == 1:
	WINVER = 0x0501 # _WIN32_WINNT_WINXP
elif major == 5 and minor == 2:
	WINVER = 0x0502 # _WIN32_WINNT_WS03
else:
	WINVER = 0x0600 # _WIN32_WINNT_LONGHORN

_WIN32_WCE = 0x0500

UNICODE = True
if WINVER < 0x0400:
	UNICODE = False
