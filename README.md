# Tank-Game

## Summer 2022 Project


__Purpose of Project__

I wanted to put my coding skills in practice over the summer and create my very first game from scratch. By implementing a game such as this, I will be able to learn more about the process of game development and creating interfaces. I will be able to design a game, implement it, and test the game throughout my process, and to make the process streamlined, the creation of the game will be separated into ten milestones to be completed throughout the summer. If I am unable to meet a milestone, I will adjust accordingly. New tasks will be added to milestones when appropriate.

<br>

## How to Run the Game

1. Install Kivy.

2. Enter the Kivy virtual environment and install NumPy and introcs.

3. Run `python ../Tank-Game` while in the Tank-Game folder.

<br>

## Milestones

The *Milestones* section outlines each milestone and their due dates.

**Milestone 1**

*Due: June 17, 2022*

> &check; Create `main` function & `start_game()` function

> &check; Create TankGame and Tank classes & create `__init__` functions for each

**Milestone 2**

*Due: June 24, 2022*

> &check; Create some functions for Tank that are not dependent on interface (i.e. adjusting the aim/power, taking down health, etc.)

> &check; Complete `start_game()` function

> &check; Research creating an interface for the game

**Milestone 3**

*Due: July 01, 2022*

> &check; Begin creating interface for game

> &check; Create designs with iPad for game (sprites and background)

**Milestone 4**

*Due: July 08, 2022*

> &check; Complete prototypes for interface & designs

**Milestone 5**

*Due: July 15, 2022*

> &cross; Make progress on Tank class and functions (with specifications)
> &check; Add Level class and adjust current code to fit new design changes

**Milestone 6**

*Due: July 22, 2022*

> &cross; Make progress TankGame class and functions (with specifications)
> &cross; Add sketches to design folder for welcome screen, game screen, and lose screen

**Milestone 7**

*Due: July 29, 2022*

> &cross; Clean up code
> &cross; Complete any code that is not finished (i.e. Tank and TankGame)

**Milestone 8**

*Due: August 05, 2022*

> &cross; Test game and fix/refine any smaller issues

**Milestone 9**

*Due: August 12, 2022*

> &cross; Add extra features if possible (i.e. moving tank or animation)

**Milestone 10**

*Due: August 19, 2022*

> &cross; Complete game :D

<br>

## Design Choices

The *Design Choices* section explains any choices that I may have made in changing certain parts of the project or any parts of the project that required outside sources.

**Milestone 2:** I decided to utilize Kivy, a Python framework that allows programmers to create a natural user interface that is platform-independent, meaning that the interface doesn't change, even when used on a different operating system or platform. Because Walker White created a GameApp module for Kivy, I utlized that in order to create the TankGame. I also imported the introcs module, which the GameApp module is dependent on. Kivy requires an installation via pip. Because I am unfamiliar with the framework, Milestones 3 and 4 will likely take an extended amount of time to complete.

**Milestone 4:** A problem I ran into straight away with the tank sprite was how to get the tank gun to turn with exact angles. A primitive solution could be to add in sprites for each increment of 10 degrees, but this wouldn't satisfy the scenarios in between, such as something like 10.5 degrees or 65.0 degrees. So, currently, to keep up with milestones, I think that it may be more suitable to have one sprite of the tank. The gun will not physically move when the angle is changed, but this will be adjusted if time permits. I also may change the design of the tank to be something like a cannon if time permits depending on which design I am more in favor of.

During this milestone, I realized that there would likely need to be another class to manage any obstacles on the screen, so that will be created in a future milestone.

**Milestone 5:** I modified Milestone 5's goal to make progress on the Tank class rather than complete it, as completing the Tank class requires the game screen and lose screen interface to be designed. I added new goals to future milestones for this and added a design folder for sketches. Another game design change will be to manage a single instance of a game within TankGame. This design change allows for the new class Level to be created, which is called when a new game begins.

<br>

## Citations

The *Citations* section cites any outside sources that I may have used throughout the project and also describes the part of the project the source was used for. All images were drawn myself (via Piskel).

| Project Section | Description of Section | Source |
| - | - | - |
| game2d Folder | Interface | Walker White, Cornell University's Department of Computer Science |