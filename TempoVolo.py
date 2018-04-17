carburante=float (input ( "dimmi la quantita' di carburante in galloni: " ))
corario=float (input ("dimmi il consumo in GALLONI/H: " ))
if carburante<0 or corario<0:
  print "i dati inseriti risultano falsati"
else:
  t=carburante/corario
  ore=int(t)
  minuti=t-ore
  minuti=minuti*60
  m=minuti
  minuti=int(minuti)
  secondi=m-minuti
  secondi=secondi*60
  secondi=int(second)

  print "Tempo di volo: ", ore, "h ", minuti, "m ",secondi,"s "

  
