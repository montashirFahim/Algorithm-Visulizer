import pygame
import math
import vis

dis_width=1200
dis_height=800

pygame.init()
screen=pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption("Algorithm Visualizer")
clock=pygame.time.Clock()

indigo=(240,248,255)

font = pygame.font.SysFont(None,70)

def msg_to_screen(msg,col,x,y):
	screen_text=font.render(msg,True,col)
	screen.blit(screen_text,[x,y])
font2 = pygame.font.SysFont(None,40)
def msg_to_screen2(msg,col,x,y):
	screen_text=font2.render(msg,True,col)
	screen.blit(screen_text,[x,y])

def run():
	screen.fill(indigo)
	msg_to_screen("Welcome To Sorting Algorithm Visualizer",(0,250,0),50,50)
	msg_to_screen2("Press s to see Sorting Algorithm Visualization",(0,0,0),50,170)
#	msg_to_screen2("Press c to see Complexity of sorting Algorithm",(0,0,0),50,250)
	pygame.display.update()
	run=True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run=False;
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
				vis.Run()

	
#if __name__ == "__main__":
#	main() 