import numpy as np
import matplotlib.pyplot as plt

class PulsesHistogram():
    def __init__(self,stopNumber,binWidth, upperLimit, pathFile, saveimage, isg2, title):
        self.stopNumber = stopNumber
        self.binWidth = binWidth
        self.upperLimit = upperLimit
        self.pathFile=pathFile
        self.saveimage=saveimage
        self.isg2= isg2
        self.title = title 
        
    


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
        if not self.isg2:
                
            # Add vertical line for mean
            plt.axvline(avgHist, color='red', linestyle='--', linewidth=1.5, label=f'Mean ({avgHist:.2f})')
            
            # Add horizontal bar for standard deviation at the mean
            plt.hlines(y=hist.max() * 0.9, xmin=avgHist - desvEst, xmax=avgHist + desvEst, color='green', linewidth=1.5, label=f'Std Dev ({desvEst:.2f})')
        else:
            avgFrequency=np.mean(hist)
            desvestFrequency=np.std(hist)
            plt.axhline(avgFrequency, color='red', linestyle='--', linewidth=1.5, label=f'Mean Freq: ({avgHist:.2f})')
            plt.vlines(x=np.mean(histogramArray), ymin=avgFrequency - desvestFrequency, ymax=avgFrequency + desvestFrequency, color='green', linewidth=4, label=f'Std Dev ({desvestFrequency:.2f})')
            avgHist=avgFrequency
            desvEst=desvestFrequency

        # Mark min and max values with points on the histogram
        min_index = np.argmin(hist)
        max_index = np.argmax(hist)
        plt.scatter( [valueX[min_index], valueX[max_index]], [min(hist), max(hist)],color='purple', marker='o', label=f'Min ({valueX[min_index]}) / Max ({valueX[max_index]})')
        
        # Add labels and title with rounded values
        plt.xlabel('Time ('+unidades+')')
        plt.ylabel('Frequency')
        plt.title(self.title)
        valueA= str(avgHist)+" "+unidades
        valueB= str(desvEst)+" "+unidades
        if not self.isg2:
            plt.title(f'Graphic:{self.title} | Mean: {avgHist:.2f} {unidades}, Std Dev: {desvEst:.2f} {unidades}, Min: {valueX[min_index]}, Max: {valueX[max_index]}')
        else:
            plt.title(f'Graphic:{self.title} | Mean: {avgHist:.2f}, Std Dev: {desvEst:.2f}, Min: {valueX[min_index]}, Max: {valueX[max_index]}')
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

objetoGraficar= PulsesHistogram(5,2000000,4000000000,'40000Pulsos24MHZ/Histograma4000024Mhz.txt',"40000Pulsos24MHZ/DataAllStops.png", False, "All Stops 20000 pulses 24Mhz")
dataOneStop = objetoGraficar.readDataOneStop()
dataAllStops = objetoGraficar.readDataAllStops()
objetoGraficar.createHistogram(dataAllStops)

objetoGraficar= PulsesHistogram(5,2000000,4000000000,'40000Pulsos24MHZ/Histograma4000024Mhz.txt',"40000Pulsos24MHZ/Data5Stop.png", False, "Stop 5 20000 pulses 24Mhz")
dataOneStop = objetoGraficar.readDataOneStop()
dataAllStops = objetoGraficar.readDataAllStops()
objetoGraficar.createHistogram(dataOneStop)

objetoGraficar= PulsesHistogram(4,2000000,4000000000,'40000Pulsos24MHZ/Histograma4000024Mhz.txt',"40000Pulsos24MHZ/Data4Stop.png", False, "Stop 4 20000 pulses 24Mhz")
dataOneStop = objetoGraficar.readDataOneStop()
dataAllStops = objetoGraficar.readDataAllStops()
objetoGraficar.createHistogram(dataOneStop)

objetoGraficar= PulsesHistogram(3,2000000,4000000000,'40000Pulsos24MHZ/Histograma4000024Mhz.txt',"40000Pulsos24MHZ/Data3Stop.png" ,False, "Stop 3 20000 pulses 24Mhz")
dataOneStop = objetoGraficar.readDataOneStop()
dataAllStops = objetoGraficar.readDataAllStops()
objetoGraficar.createHistogram(dataOneStop)

objetoGraficar= PulsesHistogram(2,2000000,4000000000,'40000Pulsos24MHZ/Histograma4000024Mhz.txt',"40000Pulsos24MHZ/Data2Stop.png",False, "Stop 2 20000 pulses 24Mhz")
dataOneStop = objetoGraficar.readDataOneStop()
dataAllStops = objetoGraficar.readDataAllStops()
objetoGraficar.createHistogram(dataOneStop)

