

　　1、git stash 将本地代码stash到仓库中。

　　　　可以使用git stash save ***定义自己的标记，方便以后查询

　　2、git pull 将远程代码拉取到本地。

　　3、git stash pop 将仓库中的代码合到本地最新代码中。

　　4、在处理bug的过程中，可能存在多次stash的操作。这时可以使用git stash list查看本地仓库中都存储了几个stash版本。

　　5、git stash pop默认将最近一次stash操作合并到本地代码中，也可以通过git stash pop stash@{Number}指定将某次stash的内容合并到本地代码中。

　　6、git stash pop命令在合并代码的同时，会把仓库中对应的内容弹出。如果只想查看，而不想弹出内容，可以使用git stash apply命令进行操作。

　　7、git stash -h 查看git stash帮助

　　8、git stash show 显示stash合并到本地代码后，哪些文件会修改，以及修改的概述

　　9、git stash show -p stash@{0} 显示修改的详细内容
　　
　　
　　
　　相关的网址：http://www.cnblogs.com/huanyou/p/6654813.html