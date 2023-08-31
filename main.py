import logics
from settings import *
import logics as lg
#import itertools as it
import ui


# TODO move square and new sprite for kill
# TODO Game icon
# TODO Fix logic
# TODO Turn history
# TODO Engine analysis
# TODO liches manual analysis
# TODO killed figure_classes
# TODO turn back
# TODO Win condition and screen
# TODO Menu -> [classic, rapid, blitz]
# TODO Check/Mate red glow
# TODO Multiplayer


if __name__ == '__main__':
    pygame.init()

    # Draw background
    screen.fill("GREY")
    ui.draw_board_background(screen)

    # Create logic and visual boards
    l_board = lg.logic_board
    figures = pygame.sprite.Group()
    for elem in l_board.ravel():
        if elem:
            figures.add(elem)

    # Game cycle
    while game:
        clock.tick(FPS)
        event_list = pygame.event.get()
        mouse_pos = pygame.mouse.get_pos()

        # Handling events
        for event in event_list:
            if event.type == pygame.QUIT:
                game = False

            # Timer
            if game_started:
                if event.type == timer_event:
                    if turn_counter % 2 != 0:
                        times, white_timer,  white_timer_rect, black_timer, black_timer_rect = ui.draw_timer_display(Black, times, timer_event)
                    else:
                        times, white_timer,  white_timer_rect, black_timer, black_timer_rect = ui.draw_timer_display(White, times, timer_event)

            # Events by mouse button down
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                if turn_counter % 2 != 0:
                    turn_flag = White
                else:
                    turn_flag = Black

                # if selected figure color equal to turn_flag color
                tmp_figure = logics.get_figure_under_mouse(mouse_pos[0], mouse_pos[1], l_board, turn_flag)
                if tmp_figure:
                    selected_figure = tmp_figure
                    old_pos = [selected_figure.x, selected_figure.y]
                    available_moves_sprites, available_moves = lg.create_available_moves_sprites(
                        lg.logic(selected_figure.val, selected_figure.color, selected_figure.x,
                                 selected_figure.y, l_board), available_moves_sprites)

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if drop_pos and selected_figure:
                    # if new position != old position
                    if [drop_pos[0], drop_pos[1]] != old_pos:
                        # if new position in available moves
                        if [drop_pos[0], drop_pos[1]] in available_moves:

                            # if new position contains figure -> kill them
                            if l_board[drop_pos[0]][drop_pos[1]]:
                                l_board[drop_pos[0]][drop_pos[1]].kill()

                            # move figure on new position
                            tmp = l_board[old_pos[0]][old_pos[1]]
                            l_board[old_pos[0]][old_pos[1]] = 0
                            l_board[drop_pos[0]][drop_pos[1]] = tmp
                            selected_figure.move_figure(drop_pos[0], drop_pos[1])

                            # TODO PAWN TO QUEEN

                            selected_figure = None
                            drop_pos = None
                            game_started = True
                            turn_counter += 1
                            available_moves_sprites.empty()

                        # if new position not in available moves -> return figure on old position
                        else:
                            selected_figure.move_figure(old_pos[0], old_pos[1])
                            drop_pos = None
                            selected_figure = None

                    # if new position == old_position -> does nothing
                    else:
                        selected_figure.move_figure(drop_pos[0], drop_pos[1])
                        drop_pos = None
                        selected_figure = None

                    # Logic board debugging
                    lg.print_lg_board(l_board)

            drop_pos = logics.dragndrop(mouse_pos[0], mouse_pos[1], selected_figure)

        screen.fill("GREY")
        ui.draw_board_background(screen)
        available_moves_sprites.draw(screen)
        figures.draw(screen)
        ui.create_turn_display(turn_counter, screen)
        screen.blit(black_timer, black_timer_rect)
        screen.blit(white_timer, white_timer_rect)
        pygame.display.flip()

    pygame.quit()
