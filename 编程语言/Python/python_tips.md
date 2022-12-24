# Python 小技巧

## Python 标准库

Python 标准库：https://docs.python.org/zh-cn/3/library/index.html

Python 包索引：https://pypi.org/

### 内置函数

内置函数：https://docs.python.org/zh-cn/3/library/functions.html#len

| 函数           | 全名 | 作用 |
| -------------- | ------ | ---- |
| abs()          |absolute  | 返回一个数的绝对值。 |
| all()          |        |      |
| any()          |        |如果 iterable 的任一元素为真值则返回 `True`。 如果可迭代对象为空，返回 `False`。 |
| ascii()        |        |      |
| bin()          |        |      |
| bool()         | boolean| 返回布尔值，`True` 或 `False`。 |
| breakpoint()   |        |      |
| bytearray()    |        |      |
| bytes()        |        |      |
| callable()     |        |      |
| chr()          | character  | 返回 Unicode 码位为整数 `i` 的字符的字符串格式。  |
| classmethod()  |        |      |
| compile()      |        |      |
| complex()      |        |      |
| delattr()      |        |      |
| dict()         | dictionary | 创建一个新的字典。|
| dir()          | directory|      |
| divmod()       |        |      |
| enumerate()    |        |      |
| eval()         |        |      |
| exec()         | execute  |这个函数支持动态执行 Python 代码。 *object* 必须是字符串或者代码对象。|
| filter()       |        |      |
| float()        |        |返回从数字或字符串 `x` 生成的浮点数。 |
| format()       |        | 将 *value* 转换为“格式化后”的形式，格式由 *format_spec* 进行控制。 |
| frozenset()    |        |      |
| getattr()      |        |      |
| globals()      |        |      |
| hasattr()      |        |      |
| hash()         |        |      |
| help()         |        |      |
| hex()          |hexadecimal |将整数转换为以“0x”为前缀的小写十六进制字符串。|
| id()           |        |      |
| input()        |        |如果存在 *prompt* 实参，则将其写入标准输出，末尾不带换行符。接下来，该函数从输入中读取一行，将其转换为字符串（除了末尾的换行符）并返回。|
| int()          |integer  |返回一个基于数字或字符串 `x` 构造的整数对象，或者在未给出参数时返回 `0`。 |
| isinstance()   |        |      |
| issubclass()   |        |      |
| iter()         |        |      |
| len()          |length |返回对象的长度（元素个数）。实参可以是序列（如 string、bytes、tuple、list 或 range 等）或集合（如 dictionary、set 或 frozen set 等）。 |
| list()         |        |      |
| locals()       |        |更新并返回表示当前本地符号表的字典。在函数代码块但不是类代码块中调用 `locals()` 时将返回自由变量。|
| map()          |        |      |
| max()          | maximum|返回可迭代对象中最大的元素，或者返回两个及以上实参中最大的。|
| memoryview()   |        |      |
| min()          | minimum|返回可迭代对象中最小的元素，或者返回两个及以上实参中最小的。|
| next()         |        |      |
| object()       |        |      |
| oct()          | octal |将一个整数转变为一个前缀为“0o”的八进制字符串。 |
| open()         |        |打开 *file* 并返回对应的 *file object*。|
| ord()          |        |对表示单个 Unicode 字符的字符串，返回代表它 Unicode 码点的整数。 |
| pow()          |        |      |
| print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)        |        | 将 _objects_ 打印输出至 _file_ 指定的文本流，以 _sep_ 分隔并在末尾加上 _end_。 _sep_ 、 _end_ 、 _file_ 和 _flush_ 必须以关键字参数的形式给出。 |
| property()     |        |      |
| range(start, stop[, step])        |        | 虽然被称为函数，但 `range` 实际上是一个不可变的序列类型 |
| repr()         |        |      |
| reversed()     |        |      |
| round(number[, ndigits])        |        |返回 *number* 舍入到小数点后 *ndigits* 位精度的值。 如果 *ndigits* 被省略或为 `None`，则返回最接近输入值的整数。|
| set()          |        |      |
| setattr()      |        |      |
| slice(start, stop[, step])       |        | 返回一个 *slice* 对象，代表由 `range(start, stop, step)` 指定索引集的切片。 其中参数 `start` 和 `step` 的默认值为 `None`。切片对象具有只读数据属性 `start` 、`stop` 和 `step`，只是返回对应的参数值（或默认值）。|
| sorted(iterable, /, *, key=None, reverse=False)      |        | 根据 _iterable_ 中的项返回一个新的已排序列表。具有两个可选参数，它们都必须指定为关键字参数。_key_ 指定带有单个参数的函数，用于从 _iterable_ 的每个元素中提取用于比较的键 (例如 `key=str.lower`)。 默认值为 `None` (直接比较元素)。_reverse_ 为一个布尔值。 如果设为 `True`，则每个列表元素将按反向顺序比较进行排序。|
| staticmethod() |        |      |
|str(object=b'', encoding='utf-8', errors='strict')         | string  |      |
| sum()          |        |      |
| super()        |        |      |
| tuple()        |        |      |
| type()         |        |      |
| vars()         |        |      |
| zip()          |        |      |
| **import**()   |        |      |

##

all(iterable)

| 函数     | 作用                        |
| -------- | --------------------------- |
| `chr(i)` | 将 ascii 码转换为对应字母   |
| `chr()`  | 返回一个字符对应的 ASCII 码 |
