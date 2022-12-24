# Linux

## 常用链接

- [The GNU C Library (glibc)](https://www.gnu.org/software/libc/started.html)：GNU C 库项目为 GNU 系统和 GNU/Linux 系统以及许多其他使用 Linux 作为内核的系统提供了核心库。这些库提供关键的 API，包括 ISO C11、POSIX.1-2008、BSD、OS-specific API 等。这些 API 包括诸如 `open`，`read`，`write`，`malloc`，`printf`，`getaddrinfo`，`dlopen`，`pthread_create`，`crypt`，`login`，`exit` 等基本构成。GNU C 库提供了许多用 C 语言或 C++ 语言编写的程序直接使用的低级组件。许多编程语言间接使用 GNU C 库，包括 C#、Java、Perl、Python 和 Ruby（解释器、VM 或这些语言的编译代码直接使用 glibc）。
- [The glibc manual](https://www.gnu.org/software/libc/documentation.html)

## 安装

1. 安装**虚拟机** [VMware Workstation](https://www.vmware.com/cn/products/workstation-pro/workstation-pro-evaluation.html)，下载后运行安装向导，**一直 Next 即可**。最后的许可证可以在网上找到。
2. [Ubuntu](https://cn.ubuntu.com/download/desktop) 镜像下载。
3. 虚拟机配置：
   - 打开第一步所下载的 VMware Workstation。在主界面中，选择【创建新的虚拟机】。
   - 如图，会自动弹出【新建虚拟向导】，选择【自定义（高级）】后，点击【下一步】。
   - 这一步选择默认值即可，点击【下一步】。
   - 选择【稍后安装操作系统】，点击【下一步】。
   - 选择【Linux】，其下方版本将默认更改为【Ubuntu】。‘
   - 填写【虚拟机名称】及【位置】，点击【下一步】。【虚拟机名称】即虚拟机的名字。【位置】可以选择容量较大的硬盘位置。
   - 【处理器数量】与【每个处理器的内核数量】选择 2 后，点击【下一步】。
   - 选择【此虚拟机的内存】，此值应依据电脑本身情况酌情调整。常用值为 1G（1024MB）、2G（2048MB）、4G（4096MB）等等。在这里选择 4G。
   - 选择【使用网络地址转换】，点击【下一步】。
   - 选择推荐的【LSI Logic】即可，点击【下一步】
   - 选择推荐的【SCSI】即可，点击【下一步】。
   - 选择【创建新虚拟磁盘】，点击【下一步】。
   - 设置【最大磁盘大小】为 40，并选择【将虚拟磁盘拆分成多个文件】后，点击【下一步】。最大磁盘大小默认为 20GB，磁盘剩余空间较大的话该数值可以往上加。
   - 点击【下一步】。
   - 点击【完成】。
   - 回到 VMware Station 界面，单机界面左侧【编辑虚拟机位置】。
   - 点击左侧的 CD/DVD 选项卡，右侧点击【使用 ISO 映像文件】，找到第二步在你清镜像中下载的 Ubuntu 镜像即可，点击【确定】。
   - 回到 VMware Station 界面，点击【开启此虚拟机】。【注】：此时若出现【此主机支持 Intel VT-x，但 Intel VT-x 处于禁用状态】的提示。请进入 BIOS，将【Intel Virtual Technology】设为【Enabled】即可，具体方法可百度。
   - 此时可以看到虚拟机画面，点击右侧【Install Ubuntu】。
   - 此时我们使用美国键盘布局【English（US）】，点击【Continue】。
   - 点击【Minimal installation】，点击【Continue】。由于 Ubuntu 虚拟机大多做学习研发使用，所以选择最小化安装。若是有用 Ubuntu 网上冲浪和打游戏的需求，请选择【Normal installation】。
   - 选择【Erase disk and install Ubuntu】，点击【Install Now】。
   - 点击地图上【中国】的位置，会默认出现 Shanghai，点击【Continue】。
   - 输入【Your name】【Your computer's name】【Pick a username】【Choose a password】【Confirm your password】后，点击【Continue】。这里建议密码设置的简单一些，因为 Ubuntu 后续很多操作需要验证密码，设置复杂的密码后期会比较麻烦。
   - 等待安装。
   - 点击【Restart Now】重新启动。重新启动后，可以看到 Ubuntu 已经安装完成，点击出现的【用户名】。
   - 输入密码即可以进入 Ubuntu 啦！
