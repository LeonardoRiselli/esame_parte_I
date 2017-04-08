carburante=float (input ( "dimmi la quantita' di carburante in galloni: " ))
corario=float (input ("dimmi il consumo in GALLONI/H: " ))
if carburante<0 or corario<0:
  print "i dati inseriti risultano falsati"
else:
  ore=carburante/corario
  minuti=ore/60
  secondi=minuti/60

  print "Il tempo di volo e' di ",ore," H ",minuti," min ",secondi" s"
