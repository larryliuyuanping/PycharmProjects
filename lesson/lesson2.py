# -*- coding:utf-8 -*-

#请实现一个电脑的类，分别主机类、显示器类、鼠标类组成，
#主机类、显示器类、鼠标类分别有品牌和价格的公有属性，
#主机类有电源，显示器有分辨率，鼠标有有线或无线的特有属性，
#请实现电脑类的两个公有对象方法，一个可以获得电脑的总价格，一个显示电脑配置的函数。
#“我的显示器是xx品牌，主机是xx品牌，”
#要求，主机类、显示器类、鼠标类和键盘类要使用继承的方法。

class Device():
    def __init__(self, band, price):

        self.__band = band
        self.__price = price

    def get_price(self):
        return self.__price

    def get_band(self):
        return self.__band

class Master(Device):#主机类
    def __init__(self,band, price, power):
        super().__init__(band, price)
        self.__power = power

class Display(Device):#显示器类
    def __init__(self,band, price, px):
        super().__init__(band, price)
        self.__px = px

class Mouse(Device):#鼠标类
    def __init__(self,band, price, wire):
        super().__init__(band, price)
        self.__wire = wire


class Computer():

    def __init__(self,master,display,mouse):
        self.__master = master
        self.__display = display
        self.__mouse = mouse

    def get_price(self):
        return self.__master.get_price() + self.__display.get_price() + self.__mouse.get_price()

    def get_info(self):
        return "主机是：" + self.__master.get_band() +  ",显示器是:" + self.__display.get_band() + ",鼠标是："+ self.__mouse.get_band()


master = Master("苹果",8888,"电源1")
display = Display("三星",3000,"1024*768")
mouse = Mouse("罗技",600,"有线")

computer = Computer(master, display, mouse)

print(computer.get_price())

print(computer.get_info())
