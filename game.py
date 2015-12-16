import meet
import random

PLAYING = True

cells=[]

user_cell={'radius':10, 'x':0, 'y':0, 'dx':0, 'dy':0, 'color': 'blue'}

for i in range(0,20):

	cells1= {'radius':meet.random.randint(2,20), 'x':meet.get_random_x(), 'y':meet.get_random_y(), 'dx':random.randint(-30,30)/100.0, 'dy':random.randint(-30,30)/100.0}
	cells1=meet.create_cell(cells1)
	cells.append(cells1)

user_cell=meet.create_cell(user_cell)
cells.append(user_cell)

def border(cells):
	for cell in cells:
		if cell.ycor() > meet.get_screen_height() or cell.ycor() < -meet.get_screen_height():
			cell.set_dy(-cell.get_dy()*1.01)
		if cell.xcor() > meet.get_screen_width() or cell.xcor() < -meet.get_screen_width():
			cell.set_dx(-cell.get_dx()*1.01)

def collision(cells):
	global user_cell, PLAYING
	for cell in cells:
		
		for boy in cells:

			if cell.distance(boy) <= cell.get_radius() + boy.get_radius():
				if cell.get_radius() > boy.get_radius():
					cell.set_radius(cell.get_radius()+boy.get_radius()/6)
					boy.goto(meet.get_random_x(), meet.get_random_y())
					boy.set_radius(meet.random.randint(2,40))
					if boy == user_cell:
						PLAYING= False
						print("game over, loser!")
				elif boy.get_radius() > cell.get_radius():
					boy.set_radius(boy.get_radius()+cell.get_radius()/6)
					cell.goto(meet.get_random_x(), meet.get_random_y())
					cell.set_radius(meet.random.randint(2,40))
					if cell == user_cell:
						PLAYING= False
						print("game over, loser!")

def user_collision(cells):
	global user_cell, PLAYING
	for cell in cells:
		if user_cell.distance(cell) <= user_cell.get_radius() + cell.get_radius():
			if user_cell.get_radius() > cell.get_radius():
				user_cell.set_radius(user_cell.get_radius()+cell.get_radius()/6)
				cell.goto(meet.get_random_x(), meet.get_random_y())
				cell.set_radius(meet.random.randint(2,40))
			elif cell.get_radius() > user_cell.get_radius():
				PLAYING = False
				print("game over! :(")
				
#if (int(boy.xcor()+boy.get_radius())>=int(cell.xcor()-cell.get_radius()) and int(boy.xcor()-boy.get_radius())<=int(cell.xcor()+cell.get_radius())) and (int(boy.ycor()+boy.get_radius())>=int(cell.ycor()-cell.get_radius()) and int(boy.ycor()-boy.get_radius())<=int(cell.ycor()+cell.get_radius())):




while PLAYING:
	meet.move_cells(cells)
	x,y=meet.get_user_direction(user_cell)
	if user_cell.ycor() > meet.get_screen_height() or user_cell.ycor() < -meet.get_screen_height():
		print("")
	elif user_cell.xcor() > meet.get_screen_width() or user_cell.xcor() < -meet.get_screen_width():
		print("")
	else:
		user_cell.set_dx(x)
		user_cell.set_dy(y)
	border(cells)
	collision(cells)
	#user_collision(cells)

