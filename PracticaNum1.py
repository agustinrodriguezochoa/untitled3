__author__ = 'agustin rodriguez ochoa'
def convercionBinario(xxx):

   if xxx > 1:
       convercionBinario(xxx//2)
   print(xxx % 2, end = '')


dec = 34

convercionBinario(dec)