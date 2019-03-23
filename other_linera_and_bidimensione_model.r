ETA<-c(24,24,23,62,64,61,16,96,47,26,30,24,24,58)
EMB<-c(14.5,12.5,14.9,12.6,14.1,13.6,12.7,11.7,13,15.2,12.6,12.4,16.1,14.5)
SEX<-c(1,0,1,0,1,0,0,0,0,1,1,0,1,0)
PEL<-c(0,1,0,0,0,1,1,1,1,0,1,0,1,1)
VID<-c(196.10117389,180.02372419,176.52849577,131.76943533,157.7203,132.84356701,147.58684744,172.25536866,155.80778802,148.1133,143.81773198,141.45771629,193.26621455,153.16638746)


y<-EMB[-c(8)]
x1<-VID[-c(8)]
x2<-ETA[-c(8)]
x3<-PEL[-c(8)]
x4<-SEX[-c(8)]


md0<-lm(y~x1)
summary(md0)#MODELLO 1: esiste una relazione positiva significativa e con una buona capacità predittiva
plot(x1,y)
abline(md0)
points(x1[x4==1],y[x4==1],pch="M",col="blue") #coppie (emoglobina,video) maschi
points(x1[x4==0],y[x4==0],pch="F",col="pink")#coppie (emoglobina,video) donne

md1<-lm(y~x2) #MODELLO 2: risultato non significativo e con poca capacità predittiva
summary(md1)

md2<-lm(y~x3) #MODELLO 3 : ""
summary(md2)

md3<-lm(y~x4) #MODELLO 4: esiste una relazione significativa e con una buona capacità predittiva
summary(md3)

md4<-lm(y~x1+x4) #MODELLO 5: no
summary(md4)

md5<-lm(y~x4+x1*x3)#no
summary(md5)
