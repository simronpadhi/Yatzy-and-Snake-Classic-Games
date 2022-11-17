"""Module for implementing snake."""

class Block:
    """Class for implementing snake blocks."""
    def __init__(self, topleft, size, colour):
        """
        Constructor for Block class.

        Args:
           topleft: Tuple of x- and y- co-ordinates of the topleft corner.
           size: Tuple of width and height of the block.
           colour: Tuple of r,g,b colour values of the block.
        """
        self.topleft = topleft
        self.size = size
        self.colour = colour

    def get_coordinates(self):
        """Returns the co-ordinates of the block."""
        return self.topleft

    def get_size(self):
        """Returns the size of the block."""
        return self.size

    def get_colour(self):
        """Returns the colour of the block."""
        return self.colour

def point_in_rect(point, topleft, size):
    """
    Checks if a point is in the given shape.

    Args:
       point: Tuple of coordinates of point.
       topleft: Tuple of coordinates of topleft corner of shape.
       size: Tuple of width and height of the shape.

    Returns:
       bool: True if the point is in the shape, False otherwise.
    """
    if point[0] < topleft[0]:
        return False
    if point[0] > (topleft[0]+size[0]):
        return False
    if point[1] < topleft[1]:
        return False
    if point[1] > (topleft[1]+size[1]):
        return False
    return True

def shape_in_shape(topleft1, size1, topleft2, size2):
    """
    Checks if first shape is inside second shape.

    Args:
       topleft1: Tuple of coordinates of topleft corner of first shape.
       size1: Tuple of width and height of first shape.
       topleft2: Tuple of coordinates of topleft corner of second shape.
       size2: Tuple of width and height of second shape.

    Returns:
       bool: True if first shape is completely inside the second shape, False otherwise.
    """
    if not point_in_rect(topleft1, topleft2, size2):
        return False
    if not point_in_rect((topleft1[0]+size1[0], topleft1[1]), topleft2, size2):
        return False
    if not point_in_rect((topleft1[0], topleft1[1]+size1[1]), topleft2, size2):
        return False
    if not point_in_rect((topleft1[0]+size1[0], topleft1[1]+size1[1]), topleft2, size2):
        return False
    return True

class BlockIterator:
    """Iterator class."""
    def __init__(self, snake):
        """Constructor for Iterator."""
        self._snake = snake
        self._index = 0

    def __next__(self):
        """Returns the next block from snake."""
        if self._index < self._snake.length:
            block = self._snake.blocks[self._index]
            self._index += 1
            return block
        raise StopIteration

class Snake:
    """Class for implementing Snake."""

    def __init__(self, head, size, colour):
        """
        Constructor for Snake class.

        Args:
           head: Tuple of x- and y- co-ordinates for top left
              of head block of snake.
           size: Tuple of width and height of each block of snake.
           colour: Tuple of r,g,b colour values that build up the snake.
        """
        self.head = head
        self.size = size
        self.colour = colour
        self.length = 1
        self.blocks = []
        self.blocks.append(Block(self.head, self.size, self.colour))

    def move_left(self):
        """Method for moving the snake to the left by one block."""
        topleft_old = self.blocks[0].topleft
        for i in range(self.length-1, 0, -1):
            self.blocks[i].topleft = self.blocks[i-1].topleft
        self.blocks[0].topleft = (topleft_old[0]-self.size[0], topleft_old[1])

    def move_right(self):
        """Method for moving the snake to the right by one block."""
        topleft_old = self.blocks[0].topleft
        for i in range(self.length-1, 0, -1):
            self.blocks[i].topleft = self.blocks[i-1].topleft
        self.blocks[0].topleft = (topleft_old[0]+self.size[0], topleft_old[1])

    def move_up(self):
        """Method for moving the snake up by one block."""
        topleft_old = self.blocks[0].topleft
        for i in range(self.length-1, 0, -1):
            self.blocks[i].topleft = self.blocks[i-1].topleft
        self.blocks[0].topleft = (topleft_old[0], topleft_old[1]-self.size[1])

    def move_down(self):
        """Method for moving the snake down by one block."""
        topleft_old = self.blocks[0].topleft
        for i in range(self.length-1, 0, -1):
            self.blocks[i].topleft = self.blocks[i-1].topleft
        self.blocks[0].topleft = (topleft_old[0], topleft_old[1]+self.size[1])

    def inside_bounds(self, topleft, bottomright):
        """
        Checks if the snake is completely inside the given area.

        Args:
           topleft: Tuple of coordinates of topleft corner of the bound.
           bottomright: Tuple of coordinates of bottomright corner of the bound.

        Returns:
           bool: True if snake is completely inside the bounds, False otherwise.
        """
        head_tl = self.blocks[0].get_coordinates()
        size = self.blocks[0].get_size()
        if head_tl[0] < topleft[0]:
            return False
        if (head_tl[0]+size[0]) > bottomright[0]:
            return False
        if head_tl[1] < topleft[1]:
            return False
        if (head_tl[1]+size[1]) > bottomright[1]:
            return False
        return True

    def check_collision(self, topleft, size):
        """
        Checks if any of the snake blocks collide with the given shape.

        Args:
           topleft: Tuple of coordinates of the shape to check collision with.
           size: Tuple of width and height of the shape to check collision with.

        Returns:
           bool: True if any of the blocks collide, False otherwise.
        """
        for block in self.blocks:
            b_tl = block.get_coordinates()
            b_s = block.get_size()
            if point_in_rect(b_tl, topleft, size):
                return True
            if point_in_rect((b_tl[0]+b_s[0], b_tl[1]), topleft, size):
                return True
            if point_in_rect((b_tl[0], b_tl[1]+b_s[1]), topleft, size):
                return True
            if point_in_rect((b_tl[0]+b_s[0], b_tl[1]+b_s[1]), topleft, size):
                return True
        return False

    def check_collision_with_fruit(self, topleft, size):
        """
        Checks if snake head completely overlaps with the fruit.

        Args:
           topleft: Tuple of coordinates of the fruit.
           size: Tuple of width and height of the fruit.

        Returns:
           bool: True if snake head completely overlaps with the fruit, False otherwise.
        """
        head_topleft = self.blocks[0].get_coordinates()
        head_size = self.blocks[0].get_size()
        return shape_in_shape(topleft, size, head_topleft, head_size)

    def check_collision_with_self(self):
        """
        Checks collision with self.

        Returns:
           bool: True if the snake collided with itself, False otherwise.
        """
        head_tl = self.blocks[0].get_coordinates()
        for block in self.blocks:
            if block != self.blocks[0]:
                if block.get_coordinates() == head_tl:
                    return True
        return False

    def grow(self):
        """Adds one block at the end of snake."""
        self.blocks.append(Block(self.blocks[-1].topleft, self.size, self.colour))
        self.length += 1

    def __iter__(self):
        """Returns the Iterator object."""
        return BlockIterator(self)
