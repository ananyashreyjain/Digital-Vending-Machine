from pygame import display as D
from pygame import image as I
from pygame import Surface as S
from pygame import Color as C
from pygame import event as E
from pygame import draw as DR
from pygame import font as F
from pygame import key as K
from pygame import mouse as M
from selenium import webdriver as W
from pyvirtualdisplay import Display as DI
from selenium.webdriver.chrome.options import Options
from pygame.mixer import music as MU
from pygame import mixer
import voice_control as V
import time
import pygame

while(True):

	class Web(object):
	
		def __init__(self,name,ph,add,option):
		
			options=Options()
			options.add_argument("--window-size=1920,1080")
			self.driver=W.Chrome("/usr/lib/chromium-browser/chromedriver",chrome_options=options)
			self.driver.get("https://dive.addthemoney.com")
			self.name=self.driver.find_element_by_name("name")
			self.num=self.driver.find_element_by_name("number")
			self.add=self.driver.find_element_by_name("email")
			self.c_name=name
			self.c_ph=ph
			self.c_add=add

			if(option==1):
			
				self.product=self.driver.find_element_by_xpath("//input[@value='Lays']")
				
			if(option==2):
			
				self.product=self.driver.find_element_by_xpath("//input[@value='Uncle Chips']")
				
			if(option==3):
			
				self.product=self.driver.find_element_by_xpath("//input[@value='Kurkure']")
				
			if(option==4):
			
				self.product=self.driver.find_element_by_xpath("//input[@value='Cheetos']")
				
			self.submit=self.driver.find_element_by_xpath("//input[@name='submit1']")
				
		def run(self):
		
			self.name.send_keys(self.c_name)
			self.num.send_keys(self.c_ph)
			self.add.send_keys(self.c_add)
			self.product.click()
			next1=self.driver.window_handles
			self.submit.click()
			while(len(next1)<=1):
			
				next1=self.driver.window_handles
				
			self.driver.switch_to_window(next1[1])
			time.sleep(20)
			self.driver.quit()

				

	class colours(object):

		BLACK = (  0,   0,   0)
		WHITE = (255, 255, 255)
		BLUE =  (  0,   0, 255)
		GREEN = (  0, 255,   0)
		RED =   (255,   0,   0)
		C_RED = (255,   75,  75)
		C_BLUE = (180,  180,  200)
		GOLD =  (255,  215,  0)
	
	class screen(object):

		def __init__(self):
	
			D.init()
			F.init()
			D.set_mode((0,0),pygame.NOFRAME)
			self.main_surface=D.get_surface()
			background=I.load("DB.jpg").convert()
			self.main_surface.blit(background,(0,0))
			D.flip()
			D.set_caption("DIVE")

		class Box():

			def __init__(self,main):
		
				self.VM=I.load("VM.jpg")
				self.machine=S((800,800))
				self.box1=S((500,40))
				self.box2=S((500,70))
				self.box3=S((600,90))
				self.machine.fill(colours.WHITE)
				self.machine.blit(self.VM,(0,0))
				self.box1.fill(colours.WHITE)
				self.box2.fill(colours.C_BLUE)
				self.box3.fill(colours.C_BLUE)
				self.ms=main.main_surface

			def display(self):
		
				DR.rect(self.machine,colours.BLACK,(0,0,800,800),4)
				self.ms.blit(self.machine,(1000,150))
				DR.rect(self.box3,colours.BLACK,(0,0,600,90),4)
				font1 = F.SysFont('loma', 50)
				self.text1 = font1.render('Digital Vending Machine',True,colours.BLACK)
				self.box3.blit(self.text1,(20,0))
				self.ms.blit(self.box3,(600,25))
				DR.rect(self.ms,colours.BLACK,(100,150,600,800),4)
				font1 = F.SysFont('loma', 45)
				self.text1 = font1.render('ENTER THE DETAILS', False, colours.GOLD)
				self.box2.blit(self.text1,(10,0))
				font1 = F.SysFont('loma', 30)
				self.text2 = font1.render('NAME', False, colours.BLACK)
				self.ms.blit(self.text2,(150,400))
				self.text3 = font1.render('PHONE', False, colours.BLACK)
				self.ms.blit(self.text3,(150,550))
				self.text4 = font1.render('EMAIL', False, colours.BLACK)
				self.ms.blit(self.text4,(150,700))
				DR.rect(self.box1,colours.BLACK,(0,0,500,40),4)
				self.ms.blit(self.box1,(150,450))
				self.ms.blit(self.box1,(150,600))
				self.ms.blit(self.box1,(150,750))
				DR.rect(self.box2,colours.BLACK,(0,0,500,70),4)
				self.ms.blit(self.box2,(150,200))
			
		class event_handler(object):
	
			def __init__(self,main):
				self.main=main
				self.ms=main.main_surface
				self.t1=""
				self.t2=""
				self.t3=""
			
			def textbox(self,event):
		
				inside=True
				global text1,text2,text3
				self.t1=text1
				self.t2=text2
				self.t3=text3
				
				for events in event:
			
					if(events.type==pygame.MOUSEBUTTONDOWN):
				
						if events.pos[0]>150 and events.pos[0]<650:
					
							if events.pos[1]>450 and events.pos[1]<490:
						
								while(inside):
							
									for keyevents in E.get():
								
										if keyevents.type==pygame.KEYDOWN:
									
											if(keyevents.unicode!="\b"):
										
												self.t1+=keyevents.unicode
											
											else:
										
												self.t1=self.t1[0:len(self.t1)-1]
											
											text.box1(self.t1)
											D.flip()
										
										if keyevents.type==pygame.MOUSEMOTION:
									
											inside=False
											text.box1(self.t1,True)
										
							if events.pos[1]>600 and events.pos[1]<640:
						
								while(inside):
									
									for keyevents in E.get():
								
										if keyevents.type==pygame.KEYDOWN:
									
											if(keyevents.unicode!="\b"):
										
												self.t2+=keyevents.unicode
											else:
										
												self.t2=self.t2[0:len(self.t2)-1]
											
											text.box2(self.t2)
											D.flip()
										
										if keyevents.type==pygame.MOUSEMOTION:
									
											inside=False
											text.box2(self.t2,True)
										
							if events.pos[1]>750 and events.pos[1]<790:
						
								while(inside):
							
									for keyevents in E.get():
								
										if keyevents.type==pygame.KEYDOWN:
									
											if(keyevents.unicode!="\b"):
										
												self.t3+=keyevents.unicode
											
											else:
										
												self.t3=self.t3[0:len(self.t3)-1]
											
											text.box3(self.t3)
											D.flip()
										
										if keyevents.type==pygame.MOUSEMOTION:
									
											inside=False
											text.box3(self.t3,True)
										
					
						if events.pos[1]>325 and events.pos[1]<365:	
									
							if events.pos[0]>150 and events.pos[0]<260:
						
								while(inside):
							
									if events.type==pygame.MOUSEBUTTONDOWN:
								
										buttons=screen.Buttons(self.main)
										buttons.Button1(True)
										inside=False
										
							if events.pos[0]>270 and events.pos[0]<380:
						
								while(inside):
							
									if events.type==pygame.MOUSEBUTTONDOWN:
								
										buttons=screen.Buttons(self.main)
										buttons.Button2(True)
										inside=False
										
							if events.pos[0]>390 and events.pos[0]<500:
						
								while(inside):
								
									if events.type==pygame.MOUSEBUTTONDOWN:
								
										buttons=screen.Buttons(self.main)
										buttons.Button3(True)
										inside=False
										
							if events.pos[0]>510 and events.pos[0]<620:
						
								while(inside):
							
									if events.type==pygame.MOUSEBUTTONDOWN:
									
										buttons=screen.Buttons(self.main)
										buttons.Button4(True)
										inside=False
									
						if events.pos[1]>850 and events.pos[1]<890:
					
							if events.pos[0]>350 and events.pos[0]<460:
						
								while(inside):
								
									if events.type==pygame.MOUSEBUTTONDOWN:
								
										buttons=screen.Buttons(self.main)
										buttons.Button5(True)
										inside=False
										global exit
										exit = True						
								
		class Text():
			def __init__(self,main):
		
				self.ms=main.main_surface
	
			def box1(self,t,last=False):
		
				self.box=S((500,40))
				self.box.fill(colours.WHITE)
				DR.rect(self.box,colours.BLACK,(0,0,500,40),4)
				self.font1 = F.SysFont('loma', 25)
				if(last):
			
					self.text = self.font1.render(t, False, colours.BLACK)
				
				else:
			
					self.text = self.font1.render(t+"|", False, colours.BLACK)
					global text1 
					text1 = t
				
				self.box.blit(self.text,(5,0))
				self.ms.blit(self.box,(150,450))
		
			def box2(self,t,last=False):

				self.box=S((500,40))
				self.box.fill(colours.WHITE)
				DR.rect(self.box,colours.BLACK,(0,0,500,40),4)
				self.font1 = F.SysFont('loma', 25)		
				if(last):
			
					self.text = self.font1.render(t, False, colours.BLACK)
				
				else:
			
					self.text = self.font1.render(t+"|", False, colours.BLACK)
					global text2 
					text2 = t
				
				self.box.blit(self.text,(5,0))
				self.ms.blit(self.box,(150,600))
			
			def box3(self,t,last=False):

				self.box=S((500,40))
				self.box.fill(colours.WHITE)
				DR.rect(self.box,colours.BLACK,(0,0,500,40),4)
				self.font1 = F.SysFont('loma', 25)		
				if(last):
			
					self.text = self.font1.render(t, False, colours.BLACK)
				
				else:
			
					self.text = self.font1.render(t+"|", False, colours.BLACK)
					global text3
					text3 = t
				
				self.box.blit(self.text,(5,0))
				self.ms.blit(self.box,(150,750))
			
		class Buttons(object):
		
			def __init__(self,main):
		
				self.ms=main.main_surface
				self.Button1()
				self.Button2()
				self.Button3()
				self.Button4()
				self.Button5()
			
			def Button1(self,clicked=False):
		
				self.B=S((110,40))
				self.B.fill(colours.C_RED)	
				self.font1 = F.SysFont('loma', 25)
				DR.rect(self.B,colours.BLACK,(0,0,110,40),4)
				if(clicked):
			
					self.button_surface = self.font1.render("Lays",False,colours.BLACK)
					global button
					button=1
				
				else:
			
					self.button_surface = self.font1.render("Lays",False,colours.WHITE)
			
				self.B.blit(self.button_surface,(20,-3))
				self.ms.blit(self.B,(160,325))
		
			def Button2(self,clicked=False):
		
				self.B=S((110,40))
				self.B.fill(colours.C_RED)
				DR.rect(self.B,colours.BLACK,(0,0,110,40),4)	
				self.font1 = F.SysFont('loma', 25)
				if(clicked):
			
					self.button_surface = self.font1.render("Chips",False,colours.BLACK)
					global button
					button=2
				
				else:
			
					self.button_surface = self.font1.render("Chips",False,colours.WHITE)
			
				self.B.blit(self.button_surface,(15,-3))
				self.ms.blit(self.B,(280,325))
	
			def Button3(self,clicked=False):
		
				self.B=S((110,40))
				self.B.fill(colours.C_RED)
				DR.rect(self.B,colours.BLACK,(0,0,110,40),4)	
				self.font1 = F.SysFont('loma', 25)
				if(clicked):
			
					self.button_surface = self.font1.render("Kurkure",False,colours.BLACK)
					global button
					button=3
				
				else:
			
					self.button_surface = self.font1.render("Kurkure",False,colours.WHITE)
			
				self.B.blit(self.button_surface,(5,-3))
				self.ms.blit(self.B,(400,325))
			
			def Button4(self,clicked=False):
		
				self.B=S((110,40))
				self.B.fill(colours.C_RED)
				DR.rect(self.B,colours.BLACK,(0,0,110,40),4)
				self.font1 = F.SysFont('loma', 25)
				if(clicked):
			
					self.button_surface = self.font1.render("Cheetos",False,colours.BLACK)
					global button
					button=4
				
				else:
			
					self.button_surface = self.font1.render("Cheetos",False,colours.WHITE)
			
				self.B.blit(self.button_surface,(5,-3))
				self.ms.blit(self.B,(520,325))
			
			def Button5(self,clicked=False):
		
				self.B=S((110,40))
				self.B.fill(colours.GREEN)
				DR.rect(self.B,colours.BLACK,(0,0,110,40),4)	
				self.font1 = F.SysFont('loma', 25)
				if(clicked):
					
					self.button_surface = self.font1.render("SUBMIT",False,colours.BLACK)
				
				else:
			
					self.button_surface = self.font1.render("SUBMIT",False,colours.WHITE)
			
				self.B.blit(self.button_surface,(5,-3))
				self.ms.blit(self.B,(350,850))
				D.flip()
				
	class Audio:
	
		def __init__(self):
		
			mixer.init()
			global text1,text2,text3,text4
			MU.load("activation.mp3")
			MU.play()
			while MU.get_busy():
				time.sleep(.01)
			MU.load("name.mp3")
			MU.play()
			while MU.get_busy():
				time.sleep(.01)
			text1=V.Voice.get_voice_input()
			text.box1(text1,True)
			D.flip()
			MU.load("order.mp3")
			MU.play()
			while MU.get_busy():
				time.sleep(.01)
			order=V.Voice.get_voice_input()
			if order=="1":
				buttons.Button1(True)
			if order=="2":
				buttons.Button2(True)
			if order=="3":
				buttons.Button3(True)
			if order=="4":
				buttons.Button4(True)
			D.flip()		
			MU.load("phone_no.mp3")
			MU.play()
			while MU.get_busy():
				time.sleep(.01)
			phone=V.Voice.get_voice_input()
			for digit in phone:
				if digit!=' ':
					text2+=digit
			text.box2(text2,True)
			D.flip()
			MU.load("email.mp3")
			MU.play()

			
	main=screen()
	name=screen.Box(main)
	text1,text2,text3,button="","","",None
	text=screen.Text(main)
	eventz=screen.event_handler(main)
	name.display()
	buttons=screen.Buttons(main)
	D.flip()
	exit=False
	VC=False
	if(VC):
		time.sleep(0.5)
		while E.poll().type != pygame.KEYDOWN:
			pass
		Audio()
		
	while(not exit):
		D.flip()
		eventz.textbox(E.get())
	
	web=Web(text1,text2,text3,button)
	web.run()



