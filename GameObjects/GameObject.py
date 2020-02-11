from abc import ABC, abstractmethod, abstractproperty


class GameObject(ABC):
    '''
    Abstract class for all GameObjects (Used so that all objects can be drawn using a common interface)
    '''
    positions = []
    def is_collision(self, object_positions):
            return next((position for position in self.positions if
                         position == object_positions), False)


    @abstractmethod
    def draw(self, surface):
        pass
