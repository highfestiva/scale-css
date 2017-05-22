#!/usr/bin/env python3

import re
import sys

scale = eval(sys.argv[1])

def scale_pixels(match):
	f = float(match.group(1)) * scale
	return '%g%s' % (f, match.group(0)[-2:])

txt = sys.stdin.read()
txt = re.sub(r'(\d+(\.)?\d*)(px|em|pt|cm|in)', scale_pixels, txt)
print(txt, end='')
