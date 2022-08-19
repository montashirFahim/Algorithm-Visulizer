import pygame 
from graph_data import graph

dis_width=1200
dis_height=800
white=(255,255,255)
blue=(50,50,160)
radius=30


def run():
	global screen,edges

	pygame.init()
	draw_edges()

	screen=pygame.display.set_mode((dis_width,dis_height))
	pygame.display.set_caption("Graph Algorithm Visualizer")
	clock=pygame.time.Clock()

	screen.fill((0,0,0))

	for n1,n2 in edges:
		pygame.draw.line(screen,white,graph[n1][0],graph[n2][0],2)
	
	for xy,_ in graph:
		circle_fill(xy, white, blue, 30, 2)

	pygame.display.update()

	T=True
	while T:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				T=False
				pygame.quit()
				quit()


def circle_fill(xy,l_col,f_col,radius,thickness):
	global screen
	pygame.draw.circle(screen,l_col,xy,radius)
	pygame.draw.circle(screen,f_col,xy,radius-thickness)
	
def edge_id(i,j):
	return (min(i,j),max(i,j))

def draw_edges():
	global edges 
	edges={}

	for i, (_,adjacents) in enumerate(graph):
		for j in adjacents:
			e_id=edge_id(i,j)
			if e_id not in edges:
				edges[e_id]=(i,j)

