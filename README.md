# Neural Network Playground

This is a desktop app that lets you watch a neural network learn in real time. All the network's math is built using NumPy, with no AI libraries like TensorFlow or PyTorch.

What it does
Open the app and you'll see a neural network rendered as connected circles and lines. Click Train and the network learns to solve XOR (a classic logic problem) over 3000 epochs(1 epoch is 1 run through the data). You can watch the weights change color and thickness as the network learns, and see the loss number drop as it gets more accurate. Click Reset to randomize the weights and start over.

How I built it
- `network.py` contains the neural network itself and all the math for it: forward pass, backpropagation, and gradient descent
- `ui/canvas.py` renders the network visually, coloring each connection based on whether its weight is positive or negative, and scaling thickness based on how strong that weight is
- `ui/app.py` builds the desktop interface using CustomTkinter

How to run it
Option 1 - Download the exe: Download the “main.exe” from the Releases page: https://github.com/Thunder-pro-grammer/neural-playground/releases/tag/v1.0

Option 2 -
1. Clone the repo
2. Install dependencies: `pip install numpy customtkinter matplotlib`
3. Run `main.py`

What's next
- Live animation during training, instead of only seeing the result after it finishes
- Support for more datasets beyond XOR
