#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

from multiprocessing.pool import ThreadPool

from time import time as timer

from urllib.request import urlretrieve

import os

import datetime


pasta = 'C:/Users/lucas/OneDrive/Desktop/IP_DATA/dadosBrutos/'

arqs = os.listdir(pasta)



urlBase = 'http://apps.mpf.mp.br/aptusmpf/protected/expediente/%s?modulo=0&sistema=portal';

#print (urlBase);





def baixa(i,processo):

    try:

        # evita baixar se ja tem

        if (processo in arqs):

            print (str(i) + '-ja tem: ' + str(processo));

        else:

            print (str(i) + '-baixando: ' + str(processo));

            urlretrieve( urlBase % processo, 'C:/Users/lucas/OneDrive/Desktop/IP_DATA/dadosBrutos/%s' % processo);

    except Exception as e:

        print ('ERRO: ' + processo + str(e));





#baixa('920000000000014398193')





df = pd.read_csv("C:/Users/lucas/OneDrive/Desktop/IP_DATA/mpf_cod_2009.csv", index_col=0,names=['numproc'], skiprows=1)

#df = pd.read_csv("dados/mpf_cod2.csv")

#df.tail()



inicio = timer()

print ('**************** Inicio: ' + str(datetime.datetime.now()))

for x, proc in df.iterrows():

    baixa(x,proc['numproc']);



#for x,processo in df2[['cod2']].head(100).iterrows():

#     baixa(str(processo['cod2']))



#em segundos, para 100

print (timer() - inicio)


# In[ ]:




