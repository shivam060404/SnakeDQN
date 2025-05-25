import torch
import os
import numpy as np
from agent import Agent
from game import SnakeGame
import pygame

# Mapping for manual control: [up, down, left, right]
DIRECTION_MAP = {
    pygame.K_UP:    [1, 0, 0, 0],
    pygame.K_DOWN:  [0, 1, 0, 0],
    pygame.K_LEFT:  [0, 0, 1, 0],
    pygame.K_RIGHT: [0, 0, 0, 1],
}

def play():
    pygame.init()
    agent = Agent()
    game = SnakeGame()
    direction = [0, 0, 0, 1]  # Default: right

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key in DIRECTION_MAP:
                    direction = DIRECTION_MAP[event.key]

        final_move = direction.copy()
        reward, done, score = game.play_step(final_move)
        if done:
            print("Game over! Score:", score)
            game.reset()
            direction = [0, 0, 0, 1]  # Reset to right

if __name__ == "__main__":
    play()
