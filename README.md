# bAmbi

> **b**ackground **Ambi**ent Monitor Lighting

[![Example Video](https://user-images.githubusercontent.com/4750998/123708982-34da8f00-d864-11eb-9d68-00c8b118d721.png)](https://i.imgur.com/ZwlL6op.mp4)

Bambi is a controller that manages the background ambient lighting of a monitor, similar to the Ambilight technology.

## How it works

The program represents the backlight of a monitor with the `Layout` class, which accepts a customisable amount of LEDs.

This `Layout` class is then passed through a `Transformer` which changes the state of the LEDs, one example transformer would be `AverageColourTransformer` which retrieves colours from the screen and maps them to the relevant LEDs.

Finally, the `Layout` is passed through a renderer, which represents an output for the LEDs, one example is the `TerminalRenderer` which outputs a representation of the LED state to the terminal. `SerialRenderer` outputs the state over a serial connection instead, to communicate with physical hardware.

### AverageColourTransformer

`AverageColourTransformer` is the most similar to Ambilight technology, and works by getting the average colour of sections on the edges of the screen.

When provided the below image, and with a layout of 9 top LEDs and 6 side LEDs (30 total):

![](https://i.imgur.com/utCfeMy.png)

the program splits it up in the following way, with each square representing the LEDs behind the monitor:

![](https://i.imgur.com/UkyPtvN.png)

## Setting up

The project is created using a tool called [Poetry](https://python-poetry.org/) which makes it easy to control dependencies and virtual environments.

You can use `poetry install` in the project directory to install the required dependencies and then import the library.

## Examples

`// TODO`
