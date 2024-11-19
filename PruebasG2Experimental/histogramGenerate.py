import numpy as np
import matplotlib.pyplot as plt

class PulsesHistogram():
    def __init__(self,stopNumber,binWidth, upperLimit, pathFile, saveimage):
        self.stopNumber = stopNumber
        self.binWidth = binWidth
        self.upperLimit = upperLimit
        self.pathFile=pathFile
        self.saveimage=saveimage
        
    


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
        
    def createHistogram(self, histogramArray):
        # Calculate mean, standard deviation, min, and max
        escalaUnidades=self.obtenerEscala(histogramArray)
        unidades=escalaUnidades[0]
        factorDivision=escalaUnidades[1]
        for i in range(len(histogramArray)):
            newValue=histogramArray[i]/factorDivision
            histogramArray[i]=newValue
        avgHist = np.mean(histogramArray)
        desvEst = np.std(histogramArray)
        min_val = min(histogramArray)
        max_val = max(histogramArray)
        
        # Define bins
        normalizedBin=self.binWidth/factorDivision
        bins = np.arange(min_val, max_val + normalizedBin, normalizedBin)
        hist, bin_edges = np.histogram(histogramArray, bins=bins)
        hist=hist[:-1]
        bin_edges= bin_edges[:-1]
        
        # Plot histogram
        plt.figure(figsize=(12, 10))
        plt.plot(bin_edges[:-1], hist, color='blue', linestyle='-', linewidth=2)
        valueX=bin_edges[:-1]
        # Add vertical line for mean
        plt.axvline(avgHist, color='red', linestyle='--', linewidth=1.5, label=f'Mean ({avgHist:.2f})')
        
        # Add horizontal bar for standard deviation at the mean
        plt.hlines(y=hist.max() * 0.9, xmin=avgHist - desvEst, xmax=avgHist + desvEst, color='green', linewidth=1.5, label=f'Std Dev ({desvEst:.2f})')
        
        # Mark min and max values with points on the histogram
        min_index = np.argmin(hist)
        max_index = np.argmax(hist)
        plt.scatter( [valueX[min_index], valueX[max_index]], [min(hist), max(hist)],color='purple', marker='o', label=f'Min ({min_val}) / Max ({max_val})')
        
        # Add labels and title with rounded values
        plt.xlabel('Time ('+unidades+')')
        plt.ylabel('Frequency')
        valueA= str(avgHist)+" "+unidades
        valueB= str(desvEst)+" "+unidades
        plt.title(f'Data Difference Histogram | Mean: {avgHist:.2f} {unidades}, Std Dev: {desvEst:.2f} {unidades}, Min: {min_val}, Max: {max_val}')
        plt.ylim(bottom=0)
        
        # Add legend
        plt.legend()
        
        # Save and show plot
        plt.savefig(self.saveimage)
        plt.show()
        
    def obtenerEscala(self,values):
        max_value = max(values)
        if max_value > 10**9:
            return ("ms", 10**9)
        elif max_value > 10**6:
            return ("us", 10**6)
        elif max_value > 10**3:
            return ("ns", 10**3)
        else:
            return ("ps", 1)

objetoGraficar= PulsesHistogram(5,500000,4000000000,'40000Pulsos24MHZ/Histograma4000024Mhz.txt',"40000Pulsos24MHZ/DataAllStops.png")
dataOneStop = objetoGraficar.readDataOneStop()
dataAllStops = objetoGraficar.readDataAllStops()
objetoGraficar.createHistogram(dataAllStops)

objetoGraficar= PulsesHistogram(5,500000,4000000000,'40000Pulsos24MHZ/Histograma4000024Mhz.txt',"40000Pulsos24MHZ/Data5Stop.png")
dataOneStop = objetoGraficar.readDataOneStop()
dataAllStops = objetoGraficar.readDataAllStops()
objetoGraficar.createHistogram(dataOneStop)

objetoGraficar= PulsesHistogram(4,500000,4000000000,'40000Pulsos24MHZ/Histograma4000024Mhz.txt',"40000Pulsos24MHZ/Data4Stop.png")
dataOneStop = objetoGraficar.readDataOneStop()
dataAllStops = objetoGraficar.readDataAllStops()
objetoGraficar.createHistogram(dataOneStop)

