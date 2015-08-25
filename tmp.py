#encoding=utf-8
'''
Created on Aug 24, 2015

@author: lowitty
'''
import os
from PyProperties import Properties
if __name__ == '__main__':
    p = Properties(os.path.dirname(__file__) + os.path.sep + "test.properties")
    print p.getProperty('uuuu')
    p.setProperty('uuuu', 'tttt')
    print p.getProperty('uuuu')
    p.store()
    pass