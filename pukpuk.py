import pygame
import random
# Собственные исключения
class ShipPlacementError(Exception):
    pass
class OutOfBoardError(Exception):
    pass
class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.is_hit = False
        self.is_ship = False

    def draw(self, surface):
        rect = pygame.Rect(self.col * CELL_SIZE, self.row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(surface, WHITE, rect, 1)
        if self.is_hit:
            if self.is_ship:
                pygame.draw.rect(surface, BLUE, rect)
            else:
                pygame.draw.rect(surface, RED, rect)

# Класс игрового поля
class Board:
    def __init__(self, size):
        self.size = size
        self.cells = [[Cell(row, col) for col in range(size)] for row in range(size)]
        self.ships = []
        self.place_ships()

    # Размещение корабля,горизонтальная или вертикальная
    def place_ships(self):
        for ship_size in SHIP_SIZES:
            # Ориентации: 0 - горизонтальный, 1 - вертикальный
            orientation = random.randint(0, 1)
            while True:
                try:
                    self.place_single_ship(ship_size, orientation)
                    break
                except ShipPlacementError:
                    orientation = (orientation + 1) % 2  # Переключение ориентации
    #ориентация,проверка размещения корабля,добавление в self.ships
    def place_single_ship(self, size, orientation):
        while True:
            if orientation == 0:
                row = random.randint(0, self.size - 1)
                col = random.randint(0, self.size - size)
            else:
                row = random.randint(0, self.size - size)
                col = random.randint(0, self.size - 1)

            if self.check_placement(row, col, size, orientation):
                for i in range(size):
                    if orientation == 0:
                        self.cells[row][col + i].is_ship = True
                    else:
                        self.cells[row + i][col].is_ship = True
                self.ships.append([(row, col + i) for i in range(size)] if orientation == 0 else [(row + i, col) for i in range(size)])
                break
            else:
                continue

    def check_placement(self, row, col, size, orientation): #проверка возможности размещения корабля определенного размера и ориентации
        if orientation == 0:  # Горизонтальная
            for i in range(col, col + size):
                if i >= self.size or not self.is_cell_clear(row, i):
                    return False
        else:  # Вертикальная
            for i in range(row, row + size):
                if i >= self.size or not self.is_cell_clear(i, col):
                    return False
        return True

    def is_cell_clear(self, row, col):#является ли конкретная ячейка на игровом поле свободной для размещения корабля
        if row < 0 or row >= self.size or col < 0 or col >= self.size:
            return False
        cell = self.cells[row][col]
        if cell.is_ship:
            return False
        for r in range(max(0, row - 1), min(self.size, row + 2)):
            for c in range(max(0, col - 1), min(self.size, col + 2)):
                if self.cells[r][c].is_ship:
                    return False
        return True

    def handle_shot(self, row, col): # проверка на выстрел,был ли он или нет
        if not (0 <= row < self.size and 0 <= col < self.size):
            raise OutOfBoardError("Выстрел за пределами игрового поля")
        cell = self.cells[row][col]
        if cell.is_hit:
            return
        cell.is_hit = True
        if cell.is_ship:
            for ship in self.ships:
                if (row, col) in ship:
                    ship.remove((row, col))
                    if not ship:
                        self.ships.remove(ship)
                        print("Корабль потоплен!")

    def draw(self, surface):#ячейки
        for row in self.cells:
            for cell in row:
                cell.draw(surface)

    def are_ships_remaining(self):#есть еще корабли или нет
        return bool(self.ships)
def draw_victory_message(surface):#если нету то победа
    font = pygame.font.SysFont("Arial", 50)
    text = font.render("ПОБЕДА!", True, (0, 255, 0))  # Зеленый цвет
    text_rect = text.get_rect()
    text_rect.center = (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2)
    surface.fill(BLACK)
    surface.blit(text, text_rect)
    pygame.display.flip()
pygame.init()
WINDOW_SIZE = (600, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Морской бой")
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
CELL_SIZE = 50
BOARD_SIZE = 10
SHIP_SIZES = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
board = Board(BOARD_SIZE)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            try:
                pos = pygame.mouse.get_pos()
                row = pos[1] // CELL_SIZE
                col = pos[0] // CELL_SIZE
                board.handle_shot(row, col)
            except OutOfBoardError as e:
                print(e)
    screen.fill(BLACK)
    board.draw(screen)
    if not board.are_ships_remaining():
        draw_victory_message(screen)
        pygame.time.wait(3000)  # Ожидаем 3 секунды, чтобы игрок увидел сообщение
        running = False
    pygame.display.flip()