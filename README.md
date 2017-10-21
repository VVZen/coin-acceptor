# DG600F Code examples
This repo contains two simple scripts.

The *.ino* file contains the code to be run on the Arduino, which uses a simple **interrupt** to detect signals sent on the serial from the **DG600F** coin acceptor.

The *serial_listener.py* shows how can we use python in order to listen to and print to stdout the serial messages sent by Arduino upon receiving coins from the DG600F.

It uses the [pyserial](https://github.com/pyserial/pyserial) module, which can be easily installed using pip.

In order to communicate with the DG600f, the switches were currently in this position:

![dg600f-switches](images/switches.png)