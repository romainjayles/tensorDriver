import pyscreenshot as ImageGrab

RECORD_INTERVAL_MS = 100

RECORD_SCREEN_X1 = 10
RECORD_SCREEN_X2 = 510
RECORD_SCREEN_Y1 = 10
RECORD_SCREEN_Y2 = 510

def take_screenshot():
	print "take_screenshot"
	im=ImageGrab.grab(bbox=(RECORD_SCREEN_X1, RECORD_SCREEN_Y1, RECORD_SCREEN_X2, RECORD_SCREEN_Y2)) # X1,Y1,X2,Y2
	im.show()

def get_keyboard_use():
	print "get_keyboard_use"


if __name__ == '__main__':
    print "Hello"
    take_screenshot()
    get_keyboard_use()
