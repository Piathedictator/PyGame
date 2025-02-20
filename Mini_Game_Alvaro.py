import pygame
import random
pygame.init()

# set basic variables
#variables for screen size
SIZE = 4
TILE_SIZE = 100
GAP_SIZE = 10
MARGIN = 20
SCREEN_SIZE = SIZE * TILE_SIZE + (SIZE + 1) * GAP_SIZE + 2 * MARGIN
SCREEN_WIDTH = SCREEN_SIZE
SCREEN_HEIGHT = SCREEN_SIZE

# variables - styling: font, color
BACKGROUND_COLOR = (255, 251, 240)
EMPTY_TILE_COLOR = (205, 192, 180)
TILE_COLORS = {
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46)
}
FONT_COLOR = (0, 0, 0)
FONT = pygame.font.SysFont('arial', 40)



# basics of game board and playing tiles
def draw_tile(screen, value, x, y): #defining the appearance of the single tiles shown (excluding the colored tiles with numbers (2,4,8...))
    color = TILE_COLORS.get(value, (60, 58, 50)) #background color of the tile
    rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE) #tile size, square
    pygame.draw.rect(screen, color, rect)
    if value != 0: #tile labeling _ color and positioning
        text = FONT.render(str(value), True, FONT_COLOR)
        text_rect = text.get_rect(center=(x + TILE_SIZE / 2, y + TILE_SIZE / 2))
        screen.blit(text, text_rect)
def draw_board(screen, board): #defining the general board appearance
    screen.fill(BACKGROUND_COLOR)
    for row in range(SIZE): #setting up the grid - row and colum
        for col in range(SIZE):
            value = board[row][col]
            x = MARGIN + GAP_SIZE + col * (TILE_SIZE + GAP_SIZE) #spacing between tiles
            y = MARGIN + GAP_SIZE + row * (TILE_SIZE + GAP_SIZE) #spacing between tiles
            draw_tile(screen, value, x, y)


# defining the main functioning parts
def add_new_tile(board): #adding new squares with a number either 2 or 4 
    empty_tiles = [(r, c) for r in range(SIZE) for c in range(SIZE) if board[r][c] == 0] #defining empty tiles
    if empty_tiles: #adding new squares only to empty tiles
        row, col = random.choice(empty_tiles)
        board[row][col] = 2 if random.random() < 0.65 else 4 #new square with number 2 or 4 - the chance for a 2 is greater

def slide_row_left(row):
    new_row = [i for i in row if i != 0] #filter of all non-empty tiles (not 0), all elements are stored in the list
    new_row += [0] * (SIZE - len(new_row)) #adding back  0s at the end of the list to maintain the same number of tiles in the list and on the board
    for i in range(SIZE - 1): 
        if new_row[i] == new_row[i + 1] and new_row[i] != 0: #comparing the elements next to each other and doubling the first value if equvalent, setting 2. value 0
            new_row[i] *= 2 
            new_row[i + 1] = 0
    new_row = [i for i in new_row if i != 0]
    new_row += [0] * (SIZE - len(new_row))
    return new_row
def move_left(board):
    new_board = []
    for row in board:
        new_board.append(slide_row_left(row))
    return new_board
def move_right(board):
    new_board = []
    for row in board:
        new_board.append(slide_row_left(row[::-1])[::-1])
    return new_board
def move_up(board):
    new_board = list(zip(*board))
    new_board = move_left(new_board)
    return [list(row) for row in zip(*new_board)]
def move_down(board):
    new_board = list(zip(*board))
    new_board = move_right(new_board)
    return [list(row) for row in zip(*new_board)]


def check_win(board):
    for row in board:
        if 2048 in row:
            return True
    return False

def check_moves_available(board):
    for row in range(SIZE):
        if 0 in board[row]:
            return True
        for col in range(SIZE - 1):
            if board[row][col] == board[row][col + 1]:
                return True
    for col in range(SIZE):
        for row in range(SIZE - 1):
            if board[row][col] == board[row + 1][col]:
                return True
    return False


def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("2048 Game")
    clock = pygame.time.Clock()

    board = [[0] * SIZE for _ in range(SIZE)]
    add_new_tile(board)
    add_new_tile(board)

    running = True
    won = False
    lost = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if not won and not lost:
                    if event.key == pygame.K_LEFT:
                        board = move_left(board)
                    elif event.key == pygame.K_RIGHT:
                        board = move_right(board)
                    elif event.key == pygame.K_UP:
                        board = move_up(board)
                    elif event.key == pygame.K_DOWN:
                        board = move_down(board)
                    add_new_tile(board)
                    won = check_win(board)
                    lost = not check_moves_available(board)

        draw_board(screen, board)

        if won:
            text = FONT.render("You won!", True, (255, 0, 0))
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            screen.blit(text, text_rect)
        elif lost:
            text = FONT.render("You lost!", True, (255, 0, 0))
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            screen.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(30)


    pygame.quit()
if __name__ == "__main__":
    main()