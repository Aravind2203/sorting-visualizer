import pygame
import random
import time
from pygame.locals import *
pygame.init()
font1=pygame.font.Font('freesansbold.ttf',50)
font2=pygame.font.Font('freesansbold.ttf',30)
WINDOW=pygame.display.set_mode((1000,600))
pygame.display.set_caption('Sorting visualizer')
class Main:
    def __int__(self):
        self.arr=[]
        self.colors=[]
        self.buttons=[]
        self.sorted=False

    def genrate_data(self):
        self.arr=[ random.randint(25,495) for _ in range(73)]
        self.colors=[(165,42,42) for _ in range(73)]
        self.sorted=False

    def draw(self):
        self.buttons=[]
        title=font1.render('SORTING VISUALIZER',True,(204,170,163))
        bub=font2.render('Selec-sort',True,(0,0,0))
        quic=font2.render('Quick-sort',True,(0,0,0))
        res=font2.render('Reset',True,(0,0,0))
        ins=font2.render('Ins-sort',True,(0,0,0))
        WINDOW.fill((0,0,0))
        pygame.draw.rect(WINDOW,(204,170,163),(0,100,800,500))
        WINDOW.blit(title,(220,30))
        x=0
        for i in range(len(self.arr)):
            pygame.draw.rect(WINDOW,self.colors[i],(x,600,9,-self.arr[i]))
            x+=11
        Bubble_sort=pygame.draw.rect(WINDOW,(127,209,212),(810,100,180,100))
        WINDOW.blit(bub,(813,135))
        self.buttons.append(Bubble_sort)
        quick_sort=pygame.draw.rect(WINDOW,(127,209,212),(810,210,180,100))
        WINDOW.blit(quic,(815,245))
        self.buttons.append(quick_sort)
        insertionsort=pygame.draw.rect(WINDOW,(127,209,212),(810,320,180,100))
        self.buttons.append(insertionsort)
        WINDOW.blit(ins,(830,355))
        reset_array=pygame.draw.rect(WINDOW,(127,209,212),(810,430,180,100))
        WINDOW.blit(res,(850,465))
        self.buttons.append(reset_array)
        reset_array=pygame
        pygame.display.update()
    def partition(self,low,high):
        i=low-1
        pivot=self.arr[high]
        self.colors[high]=(0,0,255)
        self.draw()
        for j in range(low,high):
            self.colors[j]=(0,255,0)
            self.draw()
            if self.arr[j]<pivot:
                self.colors[j]=(255,0,0)
                self.draw()
                i+=1
                self.arr[j],self.arr[i]=self.arr[i],self.arr[j]
                self.draw()
            self.draw()
            self.colors[j]=(165,42,42)
            self.draw()
        self.arr[i+1],self.arr[high]=self.arr[high],self.arr[i+1]
        self.colors[i+1]=(165,42,42)
        self.draw()
        return i+1
    def quicksort(self,low,high):
        if low<high:
            pi=self.partition(low,high)
            self.quicksort(low,pi-1)
            self.draw()
            self.quicksort(pi+1,high)
            self.draw()

    def selectionsort(self):
        for i in range(len(self.arr)):
            for j in range(i+1,len(self.arr)):
                self.colors[i]=(0,0,255)
                self.colors[j]=(0,0,255)
                self.draw()
                if self.arr[j]<=self.arr[i]:
                    self.colors[i]=(0,255,0)
                    self.colors[j]=(0,255,0)
                    self.draw()
                    self.arr[j],self.arr[i]=self.arr[i],self.arr[j]
                    self.draw()
                else:
                    self.colors[i]=(255,0,0)
                    self.colors[j]=(255,0,0)
                    self.draw()
                self.colors[i]=(165,42,42)
                self.colors[j]=(165,42,42)
                self.draw()
        self.colors=[(255,69,0) for _  in range(80)]
        self.sorted=True


    def insertionsort(self):
        for i in range(len(self.arr)-1):
            for j in range(i+1,0,-1):
                self.colors[j]=(0,0,255)
                self.colors[j-1]=(0,0,255)
                self.draw()
                if self.arr[j]<=self.arr[j-1]:
                    self.colors[j]=(0,255,0)
                    self.colors[j-1]=(0,255,0)
                    self.draw()
                    self.arr[j],self.arr[j-1]=self.arr[j-1],self.arr[j]
                else:
                    self.colors[j]=(165,42,42)
                    self.colors[j-1]=(165,42,42)
                    self.draw()
                    break
                self.colors[j]=(165,42,42)
                self.colors[j-1]=(165,42,42)
                self.draw()
        self.colors=[(255,69,0) for _  in range(80)]
        self.sorted=True
            
                    
    def check(self,pos):
        for i in range(len(self.buttons)):
            if self.buttons[i].collidepoint(pos):
                if i==1 and not self.sorted:
                    self.quicksort(0,72)
                    self.colors=[(255,69,0) for _  in range(73)]
                    self.sorted=True
                elif i==0 and not self.sorted:
                    self.selectionsort()
                elif i==3:
                    self.genrate_data()
                elif i==2 and not self.sorted:
                    self.insertionsort()

m=Main()
m.genrate_data()
run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            m.check(pos)
    m.draw()
pygame.quit()
