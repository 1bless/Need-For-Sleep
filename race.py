import pygame
import time
import pygame.mixer

# import random


class Game:
    def __init__(self):
        pygame.init()
        self.display_width = 750
        self.display_height = 600
        self.gray = (119, 119, 119)
        self.gamedisplay = pygame.display.set_mode(
            (self.display_width, self.display_height)
        )
        pygame.display.set_caption("Need For Sleep")
        self.scale_factor = 1.2
        self.car_width = 70
        self.gta = pygame.font.Font("pics/PricedownBl.ttf", 150)
        self.carimg = pygame.transform.scale(
            pygame.image.load("pics/black3.png"),
            (
                int(self.car_width * self.scale_factor),
                int(self.car_width * self.scale_factor),
            ),
        )
        self.clock = pygame.time.Clock()
        self.crashed = pygame.mixer.Sound("sounds/wasted.mp3")
        self.complete = pygame.mixer.Sound("sounds/passed.mp3")
        self.stationair = pygame.mixer.Sound("sounds/stationair.mp3")
        self.acceleration = pygame.mixer.Sound("sounds/acceleration.mp3")
        self.acceleration.set_volume(2)

        self.background_images = [
            pygame.image.load("pics/road3.png"),
            pygame.image.load("pics/road1.png"),
            pygame.image.load("pics/road1.png"),
            pygame.image.load("pics/road2.png"),
            pygame.image.load("pics/road1.png"),
            pygame.image.load("pics/road2.png"),
            pygame.image.load("pics/road1.png"),
            pygame.image.load("pics/road2.png"),
            pygame.image.load("pics/road1.png"),
            pygame.image.load("pics/road3.png"),
        ]
        self.background_index = 0
        self.background_height = self.background_images[0].get_height()
        self.myfont = pygame.font.SysFont("None", 100)
        self.small_font = pygame.font.Font("pics/PricedownBl.ttf", 25)
        self.small_font_r = pygame.font.Font("pics/PricedownBl.ttf", 55)
        self.render_text = self.gta.render("Wasted", 20, (0, 0, 0))
        self.level_text = self.myfont.render("Level-", 1, (0, 0, 0))
        self.background_speed = 5
        self.x = 340
        self.y = 320
        self.x_change = 0
        self.passed = 0
        self.level = 0
        self.score = 0
        self.bumped = False
        self.prev_background_index = 1
        self.start_time = None
        self.background_y = 200 - self.display_height

    def background(self):
        self.background_y += self.background_speed
        if self.background_y >= self.background_height:
            self.background_y = 0
            self.background_index = (self.background_index + 1) % len(
                self.background_images
            )
            if self.background_index == len(self.background_images) - 1:
                self.background_speed = 0
        background_image = self.background_images[self.background_index]
        self.gamedisplay.blit(background_image, (0, self.background_y))
        next_background_index = (self.background_index + 1) % len(
            self.background_images
        )
        next_background_image = self.background_images[next_background_index]
        self.gamedisplay.blit(
            next_background_image, (0, self.background_y - self.background_height)
        )

    def score_system(self):
        font = pygame.font.SysFont(None, 25)
        time_elapsed = (pygame.time.get_ticks() - self.start_time) / 1000
        text = font.render(
            "Time elapsed = {:.1f}s".format(time_elapsed), True, (0, 0, 0)
        )
        score = font.render("Score = " + str(self.score), True, (255, 0, 0))
        self.gamedisplay.blit(text, (2, 2))

    def car(self):
        self.gamedisplay.blit(self.carimg, (self.x, self.y))

    def game_loop(self):
        while not self.bumped:
            # self.acceleration.set_volume(5)
            # self.acceleration.play()
            for event in pygame.event.get():
                self.gamedisplay.fill(self.gray)
                self.background()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.bumped = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.x_change = -5
                    if event.key == pygame.K_RIGHT:
                        self.x_change = 5
                    if event.key == pygame.K_UP:
                        self.background_speed += 2
                    if event.key == pygame.K_DOWN:
                        self.background_speed -= 1
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        self.x_change = 0
            self.x += self.x_change
            self.gamedisplay.fill(self.gray)
            self.background()
            self.car()
            self.score_system()
            pygame.display.update()
            self.clock.tick(90)

            if self.x > 520 - self.car_width or self.x < 290 - self.car_width:
                self.gamedisplay.blit(self.render_text, (120, 150))
                self.acceleration.stop()
                self.crashed.play()
                pygame.display.update()
                time.sleep(7)
                # self.main_menu()
                pygame.quit()
                # return 0
                quit()

            if self.background_index == len(self.background_images) - 1:
                time_elapsed = (pygame.time.get_ticks() - self.start_time) / 1000
                self.score = int(time_elapsed * 10)
                self.background_speed = 0
                self.acceleration.stop()
                if self.background_speed == 0:
                    self.complete.play()
                score_sheet = pygame.Surface((400, 300))
                score_sheet.fill((255, 255, 255))
                score_sheet_rect = score_sheet.get_rect(
                    center=(self.display_width / 2, self.display_height / 2)
                )
                score_sheet.blit(
                    self.small_font_r.render("RESPECT+", 1, (0, 0, 0)), (100, 20)
                )
                score_sheet.blit(
                    self.small_font.render("Time:", 1, (0, 0, 0)), (50, 140)
                )
                score_sheet.blit(
                    self.small_font.render(
                        "{:.2f} seconds".format(time_elapsed), 1, (255, 0, 0)
                    ),
                    (230, 140),
                )
                self.gamedisplay.blit(score_sheet, score_sheet_rect)
                pygame.display.update()
                time.sleep(5)
                pygame.quit()
                # return 1
                # self.main_menu()
                quit()

    def countdown(self):
        count = 3
        countdown_font = pygame.font.Font("pics/PricedownBl.ttf", 200)
        while count > 0:
            self.gamedisplay.fill(self.gray)
            countdown_text = countdown_font.render(str(count), True, (255, 0, 0))
            countdown_rect = countdown_text.get_rect(
                center=(self.display_width / 2, self.display_height / 2)
            )
            self.gamedisplay.blit(countdown_text, countdown_rect)
            pygame.display.update()
            pygame.time.wait(1000)  # Wait for 1 second
            count -= 1
        self.start_time = pygame.time.get_ticks()  # Set the start time
        self.clock.tick()  # Reset the game clock

    def main_menu(self):
        menu_font = pygame.font.SysFont(None, 25)
        menu_title = pygame.font.SysFont(None, 50)
        title = menu_title.render("Welcome to 'Need For Sleep'", True, (255, 152, 255))
        start = menu_font.render("Press SPACE to start", True, (255, 255, 255))
        quit_text = menu_font.render("Press Esc to quit", True, (255, 255, 255))
        title_rect = title.get_rect(
            center=(self.display_width / 2, self.display_height / 2 - 200)
        )
        start_rect = start.get_rect(
            center=(self.display_width / 2, self.display_height / 2 + 1)
        )
        quit_rect = quit_text.get_rect(
            center=(self.display_width / 2, self.display_height / 2 + 30)
        )

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.start_time = pygame.time.get_ticks()
                        self.stationair.play()
                        self.countdown()
                        self.stationair.stop()
                        return self.game_loop()
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
            self.gamedisplay.fill(self.gray)
            self.gamedisplay.blit(title, title_rect)
            self.gamedisplay.blit(start, start_rect)
            self.gamedisplay.blit(quit_text, quit_rect)
            pygame.display.update()
            self.clock.tick(60)

    def run(self):
        pygame.init()
        self.main_menu()
        pygame.quit()
        quit()


if __name__ == "__main__":
    game = Game()
    game.run()
