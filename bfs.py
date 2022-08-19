import pygame
from graph_data import graph

dis_width=1200
dis_height=800

radius=30
speed=2

grey=(100,100,100)
white=(255,255,255)
yellow=(200,200,0)
red=(200,0,0)
black=(0,0,0)
blue=(50,50,150)


def run():
	global screen,edges,clock

	for node in graph:
		node.extend([grey,black])

	build_edges()
	pygame.init()

	clock=pygame.time.Clock()

	screen=pygame.display.set_mode((dis_width,dis_height))
	pygame.display.set_caption("Graph Algorithm Visualizer")
	draw_graph()
	update()
	pygame.time.delay(2000)

	queue=[0]
	while len(queue)>0:
		n1=queue.pop(0)
		curr=graph[n1]
		curr[2]=white
		curr[3]=yellow

		for n2 in curr[1]:
			if graph[n2][3]==black and n2 not in queue:
				queue.append(n2)

				graph[n2][2]=white
				graph[n2][3]=red
				edges[edge_id(n1,n2)][1]=white
				update()

		curr[3]=blue
		update()

	f=True
	while f:
		pygame.time.wait(5000)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				f=False

	pygame.quit()
		

def edge_id(n1, n2):
	return tuple(sorted((n1, n2)))

def build_edges():
	global edges
	edges={}
	for n1,(_,adjacents,_,_) in enumerate(graph):
		for n2 in adjacents:
			e_id=edge_id(n1,n2)
			if e_id not in edges:
				edges[e_id]=[(n1,n2),grey]


def draw_graph():
	global graph,screen,edges

	screen.fill((0,0,0))

	for n in edges.values():
		(n1,n2),col=n
		pygame.draw.line(screen,col,graph[n1][0],graph[n2][0],2)
	
	for xy,_,l_col,f_col in graph:
		circle_fill(xy,l_col,f_col,30,2)


def update():
	global clock
	draw_graph()
	pygame.display.update()
	clock.tick(speed)

def circle_fill(xy,l_col,f_col,radius,thickness):
	global screen
	pygame.draw.circle(screen,l_col,xy,radius)
	pygame.draw.circle(screen,f_col,xy,radius)