#
# The Tomosynthesis Image Class
#

import numpy as np
class TImage:
    
    # original variable
    dim = 0
    size_0 = 0
    size_1 = 0
    size_2 = 1
    data_type = None
    data = []
    sampled_data = []

    # derived variables
    patchesList = []
    feats = []

    predicts = []
 
    def __init__ (self, im = None):
        '''Initialization'''
        #self = im

        self.dim = 0
        self.size_0 = 0
        self.size_1 = 0
        self.size_2 = 1
        self.data_type = None
        self.data = []
        self.sampled_data = []
        
        self.patchesList = []
        self.feats = []

        self.predicts = []

    def setDim(self,dim):
        self.dim = dim

    def setSize(self, size_0, size_1, size_2):       
        self.size_0 = size_0
        self.size_1 = size_1
        self.size_2 = size_2

        self.patchesList = [None] * size_2
        self.feats = [None] * size_2

        self.predicts = [None] * size_2

    def setDataType(self,data_type):
        self.data_type = data_type

    def setData(self,data):
        self.data = data
        
    def getDim(self):
        return self.dim

    def getSize(self):
        return (self.size_0, self.size_1, self.size_2)

    def getDataType(self):
        return self.data_type

    def getData(self):
        return self.data

    def downSample(self, rate):

        rows = np.array(range(0,self.size_0,rate))
        cols = np.array(range(0,self.size_1,rate))
        
        for i in range(self.size_2):
            rs = self.data[i][rows,:]
            cs = rs[:,cols]
            self.sampled_data.append(cs)

            
class TImageSlice:
    
    LightPatchList = []
    predicts = None
    feats = None

    def __init__ (self):
        
        self.LightPatchList = []
        self.predicts = None
        self.feats = None
