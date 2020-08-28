# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from scipy import stats


class Lambda_constant(object):
    def __init__(self,lambda_init):
        self.l=np.log(lambda_init)
    def get_lambda(self):
        return np.exp(self.l)
    def derivative(self):
        return np.exp(self.l)
    def update_l(self, dloss, learning_rate):
        self.l-=learning_rate*np.mean(dloss)*self.derivative()

class Absolute_loss(object):
    def __init__(self,predicted,actual):
        """
        caculates the loss through the equation above and saves it as self.loss
        predicted and actual are both also saved along with n
        """
        self.n=predicted.shape[0]
        self.predicted=predicted
        self.actual=actual
        self.loss=np.mean(np.abs(self.predicted-self.actual))
    
    def dloss(self):
        """
        returns an array where each value is dloss/di for i in range from 1 to n
        """
        return np.sign(self.predicted-self.actual)/self.n
    def get_loss(self):
        """
        returns self.loss
        """
        return self.loss

class model(object):
    def __init__(self,delta_cases,p_death_init,lambda_init):
        self.p_death=p_death_init
        
        self.Lambda=lambda_init
        self.new_cases=delta_cases
        self.hat_deaths=self.calculate_predicted_deaths(self.new_cases.shape[0]) 
        
    def calculate_predicted_deaths(self,n):
        """
        predicts the number of deaths for the first n days
        """
        p_death=self.p_death.get_p_death()
        
        Lambda=self.Lambda.get_lambda()
        
        p_array=np.zeros((n,n))
        for i in range(n):
            p_array+=np.diag(np.full((n-i,),stats.poisson.pmf(i,Lambda)),k=i)
        return np.matmul(np.multiply(p_death,self.new_cases),p_array)
    
    def dlambda(self):
        """
        gets the derivative (d hat_death)/(d_lambda)
        """
        n=self.new_cases.shape[0]
        p_death=self.p_death.get_p_death()
        Lambda=self.Lambda.get_lambda()
        p_array=np.zeros((n,n))
        for i in range(n):
            p_array+=np.diag(np.full((n-i,),(i/Lambda-1)*stats.poisson.pmf(i,Lambda)),k=i)
        return p_death*np.matmul(self.new_cases,p_array)
    
    def dp_death(self):
        """
        gets the derivative (d hat_death)/(d p_death)
        """
        return self.hat_deaths/self.p_death.get_p_death()
    
    def update(self,loss, learning_rate):
        dloss_dp_death=np.multiply(loss.dloss(),self.dp_death())
        dloss_dlambda=np.multiply(loss.dloss(),self.dlambda())
        
        
        
        self.p_death.update_p(dloss_dp_death,learning_rate)
        self.Lambda.update_l(dloss_dlambda,learning_rate)
        
        self.hat_deaths=self.calculate_predicted_deaths(self.new_cases.shape[0]) 
    
    def get_predicted_deaths(self):
        return self.hat_deaths

class Quadratic_loss(object):
    def __init__(self,predicted,actual):
        self.n=predicted.shape[0] #acutally this could also be actual.shape[0] since these two arrays
        #are supposed to be of the same shape.
        self.predicted=predicted
        self.actual=actual
        self.loss=np.sqrt(np.mean(np.square(self.predicted-self.actual)))
    def dloss(self):
        return (self.predicted-self.actual)/(self.n**2*self.loss)
    def get_loss(self):
        return self.loss