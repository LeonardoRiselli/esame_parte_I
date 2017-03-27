carburante=float (input ( "dimmi la quantita' di carburante in galloni: " ))
corario=float (input ("dimmi il consumo in GALLONI/H: " ))
if carburante<0 or corario<0:
  print "i dati inseriti risultano falsati"
else:
  tvolo=carburante/corario
  print "Il tempo di volo e' di ",tvolo," H"
