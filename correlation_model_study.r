ETA<-c(24,24,23,62,64,61,16,96,47,26,30,24,24,58)
EMB<-c(14.5,12.5,14.9,12.6,14.1,13.6,12.7,11.7,13,15.2,12.6,12.4,16.1,14.5)
SEX<-c(1,0,1,0,1,0,0,0,0,1,1,0,1,0)
PEL<-c(0,1,0,0,0,1,1,1,1,0,1,0,1,1)
VID<-c(196.10117389,180.02372419,176.52849577,131.76943533,157.7203,132.84356701,147.58684744,172.25536866,155.80778802,148.1133,143.81773198,141.45771629,193.26621455,153.16638746)

cor(EMB,ETA) 
mo0<-lm(EMB~ETA)#primo modello: spiego emoglobina solo con età
summary(mo0) #risultato non significativo (vedi test su coefficiente)
plot(ETA,EMB)
abline(mo0)

cor(EMB,VID)
mo1<-lm(EMB~VID)# modello 2: spiego emoglobina solo con colore video
summary(mo1) #risultato POCO significativo (R^2=17%), diagnostica grafica
plot(VID,EMB, main="MODELLO 1")
abline(mo1)
points(VID[SEX==1],EMB[SEX==1],pch="M",col="blue") #coppie (emoglobina,video) maschi
points(VID[SEX==0],EMB[SEX==0],pch="F",col="pink")#coppie (emoglobina,video) donne
## NB:il plot evidenzia la presenza di due popolazioni distinte,devo tenerne conto!!! ###
plot(VID,EMB, main="MODELLO 1")
abline(mo1)
points(VID[PEL==0],EMB[PEL==0],pch="2°")
points(VID[PEL==1],EMB[PEL==1],pch="3°")
## NB: il plot non evidenzia la presenza di due popolazioni distinte,posso non tenerne conto!!! ###

#==> studio l'effetto del sesso sull'emoglobina

cor(EMB,SEX) #correlazione molto alta
mo2<-lm(EMB~SEX)# modello 3: spiego emoglobina solo con sesso
summary(mo2) # la variabile è SIGNIFICATIVA (R^2=45%)

mo4<-lm(EMB~SEX+VID) #modello4: costruisco una regressione multipla con sesso e video
summary(mo4) # il risultato è peggiore del modello precedente (r^2 adj < 45%) e variabile video risulta non significativa ==> preferisco il modello precedente
#conclusione il video non è utile#


