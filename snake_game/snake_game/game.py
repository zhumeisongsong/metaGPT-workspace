import curses
import random
import time

class Game:
    def __init__(self, width: int, height: int, delay: int):
        self.score = 0
        self.width = width
        self.height = height
        self.delay = delay
        self.direction = curses.KEY_RIGHT
        self.snake_x = [width // 2, width // 2 - 1, width // 2 - 2]
        self.snake_y = [height // 2, height // 2, height // 2]
        self.food_x = random.randint(1, width - 2)
        self.food_y = random.randint(1, height - 2)
        self.game_over = False

    def init_game(self):
        curses.initscr()
        curses.curs_set(0)
        self.win = curses.newwin(self.height, self.width, 0, 0)
        self.win.keypad(1)
        self.win.timeout(self.delay)

    def draw_border(self):
        for x in range(self.width):
            self.win.addch(0, x, curses.ACS_BLOCK)
            self.win.addch(self.height - 1, x, curses.ACS_BLOCK)
        for y in range(self.height):
            self.win.addch(y, 0, curses.ACS_BLOCK)
            self.win.addch(y, self.width - 1, curses.ACS_BLOCK)

    def draw_snake(self):
        for i in range(len(self.snake_x)):
            self.win.addch(self.snake_y[i], self.snake_x[i], curses.ACS_CKBOARD)

    def draw_food(self):
        self.win.addch(self.food_y, self.food_x, curses.ACS_DIAMOND)

    def display_score(self):
        score_text = f"Score: {self.score}"
        self.win.addstr(0, self.width // 2 - len(score_text) // 2, score_text)

    def get_user_input(self):
        key = self.win.getch()
        if key in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT]:
            self.direction = key

    def move_snake(self):
        head_x = self.snake_x[0]
        head_y = self.snake_y[0]
        if self.direction == curses.KEY_UP:
            head_y -= 1
        elif self.direction == curses.KEY_DOWN:
            head_y += 1
        elif self.direction == curses.KEY_LEFT:
            head_x -= 1
        elif self.direction == curses.KEY_RIGHT:
            head_x += 1
        self.snake_x.insert(0, head_x)
        self.snake_y.insert(0, head_y)
        if head_x == self.food_x and head_y == self.food_y:
            self.score += 1
            self.food_x = random.randint(1, self.width - 2)
            self.food_y = random.randint(1, self.height - 2)
        else:
            self.snake_x.pop()
            self.snake_y.pop()

    def check_collision(self):
        head_x = self.snake_x[0]
        head_y = self.snake_y[0]
        if head_x in [0, self.width - 1] or head_y in [0, self.height - 1]:
            self.game_over = True
        for i in range(1, len(self.snake_x)):
            if head_x == self.snake_x[i] and head_y == self.snake_y[i]:
                self.game_over = True

    def game_loop(self):
        while not self.game_over:
            self.win.clear()
            self.draw_border()
            self.draw_snake()
            self.draw_food()
            self.display_score()
            self.win.refresh()
            self.get_user_input()
            self.move_snake()
            self.check_collision()
            time.sleep(1 / self.delay)

    def start(self):
        self.init_game()
        self.game_loop()

game = Game(40, 20, 10)
game.start()
