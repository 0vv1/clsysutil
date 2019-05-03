#!/usr/bin/env  python
# filename:     ${SCR_DIR}/clsysutil.py
# purpose:      show essential system infos with Unicode symbols in terminal
# author:       (c) Alexander Puls
# bug reports:  see https://github.com/0vv1
# license:      This program is licensed under the GPL v3.
############################################################################
# note:         Needs a font patched with Nerd Font patches to show the
#               correct Unicode symbols. See https://nerdfonts.com.
############################################################################

import psutil
import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

cpu_load = psutil.cpu_percent(interval=1)
cpu_freq = psutil.cpu_freq(False)
mem = psutil.virtual_memory().active

print (u'\uf303' + str(cpu_load) + "%" + ' ' + u'\uf21e' + str(round(cpu_freq[0] / 1000, 1)) + "GHz" + ' ' + u'\ue28c' + str(mem / 1024 ** 2) + "MB")

# EOF clsysutil.py ##########################################################
