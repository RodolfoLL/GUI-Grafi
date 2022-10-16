import cv2
import math
import numpy as np
dondex=-1
dondey=-1
def bresenham(blank,x0,y0,x1,y1):
    dx=abs(x1-x0)
    dy=abs(y1-y0)
    p=2*dy-dx
    incE=2*dy
    incNE=2*(dy-dx)
    global dondex
    global dondey
    #if y0>y1:
    #    x0,x1=x1,x0
    #    y0,y1=y1,y0
    
    if dx>dy:
        if x0>x1:
            x=x1
            y=y1
            xend=x0
            yend=y0
        else:
            x=x0
            y=y0
            xend=x1
            yend=y1
        ayuda=0
        if y0>y1:
            x0,x1=x1,x0
            y0,y1=y1,y0
        for i in range(x,xend):
            if ayuda==3 :
                if dondex==-1: dondex=x
                if dondey==-1: dondey=y
            ayuda+=1
            blank[x,y]=(51,222,222)
            x=x+1 if x<x1 else x-1
            if p<0:
                p+=incE
            else:
                y=y+1 if y<y1 else y-1
                p+=incNE
    else:
        p=2*dx-dy
        incE=2*dx
        incNE=2*(dx-dy)
        if y0>y1:
            y=y1
            x=x1
            yend=y0
            xend=x0
        else:
            y=y0
            x=x0
            yend=y1
            xend=x1
        if y0>y1:
            x0,x1=x1,x0
            y0,y1=y1,y0
        ayuda=0;
        for i in range(y,yend):
           if ayuda==3 :
            if dondex==-1: dondex=x
            if dondey==-1: dondey=y
           ayuda+=1
           blank[x,y]=(51,222,222)
           y=y+1 if y<y1 else y-1
           if p<0:
               p+=incE
           else:
               x=x+1 if x<x1 else x-1
               p+=incNE
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def floodfill(blank,x,y):
    #print(x,"   ",y)
    blank[x][y]=(51,222,222)
    for i in range(len(dx)):
        x1=x+dx[i]
        y1=y+dy[i]
        X=blank[x1][y1][0]
        Y=blank[x1][y1][1]
        Z=blank[x1][y1][2];
        if X!=51 and Y!=222 and Z!=22:
            floodfill(blank,x1,y1)

def linea(x1,y1,x2,y2,ancho):
    blank=np.zeros((1080,1920,3),dtype="uint8")
    bresenham(blank,x1,y1,x2,y2)
    if ancho==0:
        cv2.imshow("Yellow",blank)
        cv2.waitKey(0)
        return
    #print("ahora  ",dondex,"  ",dondey)
    vx=x2-x1
    vy=y2-y1
    #vector A,B extermos de la linea

    #perpendicular a AB
    wx=vy
    wy=-vx
    modulo=math.sqrt(wx*wx+wy*wy)
    wx/=modulo
    wy/=modulo
    modulo=math.sqrt(vx*vx+vy*vy)
    vx/=modulo
    vy/=modulo
    #dirx=vx+wx
    #diry=vy+wy
    #modulo=math.sqrt(dirx*dirx+diry*diry)
    #dirx/=modulo
    #diry/=modulo
    #inX=int(x1+dirx)
    #inY=int(y1+diry)
    #print("empizo ",inX,"  ",inY)
    #(wx,wy) vector unitario perpendicular a AB

    #print("vector unitario  ",wx," ",wy," check ",math.sqrt(wx*wx+wy*wy))
    arribax=int(x1+wx*ancho)
    arribay=int(y1+wy*ancho)
    abajox=int(x1-wx*ancho)
    abajoy=int(y1-wy*ancho)
    #print(abajox,"  ",abajoy," yy ",arribax," ",arribay)
    bresenham(blank,abajox,abajoy,arribax,arribay);
    arribax2=int(x2+wx*ancho)
    arribay2=int(y2+wy*ancho)
    abajox2=int(x2-wx*ancho)
    abajoy2=int(y2-wy*ancho)

    bresenham(blank,abajox2,abajoy2,arribax2,arribay2)
    bresenham(blank,arribax,arribay,arribax2,arribay2)
    bresenham(blank,abajox,abajoy,abajox2,abajoy2)
    #print("donde  ",dondex," ",dondey)
    if ancho>1 : floodfill(blank,dondex,dondey)
    #bresenham(arribax,arribay,abajox,abajoy)
    #floodfill(blank,abajox,abajoy,0)
    cv2.imshow("Yellow",blank)
    cv2.waitKey(0)
def main():
    linea(200,20,300,24,5)
    #linea(300,300,5,200,5)
    
    #linea(50,50,150,24,0)
    #linea(300,24,50,50,0)
if __name__ == '__main__':
    main()
 
