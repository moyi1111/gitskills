关于Arduino UNO 控制器串口使用资料。
Arduino与计算机通信所使用的USB接口就是下载程序时所用的USB接口，当Arduino与其他设备通信时，需要用到“Serial”系列函数，所以我们要对其有所了解，下面介绍几个常“Serial”函数。
1、Serial.begin（）—设置串行每秒传输数据的速率（波特率）。在同计算机通讯时，使用下面这些值：300, 1200, 2400, 4800, 9600, 14400, 19200, 28800, 38400, 57600或 115200。你也可以在任何时候使用其它的值，比如，与0号或1号接口通信就要求特殊的波特率。
2、Serial.print（）—从串行端口输出数据。
3、Serial.println（）—从串行端口输出数据，跟随一个回车（ASCII 13, 或 '\r'）和一个换行符（ASCII 10, 或 '\n'）。这个函数所取得的值与Serial.print（）一样。
4、Serial.read（）—读取持续输入的数据。
注意观察Arduino板子上的TX/RX指示灯
TX（T：Transmitter 发送）表示为Arduino发送指令信息给计算机，RX（R:Receive 接收）表示为Arduino接收来自计算机的指令信息，当下载程序或与计算机通信时，这两个指示灯就会闪烁。


还有一个相关网址，是关于蓝牙连接的，内容我就不复制在这个上面了。网址如下：
http://www.arduino.cn/thread-16311-1-1.html


通过和同学之间的交流，了解到开发板和app之间的通信通过串口就可以实现，一下网址是一些相关的资料。包括串口通信的读取数据，写入数据，和读取数据的一些详细的分类。

网址如下：
http://m.blog.csdn.net/iracer/article/details/50334041


查阅的JAVA和arduino进行串口通信的网址如下：              重点关注arduino部分代码
http://m.blog.csdn.net/doutao6677/article/details/53907251
c#
http://www.cnblogs.com/conexpress/p/3323333.html
