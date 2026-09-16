# top

- zlib
- urllib.request
- tarfile
- numpy
- pandas
- easyocr
- tkinter
- pytesseract

## zlib

**[zlib official web](https://docs.python.org/3.14/library/zlib.html)**

## urllib.request

```python
import urllib.request

from pathlib import Path

tarball_path = Path("datasets/housing.tgz")
url = "https://github.com/ageron/data/raw/main/housing.tgz"
urllib.request.urlretrieve(url, tarball_path)
```

## tarfile

if we hava file `datasets/housing.tgz`
**structure**
./datasets/housing.tar

```python
import tarfile

from path import Path

tarball_path = Path("housing.tgz")

housing_tarball = tarfile.open(tarball_path)

housing_tarball.extractall(path="datasets")
```

**stucture**
./datasets/housing.tar
_./datasets_

## numpy

**[numpy official web](https://numpy.org/doc/stable/index.html)**

**NumPy 模块完整介绍**（Python 科学计算基础）

`NumPy`（Numerical Python）是 Python 中最核心的科学计算库，几乎所有数据科学、机器学习、深度学习库（如 Pandas、SciPy、Matplotlib、TensorFlow、PyTorch 等）都依赖于 NumPy。

### 1. 安装与导入

```bash
pip install numpy
```

```python
import numpy as np
# 官方推荐使用别名 np
```

---

### 2. 核心数据结构：`ndarray`（N 维数组）

NumPy 的灵魂是 `ndarray`，它比 Python 原生的 list 速度快几十倍，内存占用更少，支持向量化运算。

```python
# 创建数组
arr1 = np.array([1, 2, 3, 4, 5])                    # 1维
arr2 = np.array([[1, 2, 3], [4, 5, 6]])            # 2维
arr3 = np.zeros((3, 4))                             # 全0数组
arr4 = np.ones((2, 3, 4))                           # 全1数组
arr5 = np.full((3, 3), 7)                           # 填充指定值
arr6 = np.eye(5)                                    # 单位矩阵
arr7 = np.random.rand(3, 4)                         # 0-1均匀分布
arr8 = np.random.randn(3, 4)                        # 标准正态分布
arr9 = np.arange(0, 10, 2)                          # 类似 range
arr10 = np.linspace(0, 1, 11)                       # 等间距
```

---

### 3. 数组属性

```python
arr = np.random.randn(3, 4, 5)

print(arr.ndim)      # 维度数 → 3
print(arr.shape)     # 各维度大小 → (3, 4, 5)
print(arr.dtype)     # 数据类型 → float64
print(arr.size)      # 元素总数 → 60
print(arr.itemsize)  # 每个元素字节数
```

---

### 4. 索引、切片与修改

```python
arr = np.arange(1, 13).reshape(3, 4)

# 索引
arr[0, 1]        # 第0行第1列
arr[1]           # 第1行

# 切片 [start:end:step]
arr[0:2, 1:3]    # 前2行，第1-2列
arr[:, ::2]      # 所有行，每隔一列

# 布尔索引（非常强大）
arr[arr > 6]

# 花式索引
arr[[0, 2], [1, 3]]   # 第0行第1列 + 第2行第3列
```

---

### 5. 数组运算（向量化运算，最核心优势）

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

a + b          # [5, 7, 9]
a * b          # [4, 10, 18]
a ** 3         # 幂运算
np.sqrt(a)
np.exp(a)
np.log(a)

# 矩阵乘法
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
A @ B          # 或 np.dot(A, B)
```

**Broadcasting（广播机制）** —— 极大简化代码：

```python
arr = np.arange(12).reshape(3, 4)
arr + 10                    # 标量广播
arr + np.array([1, 2, 3, 4])  # 行广播
```

---

### 6. 常用数学与统计函数

```python
arr = np.random.randn(1000)

arr.mean()           # 均值
arr.std()            # 标准差
arr.sum()
arr.max(), arr.min()
arr.cumsum()         # 累加

np.median(arr)
np.percentile(arr, 95)

# 按轴操作
arr2d = np.random.randn(5, 6)
arr2d.sum(axis=0)    # 按列求和
arr2d.mean(axis=1)   # 按行求均值
```

---

### 7. 形状操作

```python
arr = np.arange(24)

arr.reshape(6, 4)           # 改变形状
arr.reshape(-1, 6)          # -1 表示自动推断

arr.ravel()                 # 展平（视图）
arr.flatten()               # 展平（拷贝）

np.transpose(arr2d)         # 转置
arr2d.T                     # 转置简写
```

---

### 8. 数组合并与分割

```python
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

np.vstack((a, b))      # 垂直合并
np.hstack((a, b))      # 水平合并
np.concatenate((a, b), axis=0)

np.split(arr, 3)       # 等分
```

---

### 9. 随机数模块

```python
np.random.seed(42)          # 固定种子

np.random.randint(1, 100, size=(3, 5))
np.random.normal(loc=0, scale=1, size=1000)
np.random.choice(['A', 'B', 'C'], size=10, p=[0.3, 0.5, 0.2])
```

---

### 10. 线性代数（linalg）

```python
A = np.random.rand(5, 5)

np.linalg.inv(A)           # 逆矩阵
np.linalg.eig(A)           # 特征值、特征向量
np.linalg.svd(A)           # 奇异值分解
np.linalg.norm(A, ord=2)   # 范数
```

---

### 11. 与 Pandas 的关系

Pandas 的 DataFrame 和 Series 底层就是基于 NumPy 数组实现的：

```python
import pandas as pd
df = pd.DataFrame(np.random.randn(10, 4), columns=list('ABCD'))

df.values          # 获取底层 ndarray
np.array(df)       # 转为 NumPy 数组
```

---

**NumPy 学习建议**：

1. 重点掌握：**创建数组**、**索引切片**、**广播机制**、**向量化运算**
2. 尽量避免使用 Python for 循环操作数组，要用向量化方式
3. 大数据处理时注意 `dtype` 指定（float64 精度高但占内存，float32 更省）

---

深入
例如：

- NumPy 性能优化技巧
- 高级广播与 einsum
- 内存视图与 copy 机制
- 实际数据处理案例

## pandas

**[pandas official web](https://pandas.pydata.org/docs/index.html)**

\*\*from 'Python for Data Analysis' p139 loc作用与标签，iloc作用域整数

## easyocr

## tkinter

extract from TkDocsTutorial

- columnconfigure and rowconfigure to indicate the columns and rows we'd like to expand if extra space is available in the window.

## tesseract

1.[Install](https://github.com/UB-Mannheim/tesseract/wiki) Tesseract OCR (the core engine)

2.Add Tesseract to your System PATH (Very Important)

3.Install pytesseract via pip

4.Test the Installation
