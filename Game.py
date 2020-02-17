from Engine.Engine import Engine
from GameObjects.Snake import Snake
from GameObjects.Apple import Apple
from Logic import Logic
from Engine.KeyboardHandler import KeyboardHandler
from Algorithms.Astar import Astar

class Game:
    def run(self):
        engine = Engine()
        snake = Snake()
        apple = Apple()
        logic = Logic(snake, apple)
        algorithm = Astar()
        is_running = True

        while is_running:
            algorithm.run(snake,apple.positions)
            KeyboardHandler.key_preesed(snake)

            snake.move()
            logic.evaluate()

            game_objects = [snake, apple, algorithm]
            engine.redraw(engine.window, game_objects)


if __name__ == '__main__':
    Game().run()