import pygame
import os
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.frame_width = 32
        self.frame_height = 48
        self.scale_factor = 2
        #animations of enemy1
        self.animations = {
            "walking": self.load_animation("assets/zombie1walk.png", 8, 1),
            "attacking": self.load_animation("assets/zombie1atack.png", 6, 1),
            "death": self.load_animation("assets/zombie1death.png",6, 1)
        }

        self.state = "walking"
        self.current_frame = 0.0
        self.animation_speed = 0.15

        self.position = pygame.Vector2(x,y)

        self.image = self.animations[self.state][0]
        self.rect = self.image.get_rect(center=(x, y))


    def load_animation(self, path, num_frames, num_rows):
        frames = []                                       #The same like for soldier
        script_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(script_dir, path)
        try:
            sheet = pygame.image.load(full_path).convert()
            sheet.set_colorkey((0,0,0))

            frame_w = sheet.get_width() // num_frames
            frame_h = sheet.get_height() //num_rows

            for i in range(num_frames):
                frame = sheet.subsurface((i * frame_w, 0, frame_w, frame_h))
                scaled_frame = pygame.transform.scale(frame, (self.frame_width * self.scale_factor, self.frame_height * self.scale_factor))
                frames.append(scaled_frame)
        except (FileNotFoundError, pygame.error) as e:
            print(f"Error loading animation from {full_path}: {e}")
            fallback = pygame.Surface(
                (self.frame_width * self.scale_factor, self.frame_height * self.scale_factor)
            )
            fallback.fill((255, 0, 255))
            frames.append(fallback)
        return frames
    def animate(self):
        frames = self.animations[self.state]

        self.current_frame += self.animation_speed
        if self.current_frame >= len(frames):
            if self.state == "death":
                self.current_frame = len(frames) - 1
            else:
                self.current_frame = 0.0
        raw_frame = frames[int(self.current_frame)]
        self.image = pygame.transform.flip(raw_frame, True, False)
    def update(self):
        self.animate()
    def set_state(self, new_state):
        if self.state != new_state:
            self.state = new_state
            self.current_frame = 0.0
