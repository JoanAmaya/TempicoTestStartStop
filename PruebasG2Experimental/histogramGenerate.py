import numpy as np
import matplotlib.pyplot as plt

class PulsesHistogram():
    def __init__(self,stopNumber,binWidth, upperLimit, pathFile):
        self.stopNumber = stopNumber
        self.binWidth = binWidth
        self.upperLimit = upperLimit
        self.pathFile=pathFile
    


    def readDataOneStop(self):
        self.oneStopData = []
        with open(self.pathFile, 'r') as archivo:
            next(archivo)
            for linea in archivo:
                columnas = linea.strip().split()
                if int(columnas[0])<=self.upperLimit and int(columnas[1])==self.stopNumber:
                    self.oneStopData.append(int(columnas[0]))
        return self.oneStopData

    def readDataAllStops(self):
        self.datosLeidos = []
        with open(self.pathFile, 'r') as archivo:
            next(archivo)
            for linea in archivo:
                columnas = linea.strip().split()
                if (int(columnas[0])<= self.upperLimit):
                    self.datosLeidos.append(int(columnas[0]))
        return self.datosLeidos
        

    def createHistogram(self,histogramArray):
        min_val = min(histogramArray)
        max_val = max(histogramArray)
        bins = np.arange(min_val, max_val + self.binWidth,  self.binWidth)
        hist, bin_edges = np.histogram(histogramArray, bins=bins)
        plt.figure(figsize=(12, 10))
        plt.plot(bin_edges[:-1], hist, color='blue', linestyle='-', linewidth=2)
        plt.xlabel('Time (ms)')
        plt.ylabel('Frequency')
        plt.title('Data difference histogram')
        plt.ylim(bottom=0)
        plt.savefig("40000PulsosPeriodicos/DataConfidentRange.02us.png")
        plt.show()

objetoGraficar= PulsesHistogram(1,20000,82500000,'40000PulsosPeriodicos/histograma.txt')
dataOneStop = objetoGraficar.readDataOneStop()
dataAllStops = objetoGraficar.readDataAllStops()
objetoGraficar.createHistogram(dataAllStops)



    