import random
import os
import sys
import pygame

pygame.init()
#Window settings
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("The last stand")

#Fps
clock = pygame.time.Clock()
#Soldier settings
class Soldier(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        #cadre of soldier size
        self.frame_width = 32
        self.frame_height = 48
        self.scale_factor = 2

        #Loading of soldier animation from assets folder
        self.animations = {
            "standing": self.load_animation("assets/soldier_stand.png", 3, 1),
            "walking": self.load_animation("assets/soldier_walk.png", 5, 1),
            "shooting": self.load_animation("assets/soldier_shoot.png", 4, 1)
        }
        self.state = "standing" #State of soldier
        self.current_frame = 0.0
        self.current_speed =0.15 #Speed of frame change
        #orientation of soldier
        self.facing_right = True
        #Image and position of soldier
        self.image =self.animations[self.state][0]
        self.rect = self.image.get_rect(center=(x,y))
        #Movement settings(float position prevents rounding jitter)
        self.pos_x = float(x)
        self.pos_y = float(y)
        self.target_x = float(x)
        self.target_y = float(y)
        self.speed = 4
        self.is_selected = False
    def load_animation(self, path, num_frames, num_rows):
        frames = []
        #Get the absolute path of the image file
        script_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(script_dir, path)
       
        try:
            sheet = pygame.image.load(full_path).convert()
            sheet.set_colorkey((0, 0, 0))  # Set black as the transparent color
            frame_w = sheet.get_width() // num_frames
            frame_h = sheet.get_height() // num_rows

            for i in range(num_frames):
                frame = sheet.subsurface((i * frame_w, 0, frame_w, frame_h))
                #Scale the frame for 1080p
                scaled_frame = pygame.transform.scale(frame, (self.frame_width * self.scale_factor, self.frame_height * self.scale_factor))
                frames.append(scaled_frame)
        except (FileNotFoundError, pygame.error) as e:
                print(f"Error loading animation from {full_path}: {e}")
                #Checking if the image file exists
                assets_dir = os.path.join(script_dir, "assets")
                if os.path.exists(assets_dir):
                    print(f"Assets directory exists: {assets_dir}")
                else:
                    print(f"Assets directory does not exist: {assets_dir}")
                fallback = pygame.Surface((self.frame_width * self.scale_factor, self.frame_height * self.scale_factor))
                fallback.fill((255, 0, 255))  # Fill with a magenta color to indicate missing texture
                frames.append(fallback)

        return frames

    # Logic of soldier movement
    def move(self):
        dx = self.target_x - self.pos_x
        dy = self.target_y - self.pos_y
        distance = (dx ** 2 + dy ** 2) ** 0.5
        if dx < -1:
            self.facing_right = False
        elif dx > 1:
            self.facing_right = True
        if distance > self.speed:
            self.pos_x += (dx / distance) * self.speed
            self.pos_y += (dy / distance) * self.speed
            self.rect.center = round(self.pos_x), round(self.pos_y)
            self.state = "walking"
        else:
            self.pos_x = float(self.target_x)
            self.pos_y = float(self.target_y)
            self.rect.center =self.target_x, self.target_y
            if self.state == "walking":
                self.state = "standing"

    # Switch cadre of soldier animation
    def animate(self):
        frames = self.animations.get(self.state, self.animations["standing"])
        self.current_frame += self.current_speed
        if self.current_frame >= len(frames):
            self.current_frame = 0.0
        raw_frame = frames[int(self.current_frame)]
        if not self.facing_right:
            self.image = pygame.transform.flip(raw_frame, True, False)
        else:
            self.image = raw_frame

    def update(self):
        self.move()
        self.animate()

    def draw_selection(self, surface):
        if self.is_selected:
            pygame.draw.rect(
                surface,
                (0, 255, 0),
                (self.rect.x, self.rect.bottom - 10, self.rect.width, 15),
                2,
            )


# Group of sprites
soldiers = pygame.sprite.Group()
soldier1 = Soldier(400, 540)
soldiers.add(soldier1)
selected_soldier = None

# Main game loop
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos
            #Checking click on soldier
            if soldier1.rect.collidepoint(mouse_pos):
                soldier1.is_selected = True
                selected_soldier = soldier1
                # If the soldier is clicked, set the target position to the mouse position
            elif selected_soldier:
                selected_soldier.target_x = mouse_pos[0]
                selected_soldier.target_y = mouse_pos[1]
                selected_soldier.is_selected = False
                selected_soldier = None

    soldiers.update()
    screen.fill((30, 30, 30))
    soldiers.draw(screen)
    for soldier in soldiers:
        soldier.draw_selection(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()