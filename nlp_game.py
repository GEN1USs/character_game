import pygame
import random
from textblob import TextBlob

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 1200, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("NLP Character Game")

# Character attributes
character_color = (0, 128, 255)
character_size = 50
character_x, character_y = width // 2, height - character_size  # Start at the ground level
velocity = 10
jumping = False
jumping_height = 150
jumping_count = 0  # Track how far the character has jumped
running = True
font = pygame.font.Font(None, 36)
text_field_rect = pygame.Rect(100, 100, 300, 50)
text_input = ""

# Function to process text commands
def process_command(command):
    command = command.lower()  # Convert command to lowercase for easier matching
    if 'move left' in command:
        return 'left'
    elif 'move right' in command:
        return 'right'
    elif 'jump' in command:
        return 'jump'
    elif 'change color' in command:
        return 'color'
    else:
        return 'unknown'

# Function to execute actions
def execute_action(action):
    global character_x, character_y, character_color, jumping, jumping_count

    if action == 'left':
        character_x -= velocity  # Move left
    elif action == 'right':
        character_x += velocity  # Move right
    elif action == 'jump' and not jumping:  # Only jump if not already jumping
        global jumping_count
        jumping = True  # Set jumping to True
        jumping_count = 0  # Reset the jump count
    elif action == 'color':
        character_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # Change color

# Main game loop
while running:
    pygame.time.delay(100)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                text_input = text_input[:-1]  # Remove last character on backspace
            elif event.key == pygame.K_RETURN:  # Execute command on Enter key
                action = process_command(text_input)  # Process the input command
                execute_action(action)  # Execute the corresponding action
                text_input = ""  # Clear the text input after processing
            else:
                text_input += event.unicode  # Add typed character to input

    # Jump logic
    if jumping:
        if jumping_count < jumping_height // 10:  # Ascend
            character_y -= 10  # Move up
        elif jumping_count < jumping_height // 5:  # Descend
            character_y += 10  # Move down
        else:
            jumping = False  # Reset jumping state
        jumping_count += 1  # Increment jump count

    # Clear screen and draw the user interface
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), text_field_rect)  # Draw text input field
    text_surface = font.render(text_input, True, (0, 0, 0))  # Render the text input
    screen.blit(text_surface, text_field_rect)  # Display the input text
    pygame.draw.circle(screen, character_color, (character_x, character_y), character_size)  # Draw the character

    # Update display
    pygame.display.update()

pygame.quit()
