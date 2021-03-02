import pygame
import random
import os

pygame.mixer.init()


x = pygame.init()


white = (255,255,255)
red =(255,0,0)
black = (0,0,0)


screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width,screen_height))


pygame.display.set_caption("Snakes")
pygame.display.update()





clock = pygame.time.Clock()
font = pygame.font.SysFont(None,55)



def text_screen(text,color,x,y):
	screen_text = font.render(text,True,color)
	gameWindow.blit(screen_text,[x,y])



def plot_snake(gameWindow,color,snake_list,size):
	snake_size=25
	for x,y in snake_list:
		pygame.draw.rect(gameWindow,color,[x,y,snake_size,snake_size])

def welcome():
	exit_game = False
	while not exit_game:
		gameWindow.fill((233,220,229))
		text_screen("Welcome to Snakes", black ,260,250)
		text_screen("Press Space to Play Snakes", black ,200,290)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit_game=True

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					pygame.mixer.music.load('bgm.mp3')
					pygame.mixer.music.play()
					gameloop()

			pygame.display.update()
			clock.tick(60)





def gameloop():
	exit_game=False
	game_over = False
	snake_x=45
	snake_y=55

	food_x=random.randint(0,screen_width/2)
	food_y=random.randint(0,screen_height/2)

	snake_list = []
	snake_length = 1

	velocity_x=0
	velocity_y=0
	init_velocity=3

	if(not os.path.exists("high score.txt")):
		with open("high score.txt","w") as f:
			f.write("0")

	with open("high score.txt","r") as f:
		highScore = f.read()


	snake_size=25
	score = 0
	fps = 60

	while not exit_game:

		if game_over:

			with open("high score.txt","w") as f:
				f.write(str(highScore))

			gameWindow.fill(white)
			text_screen("Game Over! Press Enter to Continue",red,40,screen_height/2)
			
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					exit_game=True

				if event.type==pygame.KEYDOWN:
					if event.key==pygame.K_RETURN:
						welcome()
		else:

			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					exit_game=True

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RIGHT:
						velocity_x=init_velocity
						velocity_y=0

					if event.key == pygame.K_LEFT:
						velocity_x=-init_velocity
						velocity_y=0

					if event.key == pygame.K_UP:
						velocity_y=-init_velocity
						velocity_x=0

					if event.key == pygame.K_DOWN:
						velocity_y=init_velocity
						velocity_x=0

			snake_x = snake_x + velocity_x
			snake_y = snake_y + velocity_y

			if abs(snake_x - food_x) <10 and abs(snake_y - food_y) <10:
				score+=10
				food_x=random.randint(0,screen_width)
				food_y=random.randint(0,screen_height)
				# snake_size+=10
				snake_length+=5
				if score>int(highScore):
					highScore=score



			gameWindow.fill(white)
			text_screen("Score:"+str(score) + " High Score: "+str(highScore),red,5,5)
			pygame.draw.rect(gameWindow,red,[food_x,food_y,snake_size,snake_size])

			head = []
			head.append(snake_x)
			head.append(snake_y)
			snake_list.append(head)


			if len(snake_list)>snake_length:
				del snake_list[0]


			if head in snake_list[:-2]:
				game_over = True

			if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
				game_over=True
				
			plot_snake(gameWindow,black,snake_list,snake_size)

		pygame.display.update()
		clock.tick(fps)

	pygame.quit()
	quit()

welcome()