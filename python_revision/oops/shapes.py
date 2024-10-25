## FRONT MATTER FOR DRAWING/SAVING IMAGES, ETC
import math

from PIL import Image as PILImage
from PIL.ImageEnhance import Color

# some test colors
COLORS = {
    "red": (255, 0, 0),
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "green": (0, 100, 0),
    "lime": (0, 255, 0),
    "blue": (0, 0, 255),
    "cyan": (0, 255, 255),
    "yellow": (255, 230, 0),
    "purple": (179, 0, 199),
    "pink": (255, 0, 255),
    "orange": (255, 77, 0),
    "brown": (66, 52, 0),
    "grey": (152, 152, 152),
}


def new_image(width, height, fill=(240, 240, 240)):
    return {
        "height": height,
        "width": width,
        "pixels": [fill for r in range(height) for c in range(width)],
    }


def flat_index(image, x, y):
    assert 0 <= x < image["width"] and 0 <= y < image["height"]
    return (image["height"] - 1 - y) * image["width"] + x


def get_pixel(image, x, y):
    return image["pixels"][flat_index(image, x, y)]


def set_pixel(image, x, y, c):
    assert (
        isinstance(c, tuple)
        and len(c) == 3
        and all((isinstance(i, int) and 0 <= i <= 255) for i in c)
    )
    if 0 <= x < image["width"] and 0 <= y < image["height"]:
        image["pixels"][flat_index(image, x, y)] = c


def save_color_image(image, filename, mode="PNG"):
    out = PILImage.new(mode="RGB", size=(image["width"], image["height"]))
    out.putdata(image["pixels"])
    if isinstance(filename, str):
        out.save(filename)
    else:
        out.save(filename, mode)
    out.close()


## SHAPES!


class Shape:
    # All subclasses MUST implement the following:
    #
    # __contains__(self, p) returns True if point p is inside the shape
    # represented by self
    #
    # note that "(x, y) in s" for some instance of Shape
    # will be translated automatically to "s.__contains__((x, y))"
    #
    # s.center should give the (x,y) center point of the shape
    #
    # draw(self, image, color) should mutate the given image to draw the shape
    # represented by self on the given image in the given color
    #
    def __contains__(self, p):
        raise NotImplementedError("Subclass must implement this")

    def draw(self, image, color):
        for x in range(image["width"]):
            for y in range(image["height"]):
                if (x, y) in self:
                    set_pixel(image, x, y, color)


class Circle(Shape):
    def __init__(self, center, radius):
        # self._center_x,self._center_y = center
        self.center = center
        self._radius = radius
        # self._area =

    # @property
    # def area(self):
    #     return self._radius * self._radius

    def __contains__(self, point):
        assert type(point) == tuple and len(point) == 2

        # return math.pi*abs(x-self.center[0])*abs(y-self.center[1])<=self.area
        return (
            sum((i - j) ** 2 for i, j in zip(self.center, point))
            <= self._radius * self._radius
        )


class Rectangle(Shape):
    def __init__(self, lower_left, width, height):
        self.lower_left = lower_left
        self.width = width
        self.height = height

    @property
    def center(self):
        return (
            self.lower_left[0] + self.width // 2,
            self.lower_left[1] + self.height // 2,
        )

    # @center.setter
    # def center(self, value):
    #     self.lower_left = (value[0] - self.width // 2, value[1] - self.height // 2)
    #
    # def area(self):
    #     return self.width * self.height

    # def __contains__(self, item):
    #     # x,y = item
    #     # lx,ly = self.lower_left
    #     return sum((i-j)**2 for i,j in zip(self.center,item))<=self.area
    def __contains__(self, item):
        px, py = item
        lx, ly = self.lower_left[0], self.lower_left[1]
        return lx <= px <= lx + self.width and ly <= py <= ly + self.height


class Square(Rectangle):
    def __init__(self, lower_left, side):
        Rectangle.__init__(self, lower_left, side, side)
        # self.lower_left=lower_left
        # self.width=side
        # self.height=side
        # #self.area=side*side


if __name__ == "__main__":
    out_image = new_image(500, 500)

    # add code here to draw some shapes
    # circle = new_image(Circle((0,0),2),2)
    c = Circle((250, 250), 50)
    r = Rectangle((400, 400), 70, 20)
    c1 = Circle((20, 20), 40)
    square = Square((15, 25), 100)
    print(c.center)
    print(r.center)
    print(square.height, square.width)
    shapes = [
        (c, COLORS["purple"]),
        (r, COLORS["blue"]),
        (square, COLORS["green"]),
        (c1, COLORS["black"]),
    ]

    # print(square.area())
    # print(r.area())
    # print(square.area())
    for shape, color in shapes:
        shape.draw(out_image, color)
    save_color_image(out_image, "shapes.png")
