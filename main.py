import pygame
import math

pygame.font.init()
FONT = pygame.font.SysFont('arial',24)

class Planet:
    AU = 149.6e6 * 1000 # 1 AU in meters
    G = 6.67430e-11 # Gravitational constant
    SCALE = 250 / AU # 1 meter to 250 pixels
    TIMESTEP = 24*3600 # 1 day in seconds

    def __init__(self,x,y,radius,color,mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        
        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0
    
    def draw(self,win):
        x =self.x * self.SCALE + WIDTH/2
        y = self.y * self.SCALE + HEIGHT/2
        if len(self.orbit) > 2:
                
            updated_points = []
            for point in self.orbit:
                x,y = point
                x = x * self.SCALE + WIDTH/2
                y = y * self.SCALE + HEIGHT/2
                updated_points.append((x,y))

            pygame.draw.lines(win,self.color,False,updated_points,2)   
        
        if not self.sun:
            distance_text = FONT.render(f"{self.distance_to_sun/Planet.AU:.2f} AU",1,WHITE)
            win.blit(distance_text,(x,y))


        pygame.draw.circle(win,self.color,(x,y),self.radius)

    def attraction(self,other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.hypot(distance_x,distance_y)

        if other.sun:
            self.distance_to_sun = distance
        
        force = self.G * self.mass * other.mass / distance**2
        theta = math.atan2(distance_y,distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force

        return force_x, force_y
    
    def update(self,planets):
        total_fx = total_fy = 0
        for planet in planets:
            if planet == self:
                continue
            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy
        
        self.x_vel += total_fx / self.mass * self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP

        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP

        self.orbit.append((self.x,self.y))




pygame.init()

# Set up the drawing window

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("gravity simulation")

# Colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 100, 255)
RED = (255, 0, 0)

# Event loop
def main():
    run = True
    clock = pygame.time.Clock()

    sun = Planet(0,0,30,YELLOW,1.989e30)
    sun.sun = True

    earth = Planet(-1*Planet.AU,0,16,BLUE,5.972*10**24)
    earth.y_vel = 29.783*1000

    mars = Planet(-1.524*Planet.AU,0,12,RED,6.39*10**23)
    mars.y_vel = 24.077*1000

    mercury = Planet(-0.39*Planet.AU,0,8,(128,128,128),3.285*10**23)
    mercury.y_vel = 47.87*1000

    venus = Planet(-0.723*Planet.AU,0,10,(255,69,0),4.867*10**24)
    venus.y_vel = 35.02*1000


    planets = [sun,earth,mars,mercury,venus]

    while run:
        clock.tick(60)
        WIN.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.update(planets)
            planet.draw(WIN)
        pygame.display.update()
    pygame.quit()

main()