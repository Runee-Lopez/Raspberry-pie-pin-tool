import os
import RPi.GPIO as GPIO
#模块区————————————————————————————————————————
cmm=['mode','cap','output']
mode=1#默认模式:BOARD
BOARD=[3,5,7,11,13,15,19,21,23,27,29,31,33,35,37,8,10,12,16,18,22,24,26,28,32,36,38,40]#BOARD模式的pin口
BCM=[2,3,4,17,27,22,10,9,11,0,5,6,13,19,14,15,18,23,24,25,8,7,1,12,16,20,21]
ava=[]#可用引脚列表
unava=[]#不可用引脚列表
#变量区----------------------------------------
def output(m,hl,p):#m为模式,hl为高/低电平,p为引脚
    if m==0:#模式为BOARD时
        try:
            GPIO.setwarnings(False)#取消"重复设置pin口为输出"警告
            GPIO.setup(p,GPIO.OUT)#设置对应pin口为输出
            if hl==0:#激活时
                GPIO.output(p,GPIO.HIGH)
                print(p,"--HIGH")
            if hl==1:#关闭时
                GPIO.output(p,GPIO.LOW)
                print(p,"--LOW")
        except:#失败时
            print("This pin is not available")
    if m==1:#模式为BOARD时
        try:
            GPIO.setwarnings(False)#取消"重复设置pin口为输出"警告
            GPIO.setup(p,GPIO.OUT)#设置对应pin口为输出
            if hl==0:#激活时
                ava.append(p)
                GPIO.output(p,GPIO.HIGH)
                print(p,"--HIGH")
            if hl==1:#关闭时
                GPIO.output(p,GPIO.LOW)
                print(p,"--LOW")
        except:#失败时
            print("This pin is not available")
def cheakallpin(m):#定义'cheakallpin'
    if m==0:#模式为BOARD时
        for i in BOARD:
            GPIO.setwarnings(False)#取消"重复设置pin口为输出"警告
            try:
                GPIO.setup(i,GPIO.OUT)
                ava.append(i)#加入到'可用'列表
            except:
                unava.append(i)#加入'不可用'列表
        print("BOARD")
        print("Available:",ava)#显示'可用'列表
        print("Not available",unava)#显示'可用'列表
        ava.clear()#清理'可用'列表
        unava.clear()#清理'不可用'列表
    if m==1:#模式为BCM时
        for o in BCM:
            GPIO.setwarnings(False)#取消"重复设置pin口为输出"警告
            try:
                GPIO.setup(o,GPIO.OUT)
                ava.append(o)#加入到'可用'列表
            except:
                unava.append(o)#加入到'不可用'列表
        print("BCM")
        print("Available:",ava)#显示'可用'列表
        print("Not available",unava)#显示'可用'列表
        ava.clear()#清理'可用'列表
        unava.clear()#清理'不可用'列表
#定义函数区--------------------------------------
try:
    while True:
        print(cmm)
        com_input=input(">>>")
        if com_input.find('output -h')!=-1:#寻找'高电平'关键命令
            if mode ==0:#模式为BOARDD时
                output(0,0,int(com_input[10:]))
            if mode ==1:#模式为BCM时
                print("BCM")
        elif com_input.find('output -l')!=-1:#寻找'低电平'关键命令
            if mode==0:#模式为BOARD时
                output(0,1,int(com_input[10:]))
            if mode==1:#模式为BCM时
                print("BCM")
#固定命令区
        elif com_input in cmm:
            if com_input=="mode":#切换模式
                if mode==0:#BOARD
                    GPIO.setmode(GPIO.BOARD)
                    print("Mode:BOARD")
                elif mode==1:#BCM
                    GPIO.setmode(GPIO.BCM)
                    print("Mode:BCM")
            elif com_input=="cap":#添加cap:检查所有pin口
                if mode==0:#模式为BOARD时
                    print("BOARD")
                    cheakallpin(0)
                elif mode==1:#模式为BCM时
                    print("BCM")
                    cheakallpin(1)
            elif com_input=="output":
                print("output -h |Set pin to high level")
                print("output -l |Set pin to low level")
        else:
            print("Not Found")
except:
    print("Exit")
