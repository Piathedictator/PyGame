import pygame
import random
pygame.init()

# set basic variables
#variables for screen size
SIZE = 4
TILE_SIZE = 127.5
GAP_SIZE = 10
MARGIN = 45
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

#############################

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

#############################
# defining the main functioning parts – moving and adding tiles
def add_new_tile(board): #adding new squares with a number either 2 or 4 
    empty_tiles = [(r, c) for r in range(SIZE) for c in range(SIZE) if board[r][c] == 0] #defining empty tiles
    if empty_tiles: #adding new squares only to empty tiles
        row, col = random.choice(empty_tiles)
        board[row][col] = 2 if random.random() < 0.65 else 4 #new square with number 2 or 4 - the chance for a 2 is greater

def slide_row_left(row):
    new_row = [i for i in row if i != 0] #filter of all non-empty tiles (not 0), all elements are stored in the list
    new_row += [0] * (SIZE - len(new_row)) #adding back  0s at the end of the list to maintain the same number of tiles in the list and on the board
    score_2048 = 0
    for i in range(SIZE - 1):
        if new_row[i] == new_row[i + 1] and new_row[i] != 0: #comparing the elements next to each other and doubling the first value if equivalent, setting 2. value 0
            new_row[i] *= 2
            score_2048 += new_row[i]  # Update score
            new_row[i + 1] = 0
    new_row = [i for i in new_row if i != 0] #filter of all 0s
    new_row += [0] * (SIZE - len(new_row)) #adding the 0s at the end of the list | see above
    return new_row, score_2048

def move_left(board): #adding the merged and shifted rows to the new board
    new_board = []
    partial_score_2048 = 0
    for row in board:
        new_row, score_2048 = slide_row_left(row)
        new_board.append(new_row)
        partial_score_2048 += score_2048
    return new_board, partial_score_2048
def move_right(board):
    new_board = []
    partial_score_2048 = 0
    for row in board:
        new_row, score_2048 = slide_row_left(row[::-1])  # Get the new row and score
        new_board.append(new_row[::-1])  # Reverse the new row back to the original order
        partial_score_2048 += score_2048
    return new_board, partial_score_2048
def move_up(board):
    new_board = list(zip(*board)) #swapping row and column | note: zip returns tuples | therefore unpacking(*) and converting to list
    new_board, partial_score_2048 = move_left(new_board) #performing the merge and shift (left)
    return [list(row) for row in zip(*new_board)], partial_score_2048 #swapping row and column back | unpack | list
def move_down(board):
    new_board = list(zip(*board)) #swapping row and column | note: zip returns tuples | therefore unpacking(*) and converting to list
    new_board, partial_score_2048 = move_right(new_board) #performing the merge and shift (right)
    return [list(row) for row in zip(*new_board)], partial_score_2048 #swapping row and column back | unpack | list

#############################

def check_moves_available(board):
    for row in range(SIZE): #checking rows
        if 0 in board[row]: #checking for empty tiles
            return True #if row with 0: true
        for col in range(SIZE - 1):
            if board[row][col] == board[row][col + 1]: #checking for identical tiles next to each other (horizontal merges)
                return True
    for col in range(SIZE): #checking columns
        for row in range(SIZE - 1):
            if board[row][col] == board[row + 1][col]: #checking for identical tiles next to each other (vertical merges)
                return True
    return False #if not able to merge or empty = false

#############################

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #game window
    pygame.display.set_caption("2048 Game") #title
    clock = pygame.time.Clock() #frame rate

    board = [[0] * SIZE for _ in range(SIZE)] #list of 0s size times, size times | creating a grid of e.g. 4x4
    add_new_tile(board) #initializing a random tile (2/ 4)
    add_new_tile(board) #start with two random tiles

    running = True
    lost = False
    total_score_2048 = 0

    while running:
        for event in pygame.event.get(): #recalls previous frame
            if event.type == pygame.QUIT: #closing game
                running = False
            elif event.type == pygame.KEYDOWN: #implementing the keys
                if not lost: #moving left, right, up, down
                    if event.key == pygame.K_LEFT:
                        board, score_increment_2048 = move_left(board)
                    elif event.key == pygame.K_RIGHT:
                        board, score_increment_2048 = move_right(board)
                    elif event.key == pygame.K_UP:
                        board,score_increment_2048 = move_up(board)
                    elif event.key == pygame.K_DOWN:
                        board, score_increment_2048 = move_down(board)
                    total_score_2048 += score_increment_2048
                    add_new_tile(board) #after a move/ merge add new tile
                    lost = not check_moves_available(board) #if free moves = true -> lost = false | if free moves = false -> lost = true

        draw_board(screen, board) #draw current state

        if lost:
            text = FONT.render("You lost!", True, (255, 0, 0)) #losing text
            text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)) #center
            screen.blit(text, text_rect) #show text

        score_text = FONT.render(f"Score: {total_score_2048}", True, (0, 0, 0)) # Display the score
        score_x = SCREEN_WIDTH - MARGIN - score_text.get_width()  # Calculate x position for top right
        screen.blit(score_text, (score_x, 0))  # Display score

        pygame.display.flip() #updating the frame
        clock.tick(30) #30 fps

    pygame.quit()

if __name__ == "__main__":
    main()