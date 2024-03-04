import pygame
import time





RED   = (255, 0, 0)
pygame.init()
VULTURE_COLOUR = (255, 255, 0)
WHITE = (255, 255, 255)
star_pattern=[
(300, 100),
(515, 225),
(470, 500),
(130, 500),
(100, 225),
(248, 225),
(212, 315),
(304, 375),
(392, 312),
(352, 225)
]
BLACK = (0, 0, 0)


screen = pygame.display.set_mode((600, 600))
GREEN = (0, 255, 0)


def display_game(vulture_position, crows_positions, selected_crow, status, crows_captured, display_text):
 
    screen.fill(WHITE)
    pygame.draw.line(screen, BLACK, star_pattern[0], star_pattern[3], 2)
    pygame.draw.line(screen, BLACK, star_pattern[1], star_pattern[3], 2)
    pygame.draw.line(screen, BLACK, star_pattern[4], star_pattern[2], 2)
    pygame.draw.line(screen, BLACK, star_pattern[1], star_pattern[4], 2)
    pygame.draw.line(screen, BLACK, star_pattern[0], star_pattern[2], 2)

    for node in star_pattern:
        pygame.draw.circle(screen, WHITE, node, 8)
        pygame.draw.circle(screen, BLACK, node, 10, 2)
    if vulture_position != (0, 0):
        pygame.draw.circle(screen, BLACK, vulture_position, 12, 1)
        pygame.draw.circle(screen, VULTURE_COLOUR, vulture_position, 12)
    if crows_positions != []:
        for crow in crows_positions:
            pygame.draw.circle(screen, (0, 255, 255), crow, 12)
            pygame.draw.circle(screen, BLACK, crow, 12, 1)
    if selected_crow != (-1, -1):
        pygame.draw.circle(screen, BLACK, selected_crow, 12)
        pygame.draw.circle(screen, (0, 0, 255), selected_crow, 10)
    
 

    game_status = 0
    if crows_captured != 0 and len(crows_positions) > 0:
        font = pygame.font.Font(None, 25)
        text_line1 = font.render(f"Crows: {len(crows_positions)}", True, BLACK)
        game_status = 2
        text_line2 = font.render(f"captured: {crows_captured}", True, BLACK)
    
    if crows_captured != 0 and len(crows_positions) == 0:
        font = pygame.font.Font(None, 25)
        text = font.render(f"captured: {crows_captured}", True, BLACK)
        game_status = 1

    if crows_captured == 0 and len(crows_positions) > 0:
        font = pygame.font.Font(None, 25)
        text = font.render(f"Crows: {len(crows_positions)}", True, BLACK)
        game_status = 1

    if game_status != 0:
        text_main = font.render("Current board", True, (0,0,0))
        text_main_rect = text_main.get_rect(topleft=(450, 80))
        pygame.draw.line(screen, BLACK, (450, 95), (450 + text_main_rect.width, 95), 2)
        screen.blit(text_main, text_main_rect)
        
    if game_status == 2:
        text_rect = text_line1.get_rect(topleft=(450, 100))
        screen.blit(text_line1, text_rect)
        text_rect_2 = text_line2.get_rect(topleft=(450, 120))
        game_status=2
        screen.blit(text_line2, text_rect_2)

    if game_status == 1:
        text_rect = text.get_rect(topleft=(450, 100))
        screen.blit(text, text_rect)
        game_status=1

    if display_text != "":
        font = pygame.font.Font(None, 25)
        display_text_content = font.render(display_text, True, BLACK)
        display_text_rect = display_text_content.get_rect(topleft=(10, 570))
        # box_height = text_rect.height + 20
        screen.blit(display_text_content, display_text_rect)

    if status != 0:
        font = pygame.font.Font(None, 100)
        if status == 1:
            message = "Crows win!"
            text = font.render(message, True, BLACK)
        text_rect = text.get_rect(center=(600 // 2, 600 // 2))

        box_height = text_rect.height + 20
        if status == 2:
            message = "Vulture wins!"
            text = font.render(message, True, BLACK)
 
        box_width = text_rect.width + 20
        box_rect = pygame.Rect((600 - box_width) // 2, (600 - box_height) // 2, box_width, box_height)
        border_rect = pygame.Rect(box_rect.left - 5, box_rect.top - 5, box_rect.width + 10, box_rect.height + 10)
        pygame.draw.rect(screen, BLACK, border_rect)
        box_width = text_rect.width + 20
        pygame.draw.rect(screen, WHITE, box_rect)
        
        box_width = text_rect.width + 20

        screen.blit(text, text_rect)
        pygame.display.update()
        time.sleep(5)
        pygame.quit()

    pygame.display.update()



    
moves = {
    star_pattern[0]: [star_pattern[5], star_pattern[9]],
    star_pattern[1]: [star_pattern[8], star_pattern[9]],
    star_pattern[2]: [star_pattern[8], star_pattern[7]],
    star_pattern[3]: [star_pattern[7], star_pattern[6]],
    star_pattern[4]: [star_pattern[5], star_pattern[6]],
    star_pattern[5]: [star_pattern[6], star_pattern[9], star_pattern[0], star_pattern[4]],
    star_pattern[6]: [star_pattern[5], star_pattern[7], star_pattern[4], star_pattern[3]],
    star_pattern[7]: [star_pattern[6], star_pattern[8], star_pattern[3], star_pattern[2]],
    star_pattern[8]: [star_pattern[7], star_pattern[9], star_pattern[2], star_pattern[1]],
    star_pattern[9]: [star_pattern[5], star_pattern[8], star_pattern[1], star_pattern[0]]
}

kill_moves = {
    star_pattern[0]: [star_pattern[6], star_pattern[8]],
    star_pattern[1]: [star_pattern[5], star_pattern[7]],
    star_pattern[2]: [star_pattern[6], star_pattern[9]],
    star_pattern[3]: [star_pattern[5], star_pattern[8]],
    star_pattern[4]: [star_pattern[7], star_pattern[9]],
    star_pattern[5]: [star_pattern[3], star_pattern[1]],
    star_pattern[6]: [star_pattern[0], star_pattern[2]],
    star_pattern[7]: [star_pattern[4], star_pattern[1]],
    star_pattern[8]: [star_pattern[0], star_pattern[3]],
    star_pattern[9]: [star_pattern[4], star_pattern[2]]
}



def killed_crow_pos(start, end):

    star_moves = {
        star_pattern[0]: {
            star_pattern[6]: star_pattern[5],
            star_pattern[8]: star_pattern[9]
        },
        star_pattern[1]: {
            star_pattern[5]: star_pattern[9],
            star_pattern[7]: star_pattern[8]
        },
        star_pattern[2]: {
            star_pattern[6]: star_pattern[7],
            star_pattern[9]: star_pattern[8]
        },
        star_pattern[3]: {
            star_pattern[5]: star_pattern[6],
            star_pattern[8]: star_pattern[7]
        },
        star_pattern[4]: {
            star_pattern[7]: star_pattern[6],
            star_pattern[9]: star_pattern[5]
        },
        star_pattern[5]: {
            star_pattern[1]: star_pattern[9],
            star_pattern[3]: star_pattern[6]
        },
        star_pattern[6]: {
            star_pattern[0]: star_pattern[5],
            star_pattern[2]: star_pattern[7]
        },
        star_pattern[7]: {
            star_pattern[4]: star_pattern[6],
            star_pattern[1]: star_pattern[8]
        },
        star_pattern[8]: {
            star_pattern[0]: star_pattern[9],
            star_pattern[3]: star_pattern[7]
        },
        star_pattern[9]: {
            star_pattern[4]: star_pattern[5],
            star_pattern[2]: star_pattern[8]
        }
    }
    return star_moves.get(start, {}).get(end)

def is_valid_vulture_move(start, end, crow_positions):

    if end in kill_moves[start]:
        if end not in crow_positions:
            crow_position = killed_crow_pos(start, end)
            if crow_position in crow_positions:
                pygame.draw.circle(screen, BLACK, crow_position, 10, 2)
                crow_positions.remove(crow_position)
                print("Crow captured at: ", crow_position)
                pygame.draw.circle(screen, WHITE, crow_position, 8)
                return 2
            else:
                return 0
    if end in moves[start]:
        return 1
    return 0

def is_valid_move(start, end):
   
    if end in moves[start]:
        return True
    return False

def check_move_possible(vulture_position, crows_positions):
    if vulture_position == (0,0):
        return True
    
    captures = kill_moves[vulture_position]
    move_possible = False
    possible_moves = moves[vulture_position]
    for i in captures:
        possible_moves.append(i)
    count = 0
    possible_moves = list(set(possible_moves))    
    
    for move in possible_moves:
        if move not in crows_positions:
            move_possible = True
            count += 1
    return move_possible  
    

def get_node_name(node):
    if node[0] in nodes:
        if node[1] == nodes[node[0]]["y"]:
            return nodes[node[0]]["name"]
    return "Unknown"

nodes = {
    130: {"y": 500, "name": "star_pattern[3]"},
    212: {"y": 310, "name": "star_pattern[6]"},
    304: {"y": 375, "name": "star_pattern[7]"},
    300: {"y": 100, "name": "star_pattern[0]"},
    515: {"y": 225, "name": "star_pattern[1]"},
    100: {"y": 225, "name": "star_pattern[4]"},
    470: {"y": 500, "name": "star_pattern[2]"},
    248: {"y": 225, "name": "star_pattern[5]"},
    392: {"y": 312, "name": "star_pattern[8]"},
    352: {"y": 225, "name": "star_pattern[9]"}
}


def main():
  
    player = "vulture"
    running = True

    vulture_position = (0, 0)
    num_crows = 0
    crows_captured = 0
    selected_crow = (-1, -1)
    crows_positions = []
    crow_drop = 0

    display_text = "Welcome!"
    status = 0
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                mouse_x, mouse_y = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if player == "vulture":
                    if num_crows != 0:                   
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        for node in star_pattern:
                            if (((mouse_x-node[0]) ** 2 + (mouse_y-node[1]) ** 2) ** 0.5)<=10:
                                ret = is_valid_vulture_move(vulture_position, (node[0], node[1]), crows_positions) 
                                if ((node in crows_positions) == False):
                                    if node != vulture_position:
                                        if ret == 1:
                                            if node not in crows_positions and node != vulture_position:
                                                player = "crow"
                                                vulture_position = node
                                                display_text = "Vulture moved"
                                                print(f"Vulture moved to {node} ({get_node_name(node)})")
                                        elif ret == 2:
                                            vulture_position = node
                                            player = "crow"
                                            print(f"Vulture moved to {node} ({get_node_name(node)}) and captured")
                                            display_text = f"Vulture captured crow {crows_captured}!"
                                            crows_captured += 1
                                        elif ret == 0:
                                            display_text = "Invalid vulture move"
                                            print("Invalid move")
                    else:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        for node in star_pattern:
                            if (((mouse_x-node[0]) ** 2 + (mouse_y-node[1]) ** 2) ** 0.5)<=10:
                                display_text = "Vulture placed" 
                                print(f"Vulture placed at {node} ({get_node_name(node)})")  
                                player = "crow"
                                vulture_position = node
                else:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if num_crows < 7:
                        for node in star_pattern:
                            if (((mouse_x-node[0]) ** 2 + (mouse_y-node[1]) ** 2) ** 0.5)<=10:
                                if node not in crows_positions and node != vulture_position:
                                    print(f"Crow placed at {node} ({get_node_name(node)})")
                                    display_text = f"Crow {num_crows + 1} placed"
                                    crows_positions.append((node[0], node[1]))
                                    player = "vulture"
                                    num_crows += 1
                    else:
                        # All crows placed, move crows
                        if crow_drop == 0:
                            mouse_x, mouse_y = pygame.mouse.get_pos()
                            for node in star_pattern:
                                if (((mouse_x-node[0]) ** 2 + (mouse_y-node[1]) ** 2) ** 0.5)<=10:
                                    if node in crows_positions:
                                        selected_crow = node
                                        crow_drop = 1
                                        print(f"Crow at {node} ({get_node_name(node)}) selected")
                                        display_text = "Crow selected"
                                    else:
                                        if node is vulture_position:
                                            display_text = "Invalid move! Crows turn"
                                        else:
                                            if crows_captured != 0:
                                                display_text = "Select a crow to move!"
                                            else:
                                                display_text = "All 7 crows placed, select a crow to move!"
                                        print("Invalid move")

                        else:
                            mouse_x, mouse_y = pygame.mouse.get_pos()
                            for node_2 in star_pattern:
                                if (((mouse_x-node_2[0]) ** 2 + (mouse_y-node_2[1]) ** 2) ** 0.5)<=10:
                                    if node_2 in moves[selected_crow]:
                                        if node_2 not in crows_positions and node_2 != vulture_position:
                                            pygame.draw.circle(screen, BLACK, selected_crow, 10, 2)
                                            crows_positions.remove(selected_crow)
                                            pygame.draw.circle(screen, WHITE, selected_crow, 8)
                                            selected_crow = (-1, -1)
                                            crows_positions.append((node_2[0], node_2[1]))
                                            print(f"Crow moved to {node} ({get_node_name(node)})")
                                            crow_drop = 0
                                            display_text = "Crow moved"
                                            player = "vulture"
                                            break
                                    else:
                                        display_text = "Invalid move for selected crow!"
        
        moves_possible = check_move_possible(vulture_position, crows_positions)
        if moves_possible == False:
            print("Vulture has no moves left, crows win!")
            running = False
            status = 1 
            display_text = "Vulture has no moves left, crows win!"
        
        if crows_captured == 4:
            status = 2 
            print("4 crows captured")
            display_text = "4 crows captured"

        display_game(vulture_position, crows_positions, selected_crow, status, crows_captured, display_text)

    pygame.quit()
    
if __name__ == "__main__":
    main()