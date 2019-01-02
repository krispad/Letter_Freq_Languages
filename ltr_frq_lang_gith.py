#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 10:54:58 2018

@author: krishna
"""

#Western European Alphabet
wstrneu_alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] + ['ä', 'ö', 'ß', 'ü'] + ['ñ'] + ['ç', 'à', 'æ' , 'î', 'ô', 'û',
     'â', 'ê','ë', 'ï', 'ü', 'ÿ','œ', 'é', 'è', 'ù'] # german , spanish, english and french

##############################################################################
def most_freq(alpha):
  
    import decimal as dec
    dec.getcontext().prec = 2
    freq = dict() # freq is a dictionary with letters representing keys
    t  = [] # a list of tuples - (letter , frequency ) pairs
    
    
    fl = input('Enter the filename here:' ) # name of text file 
   
    with open(fl) as fin:
        for line in fin:
           line = line.rstrip()
           for s in line.split():    # s is a string of words      
           
               for w in s:
                   if w not in alpha: continue
                   freq[w] = freq.get(w, 0) + 1 # counting the number of times a letter appears
                                         
    total = 0
    for x, freq[x] in freq.items():
        total = total + freq[x]
        t.append((freq[x], x))
        
    t.sort(reverse = True)
    
    ltr = []
    num = []
    
    for n, w in t:
        num.append(dec.Decimal(n)/dec.Decimal(total))
        ltr.append(w)
    
    ltr_freq = [ltr, num]
    return(ltr_freq)
    
def panel_gen(nbrLang):
    import matplotlib.pyplot as plt
    #import numpy as np
    import math as math
    alpha = input('Enter the alphabet used here: ')
    alpha = eval(alpha)
    
    if nbrLang in (1, 2):
        fig , axs = plt.subplots(nrows = 1, ncols = 2 , constrained_layout = True, figsize = (12, 12))
        fig.suptitle("Western European Alphabets", fontsize = 16)
        for k in range(math.ceil(nbrLang/2) + 1):
           
                freq = most_freq(alpha)                  
                x1 = freq[0]
                y1 = freq[1]   
                axs[k].bar(x1, y1, color = 'g')                                 
                titl1 = input('Enter the title (heading) here:')
                axs[k].set_title(titl1)
                axs[k].tick_params(axis = 'x', labelsize = 12)               
                axs[k].set_xlabel(list(map(lambda x: x, x1)), fontsize = 'x-small')
    if nbrLang == 3:
        fig , axs = plt.subplots(nrows = 2, ncols = 2 , constrained_layout = True, figsize = (12, 12))
        fig.suptitle("Western European Alphabets", fontsize = 16)
        for k in range(math.ceil(nbrLang/2)):
            for m in range(0, int(nbrLang/2) + 1):
                if (k == 0  and m in (0, 1)) or (k ==1 and m == 0):
                   freq  = most_freq(alpha)
                   x1 = freq[0] #data
                   y1 = freq[1] #data  
                   axs[k, m].bar(x1, y1, color = 'g')
                   titl1 = input('Enter the title here:')
                   axs[k, m].set_title(titl1)
                   axs[k, m].tick_params(axis = 'x', labelsize = 12)
                   axs[k, m].set_xlabel(list(map(lambda x: x, x1)), fontsize = 'x-small')
    if nbrLang == 4:
        fig , axs = plt.subplots(nrows = 2, ncols = 2 , constrained_layout = True, figsize = (12, 12))
        fig.suptitle("Western European Alphabets", fontsize = 16)
        for k in range(math.ceil(nbrLang/2)):
            for m in range(math.ceil(nbrLang/2)):             
                   freq  = most_freq(alpha)
                   x1 = freq[0]  #data
                   y1 = freq[1]  #data 
                   axs[k, m].bar(x1, y1, color = 'g')
                   titl1 = input('Enter the title here:')
                   axs[k, m].set_title(titl1)
                   axs[k, m].tick_params(axis = 'x', labelsize = 12)
                   axs[k, m].set_xlabel(list(map(lambda x: x, x1)), fontsize = 'x-small')
            
   
    if nbrLang == 1:
        axs[1].remove()
    
    if nbrLang == 3:
        axs[1, 1].remove()
           