from GameObjects.GameObject import GameObject
from GameObjects.GridRectangle import GridRectangle
from Settings.InitParameters import InitParameters
from Directions import Directions

class Snake(GameObject):
    '''
    Initializes snake with start positions
    '''
    def __init__(self):
        grid_size = InitParameters.GRID_SIZE
        red_color = (255,0,0)
        self.positions = [GridRectangle(grid_size / 2, grid_size / 2, red_color), GridRectangle(grid_size / 2 + 1, grid_size / 2, red_color)]
        self._direction = Directions.RIGHT

    '''
    Algorithm:
        1. Delete Tail (Last position in positions)
        2. Append a new position with the same values as the Head
        3. Move it in the _direction currently facing
    '''
    def move(self):
        #delete last
        del(self.positions[0])

        #create new position at exact position as first
        new_position = GridRectangle(self.positions[-1].x_pos, self.positions[-1].y_pos, self.positions[-1].color)
        self.positions.append(new_position)

        #Move it in the right _direction
        if self._direction is Directions.UP:
            self.positions[-1].y_pos-=1
        elif self._direction is Directions.RIGHT:
            self.positions[-1].x_pos+=1
        elif self._direction is Directions.DOWN:
            self.positions[-1].y_pos+=1
        elif self._direction is Directions.LEFT:
            self.positions[-1].x_pos-=1
    '''
    Makes snake bigger by 1 block
    Algorithm:
        1. Create a block at snakes tail
    '''
    def grow(self):
        new_position = new_position = GridRectangle(self.positions[0].x_pos, self.positions[0].y_pos, self.positions[0].color)
        self.positions.insert(0, new_position)


    '''
    Make sure snake cannot move backwards
    '''
    def change_direction(self, direction):
        if self._direction == Directions.UP and direction != Directions.DOWN:
            self._direction = direction
        elif self._direction == Directions.RIGHT and direction != Directions.LEFT:
            self._direction = direction
        elif self._direction == Directions.DOWN and direction != Directions.UP:
            self._direction = direction
        elif self._direction == Directions.LEFT and direction != Directions.RIGHT:
            self._direction = direction

    '''
    Draws each snake position on the GridBoard
    :param surface: window from PyGame
    '''
    def draw(self, surface):
        for position in self.positions:
            position.draw(surface)

