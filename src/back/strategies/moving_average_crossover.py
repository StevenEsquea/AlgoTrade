import io
import base64

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

from back.core.kernel import Strategy, Operation

STRATEGY_NAME = "Moving Average Cross"

class MovingAverageCross(Strategy):

    def __init__(self, low_period = None, high_period = None, data = None):
        self.name = "Cruce de medias móviles"
        self.low_period = low_period
        self.high_period = high_period
        self.short_name = f"Cruce {self.low_period}-{self.high_period}"
        self.data = data

    def MA(self, data, N):
        '''
        Devuelve un objeto tipo pandas.Series.
        '''

        if type(data) == None.__class__:
            print(f"Debe ingresar un conjunto de precios en forma de un \nobjeto tipo pandas.Series.")
            return None

        elif type(data) == pd.Series:

            resultado = pd.Series(None, index = data.index, dtype=object)

            for i in np.arange(data.size):

                if np.append(data.iloc[-(N+i):-(1+i)], data.iloc[-(1+i)]).size >= N:

                    resultado.iloc[-(1+i)] = np.average(np.append(data.iloc[-(N+i):-(1+i)], data.iloc[-(1+i)]))

                else:
                    break
        else:
            print(f"El primer argumento de MA() debe ser de tipo pandas.Series.")
            return None

        return resultado
    
    
    def get_operations(self, data = None, lowPeriod = None, highPeriod = None):
        '''
        Return an array of Operation objects.
        '''

        if lowPeriod == None:
            lowPeriod = self.low_period
        if highPeriod == None:
            highPeriod = self.high_period
        if type(data) == None.__class__:
            if type(self.data) != None.__class__:
                data = self.data
            else:
                print(f"Debe ingresar un conjunto de precios en forma de un \nobjeto tipo pandas.Series.")
                return None

        _resta = self.MA(data, lowPeriod) - self.MA(data, highPeriod)
        _compras = pd.Series([], dtype=object)
        _ventas = pd.Series([], dtype=object)

        there_is_opened_operations = False

        for i in np.arange(_resta.size-1):
            _restaDeSigno = np.sign(_resta[i+1])-np.sign(_resta[i])

            if np.sign(_restaDeSigno) == 1 and not there_is_opened_operations:
                # _compras = pd.concat([_compras, pd.Series(["Compra"], index=[data.index[i+1]])], dtype=object)
                _compras = pd.concat(
                    [_compras, pd.Series([data.iloc[i+1]], index=[data.index[i+1]], dtype=object)])
                there_is_opened_operations = True

# Se activa sólo para debugging
#                print(f"Compra en {data.index[i+1]} a USD {data.iloc[i+1]}")
            elif np.sign(_restaDeSigno) == -1 and there_is_opened_operations:
                if _compras.size == 0:
                    pass
                else:
                    _ventas = pd.concat([_ventas, pd.Series([data.iloc[i+1]], index=[data.index[i+1]], dtype=object)])
                    there_is_opened_operations = False

# Se activa sólo para debugging
#                    print(f"Venta en: {data.index[i+1]} a USD {data.iloc[i+1]}")

        operations = np.array([])

        for i in np.arange(_ventas.size):
            operations = np.append(
                operations, Operation( _compras.index[i], _ventas.index[i]))

        if _compras.size > _ventas.size:
            operations = np.append(
                operations, Operation( _compras.index[-1], data.index[-1], is_closed = False))

        return operations


    def ganancia(self):

        operations = self.get_operations(self.data, self.low_period, self.high_period)

        there_is_operations = True if operations.size != 0 else False

        if there_is_operations == False:
#            return {"ganancia": 0, "rentabilidad": 0, "rentabilidad_anual": 0}
            return {"rentabilidad": 0, "operaciones":0, "rentabilidad_anual": 0}

        initial_capital = self.data[operations[0].entry_point]
        capital = initial_capital

#        print(f"Capital inicial: {capital}\n")

        for i, operation in enumerate(operations):
            if operation.is_closed:
                gain = self.data[operation.exit_point] - self.data[operation.entry_point]
                capital += gain
            else:
                print("Mirar qué hacer cuando la operación esté abierta")

#            print(f"Operation {i} gain: {gain}")

        ganancia = capital - initial_capital

#        salida = {"ganancia": ganancia,
#                  "rentabilidad": ganancia/initial_capital,
#                  "operaciones": operations.size,
#                  "rentabilidad_anual": ganancia/initial_capital}

        salida = {"rentabilidad": str((ganancia/initial_capital)*100)+" %",
                  "operaciones": operations.size}

        return salida


    def visualizar(self, data = None): # En fechas

        if type(data) == None.__class__:
            if type(self.data) != None.__class__:
                data = self.data
            else:
                print(f"Debe ingresar un conjunto de precios en forma de un \nobjeto tipo pandas.Series.")
                return None

        plt.figure(figsize=(10,6))

#        data_with_no_weekends = data[data.index.weekday < 5]
#        data.plot(x = data_with_no_weekends.index)
        data.plot()

        self.MA(data, self.high_period).plot(label = f"MA-{self.high_period}")
        self.MA(data, self.low_period).plot(label = f"MA-{self.low_period}")

        operations = self.get_operations(data, self.low_period, self.high_period)

        for operation in operations:

            interval = data[operation.entry_point: operation.exit_point]
            
            gain = data[operation.exit_point] - data[operation.entry_point]
            interval_color = "b"


            if operation.is_closed:
                if gain > 0:
                    interval_color = "g"
                elif gain < 0:
                    interval_color = "r"
            else:
                interval_color = "gray"

            plt.scatter(
                [operation.entry_point],
                [interval[operation.entry_point]],
                color = "b")
            plt.scatter(
                [operation.exit_point],
                [interval[operation.exit_point]],
                color = interval_color)
            plt.fill_between(
                interval.index,
                interval, data.min(),
                color = interval_color, alpha = 0.2)

        plt.legend()

        img_buffer = io.BytesIO()
        plt.savefig(img_buffer, format="png")
        img_buffer.seek(0)

        img_in_base64 = base64.b64encode(img_buffer.read()).decode("utf-8")

        return img_in_base64
