from math import sqrt
from collections import namedtuple
from GameObjects.GameObject import GameObject
from GameObjects.GridRectangle import GridRectangle
from Directions import Directions

class Astar(GameObject):
    def __init__(self, ai=True):
        self.ai = ai

    def run(self, snake, destination):
        snake_head = snake.positions[-1]
        AstarTile = namedtuple('AstarTile', 'tile score')

        self.open_list = [AstarTile(snake_head, self.evaluate_score(snake_head, destination, snake))]
        self.closed_list = []
        iteration=1
        while(len(self.open_list) > 0):
            iteration+=1
            current_square = min(self.open_list, key=lambda x: x.score)
            self.closed_list.append(current_square)

            if next((position for position in self.closed_list if
                         position.tile == destination), False):
                break

            adjacent_squares = [GridRectangle(current_square.tile.x_pos - 1, current_square.tile.y_pos, (0, 0, 255)),
                               GridRectangle(current_square.tile.x_pos + 1, current_square.tile.y_pos, (0, 0, 255)),
                               GridRectangle(current_square.tile.x_pos, current_square.tile.y_pos + 1, (0, 0, 255)),
                               GridRectangle(current_square.tile.x_pos, current_square.tile.y_pos - 1, (0, 0, 255))]

            for aSquare in adjacent_squares:
                if aSquare in self.closed_list:
                    continue
                if aSquare not in self.open_list:
                    self.open_list.append(AstarTile(aSquare, self.evaluate_score(aSquare, destination, snake)))
                else:
                    pass
            if iteration == 100:
                break

        if self.ai == True:
            good_direction = self.closed_list[1]
            self.snake_change_direction(good_direction.tile, snake)

    def snake_change_direction(self, good_direction, snake):
        snake_head = snake.positions[-1]
        if snake.direction is Directions.RIGHT or snake.direction is Directions.LEFT:
            if snake_head.y_pos<good_direction.y_pos:
                snake.change_direction(Directions.DOWN)
            elif snake_head.y_pos>good_direction.y_pos:
                snake.change_direction(Directions.UP)

        if snake.direction is Directions.DOWN or snake.direction is Directions.UP:
            if snake_head.x_pos<good_direction.x_pos:
                snake.change_direction(Directions.RIGHT)
            elif snake_head.x_pos>good_direction.x_pos:
                snake.change_direction(Directions.LEFT)


    def evaluate_score(self, start, destination, snake):
        #If start in snake return max value this means collision
        if start in snake.positions:
            return 9999
        return sqrt(pow((destination.x_pos - start.x_pos),2) + pow((destination.y_pos-start.y_pos),2))

    def draw(self, surface):
        for square in self.closed_list:
            square.tile.draw(surface)

