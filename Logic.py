from Settings.InitParameters import InitParameters
from GameObjects.Snake import Snake
from GameObjects.Apple import Apple


class Logic:
    '''
    :param snake: Instance of a snake object in game
    :type snake: Snake
    :param apple: Fruit for snake to grow
    :type apple: Apple
    '''
    def __init__(self, snake, apple):
        self.snake = snake
        self.apple = apple

    '''
    checks for collisions with walls
    '''
    def wall_collisions(self):
        grid_size = InitParameters.GRID_SIZE
        flag =  next((True for snake in self.snake.positions if
                      snake.x_pos >= grid_size or
                      snake.y_pos >= grid_size or
                      snake.x_pos < 0 or
                      snake.y_pos < 0), False)
        if flag:
            self.game_over()
            return True
        else:
            return False

    '''
    Checks if head is in the tail
    '''
    def snake_collision(self):
        head = self.snake.positions[-1]
        for tail in range(len(self.snake.positions) - 1):
            if head == self.snake.positions[tail]:
                self.game_over()
                return True
        else:
            return False

    '''
    Checks if snake is on apple and if it is makes it grow
    '''
    def is_on_apple(self):
        if self.snake.is_collision(self.apple.positions):
            self.apple.place_random()
            self.snake.grow()

    '''
    Game over condition
    '''
    def game_over(self):
        print("Game Over")
        self.snake.__init__()
        self.apple.__init__()

    def evaluate(self):
        self.wall_collisions()
        self.snake_collision()
        self.is_on_apple()
