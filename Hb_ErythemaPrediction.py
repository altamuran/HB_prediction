# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 12:08:48 2019

@author: USER
"""
    
import numpy as np
import scipy.stats
import scipy as scy
import cv2 
import matplotlib.pyplot as plt
import time 

#compute eqauzione of the line
def preditction_emo(slope,intercept,x):
    return intercept+(slope*x)       
    #img = cv2.imread(r"C:\Users\USER\Pictures\prova1.jpg")
    #img2 = cv2.imread(r"C:\Users\USER\Pictures\prova2.jpg")
    
video=[]
AI=[] #inizialize Averange Erytema Index
RI=[] #inizialize Averange Red-color Index
array_frame_index=[]
#loop for reading video and append in array 
for v in range(1,14):
    video=np.append(video,cv2.VideoCapture ( r"C:\Users\USER\Pictures\V"+str(v)+".mp4",0 ))
#for each video in arrray
for s in range(len(video)):
    indice_frame=0
    Array_AEI=[]
    AEI=0
    I=0
    MI=0
    REI=0
    ret=True
    n=0;
    k=0;
    new1=0
    start = time.time();
    SR=0
    SG=0;
    SI=0;
    r=0
    index=0
    #processed and analyze each frame in video 
    while(ret and indice_frame<800):
        ret, frame = video[s].read() #read video frame and rerutn frame and reading flag 
        if(ret!=False): #check if reading flag is true and frame exists
            new1=frame #assign frame at new1 varible
            b, g, r = cv2.split(new1) #split the frame image in RGB color
            I=(r-g) #compute Erythema Index for current frame
            SR=SR+r.mean(); #increment the sum of averenge red colo in frame
            MI=MI+I.mean(); #increment the sum of Erythema index for each frame analyzed
        indice_frame=indice_frame+1 #increment count of analyzed frame
    #when each frame for current video is analyzed
    AEI=MI/indice_frame #compute Averange Erythema index for video :
    #sum of each erythema index divded for count of analyzed frame.
    #I get resultant Erythema index for analyzed video
    REI=SR/indice_frame #coumpute Averange Red Index
    #sum of every red index in all frame divded by count of analyzed frame
    #I get resultant Red index for analyzed video
    print('indice rilevato',s);
    print(AEI);
    AI = np.append(AI,AEI) #appeand Erythema index of the video just analyzed to the array

    RI=np.append(RI,REI) #appeand Red index of the video just analyzed to the array
    cv2.waitKey(0) 
    video[s].release() #close the current video stream
    cv2.destroyAllWindows() 
    
print(AI)    

f =[14.5, 12.5, 14.9, 12.6, 14.1,13.6, 12.7,13,15.2,12.6,12.4,16.1,14.5]
#hemoglobin revelations
slope,intercept,r_value, p_value, std_err = scipy.stats.linregress(AI,f)
#coumpte a linear regression model for Erythema index and hemoglobin revelations
slope1,intercept1, r_value1, p_value1, std_err1 = scipy.stats.linregress(RI,f)
#coumpte a linear regression model for Red index and hemoglobin revelations

correlation1=scy.stats.pearsonr(f,AI)
#compute a Pearson correlation to discover the relationship between hemoglobin and Erythema index

r2=r_value**2
#compute R square  to discover  how much the model explains for my Erythema index model

corrRed=scy.stats.pearsonr(f,RI)
#compute a Pearson correlation to discover the relationship between hemoglobin and Red index
rRed2=r_value1**2
#compute R square  to discover  how much the model explains for my Red index model


plt.xlim(100,210)
plt.plot(AI,f,linestyle='', marker='o')
plt.plot(AI,scy.polyval((slope,intercept),AI),'r-') 
plt.show()
#create and show the  Erythema index - hemoglobin chart
print('valori di regressione linerare per modello di stima tramite EI')
print(slope,intercept,r_value,p_value,std_err)
print('*****************')
print(preditction_emo(slope,intercept,130))
#print the approsimate value of hemoglobin predicted by  Erythema index model 
print('*****************')
print('correlazioni')
print('erythema index correlation: ',r_value)
print('erythema index r square correlation: ',r2)




plt.plot(RI,f,linestyle='', marker='*')
plt.plot(RI,scy.polyval((slope1,intercept1),RI),'b-') 
plt.show()
#create and show the  Red index - hemoglobin chart
print('valori di regressione linerare per modello di stima tramite indice R')
print(slope1,intercept1,r_value1,p_value1,std_err)
print('*****************')
print(preditction_emo(slope1,intercept1,210))
#print the approsimate value of hemoglobin predicted by  Red index model
print('*****************')
print('correlazioni')
print('red index correlation: ',r_value1)
print('red index rsquare correlation: ',rRed2)

res =  scipy.stats.theilslopes(f, AI, 0.90)
#implements a method for robust linear regression. 
#It computes the slope as the median of all slopes between paired values.
#this method returns the lower bound of the confidence interval on medslope and 
#ipper bound of the confidence interval on medslope.
#these limits could be used to calculate a degree of confidence to analyze the results

plt.xlim(100,210)
plt.plot(AI,f,linestyle='', marker='o')
plt.plot(AI,scy.polyval((res[0],res[1]),AI),'r-') 
plt.show()
#show the newx chart with new robust linear regression
print('*****************')
print('calcolo una regressione più robusta della precedente:Calcola la pendenza' 
      ,'come mediana di tutte le pendenze tra valori accoppiati.')
print(res);
print('*****************')
print('predico con un modello di regressione robusto')
print(preditction_emo(res[0],res[1],130))
#print the approsimate value of hemoglobin predicted by  robust Erythema index model
                    
                       
                         
                           
            
            
            
            
            
            
            
            
            