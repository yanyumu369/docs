## VScode 使用问题

#### 1. 终端进程已终止，退出代码: -1。终端将被任务重用，按任意键关闭。

<div align=center>
<img width="60%" src="programme\C_C++\使用问题\image\VScode插件问题.png"/> <br>
<div style="text-align: justify; display: inline-block; color: #5b5b5b; padding: 2px;"> </div>
</div>

解决方法：中文路径改为英文路径。

#### 2. VS Code C 语言终端输出中文乱码编码设置

原因：vscode 终端调用的是 cmd.exe，cmd 默认编码为 GBK，vscode 默认使用 UTF-8 编码，所以二者冲突发生乱码。

点击左下角齿轮标志，点击**设置**，打开 setting.json 文件。然后在 json 文件中，加入下列代码：

```
"[cpp]": {
    "files.encoding": "gbk"
},
"[c]": {
    "files.encoding": "gbk"
}
```

这段话意思是针对 C/C++文件默认分配 GBK 编码，不影响其他语言文件编码，这样每次新建 C/C++文件默认分配 GBK 编码，无需每次切换，且与终端编码保持一致，且不会干扰系统 cmd 设置。配置其他语言，修改方括号内参数（语言文件后缀）即可。

#### 3. Vscode 运行 C++ 程序修改代码运行不生效

经过查看官方文档等等对比 C++ 环境的配置发现是在配置 launch.json 文件时点击 add configuration 时添加的配置少了下面句语句，在添加以后就成功了。
```
"preLaunchTask": "C/C++: g++.exe 生成活动文件",
```

这里解释一下 launch.json 文件的作用，launch.json 文件是 Vscode 关于代码调试的配置文件，在这里面配置了 gdb.exe 调试程序的运行，下面是官方文档的一些信息：

其中 program 设置指定要调试的程序。stopAtEntry 将值更改为 true 以使调试器 main 在您开始调试时停止该方法。另外 preLaunchTask 设置用于指定要在启动前执行的任务。确保它与 tasks.json 文件 label 设置一致。

完整配置代码：
```
{
    // 使用 IntelliSense 了解相关属性。 
    // 悬停以查看现有属性的描述。
    // 欲了解更多信息，请访问: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "(gdb) 启动",
            "preLaunchTask": "C/C++: g++.exe 生成活动文件",
            "type": "cppdbg",
            "request": "launch",
            "program": "${fileDirname}\\${fileBasenameNoExtension}.exe",
            "args": [],
            "stopAtEntry": false,
            "cwd": "${workspaceFolder}",
            "environment": [],
            "externalConsole": false,
            "MIMode": "gdb",
            "miDebuggerPath": "D:\\TDM-GCC-64\\bin\\gdb.exe",
            "setupCommands": [
                {
                    "description": "为 gdb 启用整齐打印",
                    "text": "-enable-pretty-printing",
                    "ignoreFailures": true
                },
                {
                    "description":  "将反汇编风格设置为 Intel",
                    "text": "-gdb-set disassembly-flavor intel",
                    "ignoreFailures": true
                }
            ]
        }
        
    ]
}
```
