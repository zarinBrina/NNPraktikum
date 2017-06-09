# -*- coding: utf-8 -*-

"""
Activation functions which can be used within neurons.
"""

from numpy import exp
from numpy import divide


class Activation:
    """
    Containing various activation functions and their derivatives
    """

    @staticmethod
    def sign(netOutput, threshold=0):
        return netOutput >= threshold

    @staticmethod
    def sigmoid(netOutput):
        #return 1 / (1 + np.exp(-netOutput))
        
    @staticmethod
    def sigmoidPrime(netOutput):
        # Here you have to code the derivative of sigmoid function
        # return netOutput.*(1-netOutput)
        
    @staticmethod
    def tanh(netOutput):
        # return np.tanh(netOutput)
                
    @staticmethod
    def tanhPrime(netOutput):
        # Here you have to code the derivative of tanh function
        # return (1 - (netOutput ** 2))
      
    @staticmethod
    def rectified(netOutput):
        return lambda x: max(0.0, x)

    @staticmethod
    def rectifiedPrime(netOutput):
        # Here you have to code the derivative of rectified linear function
        # if netOutput > 0:
        #   return netOutput = 1
        # else:
        #   return netOutput = 0
       
         
    @staticmethod
    def identity(netOutput):
        return lambda x: x

    @staticmethod
    def identityPrime(netOutput):
        # Here you have to code the derivative of identity function
        # return 1
       
    @staticmethod
    def softmax(netOutput):      
        # Here you have to code the softmax function
        #    e = np.exp(numpy.array(netOutput))
        # dist = e / np.sum(e)
        # return dist
        

    @staticmethod
    def getActivation(str):
        """
        Returns the activation function corresponding to the given string
        """

        if str == 'sigmoid':
            return Activation.sigmoid
        elif str == 'softmax':
            return Activation.softmax
        elif str == 'tanh':
            return Activation.tanh
        elif str == 'relu':
            return Activation.rectified
        elif str == 'linear':
            return Activation.identity
        else:
            raise ValueError('Unknown activation function: ' + str)

    @staticmethod
    def getDerivative(str):
        """
        Returns the derivative function corresponding to a given string which
        specify the activation function
        """

        if str == 'sigmoid':
            return Activation.sigmoidPrime
        elif str == 'tanh':
            return Activation.tanhPrime
        elif str == 'relu':
            return Activation.rectifiedPrime
        elif str == 'linear':
            return Activation.identityPrime
        else:
            raise ValueError('Cannot get the derivative of'
                             ' the activation function: ' + str)