objetoGraficar= PulsesHistogram(1,2000000,4000000000,'40000Pulsos24MHZ/Histograma4000024Mhz.txt',"40000Pulsos24MHZ/Data1Stop.png",False, "Stop 1 20000 pulses 24Mhz")
dataOneStop = objetoGraficar.readDataOneStop()
dataAllStops = objetoGraficar.readDataAllStops()
objetoGraficar.createHistogram(dataOneStop)


objetoGraficar= PulsesHistogram(5,200000,200000000,'40000Pulsos24MHZ/Histograma4000024Mhz.txt',"40000Pulsos24MHZ/Data5StopZoom.png",False, "Stop 5 Zoom 20000 pulses 24Mhz")
dataOneStop = objetoGraficar.readDataOneStop()
dataAllStops = objetoGraficar.readDataAllStops()
objetoGraficar.createHistogram(dataOneStop)

objetoGraficar= PulsesHistogram(4,200000,200000000,'40000Pulsos24MHZ/Histograma4000024Mhz.txt',"40000Pulsos24MHZ/Data4StopZoom.png",False, "Stop 4 Zoom 20000 pulses 24Mhz")
dataOneStop = objetoGraficar.readDataOneStop()
dataAllStops = objetoGraficar.readDataAllStops()
objetoGraficar.createHistogram(dataOneStop)

objetoGraficar= PulsesHistogram(3,200000,200000000,'40000Pulsos24MHZ/Histograma4000024Mhz.txt',"40000Pulsos24MHZ/Data3StopZoom.png",False, "Stop 3 Zoom 20000 pulses 24Mhz")
dataOneStop = objetoGraficar.readDataOneStop()
dataAllStops = objetoGraficar.readDataAllStops()
objetoGraficar.createHistogram(dataOneStop)

objetoGraficar= PulsesHistogram(2,200000,200000000,'40000Pulsos24MHZ/Histograma4000024Mhz.txt',"40000Pulsos24MHZ/Data2StopZoom.png",False, "Stop 2 Zoom 20000 pulses 24Mhz")
dataOneStop = objetoGraficar.readDataOneStop()
dataAllStops = objetoGraficar.readDataAllStops()
objetoGraficar.createHistogram(dataOneStop)

objetoGraficar= PulsesHistogram(1,200000,200000000,'40000Pulsos24MHZ/Histograma4000024Mhz.txt',"40000Pulsos24MHZ/Data1StopZoom.png",False, "Stop 1 Zoom 20000 pulses 24Mhz")
dataOneStop = objetoGraficar.readDataOneStop()
dataAllStops = objetoGraficar.readDataAllStops()
objetoGraficar.createHistogram(dataOneStop)


objetoGraficar= PulsesHistogram(5,300000,144500000,'40000Pulsos24MHZ/Histograma4000024Mhz.txt',"40000Pulsos24MHZ/DataConfident0.3us.png",True, "g2 0.3 us bin size")
dataOneStop = objetoGraficar.readDataOneStop()
dataAllStops = objetoGraficar.readDataAllStops()
objetoGraficar.createHistogram(dataAllStops)

objetoGraficar= PulsesHistogram(5,200000,144500000,'40000Pulsos24MHZ/Histograma4000024Mhz.txt',"40000Pulsos24MHZ/DataConfident0.2us.png",True, "g2 0.2 us bin size")
dataOneStop = objetoGraficar.readDataOneStop()
dataAllStops = objetoGraficar.readDataAllStops()
objetoGraficar.createHistogram(dataAllStops)

objetoGraficar= PulsesHistogram(5,100000,144500000,'40000Pulsos24MHZ/Histograma4000024Mhz.txt',"40000Pulsos24MHZ/DataConfident0.1us.png",True, "g2 0.1 us bin size")
dataOneStop = objetoGraficar.readDataOneStop()
dataAllStops = objetoGraficar.readDataAllStops()
objetoGraficar.createHistogram(dataAllStops)

objetoGraficar= PulsesHistogram(5,50000,144500000,'40000Pulsos24MHZ/Histograma4000024Mhz.txt',"40000Pulsos24MHZ/DataConfident0.05us.png",True, "g2 0.05 us bin size")
dataOneStop = objetoGraficar.readDataOneStop()
dataAllStops = objetoGraficar.readDataAllStops()
objetoGraficar.createHistogram(dataAllStops)





