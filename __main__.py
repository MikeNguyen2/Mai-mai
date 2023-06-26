import pygame
# Initialize Pygame
pygame.init()

from pages import start_page, settings_page, end_page, pause_page, \
    song_selection_page, game_page, account_page, editor_page

# Set up the game window
window_width = 1000
window_height = 1000
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Mymai")

# Set up the pages
start = start_page(window)
settings = settings_page(window)
end = end_page(window)
pause = pause_page(window)
song_selection = song_selection_page(window)
game = game_page(window)
account = account_page(window)
editor = editor_page(window)

# Set up the game clock
clock = pygame.time.Clock()

# start, game, pause, end, settings, song selection
prev_page =""
page = "start"
game_over = False
page_draw = {
    "start": start.draw,
    "song selection": song_selection.draw,
    "pause": pause.draw,
    "end": end.draw,
    "settings": settings.draw,
    "game": game.draw,
    "editor": editor.draw,
    "account": account.draw,
}

page_click = {
    "settings": settings.click,
    "start": start.click,
    "song selection": song_selection.click,
    "pause": pause.click,
    "end": end.click,
    "game": game.click,
    "editor": editor.click,
    "account": account.click
}

"""
main loop of the game
events: quit, mouseclick, buttonclick, generate for testing
create object per set timer
draw the objects
update the objects
"""
while not game_over:
    # TODO mustn't reload every tick
    if page != prev_page:
        page_draw[page]()
    prev_page = page
    if page == "game": 
        page = game.tick()
        if page != "game": pygame.mixer.music.pause()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: game_over = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            (x,y) = pygame.mouse.get_pos()
            next_page = page_click[page](x, y)
            if page == "song selection" and next_page == "game": game.reset(),
            if page == "end" and next_page == "game": game.reset(),
            page = next_page
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: game_over = True
            if event.key == pygame.K_F1: page = "start"
            if event.key == pygame.K_F2: page = "game"
            if event.key == pygame.K_F3: page = "pause"
            if event.key == pygame.K_F4: page = "end"
            if event.key == pygame.K_F5: page = "settings"
            if event.key == pygame.K_F6: page = "song selection"
            if event.key == pygame.K_p and page == "game": 
                pygame.mixer.music.pause(), 
                page = "pause"
            elif event.key == pygame.K_p and page == "pause": 
                pygame.mixer.music.unpause(), 
                page = "game"
            if event.key == pygame.K_j and page == "game": game.generate_star()
            if event.key == pygame.K_k and page == "game": game.generate_tap()
            if event.key == pygame.K_l and page == "game": game.generate_circle()
            if event.key == pygame.K_q and page == "game": game.click(game.startcircles[0].e_x, game.startcircles[0].e_y)
            if event.key == pygame.K_w and page == "game": game.click(game.startcircles[1].e_x, game.startcircles[1].e_y)
            if event.key == pygame.K_e and page == "game": game.click(game.startcircles[2].e_x, game.startcircles[2].e_y)
            if event.key == pygame.K_r and page == "game": game.click(game.startcircles[3].e_x, game.startcircles[3].e_y)
            if event.key == pygame.K_a and page == "game": game.click(game.startcircles[4].e_x, game.startcircles[4].e_y)
            if event.key == pygame.K_s and page == "game": game.click(game.startcircles[5].e_x, game.startcircles[5].e_y)
            if event.key == pygame.K_d and page == "game": game.click(game.startcircles[6].e_x, game.startcircles[6].e_y)
            if event.key == pygame.K_f and page == "game": game.click(game.startcircles[7].e_x, game.startcircles[7].e_y)
            
            if event.key == pygame.K_UP and page == "editor": editor.move_up()
            if event.key == pygame.K_RIGHT and page == "editor": editor.move_right()
            if event.key == pygame.K_DOWN and page == "editor": editor.move_down()
            if event.key == pygame.K_LEFT and page == "editor": editor.move_left()

    # Update the display
    pygame.display.update()

    # Set the game speed
    clock.tick(10)

pygame.mixer.music.unload()