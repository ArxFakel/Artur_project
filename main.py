import pygame
import random
from Object_Lines import Object_lin
from Enemys import Enemy
from Plants import Plant

pygame.init()  # инициализируем библиотеку pygame (программа синхронизируется с компьютером - настраивается звук, размер экрана и т.д)

screen_width = 1280
screen_height = 720

screen = pygame.display.set_mode((screen_width, screen_height)) # передали размеры экрана как картеж
point_for_soln = 0

# Делаем класс для кнопок
class Button():
    def __init__(self, x, y, width, height, text, font, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.font = font

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        text_surface = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.center = (self.x + self.width // 2, self.y + self.height // 2)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.x < pos[0] < self.x + self.width and self.y < pos[1] < self.y + self.height

class Frame():
    def __init__(self, x, y, width, height, color, background_Frame):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.background_Frame = background_Frame

    def draw(self):
        screen.blit(self.background_Frame, (self.x, self.y))

randsp = [124, 268, 412, 556, 680]

class Fire_bat:
    def __init__(self, x, y, picture, speed):
        self.x = x
        self.y = random_point = random.choice(randsp)
        self.picture = pygame.image.load(picture)  # загружаем картинку сразу в классе, а не в объекте (шаг 1)
        self.speed = speed

    def bat_move(self):
        if self.x > 200:
            self.x -= 0.1

fire_bat = Fire_bat(x=1000, y=random.choice(randsp), speed=0.1, picture="Picter/bat-a.png")  # Устанавливаем картинку для объекта класса (шаг 2)


def place_plant(flo, plant_type):
    global point_for_soln


    plant_cost = {
        "sunflower": 50,
        "shooter": 100,
        "vino": 150
    }


    if flo.empty and point_for_soln >= plant_cost.get(plant_type, float('inf')):
        # Создаем растение
        if plant_type == "sunflower":
            plant = Plant(x=flo.x, y=flo.y, picture="Picter/Podsolnyh.png")
        elif plant_type == "shooter":
            plant = Plant(x=flo.x, y=flo.y, picture="Picter/Cannon1.png")
        elif plant_type == "vino":
            plant = Plant(x=flo.x, y=flo.y, picture="Picter/vino_card.png")
        else:
            return False


        flo.empty = False
        flo.plant = plant

        point_for_soln -= plant_cost[plant_type]

        global sun_text, sun_text_surface
        sun_text = "Point: " + str(point_for_soln)
        sun_text_surface = font_sun.render(sun_text, True, color_font_sun)

        return True
    else:
        return False

def sun_spawn():
    pass

font_sun = pygame.font.Font(None, 36)  # Создали переменную где сохраняется тип шрифта(None=arial)

sun_text = "Point: " + str(point_for_soln)  # Создали переменную в которой сохраняется текст
color_font_sun = (250, 250, 250)  # ТИП ДАННЫХ tuple-картеж
print(type(color_font_sun), "----------------------------------")
sun_text_surface = font_sun.render(sun_text, True, color_font_sun)  # Создали объект где сохраняется настроенный текст

# Кнопки 1 фрейма (главное меню)
buttonplay = Button(530, 100, 200, 50, "Играть", pygame.font.SysFont("Arial", 20), (255, 255, 255))
buttonexit = Button(530, 200, 200, 50, "Выход", pygame.font.SysFont("Arial", 20), (255, 255, 255))
buttoncopper = Button(530, 300, 200, 50, "Настройки", pygame.font.SysFont("Arial", 20), (255, 255, 255))

# Кнопки 2 фрейма (меню обучения)
buttonesc = Button(10, 10, 50, 50, "Esc", pygame.font.SysFont("Arial", 20), (255, 255, 255))
button_Skip_training = Button(530, 200, 200, 50, "Пропустить обучение", pygame.font.SysFont("Arial", 20), (255, 255, 255))

# Кнопки 3 фрейма (игровой процесс)
button_start_game = Button(530, 300, 200, 50, "Начать игру", pygame.font.SysFont("Arial", 20), (255, 255, 255))
imagepvz = pygame.draw.rect(screen, (255, 179, 0), (150, 50, 75, 75))

# Загружаем фоновые изображения
background_image = pygame.image.load("Picter/PvZFon.png")
background_Frame = pygame.image.load("Picter/Frame_1.png")
background_image = pygame.transform.scale(background_image, (1280, 720))
background_Frame3 = pygame.image.load("Picter/Pvz.png")

# Песронажи/Структуры
cannon1 = pygame.image.load("Picter/Cannon1.png")
cannon1_x = 1050  # задали x для изображения пушки на 3 фрейме
cannon1_y = 10  # задали y для изображения пушки на 3 фрейме

podsolnyh = pygame.image.load("Picter/Podsolnyh.png").convert_alpha()  # Конвертировали изображение в Alpha-канал что бы убрать белый фон
podsolnyh = pygame.transform.scale(podsolnyh, (80, 88))  # Изменили размер изображение в коде при помощи transfor.scale
podsolnyh_x = 220
podsolnyh_y = 120

soln = pygame.image.load("Picter/solnishko.png").convert_alpha()
soln = pygame.transform.scale(soln, (80, 88))
soln_x = random.randint(0, 1180)
soln_y = random.randint(0, 650)
soln_visible = True  # Добавляем переменную для отслеживания видимости объекта soln

strplan = pygame.image.load("Picter/StrPlant.png")
strplan = pygame.transform.scale(strplan, (1770, 820))
strplan_x = -70
strplan_y = -330

card_sunflo = pygame.image.load("Picter/card_sunflower_black.png")
card_sunflo_x = 510
card_sunflo_y = 30
card_sunflo_st = True
card_sunflo_rect = pygame.Rect(card_sunflo_x, card_sunflo_y, 65, 90)

card_shoot = pygame.image.load("Picter/card_shooter_black.png")
card_shoot_x = 570
card_shoot_y = 30
card_shoot_st = True
card_shoot_rect = pygame.Rect(card_shoot_x, card_shoot_y, 65, 90)

card_vino = pygame.image.load("Picter/vino_card_black.png")
card_vino = pygame.transform.scale(card_vino, (65, 90))
card_vino_x = 630
card_vino_y = 30
card_vino_st = True
card_vino_rect = pygame.Rect(card_vino_x, card_vino_y, 65, 90)

bat_a = pygame.image.load("Picter/bat-a.png")
bat_a_x = 150
bat_a_y = 50
bat_b = pygame.image.load("Picter/bat-b.png")

bat_a2 = pygame.image.load("Picter/bat-a.png")
bat_a_x2 = 450
bat_a_y2 = 50
bat_b2 = pygame.image.load("Picter/bat-b.png")

cat = pygame.image.load("Picter/cat 2.png")
cat_x = 500
cat_y = 50

rect1 = pygame.Rect(120, 130, 75, 75)
rect1_color = (255, 179, 0)
rect1_color2 = (255, 179, 0)
rect2 = pygame.Rect(220, 130, 75, 75)

# Добавляем переменную для текущего кадра анимации
bat_frame = 0

# Добавляем переменную для времени последнего обновления кадра
last_update = pygame.time.get_ticks()

# Добавляем переменную для текущей позиции персонажа
bat_y = 50
bat_y2 = 50
cat_G2 = 50

zombie = Enemy(x=1000, y=350, picture=("Picter/zombie.png"), hp=120, speed=5000)

y_zrange = 20
zsplin = []
for z_l in range(5):
    y_zrange += 115
    zom_zl = Enemy(x=1000, y=y_zrange, picture=("Picter/zoombie.png"), hp=120, speed=5000)
    zsplin.append(zom_zl)

x_range = 30
y_range = 20
splin = []
for s_z in range(5):
    y_range += 115
    for n_z in range(9):
        x_range += 100
        obj_nz = Object_lin(x=x_range, y=y_range, width=80, height=80, color=(230, 0, 20), empty=True)
        splin.append(obj_nz)
    x_range = 30
print(splin)
status_rect = False

# Добавляем функцию для обновления кадра анимации
def update_bat_frame():
    global bat_frame, last_update

    # Проверяем, прошло ли достаточно времени с последнего обновления кадра
    if pygame.time.get_ticks() - last_update > 350:  # 350 миллисекунд между кадрами
        last_update = pygame.time.get_ticks()
        bat_frame = (bat_frame + 1) % 2  # Переключаем кадр между 0 и 1

# Создаем переменные для управления кнопками и фреймами
button_visible = True
frame = None
frame3 = None
running = True
Logica_exit = True

while running:  # while running == True
    current_time = pygame.time.get_ticks()  # Создали переменную в которой сохраняется время от запуска(в миллисекундах
    update_bat_frame()  # Вызываем функцию update_bat_frame

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  # 1
            pos = pygame.mouse.get_pos()
            print(pos)

            if frame3 is not None:  # Создали проверку работы процесса игры для активного фрейма
                print("Вы в процессе игры")
                if rect1.collidepoint(event.pos):
                    rect1_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                if rect2.collidepoint(event.pos):
                    rect1_color2 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

                if soln_visible and soln.get_rect(topleft=(soln_x, soln_y)).collidepoint(event.pos):
                    soln_visible = False
                    point_for_soln += 50
                    print(point_for_soln)
                    sun_text = "Point: " + str(point_for_soln)
                    sun_text_surface = font_sun.render(sun_text, True, color_font_sun)

                if card_sunflo_rect.collidepoint(event.pos):
                    if not card_sunflo_st:
                        # Если карточка подсолнуха не выбрана, выбираем её
                        card_sunflo = pygame.image.load("Picter/card_sunflower.png")
                        card_sunflo_st = True
                        card_shoot_st = False  # Сбрасываем выбор других карточек
                        card_vino_st = False
                        print("Вы Выбрали Карту Подсолнуха")
                    else:
                        # Если карточка подсолнуха уже выбрана, отменяем её выбор
                        card_sunflo = pygame.image.load("Picter/card_sunflower_black.png")
                        card_sunflo_st = False
                        print("Вы Отменили выбор Карты Подсолнуха")

                if card_shoot_rect.collidepoint(event.pos):
                    if not card_shoot_st:
                        card_shoot = pygame.image.load("Picter/card_shooter.png")
                        card_shoot_st = True
                        card_sunflo_st = False  # Сбрасываем выбор других карточек
                        card_vino_st = False
                        print("Вы Выбрали Карту Горохострела")
                    else:
                        card_shoot = pygame.image.load("Picter/card_shooter_black.png")
                        card_shoot_st = False
                        print("Вы Отменили выбор Карты Горохострела")

                if card_vino_rect.collidepoint(event.pos):
                    if not card_vino_st:
                        card_vino = pygame.image.load("Picter/vino_card.png")
                        card_vino_st = True
                        card_sunflo_st = False  # Сбрасываем выбор других карточек
                        card_shoot_st = False
                        print("Вы Выбрали Карту Виноградастрела")
                    else:
                        card_vino = pygame.image.load("Picter/vino_card_black.png")
                        card_vino_st = False
                        print("Вы Отменили выбор Карты Виноградастрела")

                for cl_z in splin:
                    if cl_z.rect.collidepoint(event.pos):
                        if card_vino_st:
                            if place_plant(cl_z, "vino"):
                                print("Вы вывели виноградастрела")
                                card_vino_st = False
                                card_vino = pygame.image.load("Picter/vino_card_black.png")
                        elif card_sunflo_st:
                            if place_plant(cl_z, "sunflower"):
                                print("Вы выбрали подсолнух")
                                card_sunflo_st = False
                                card_sunflo = pygame.image.load("Picter/card_sunflower_black.png")
                        elif card_shoot_st:
                            if place_plant(cl_z, "shooter"):
                                print("Вы выбрали горохострел")
                                card_shoot_st = False
                                card_shoot = pygame.image.load("Picter/card_shooter_black.png")

            else:
                print("Вы не в процессе игры")

            if buttonplay.is_clicked(pos):
                screen.fill((0, 0, 0))
                button_visible = False
                frame = Frame(0, 0, 1280, 720, (100, 100, 100), background_Frame)
                Logica_exit = False

                button4 = Button(530, 300, 200, 50, "Начать Обучение", pygame.font.SysFont("Arial", 20), (255, 255, 255))
                button_Skip_training = Button(530, 200, 200, 50, "Пропустить Обучение", pygame.font.SysFont("Arial", 20), (255, 255, 255))
                buttonesc = Button(10, 10, 50, 50, "Esc", pygame.font.SysFont("Arial", 20), (255, 255, 255))

            if button_Skip_training.is_clicked(pos):  # Проверяем нажатали кнопка пропустить игру
                print("Вы пропустили тренировку")
                screen.fill((0, 0, 0))
                button_visible = False
                frame = None
                frame3 = Frame(0, 0, 1280, 720, (100, 100, 100), background_Frame3)
                next_soln = pygame.time.get_ticks() + 8000
                print("Время в которое появляется солнце", str(next_soln))

            if buttonesc.is_clicked(pos):
                print("Кнопка esc нажата")
                print(buttonesc.is_clicked(pos))
                button_visible = True
                frame = None
                frame3 = None
                button4 = None
                button_Skip_training = None
                button_start_game = None

            elif buttonexit.is_clicked(pos) and Logica_exit == True:
                running = False
            else:
                print("Мышь нажата но не активирована")

    # Конец цикла for-проверки событий
    # НАЧАЛО ОТОБРАЖЕНИЯ ЭЛЕМЕНТОВ
    screen.blit(background_image, (0, 0))

    if button_visible:
        buttonplay.draw()
        buttonexit.draw()
        buttoncopper.draw()

    if frame:
        frame.draw()
        if button4 and not button_visible:
            button4.draw()
            button_Skip_training.draw()
            buttonesc.draw()

    if frame3:
        frame3.draw()

        # Выбираем текущее изображение в зависимости от текущего кадра
        bat_image = bat_a if bat_frame == 0 else bat_b

        screen.blit(fire_bat.picture, (fire_bat.x, fire_bat.y))

        fire_bat.bat_move()

        screen.blit(zombie.picture, (zombie.x, zombie.y))

        screen.blit(strplan, (strplan_x, strplan_y))

        screen.blit(card_sunflo, (card_sunflo_x, card_sunflo_y))

        screen.blit(card_shoot, (card_shoot_x, card_shoot_y))

        screen.blit(card_vino, (card_vino_x, card_vino_y))

        screen.blit(sun_text_surface, (20, 80))  # Отобразили текст на экране
        for d_kl in splin:  # Выводим на экран клетки
            d_kl.draw(screen)
        for z_kl in zsplin:  # Выводим на экран зомби
            z_kl.scblt(screen)
        if soln_visible and current_time > next_soln:
            screen.blit(soln, (soln_x, soln_y))
    pygame.display.update()

pygame.quit()
