# Nand2Tetris
the project code of [Nand2Tetris](https://www.coursera.org/learn/build-a-computer)(an online course)

## Introduction

Nand2Teris(从与非门到俄罗斯方块)是一个基于项目的课程，其从一个与非门(Nand)开始，根据设计好的指令系统，构建一个完整的计算机(HACK Computer)，并编写汇编器及编译器，最终实现Tetris游戏。这里是PART1部分。

任何逻辑表达式均可以用“与或非”表示，而“与或非”又能用“与非门”表示，基于此用Nand构建HACK Computer:
<div align=center><img src=image/Hack.png width=40%></div>

## Proposal
- 在上这门课之前，可以先学[计算机组成](https://www.coursera.org/learn/jisuanji-zucheng)，这门课介绍了计算机的组成结构以及计算机是如何工作的，而Nand2Teris讲述的是如何构建一个计算机。所以先学‘计算机组成’，再学‘Nand2Teris’会更好理解。
- 这门课用的是一种专为课程开发的简化HDL，该语言插件可以在VsCode里搜到，方便编写HDL代码。

## Project Notes
该课程使用的HDL跟Verilog有点类似，但相对笨拙，有很多verilog语法不能用，所以会遇到许多莫名其妙的问题。这里对工程里遇到的问题进行总结：

#### project02:
   - Add16.hdl & Inc16.hdl:1和0用true和false表示，如a[16]=false,则a所有bit全为0.如果想让a=1，可以这样表示：a[1..15]=false,a[0]=true
   - ALU.hdl:信号名不能有下划线，如x1_,不能将内部信号拆分，如out1为16位内部信号，那么就不能有out[0..7]这样的表述

#### project03:
   - Bit.hdl:在组合逻辑里，不能将输出连到输入里，但在时序逻辑里需要将输出连到输入，可以如下表示(即将DFF输出连到两个信号上，一个信号连到输出端口信号，一个作为内部信号)：
<div align=center><img src=image/bit_hdl.png width=40%></div>

   - PC.hdl:这个当时想了好长时间，如何实现多分支条件？后来想这是一个固定优先的选择模块，所以可以如下实现PC寄存器(老是想着用Verilog里的if，但这种思维是软件思维，应该用逻辑门做选择控制)：
<div align=center><img src=image/pc_hdl.png width=40%></div>
   
#### project05:
   - CPU.hdl:这是这门课里比较复杂的模块，按照下图搭建电路即可。注意图中并没有控制信号c的逻辑，需要自己结合课程和文档判断控制信号逻辑，这也是比较难的地方。

#### project06:
   - Project6需要编一个汇编器，我是用python写的，可以参考下。pong目录下有一个弹球的游戏，编译后用CPU Emulator打开就可以玩了，附上一张我玩的最高分，哈哈：
<div align=center><img src=image/game_over.png width=45%></div>
