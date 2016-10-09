# CAFFE DRAW

## Introduction
When we try to use the application in caffe to generate the graphs about our training acc or loss, we failed. So we decided to make a new one. It can help us draw the graphs.

### Examples:
These are the graphs about googLeNet training. They are in the log_example folder, so you can try it.

![image](https://github.com/aimreant/caffe_draw/log_example/googLeNet/[TEST]NumIters-loss3.top-1.jpg)

![image](https://github.com/aimreant/caffe_draw/log_example/googLeNet/[TEST]NumIters-loss3.loss3.jpg)


## Requirements:
Python 2.7.x
pycaffe

## Usage

### First Step: Generate log file when training:

```
$TOOLS/caffe train --solver=$SOLVERFILE 2>&1 |tee out.log
```

### Second Step: Clone the files from github

```
# cd /path/to/your/caffe/
# git clone https://github.com/GDUTCPSDL/caffe_draw.git
```

### Third Step: Modify and Run

Modify caffe_draw/draw.sh

```
# chmod +x ./caffe_draw/draw.sh
# ./caffe_draw/draw.sh
```

Then you will find graphics in the directory where log file is.


