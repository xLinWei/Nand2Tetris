# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 20:33:26 2019

@author: Lin
"""

import sys
import re

comp_dict={'0':'0101010','1':'0111111','-1':'0111010',
           'D':'0001100','A':'0110000','M':'1110000',
           '!D':'0001101','!A':'0110001','!M':'1110001',
           '-D':'0001111','-A':'0110011','-M':'1110011',
           'D+1':'0011111','A+1':'0110111','M+1':'1110111',
           'D-1':'0001110','A-1':'0110010','M-1':'1110010',
           'D+A':'0000010','D+M':'1000010','D-A':'0010011','D-M':'1010011',
           'A-D':'0000111','M-D':'1000111','D&A':'0000000','D&M':'1000000',
           'D|A':'0010101','D|M':'1010101'}

dist_dict={'':'000','M':'001','D':'010','MD':'011',
           'A':'100','AM':'101','AD':'110','AMD':'111'}

jump_dict={'':'000','JGT':'001','JEQ':'010','JGE':'011',
           'JLT':'100','JNE':'101','JLE':'110','JMP':'111'}

symbol_dict={'R0':0,'R1':1,'R2':2,'R3':3,'R4':4,'R5':5,'R6':6,'R7':7,'R8':8,
             'R9':9,'R10':10,'R11':11,'R12':12,'R13':13,'R14':14,'R15':15,
             'SCREEN':16384,'KBD':24576,'SP':0,'LCL':1,'ARG':2,'THIS':3,'THAT':4}

line_num=0 #行号
var_index=16 #变量起始地址

def pre_process1(line):
    global line_num#将line_num声明为全局变量
    if line=='':
        pass
    elif line.startswith('//'):
        pass
    elif line.startswith('('):#处理（...）的行
        label=line[1:-1]
        symbol_dict[label]=line_num
    else:
        line_num=line_num+1

            
def pre_process2(line):
    global var_index#将var_index声明为全局变量
    if line.startswith('@') and not(line[1:].isdigit()):#@后面有非数字字符的行
        var=line[1:]
        if var in symbol_dict:
            pass
        else:
            symbol_dict[var]=var_index
            var_index=var_index+1
        
        
def process(line):
    if line=='':
        pass
    elif line.startswith('//'):
        pass
    elif line.startswith('('):
        pass
    elif line.startswith('@'):
        if not(line[1:].isdigit()):
            symbol=line[1:]
            value=symbol_dict[symbol]
        else:
            value=line[1:]
        code='{:016b}'.format(int(value))#转成16位二进制，高位补零
        f.write(code+'\n')
    else:
        str1=line.split(';')
        if len(str1)==1:
            jump=''
        else:
            jump=str1[1]
        str2=str1[0].split('=')
        if len(str2)==1:
            dest=''
            comp=str2[0]
        else:
            dest=str2[0]
            comp=str2[1]
        code='111'+comp_dict[comp]+dist_dict[dest]+jump_dict[jump]
        f.write(code+'\n')
        

file=sys.argv[1]
filename=file.split('.')[0]
f=open(filename+'.hack','w')
for line in open(file):
    line = re.sub(r'//.*$', "", line)#re.sub用于替换字符串中的匹配项,这里将注释替换成空格
    line=line.strip()#去除开头和末尾的空白
    pre_process1(line)#预处理1，将label添加到symbol_dict
    
for line in open(file):
    line = re.sub(r'//.*$', "", line)#re.sub用于替换字符串中的匹配项,这里将注释替换成空格
    line=line.strip()#去除开头和末尾的空白
    pre_process2(line)#预处理2，将var添加到symbol_dict
    
for line in open(file):#开始编译
    line = re.sub(r'//.*$', "", line)#re.sub用于替换字符串中的匹配项,这里将注释替换成空格
    line=line.strip()#去除开头和末尾的空白
    process(line)
    
f.close()