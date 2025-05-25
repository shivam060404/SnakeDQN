# Snake Game with Deep Q-Learning (DQN)

A Deep Reinforcement Learning project where an AI agent learns to play Snake using Deep Q-Network (DQN) algorithm. The agent starts with random moves and gradually learns optimal strategies through trial and error.

## 🎮 Project Overview

This project implements a classic Snake game using PyGame and trains an AI agent to play it using Deep Q-Learning. The agent observes the game state, makes decisions, and learns from rewards to improve its performance over time.

### Key Features
- **Deep Q-Network (DQN)** implementation with experience replay
- **Real-time visualization** of training progress
- **Manual play mode** for human interaction
- **Model persistence** - saves trained models automatically
- **Configurable hyperparameters** for experimentation

## 🏗️ Architecture

### Game Environment (`game.py`)
- Grid-based Snake game built with PyGame
- 800x800 pixel window with 20x20 pixel blocks
- Collision detection for walls and self-collision
- Food placement and score tracking
- Adjustable game speed

### AI Agent (`agent.py`)
- **State representation**: 11-dimensional vector including:
  - Danger detection (straight, left, right)
  - Current movement direction (4 directions)
  - Food location relative to head (4 directions)
- **Action space**: 3 possible actions (straight, turn left, turn right)
- **Experience replay** with memory buffer (100,000 transitions)
- **Epsilon-greedy exploration** with decay

### Neural Network (`model.py`)
- **Architecture**: 11 → 256 → 3 (fully connected layers)
- **Activation**: ReLU for hidden layer
- **Optimizer**: Adam with learning rate 0.001
- **Loss function**: Mean Squared Error (MSE)

## 📋 Requirements

```bash
pip install -r requirements.txt
```

Dependencies:
- `pygame` - Game environment and visualization
- `torch` - Neural network implementation
- `numpy` - Numerical computations
- `matplotlib` - Training progress visualization

## 🚀 Getting Started

### 1. Training the Agent

Run the training script to start teaching the AI:

```bash
python train.py
```

**What happens during training:**
- Agent starts with random exploration (high epsilon)
- Gradually reduces randomness as it learns
- Model is saved after each game as `model.pth`
- Training progress is printed to console
- Continues indefinitely until manually stopped

**Training Output:**
```
Game 1 | Score: 0 | Record: 0
Game 2 | Score: 1 | Record: 1
Game 15 | Score: 12 | Record: 12
...
```

### 2. Manual Play

Play the game yourself using arrow keys:

```bash
python play.py
```

**Controls:**
- ↑ Arrow Key: Move Up
- ↓ Arrow Key: Move Down
- ← Arrow Key: Move Left  
- → Arrow Key: Move Right

## 🧠 How the AI Learns

### State Representation
The agent observes 11 features:
1. **Danger straight ahead** (boolean)
2. **Danger to the right** (boolean)  
3. **Danger to the left** (boolean)
4. **Moving left** (boolean)
5. **Moving right** (boolean)
6. **Moving up** (boolean)
7. **Moving down** (boolean)
8. **Food is left** (boolean)
9. **Food is right** (boolean)
10. **Food is up** (boolean)
11. **Food is down** (boolean)

### Action Space
The agent chooses from 3 actions:
- **[1,0,0]**: Continue straight
- **[0,1,0]**: Turn right
- **[0,0,1]**: Turn left

### Reward System
- **+10**: Eating food
- **-10**: Game over (collision)
- **0**: Normal movement

### Learning Process
1. **Exploration vs Exploitation**: Starts with 80% exploration, decreases with each game
2. **Experience Replay**: Stores transitions and trains on random batches
3. **Target Network Updates**: Uses Q-learning update rule with discount factor γ=0.9

## 📊 Hyperparameters

You can modify these values in `agent.py`:

```python
MAX_MEMORY = 100_000    # Experience replay buffer size
BATCH_SIZE = 1000       # Training batch size  
LR = 0.001             # Learning rate
gamma = 0.9            # Discount factor
epsilon = 80 - n_games # Exploration rate (decreases over time)
```

## 📁 Project Structure

```
snake-dql/
├── agent.py          # DQN Agent implementation
├── game.py           # Snake game environment  
├── model.py          # Neural network and training logic
├── train.py          # Training script
├── play.py           # Manual play script
├── requirements.txt  # Python dependencies
└── model.pth         # Saved model weights (created after training)
```

## 🎯 Training Tips

### For Better Performance:
1. **Let it train longer** - Performance improves significantly after 100+ games
2. **Adjust exploration** - Modify epsilon decay rate for different exploration strategies
3. **Experiment with rewards** - Try different reward values for various actions
4. **Network architecture** - Experiment with hidden layer sizes

### Expected Results:
- **Early games (1-50)**: Mostly random movement, scores 0-5
- **Mid training (50-200)**: Starts learning basic survival, scores 5-15  
- **Advanced (200+)**: Develops strategies, scores 15-30+

## 🔧 Customization

### Modify Game Settings:
```python
# In game.py
BLOCK_SIZE = 20        # Size of snake segments
SPEED = 10            # Game speed (FPS)
w, h = 800, 800       # Window dimensions
```

### Adjust Network Architecture:
```python
# In agent.py  
self.model = LinearQNet(11, 256, 3)  # input, hidden, output
```

## 🐛 Troubleshooting

**Common Issues:**

1. **PyGame window closes immediately**
   - Make sure you're running the correct script
   - Check that pygame is properly installed

2. **Training seems stuck**
   - This is normal early in training
   - Let it run for at least 50+ games

3. **Model not saving**
   - Check file permissions in the project directory
   - Ensure torch is properly installed

## 📈 Monitoring Progress

The training script outputs:
- Current game number
- Score achieved  
- Best score (record)
- Model save confirmation

Watch for gradual improvement in average scores over time.

## 🎓 Learning Outcomes

This project demonstrates:
- **Reinforcement Learning** fundamentals
- **Deep Q-Network** implementation
- **Experience replay** and **target networks**
- **Exploration vs exploitation** tradeoff
- **Neural network** training with PyTorch
- **Game development** with PyGame

## 🤝 Contributing

Feel free to experiment with:
- Different neural network architectures
- Alternative reward structures  
- Modified state representations
- Advanced DQN variants (Double DQN, Dueling DQN)

## 📝 License
This project is open source and available for educational purposes.
