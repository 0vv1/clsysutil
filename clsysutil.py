#!/usr/bin/env python

# @author   (c) 2019 Alexander Puls <https://0vv1.io>
# @license  GPL v3 <https://opensource.org/licenses/GPL-3.0>
# ----------------------------------------------------------

import psutil
import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

cpu_load = psutil.cpu_percent(interval=1)
cpu_freq = psutil.cpu_freq(False)
mem = psutil.virtual_memory().active

print (u'\uf303' + str(cpu_load) + "%" + ' ' + u'\uf21e' + str(round(cpu_freq[0] / 1000, 1)) + "GHz" + ' ' + u'\ue28c' + str(mem / 1024 ** 2) + "MB")

# EOF ${SCR_DIR}/clsysutil/clsysutil.py --------------------
