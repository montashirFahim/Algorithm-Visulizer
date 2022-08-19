import add_edges
import bfs
import circles
import dfs
import vis
import pygame
import c_count


dis_width=1200
dis_height=800

pygame.init()
screen=pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption("Algorithm Visualizer")
clock=pygame.time.Clock()

grey=(100,100,100)
white=(255,255,255)
yellow=(200,200,0)
red=(200,0,0)
black=(0,0,0)
blue=(50,50,150)
indigo=(240,248,255)

graph_img=pygame.image.load("graph_icon.png")
s_img=pygame.image.load("images.png")

def show(x,y):
	screen.blit(graph_img,(x,y))
	screen.blit(s_img,(x+400,y))

b2=(250,235,215)
def draw_rect(x,y):
	pygame.draw.rect(screen,black,[x-20,y-20,350,350])
	pygame.draw.rect(screen,black,[x-20+400,y-20,350,350])

def draw_rect2(x,y):
	pygame.draw.rect(screen,indigo,[x-10,y-10,330,330])
	pygame.draw.rect(screen,indigo,[x-10+400,y-10,330,330])

font = pygame.font.SysFont(None,100)

def msg_to_screen(msg,col,x,y):
	screen_text=font.render(msg,True,col)
	screen.blit(screen_text,[x,y])

font2 = pygame.font.SysFont(None,40)
def msg_to_screen2(msg,col,x,y):
	screen_text=font2.render(msg,True,col)
	screen.blit(screen_text,[x,y])


x=300
y=400

def main():
	screen.fill(indigo)
	draw_rect(x,y)
	draw_rect2(x,y)
	show(x,y)
	msg_to_screen("Welcome To Algorithm Visualizer",(0,250,0),50,50)
	msg_to_screen2("Press s to see Sorting Algorithm",(0,0,0),50,170)
	msg_to_screen2("Press b to see Breadth First Search Algorithm",(0,0,0),50,250)
	msg_to_screen2("Press d to see Depth First Search Algorithm",(0,0,0),50,330)
	pygame.display.update()
	run=True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run=False;

			elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
				c_count.run()

			elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
				dfs.run()

			elif event.type == pygame.KEYDOWN and event.key == pygame.K_b:
				bfs.run()
			pygame.display.update()

	pygame.quit()			



if __name__ == "__main__":
	main() 
