class colors:
	BLACK='\x1b[30m'
	RED = '\x1b[31m'
	GREEN = '\x1b[32m'
	YELLOW = '\x1b[33m'
	BLUE = '\x1b[34m'
	MAGENTA = '\x1b[35m'
	CYAN = '\x1b[36m'
	WHITE = '\x1b[37m'

	#High Intensities
	HIGH_BLACK='\x1b[90m'
	HIGH_RED = '\x1b[91m'
	HIGH_GREEN = '\x1b[92m'
	HIGH_YELLOW = '\x1b[93m'
	HIGH_BLUE = '\x1b[94m'
	HIGH_MAGENTA = '\x1b[95m'
	HIGH_CYAN = '\x1b[96m'
	HIGH_WHITE = '\x1b[97m'

	BOLDRED='\x1b[1m'

	BLACKBG='\x1b[40m'
	REDBG = '\x1b[41m'
	GREENBG = '\x1b[42m'
	YELLOWBG = '\x1b[43m'
	BLUEBG = '\x1b[44m'
	MAGENTABG = '\x1b[45m'
	CYANBG = '\x1b[46m'
	WHITEBG = '\x1b[47m'

	#High Intensities
	HIGH_BLACKBG='\x1b[100m'
	HIGH_REDBG = '\x1b[101m'
	HIGH_GREENBG = '\x1b[102m'
	HIGH_YELLOWBG = '\x1b[103m'
	HIGH_BLUEBG = '\x1b[104m'
	HIGH_MAGENTABG = '\x1b[105m'
	HIGH_CYANBG = '\x1b[106m'
	HIGH_WHITEBG = '\x1b[107m'		
	
	NOCOL = '\x1b[0m'

	
	#Color Wheel

	#Foreground
	#for x in range(255):
	    #print("\033[38;5;%smOk%s\033[0;00m"%(x,x))
	#Background

class textattributes:
	BLINKING='\x1b[5m'
	UNDERLINED='\x1b[4m'
	REVERSE_BGFB='\x1b[7m'

def colorify(item,color,textonly=False):
	if textonly:
		if color=="black":
			return "%s%s%s"%(colors.BLACK,item,colors.NOCOL)
		elif color=="red":
			return "%s%s%s"%(colors.RED,item,colors.NOCOL)
		elif color=="green":
			return "%s%s%s"%(colors.GREEN,item,colors.NOCOL)
		elif color=="yellow":
			return "%s%s%s"%(colors.YELLOW,item,colors.NOCOL)
		elif color=="blue":
			return "%s%s%s"%(colors.BLUE,item,colors.NOCOL)
		elif color=="magenta":
			return "%s%s%s"%(colors.MAGENTA,item,colors.NOCOL)
		elif color=="cyan":
			return "%s%s%s"%(colors.CYAN,item,colors.NOCOL)
		elif color=="white":
			return "%s%s%s"%(colors.WHITE,item,colors.NOCOL)
	else:
		if color=="black":
			return "%s%s%s%s"%(colors.BLACK,colors.BLACKBG,item,colors.NOCOL)
		elif color=="red":
			return "%s%s%s%s"%(colors.RED,colors.REDBG,item,colors.NOCOL)
		elif color=="green":
			return "%s%s%s%s"%(colors.GREEN,colors.GREENBG,item,colors.NOCOL)
		elif color=="yellow":
			return "%s%s%s%s"%(colors.YELLOW,colors.YELLOWBG,item,colors.NOCOL)
		elif color=="blue":
			return "%s%s%s%s"%(colors.BLUE,colors.BLUEBG,item,colors.NOCOL)
		elif color=="magenta":
			return "%s%s%s%s"%(colors.MAGENTA,colors.MAGENTABG,item,colors.NOCOL)
		elif color=="cyan":
			return "%s%s%s%s"%(colors.CYAN,colors.CYANBG,item,colors.NOCOL)
		elif color=="white":
			return "%s%s%s%s"%(colors.WHITE,colors.WHITEBG,item,colors.NOCOL)
