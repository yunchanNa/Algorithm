Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import re

def solution(s):
    a = re.sub('zero','0',s)
    a = re.sub('one','1',a)
    a = re.sub('two','2',a)
    a = re.sub('three','3',a)
    a = re.sub('four','4',a)
    a = re.sub('five','5',a)
    a = re.sub('six','6',a)
    a = re.sub('seven','7',a)
    a = re.sub('eight','8',a)
    a = re.sub('nine','9',a)
    return int(a)