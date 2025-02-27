#
#
# TUTORIAL DE PONG
# CREADOR: MUNDO PYTHON
# YOUTUBE CHANNEL: MUNDO PYTHON
#
#


def marcador(marca_izq, marca_der):
	# Marcador
	font = pygame.font.SysFont("serif", 30) # Fuente
	text = font.render(f"{marca_izq}         {marca_der}", True, white) # Texto
	center_x = (screen_size[0] // 2) - (text.get_width() // 2) # posicion text
	center_y = 20
	return screen.blit(text, [center_x, center_y]) # ponerlo en pantalla

# Para dibujar una línea discontinua
def dib_lin_dis(surface, color, start_pos, end_pos, dash_length=10, gap_length=5):
    x1, y1 = start_pos
    x2, y2 = end_pos
    dx = x2 - x1
    dy = y2 - y1
    distance = max(abs(dx), abs(dy))
    dx /= distance
    dy /= distance
    x, y = x1, y1
    for _ in range(int(distance / (dash_length + gap_length))):
        pygame.draw.line(surface, color, (int(x), int(y)), (int(x + dx * dash_length), int(y + dy * dash_length)))
        x += dx * (dash_length + gap_length)
        y += dy * (dash_length + gap_length)



import pygame
pygame.init()

#Colores
black = (0, 0, 0)
white = (255, 255, 255)
screen_size = (800, 600)
player_width = 15
player_height = 90
marca_izq, marca_der = 0, 0
cuenta_devueltas = 0


screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

#Coordenadas y velocidad del jugador 1
player1_x_coor = 50
player1_y_coor = 300 - 45
player1_y_speed = 0
p1_mov_spe = 3
p1_mov_spe_x = 3
player1_x_speed = 3
#Coordenadas y velocidad del jugador 2
player2_x_coor = 750 - player_width
player2_y_coor = 300 - 45
player2_y_speed = 0
p2_mov_spe = 3
p2_mov_spe_x = 3
player2_x_speed = 3

# Coordenadas de la pelota
pelota_x = 400
pelota_y = 300
pelota_speed_x = 3
pelota_speed_y = 3


game_over = False

while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_over = True
		if event.type == pygame.KEYDOWN:
			# Jugador 1
			if event.key == pygame.K_w:
				player1_y_speed = -p1_mov_spe
			if event.key == pygame.K_s:
				player1_y_speed = p1_mov_spe
			if event.key == pygame.K_a:
				player1_x_speed = -p1_mov_spe_x
			if event.key == pygame.K_d:
				player1_x_speed = p1_mov_spe_x
			# Jugador 2
			if event.key == pygame.K_UP:
				player2_y_speed = -p2_mov_spe
			if event.key == pygame.K_DOWN:
				player2_y_speed = p2_mov_spe
			if event.key == pygame.K_LEFT:
				player2_x_speed = -p2_mov_spe_x
			if event.key == pygame.K_RIGHT:
				player2_x_speed = p2_mov_spe_x

		if event.type == pygame.KEYUP:
			# Jugador 1
			if event.key == pygame.K_w:
				player1_y_speed = 0
			if event.key == pygame.K_s:
				player1_y_speed = 0
			if event.key == pygame.K_a:
				player1_x_speed = 0
			if event.key == pygame.K_d:
				player1_x_speed = 0
			# Jugador 2
			if event.key == pygame.K_UP:
				player2_y_speed = 0
			if event.key == pygame.K_DOWN:
				player2_y_speed = 0
			if event.key == pygame.K_LEFT:
				player2_x_speed = 0
			if event.key == pygame.K_RIGHT:
				player2_x_speed = 0

	if pelota_y > 590 or pelota_y < 10:
		pelota_speed_y *= -1

	# Control de jugadores que no se salgan de los límites de la pantalla
	if player1_x_coor < 5:
		player1_x_coor = 5

	if player1_x_coor > screen_size[0] // 2 - 20:
		player1_x_coor = screen_size[0] // 2 - 20

	if player1_y_coor > 595:
		player1_y_coor = 595
	
	if player1_y_coor < -85:
		player1_y_coor = -85
	
	if player2_x_coor < screen_size[0] // 2 + 5:
		player2_x_coor = screen_size[0] // 2 + 5

	if player2_x_coor > screen_size[0] - 20:
		player2_x_coor = screen_size[0] - 20
	
	if player2_y_coor > 595:
		player2_y_coor = 595
	
	if player2_y_coor < -85:
		player2_y_coor = -85


	# Revisa si la pelota sale del lado derecho
	if pelota_x > 800:
		pelota_x = 400
		pelota_y = 300
		marca_der += 1
		pelota_speed_x = 3
		pelota_speed_y = 3
		player1_y_speed = 3
		player2_y_speed = 3
		
		# Si sale de la pantalla, invierte direccion
		pelota_speed_x *= -1
		pelota_speed_y *= -1

	# Revisa si la pelota sale del lado izquierdo
	if pelota_x < 0:
		pelota_x = 400
		pelota_y = 300
		marca_izq += 1
		pelota_speed_x = 3
		pelota_speed_y = 3
		player1_y_speed = 3
		player2_y_speed = 3
		
		# Si sale de la pantalla, invierte direccion
		pelota_speed_x *= -1
		pelota_speed_y *= -1


	# Modifica las coordenadas para dar mov. a los jugadores/ pelota
	player1_y_coor += player1_y_speed
	player2_y_coor += player2_y_speed
	player1_x_coor += player1_x_speed
	player2_x_coor += player2_x_speed

	# Movimiento pelota
	pelota_x += pelota_speed_x
	pelota_y += pelota_speed_y

	screen.fill(black)
	#Zona de dibujo
	jugador1 = pygame.draw.rect(screen, white, (player1_x_coor, player1_y_coor, player_width, player_height))
	jugador2 = pygame.draw.rect(screen, white, (player2_x_coor, player2_y_coor, player_width, player_height))
	marcador(marca_der, marca_izq)
	dib_lin_dis(screen, white, (screen_size[0] // 2, 0), (screen_size[0] // 2, screen_size[1]))
	pelota = pygame.draw.circle(screen, white, (pelota_x, pelota_y), 10)


	# Colisiones
	if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
		cuenta_devueltas += 1
		pelota_speed_x *= -1
		if cuenta_devueltas >= 3:
			pelota_speed_x *= 1.1
			pelota_speed_y *= 1.1
			p1_mov_spe *= 1.1
			p2_mov_spe *= 1.1
			cuenta_vueltas = 0
			
		

	pygame.display.flip()
	clock.tick(60)
pygame.quit()
