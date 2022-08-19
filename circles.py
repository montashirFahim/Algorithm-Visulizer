import pygame
from graph_data import graph

dis_width=1200
dis_height=800
bg_col = (0,0,0)
radius=30

def run():
	pygame.init()

	screen=pygame.display.set_mode((dis_width,dis_height))
	pygame.display.set_caption("Graph Algorithm Visualizer")
	clock=pygame.time.Clock()

	screen.fill(bg_col)

	for xy, _ in graph:
			pygame.draw.circle(screen,(255,255,200),xy,radius)
			pygame.draw.circle(screen,(0,150,150),xy,radius-4)

			pygame.display.update()

	run=True

	while run:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run=False
				pygame.quit()
				quit()