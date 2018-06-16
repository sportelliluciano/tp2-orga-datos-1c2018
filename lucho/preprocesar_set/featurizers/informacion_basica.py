#!/usr/bin/python3

'''
Genera tres features que refieren a la información básica del postulante.
- edad: Edad del postulante, por defecto: .EDAD_MEDIA
- sexo: Sexo del postulante -1 si es mujer, 1 si es hombre, 0 por defecto.
- educacion: Nivel educativo del postulante, de 0 a 10 basado en 
    ESCALA_EDUCATIVA, por defecto .NIVEL_EDUCATIVO_MEDIO
Si no se tiene la edad del postulante, devuelve EdadPostulante.EDAD_MEDIA.
'''

import datasets.postulantes as postulantes

import pandas as pd

class InformacionBasica:
    def get_name(self):
        return 'Información básica'

    def featurize(self, df):
        df = pd.merge(df, postulantes.df_genero_edad, how='left', left_on='idpostulante', right_index=True)
        df = pd.merge(df, postulantes.df_educacion, how='left', left_on='idpostulante', right_index=True)
        

        return df.rename(columns={'sexo': 'sexo_postulante', 
                    'fechanacimiento':'edad_postulante', 'nombre': 'nivel_educativo'})
