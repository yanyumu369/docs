# CMake

## 安装

1. [CMake 的下载](https://cmake.org/download/)。
2. MinGW 和 CMake 下载完后需要配置系统环境变量，将 MinGW 和 CMake 下的 bin 目录添加进去即可，在 cmd 下输入 g++ --version 和 cmake --version 有版本号输出说明 MinGW，CMake 安装成功。
3. 安装完 WinGW 之后，需要将 WinGW 自带的 make 工具改一下名称，将 WinGW 的 bin 文件夹下的 mingw32-make.exe 复制一份然后改名为 make.exe，不要直接改，mingw32-make.exe 在 cmake 的时候会被调用。不改也行，后面使用 make 命令的时候需要写 mingw32-make。
4. 在 vscode 中安装插件 c/c++和 CMake 以及 CMake tools。
5. 点开设置，搜索 Cmake Path ，指定 cmake.exe 的绝对路径。
6. 新建一个工程夹
   1. 新建一个文件夹 Cmake_test，用 vscode 打开；
   2. 在文件夹下新建 include 文件夹 和 src 文件夹，include 下存放头文件，src 下存放源文件；
   3. 在根目录下新建 CMakeLists.txt 文件。
7. 编译，执行
   1. 在 cmake 编译之前，先使用之前下载的 MinGW 配置一些 cmake 环境。安装好 cmake 后左边会有如图所示图标。
   2. 配置好后，发现会生成 build 文件，这是 Cmake Tools 工具帮你直接生成的，省去在终端 cmake，之后直接点击 vscode 下方的运行按钮即可在终端查看运行结果。build 目录下会生成一个 main.exe 可执行文件。

## 注意事项

1. 含有 Cmake 文件的文件夹移动需要删除其中的 build 文件夹，然后重新配置，否则路径不匹配。

## 使用

[CMake 应用：CMakeLists.txt 完全指南](https://zhuanlan.zhihu.com/p/371257515)
