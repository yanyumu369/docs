# VSCode

> 本文主要解决VSCode软件使用过程中遇到的一些问题。

## 基本设置

**1. VSCode 设置打开新文件不覆盖前一个窗口：**

- 按下 `Ctrl/Command + Shift + P` 快捷键打开命令面板，输入 `json` ，选择：`首选项：打开工作区设置(json)`。
- 在 `json` 设置中添加以下两行或将对应属性设置成 `false/true`。
    ``` javascript
    "workbench.editor.enablePreview": false,
    "workbench.editor.showTabs": true
    ```

**2. 设置代码在可视区宽度处换行：**

- `设置` >> `Editor: Word Wrap 控制折行的方式。` >> 选择 `on`。