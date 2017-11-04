# encoding:utf-8
'''
Created on 2017年10月19日
题目：模仿静态变量(static)另一案例。
@author: wangtaoyuan
'''
class Num:
    nNum = 1
    def inc(self):
        self.nNum += 1
        print 'nNum = %d' % self.nNum
        
if __name__ == '__main__':
    nNum = 100
    inst = Num()#为类Num赋予类名inst
    for i in range(3):
        nNum += 1
        print 'The num = %d' % nNum
        inst.inc()