objetoGraficar= PulsesHistogram(3,500000,4000000000,'40000Pulsos24MHZ/Histograma4000024Mhz.txt',"40000Pulsos24MHZ/Data3Stop.png")
dataOneStop = objetoGraficar.readDataOneStop()
dataAllStops = objetoGraficar.readDataAllStops()
objetoGraficar.createHistogram(dataOneStop)

objetoGraficar= PulsesHistogram(2,500000,4000000000,'40000Pulsos24MHZ/Histograma4000024Mhz.txt',"40000Pulsos24MHZ/Data2Stop.png")
dataOneStop = objetoGraficar.readDataOneStop()
dataAllStops = objetoGraficar.readDataAllStops()
objetoGraficar.createHistogram(dataOneStop)

objetoGraficar= PulsesHistogram(1,500000,4000000000,'40000Pulsos24MHZ/Histograma4000024Mhz.txt',"40000Pulsos24MHZ/Data1Stop.png")
dataOneStop = objetoGraficar.readDataOneStop()
dataAllStops = objetoGraficar.readDataAllStops()
objetoGraficar.createHistogram(dataOneStop)


objetoGraficar= PulsesHistogram(5,500000,200000000,'40000Pulsos24MHZ/Histograma4000024Mhz.txt',"40000Pulsos24MHZ/Data5StopZoom.png")
dataOneStop = objetoGraficar.readDataOneStop()
dataAllStops = objetoGraficar.readDataAllStops()
objetoGraficar.createHistogram(dataOneStop)

objetoGraficar= PulsesHistogram(4,500000,200000000,'40000Pulsos24MHZ/Histograma4000024Mhz.txt',"40000Pulsos24MHZ/Data4StopZoom.png")
dataOneStop = objetoGraficar.readDataOneStop()
dataAllStops = objetoGraficar.readDataAllStops()
objetoGraficar.createHistogram(dataOneStop)

objetoGraficar= PulsesHistogram(3,500000,200000000,'40000Pulsos24MHZ/Histograma4000024Mhz.txt',"40000Pulsos24MHZ/Data3StopZoom.png")
dataOneStop = objetoGraficar.readDataOneStop()
dataAllStops = objetoGraficar.readDataAllStops()
objetoGraficar.createHistogram(dataOneStop)

objetoGraficar= PulsesHistogram(2,500000,200000000,'40000Pulsos24MHZ/Histograma4000024Mhz.txt',"40000Pulsos24MHZ/Data2StopZoom.png")
dataOneStop = objetoGraficar.readDataOneStop()
dataAllStops = objetoGraficar.readDataAllStops()
objetoGraficar.createHistogram(dataOneStop)

objetoGraficar= PulsesHistogram(1,500000,200000000,'40000Pulsos24MHZ/Histograma4000024Mhz.txt',"40000Pulsos24MHZ/Data1StopZoom.png")
dataOneStop = objetoGraficar.readDataOneStop()
dataAllStops = objetoGraficar.readDataAllStops()
objetoGraficar.createHistogram(dataOneStop)


objetoGraficar= PulsesHistogram(5,300000,140000000,'40000Pulsos24MHZ/Histograma4000024Mhz.txt',"40000Pulsos24MHZ/DataConfident0.3us.png")
dataOneStop = objetoGraficar.readDataOneStop()
dataAllStops = objetoGraficar.readDataAllStops()
objetoGraficar.createHistogram(dataAllStops)

objetoGraficar= PulsesHistogram(5,200000,140000000,'40000Pulsos24MHZ/Histograma4000024Mhz.txt',"40000Pulsos24MHZ/DataConfident0.2us.png")
dataOneStop = objetoGraficar.readDataOneStop()
dataAllStops = objetoGraficar.readDataAllStops()
objetoGraficar.createHistogram(dataAllStops)

objetoGraficar= PulsesHistogram(5,100000,140000000,'40000Pulsos24MHZ/Histograma4000024Mhz.txt',"40000Pulsos24MHZ/DataConfident0.1us.png")
dataOneStop = objetoGraficar.readDataOneStop()
dataAllStops = objetoGraficar.readDataAllStops()
objetoGraficar.createHistogram(dataAllStops)

objetoGraficar= PulsesHistogram(5,50000,140000000,'40000Pulsos24MHZ/Histograma4000024Mhz.txt',"40000Pulsos24MHZ/DataConfident0.05us.png")
dataOneStop = objetoGraficar.readDataOneStop()
dataAllStops = objetoGraficar.readDataAllStops()
objetoGraficar.createHistogram(dataAllStops)






    