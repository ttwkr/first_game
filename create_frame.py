import pygame

pygame.init()  # 초기화

screen_width = 480
screen_height = 640

# 화면 출력
screen = pygame.display.set_mode((screen_width, screen_height))
# 배경화면 그리기
background = pygame.image.load("./src/img/background.png")
# 캐릭터그리기
character = pygame.image.load("./src/img/character1.png")
# 이미지의 사이즈 구해옴
character_size = character.get_rect().size
character_width = character_size[0]  # 캐릭터 가로크기
character_height = character_size[1]  # 캐릭터 세로크기
character_x_pos = (screen_width/2)-(character_width/2)  # 화면가로크기 중앙
character_y_pos = screen_height - character_height  # 화면세로크기 가장 밑

pygame.display.set_caption('nado_game')

# 이벤트 루프
running = True  # 게임이 진행중인가?

# 이동할 좌표
to_x = 0
to_y = 0

while running:
    for event in pygame.event.get():  # 이벤트를 받는다
        if event.type == pygame.QUIT:  # 창을 껏을때
            running = False

        if event.type == pygame.KEYDOWN:  # 키 눌렸을때
            if event.key == pygame.K_RIGHT:  # 오른쪽키 눌렀을때
                to_x += 5
            elif event.key == pygame.K_LEFT:  # 왼쪽방향키 눌렀을때
                to_x -= 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    character_x_pos += to_x
    # screen.fill((0,0,255)) RGB값을 넣어준다
    # 또는
    screen.blit(background, (0, 0))  # 배경그리기
    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터그리기
    pygame.display.update()  # 게임화면을 다시그리기 ( 반드시 계속 실행해야한다)


pygame.quit()
