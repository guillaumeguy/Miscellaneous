import numpy as np
        
class ROC_Point(object):
    def __init__(self,actual,predicted):
        ''' Method to initialize a ROC Curve with an observation'''
        self.true_positive = 0
        self.true_negative = 0
        self.false_positive= 0
        self.false_negative= 0        
        if actual and predicted:
            self.true_positive = 1
        elif not actual and not predicted:
            self.true_negative = 1
        elif not actual and  predicted:
            self.false_positive= 1
        elif actual and not predicted:
            self.false_negative= 1   
 
    def ROC_add(self, ROC_Point):    
        ''' Method to aggregate ROC Curve'''
        self.true_positive  += ROC_Point.true_positive
        self.true_negative  += ROC_Point.true_negative
        self.false_positive += ROC_Point.false_positive
        self.false_negative += ROC_Point.false_negative
        return self
    def printme(self):
        print 'true_positive ... ' + str(self.true_positive) + '\n'
        print 'true_negative ... ' + str(self.true_negative) + '\n'
        print 'false_positive... ' + str(self.false_positive) + '\n'
        print 'false_negative ...' + str(self.false_negative) + '\n'
