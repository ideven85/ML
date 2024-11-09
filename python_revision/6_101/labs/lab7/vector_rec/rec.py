from rec_vector import Vector

GRAVITATIONAL_CONSTANT = 6.67e-11


class Body:
    def __init__(self, mass, position, initial_velocity=None):
        self.mass = mass
        self.position = position
        self.velocity = initial_velocity or Vector((0, 0))

    def force_from(self, other):
        """
        Compute the force exerted on one body (self) by another body (other).
        Returns a vector representing both the strength and direction of the
        force.
        """
        delta = other.position.sub(self.position)
        dist = delta.magnitude()
        direction = delta.normalized()
        magnitude = (
            (GRAVITATIONAL_CONSTANT * self.mass * other.mass)
            / (dist * dist)
        )
        return direction.scaled(magnitude)

    def net_force(self, bodies):
        """
        Computes the net force applied to self by all other bodies.
        """
        total = Vector((0, 0))
        for body in bodies:
            if body is self:
                continue
            total = total.add(self.force_from(body))
        return total

    def move(self, f, dt):
        """
        Given a force and a timestep duration, update the body's velocity and
        position.  f is a vector, dt is a float.
        """
        acceleration = f.scaled(1 / self.mass)
        self.velocity = self.velocity.add(acceleration.scaled(dt))
        self.position = self.position.add(self.velocity.scaled(dt))


class System:
    def __init__(self, bodies):
        self.bodies = bodies

    def step(self, dt):
        # Compute the net force acting on each body before moving anything
        net_forces = [b.net_force(self.bodies) for b in self.bodies]

        # Finally, apply the forces.
        for b, f in zip(self.bodies, net_forces):
            b.move(f, dt)


if __name__ == "__main__":
    # two bodies, stable motion
    bodies = [
        Body(1e25, Vector((0, 0.91e9)), Vector((400, 0))),
        Body(1e25, Vector((0, -0.91e9)), Vector((-400, 0))),
    ]

    ## two bodies, erratic motion
    #bodies = [
    #    Body(1e25, Vector((0, 0.91e9)), Vector((200, 0))),
    #    Body(1e25, Vector((0, -0.91e9)), Vector((-300, 0))),
    #]

    ## three bodies
    #bodies = [
    #    Body(1e25, Vector((0, 0.91e9)), Vector((400, 0))),
    #    Body(1e25, Vector((0, -0.91e9)), Vector((-400, 0))),
    #    Body(5e8, Vector((0, 0)), Vector((25, 0))),
    #]

    ## four bodies
    #bodies = [
    #    Body(1e25, Vector((0, 0.91e9)), Vector((400, 0))),
    #    Body(1e25, Vector((0, -0.91e9)), Vector((-400, 0))),
    #    Body(5e8, Vector((50, 0)), Vector((25, 0))),
    #    Body(5e8, Vector((-50, 0)), Vector((-25, 0))),
    #]

    ## seven bodies, stable motion
    #bodies = [
    #    Body(1e25, Vector((0, 0.91e9)), Vector((400, 0))),
    #    Body(1e25, Vector((0, -0.91e9)), Vector((-400, 0))),
    #    Body(5e8, Vector((1e5, 0)), Vector((25, 25))),
    #    Body(5e8, Vector((-1e5, 0)), Vector((-25, -25))),
    #    Body(1e20, Vector((1e8, 1e8)), Vector((0, 100))),
    #    Body(1e20, Vector((-1e8, -1e8)), Vector((0, -100))),
    #    Body(1e10, Vector((0, 0)), Vector((0, 0))),
    #]

    ## seven bodies, erratic motion
    #bodies = [
    #    Body(1e25, Vector((0, 0.91e9)), Vector((400, 0))),
    #    Body(1e25, Vector((0, -0.91e9)), Vector((-400, 0))),
    #    Body(5e8, Vector((1e5, 0)), Vector((25, 25))),
    #    Body(5e8, Vector((-1e5, 0)), Vector((-25, -25))),
    #    Body(1e20, Vector((1e8, 1e8)), Vector((0, 150))),
    #    Body(1e20, Vector((-1e8, -1e8)), Vector((0, -100))),
    #    Body(1e10, Vector((0, 0)), Vector((0, 0))),
    #]

    import pygame
    import sys
    import time

    class GraphicalSimulation(System):
        """
        Like the simulation, but also displays things to the screen
        """

        size = 700
        colors = [
            (255, 0, 0),
            (0, 0, 255),
            (66, 52, 0),
            (152, 152, 152),
            (0, 255, 255),
            (255, 150, 0),
            (255, 0, 255),
        ]
        background = "white"

        def __init__(self, bodies, screen_limit):
            System.__init__(self, bodies)
            self.screen_limit = screen_limit
            self.screen = pygame.display.set_mode((self.size, self.size))

        def draw(self):
            self.screen.fill(self.background)
            for b, c in zip(self.bodies, self.colors):
                x = (
                    self.size // 2
                    + (b.position[0] / self.screen_limit) * self.size // 2
                )
                y = (
                    self.size // 2
                    + (b.position[1] / self.screen_limit) * self.size // 2
                )
                pygame.draw.circle(self.screen, c, (x, y), 7)
            pygame.display.flip()

        def step(self, dt):
            System.step(self, dt)
            self.draw()

    dt = 2000
    sim = GraphicalSimulation(bodies, 2e9)

    pygame.init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
        sim.step(dt)
        time.sleep(1e-3)
