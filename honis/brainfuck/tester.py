# クッソ適当なテストスクリプトです
from brain import *

code = """
++++[>+++++[>+++<-]<-]>+++++[>>+>++>+++>++++>+++++>++++++[<]>-]>[>[+>]<-[<]>-]>>>.++++.---->>.++++.----<<<<.>>>++++..----<<<++++.---->>>++++.---->.<<.<<.>+++.--->++.--<<.>>>+++.--->.<<
"""
long_onlyover16bit_code = """
>>++++++++[>++++++++[<<++++>>-]<-]<[>++++[>++++++++[<<<++++>>>-]<-]<-]+<[+>-<[>+<---]>>>++++++++++++[<+++++++++++[<+++++++++++>-]>-]<+++++[<----->-]<++>>>+++++[<++++++>-]+++++[<++++++++++>-]<--->>+++++[<+++++++>-]>+++++[<+++>-]<---->>+++++[<+++>-]>+++++[<++++++>-]+++++[<++++++++++>-]<---->>+++++[<++++++>-]+++++[<+++++++++++>-]<-->>+++++[<+++++++>-]<-->>+++++[<++++++>-]+++++[<++>-]<->>+++++[<+++++>-]>+++++[<++++++>-]+++++[<+++++++>-]<--->>+++++[<++++++>-]+++++[<+++++++++>-]<[<]>[[<+<+>>-]<<.>[<->-]>>[[<+>-]>]<<[<]>]<]>[[-]<++++[>+++++[>+++<-]<-]>+++++[>>+>++>+++>++++>+++++>++++++[<]>-]>[>[+>]<-[<]>-]>>>>>.<<+++.---<<+++.+.---->>>++.-->>++.+++++++++++++++++.-------------------<<<<<-----------.+++++++++++>>>>>++.--<<<<<+.->+++.--->>++++.---->>++.--<<<<<+++.+.---->>>++++.----<<<++++.--.-->>>++++.----[<]]
"""

brain(code)
# KOUYATTETUKAIMASU

print()

print(len(brain(code, retmode=True)))
# 17
brain(code, stepmode=True)
#
# ++++[>+++++[>+++<-]<-]>+++++[>>+>++>+++>++++>+++++>++++++[<]>-]>[>[+>]<-[<]>-]>>>.++++.---->>.++++.----<<<<.>>>++++..----<<<++++.---->>>++++.---->.<<.<<.>+++.--->++.--<<.>>>+++.--->.<<
# 
# codeat;184 codein;< step;2940 nowpoint;5 point;[0, 0, 0, 65, 70, 75, 80, 85, 30, 0] output;[KOUYATTETUKAIMASU]
brain(code, debug=True)
#
# ++++[>+++++[>+++<-]<-]>+++++[>>+>++>+++>++++>+++++>++++++[<]>-]>[>[+>]<-[<]>-]>>>.++++.---->>.++++.----<<<<.>>>++++..----<<<++++.---->>>++++.---->.<<.<<.>+++.--->++.--<<.>>>+++.--->.<<
#
# KOUYATTETUKAIMASU
#
# 5
# [0, 0, 0, 65, 70, 75, 80, 85, 30, 0]
brain(long_onlyover16bit_code)
# UNDER 16 BIT DETECT
print()
brain(long_onlyover16bit_code, sizebit=16)
# ろっかくれんちですまる
print()
try:
    brain(long_onlyover16bit_code, sizemem=5)
except PointError as e:
    print(e)
    # Pointer too increment
try:
    brain("<")
except PointError as e:
    print(e)
    # Pointer too decrement
for i in brain(code, yiemode=True):
    print(i["output"], end="")
# KOUYATTETUKAIMASU
print()
brain(",.,.", speinp="aiueo")
# ai
print()
for i in brain(code, yiemode=True, debug=True):
    print(i["output"],end="")
# KOUYATTETUKAIMASU
print()
for i in brain(code, yiemode=True, stepmode=True):
    print(str(i["codeat"])+"\r", end="")
# 184
print()
print(len(brain(code, yiemode=True, stepmode=True, debug=True)))
# 2940
print(brain(code, retmode=True, yiemode=True, debug=True, stepmode=True))
# KOUYATTETUKAIMASU
print(len(brain(long_onlyover16bit_code ,yiemode=True ,stepmode=True, steptime=1, sizebit=16)))
# 215789
brain(code, debug=True, stepmode=True)
#
# ++++[>+++++[>+++<-]<-]>+++++[>>+>++>+++>++++>+++++>++++++[<]>-]>[>[+>]<-[<]>-]>>>.++++.---->>.++++.----<<<<.>>>++++..----<<<++++.---->>>++++.---->.<<.<<.>+++.--->++.--<<.>>>+++.--->.<<
#
# codeat;184 codein;< step;2940 nowpoint;5 point;[0, 0, 0, 65, 70, 75, 80, 85, 30, 0] output;[KOUYATTETUKAIMASU]
#
# 5
# [0, 0, 0, 65, 70, 75, 80, 85, 30, 0]