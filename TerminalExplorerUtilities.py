class colors:
	BLACK='\x1b[30m'
	RED = '\x1b[31m'
	GREEN = '\x1b[32m'
	YELLOW = '\x1b[33m'
	BLUE = '\x1b[34m'
	MAGENTA = '\x1b[35m'
	CYAN = '\x1b[36m'
	WHITE = '\x1b[37m'

	BLACKBG='\x1b[40m'
	REDBG = '\x1b[41m'
	GREENBG = '\x1b[42m'
	YELLOWBG = '\x1b[43m'
	BLUEBG = '\x1b[44m'
	MAGENTABG = '\x1b[45m'
	CYANBG = '\x1b[46m'
	WHITEBG = '\x1b[47m'		
	
	NOCOL = '\x1b[0m'

def colorify(item,color):

	if color=="black":
		return "%s%s%s%s"%(colors.BLACK,colors.BLACKBG,item,colors.NOCOL)
	if color=="red":
		return "%s%s%s%s"%(colors.RED,colors.REDBG,item,colors.NOCOL)
	if color=="green":
		return "%s%s%s%s"%(colors.GREEN,colors.GREENBG,item,colors.NOCOL)
	if color=="yellow":
		return "%s%s%s%s"%(colors.YELLOW,colors.YELLOWBG,item,colors.NOCOL)
	if color=="blue":
		return "%s%s%s%s"%(colors.BLUE,colors.BLUEBG,item,colors.NOCOL)
	if color=="magenta":
		return "%s%s%s%s"%(colors.MAGENTA,colors.MAGENTABG,item,colors.NOCOL)
	if color=="cyan":
		return "%s%s%s%s"%(colors.CYAN,colors.CYANBG,item,colors.NOCOL)
	if color=="white":
		return "%s%s%s%s"%(colors.WHITE,colors.WHITEBG,item,colors.NOCOL)