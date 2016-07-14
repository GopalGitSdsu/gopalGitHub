# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 15:38:13 2016

@author: Gopalakrishnan
"""

import string
import decimal
from decimal import Decimal

decimal.getcontext().prec=20

def main():
    input_string = input("Enter the string to be encoded \n")
    strlen = len(input_string)
    print('Length of the input string is \n',strlen)
    print('Set decimal Precision for compression is \n',decimal.getcontext().prec)
    step_size = 3
    encoded = encoder(input_string, step_size)
    #print('The  ',encoded)
    decoded = decode(encoded, strlen, step_size)
    print('Decoded value of the encoded message',decoded)


def encoder(input_string, step):
    dict_set_one = dict.fromkeys(string.hexdigits, 1)                                        
    print('Upper limit set to the dictionary   \n',dict_set_one)
    dict_set_cdf = dict.fromkeys(string.hexdigits, 0)
    print('Lower limit set to the dictionary   \n',dict_set_cdf)
    dict_set_pdf = dict.fromkeys(string.hexdigits, 0)

    low = 0
    high = Decimal(1)/Decimal(26)

    for tag, pby in sorted(dict_set_cdf.items()):
        dict_set_cdf[tag] = [low, high]
        low = high
        high += Decimal(1)/Decimal(26)
    
     

    for tag, pby in sorted(dict_set_pdf.items()):
        dict_set_pdf[tag] = Decimal(1)/Decimal(26)

   

    tot_cnt = 26

    level_low = 0                                                                     
    level_high = 1                                                                     

    u = 0
    i = 0

    for sym in input_string:
                
        tot_cnt += 1
        u += 1
        dict_set_one[sym] += 1

        diff_bound = level_high - level_low                                         
        level_high = level_low + (diff_bound * dict_set_cdf[sym][1])                
        level_low = level_low + (diff_bound * dict_set_cdf[sym][0])                   

        # update dict_set_cdf after N symbols have been read
        if (u == step):
            u = 0

            for tag, pby in sorted(dict_set_pdf.items()):
                dict_set_pdf[tag] = Decimal(dict_set_one[tag])/Decimal(tot_cnt)

            low = 0
            for tag, pby in sorted(dict_set_cdf.items()):
                high = dict_set_pdf[tag] + low
                dict_set_cdf[tag] = [low, high]
                
                
                low = high
                    
        i = i + 1       
        
        print("Lower and Upoper limits of the encoder Chunk is ",level_low,level_high)
        
        
    
    print("Binary expanded value of the encoded message is \n",level_low)
               
   
    return level_low

def decode(encoded, strlen, step_size):
    dec_message = ""

    dict_set_one = dict.fromkeys(string.hexdigits, 1)                                        
    dict_set_cdf = dict.fromkeys(string.hexdigits, 0)
    dict_set_pdf = dict.fromkeys(string.hexdigits, 0)

    low = 0
    high = Decimal(1)/Decimal(26)

    for tag, pby in sorted(dict_set_cdf.items()):
        dict_set_cdf[tag] = [low, high]
        low = high
        high += Decimal(1)/Decimal(26)

    for tag, pby in sorted(dict_set_pdf.items()):
        dict_set_pdf[tag] = Decimal(1)/Decimal(26)


    level_low = 0                                                                    
    level_high = 1                                                                     

    k = 0

    while (strlen != len(dec_message)):
        for tag, pby in sorted(dict_set_pdf.items()):

            diff_bound = level_high - level_low                                      
            upper_cand = level_low + (diff_bound * dict_set_cdf[tag][1])                 
            lower_cand = level_low + (diff_bound * dict_set_cdf[tag][0])                 

            if (lower_cand <= encoded < upper_cand):
                k += 1
                dec_message += tag

                if (strlen == len(dec_message)):
                    break

                level_high = upper_cand
                level_low = lower_cand

                dict_set_one[tag] += 1

                if (k == step_size):
                    k = 0
                    for tag, pby in sorted(dict_set_pdf.items()):
                        dict_set_pdf[tag] = Decimal(dict_set_one[tag])/Decimal(26+len(dec_message))

                    low = 0
                    for tag, pby in sorted(dict_set_cdf.items()):
                        high = dict_set_pdf[tag] + low
                        dict_set_cdf[tag] = [low, high]
                        low = high

        print('decoder output iterated are', upper_cand,lower_cand,dec_message)
    #print('trial run output iterated are', level_high,level_low,dec_message)
                       
    return dec_message

if __name__ == '__main__':
    main()
