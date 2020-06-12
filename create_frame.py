import pygame

pygame.init()  # 초기화

screen_width = 480
screen_height = 640

# 화면 출력
screen = pygame.display.set_mode((screen_width, screen_height))
# 배경화면 그리기
background = pygame.image.load("./src/img/background.png")

# 폰트 정의
font = pygame.font.Font(None, 40)

# 총 시간
total_time = 10

# 시작시간
start_tick = pygame.time.get_ticks()

# 캐릭터그리기
character = pygame.image.load("./src/img/character1.png")
# 이미지의 사이즈 구해옴
character_size = character.get_rect().size
character_width = character_size[0]  # 캐릭터 가로크기
character_height = character_size[1]  # 캐릭터 세로크기
character_x_pos = (screen_width/2)-(character_width/2)  # 화면가로크기 중앙
character_y_pos = screen_height - character_height  # 화면세로크기 가장 밑

character_speed = 0.5


# 적 캐릭터

enemy = pygame.image.load("./src/img/enemy.png")

enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]  # 캐릭터 가로크기
enemy_height = enemy_size[1]  # 캐릭터 세로크기
enemy_x_pos = screen_width/2  # 화면가로크기 중앙
enemy_y_pos = screen_height/2  # 화면세로크기 가장 밑


# FPS(프레임 퍼 세컨드)
clock = pygame.time.Clock()

pygame.display.set_caption('nado_game')

# 이벤트 루프
running = True  # 게임이 진행중인가?

# 이동할 좌표
to_x = 0
to_y = 0

while running:
    frame = clock.tick(144)
    print('fps : ' + str(clock.get_fps()))
    for event in pygame.event.get():  # 이벤트를 받는다
        if event.type == pygame.QUIT:  # 창을 껏을때
            running = False

        if event.type == pygame.KEYDOWN:  # 키 눌렸을때
            if event.key == pygame.K_RIGHT:  # 오른쪽키 눌렀을때
                to_x += character_speed
            elif event.key == pygame.K_LEFT:  # 왼쪽방향키 눌렀을때
                to_x -= character_speed
            elif event.key == pygame.K_UP:  # 왼쪽방향키 눌렀을때
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:  # 왼쪽방향키 눌렀을때
                to_y += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * frame
    character_y_pos += to_y * frame
    # 가로 경계값
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # 충돌 처리
    # 캐릭터의 위치값을 가져온다
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    # 적의 위치값을 가져온다
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print('충돌했습니다.')
        running = False
    # screen.fill((0,0,255)) RGB값을 넣어준다
    # 또는
    screen.blit(background, (0, 0))  # 배경그리기
    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    # 타이머 넣는다
    # 경과시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_tick)/1000

    # 타이머
    timer = font.render(str(int(total_time - elapsed_time)),
                        True, (255, 255, 255))
    screen.blit(timer, (10, 10))

    if total_time - elapsed_time <= 0:
        running = False

    pygame.display.update()  # 게임화면을 다시그리기 ( 반드시 계속 실행해야한다)

pygame.time.delay(2000)

pygame.quit()
