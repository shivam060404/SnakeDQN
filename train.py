from agent import Agent
from game import SnakeGame
import matplotlib.pyplot as plt
import torch
import os

def train():
    plot_scores = []
    plot_mean_scores = []
    total_score = 0
    record = 0
    agent = Agent()
    game = SnakeGame()

    while True:
        print("Top of training loop")
        state_old = agent.get_state(game)
        final_move = agent.get_action(state_old)
        reward, done, score = game.play_step(final_move)
        print("After play_step, reward:", reward, "done:", done, "score:", score)
        state_new = agent.get_state(game)

        
        print("Step executed, done:", done)
        agent.train_short_memory(state_old, final_move, reward, state_new, done)
        agent.remember(state_old, final_move, reward, state_new, done)

        if done:
            game.reset()
            agent.n_games += 1
            agent.train_long_memory()

            # Always save the model after each game
            model_path = os.path.abspath("model.pth")
            torch.save(agent.model.state_dict(), model_path)  # Save model
            print(f"Model saved to: {model_path}")

            if score > record:
               record = score

            print(f'Game {agent.n_games} | Score: {score} | Record: {record}')
            plot_scores.append(score)
            total_score += score
            mean_score = total_score / agent.n_games
            plot_mean_scores.append(mean_score)


if __name__ == "__main__":
    train()