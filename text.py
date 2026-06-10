
import matplotlib.pyplot
import numpy
import scipy.special

class neuralNetwork:

    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes
        self.lr = learningrate
        self.wih = numpy.random.rand(self.hnodes, self.inodes) - 0.5
        self.who = numpy.random.rand(self.onodes, self.hnodes) - 0.5
        self.activation_function = lambda x: scipy.special.expit(x)
        pass

    def train(self, inputs_list, targets_list):

        inputs = numpy.array(inputs_list, ndmin=2).T
        targets = numpy.array(targets_list, ndmin=2).T
        hidden_inputs = numpy.dot(self.wih, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)
        final_inputs = numpy.dot(self.who, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)
        output_errors = targets - final_outputs
        hiddent_errors = numpy.dot(self.who.T, output_errors)

        self.who += self.lr * numpy.dot((output_errors * final_outputs*(1.0 - final_outputs) ), numpy.transpose(hidden_outputs))
        self.wih += self.lr * numpy.dot((hiddent_errors * hidden_outputs*(1.0 - hidden_outputs) ), numpy.transpose(inputs))

        pass

    def query(self, inputs_list):
        inputs = numpy.array(inputs_list, ndmin=2).T
        hidden_inputs = numpy.dot(self.wih, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)
        final_inputs = numpy.dot(self.who, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)
        return final_outputs



def functionTest():
    # deleme a function y = x^2
    inputs_list=[0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
    targets_list=[0.04, 0.09, 0.16, 0.25, 0.36, 0.49, 0.64]
    Net = neuralNetwork(inputnodes=7,hiddennodes=7,outputnodes=7,learningrate=0.25)
    trainNum=100000
    while trainNum>0:
        Net.train(inputs_list, targets_list)
        trainNum = trainNum-1
    print(Net.query(inputs_list))

    print("DONE!")


functionTest()

