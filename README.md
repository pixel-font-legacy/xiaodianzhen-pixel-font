> [!WARNING]
>
> 本字体并非公有领域，您在使用时，请务必谨慎考量并自负版权风险。

# 小点阵像素字体

[![Releases](https://img.shields.io/github/v/release/pixel-font-legacy/xiaodianzhen-pixel-font?style=flat-square)](https://github.com/pixel-font-legacy/xiaodianzhen-pixel-font/releases)

一款 8px 尺寸的中文点阵字体，来源不明。

原始字体的点阵数据基于内嵌的 [OpenType - EBDT](https://learn.microsoft.com/en-us/typography/opentype/spec/ebdt) 数据格式，其点阵字形在现代系统中使用起来不太方便。

这个项目进行了如下工作：

1. 将原始字体中的每个点阵尺寸各拆分为一个独立字体。
2. 将原始的点阵数据转换为轮廓字形。

## 程序依赖

- [Pixel Font Builder](https://github.com/TakWolf/pixel-font-builder)
- [FontTools](https://github.com/fonttools/fonttools)
- [Loguru](https://github.com/Delgan/loguru)
- [Cyclopts](https://github.com/BrianPugh/cyclopts)
- [Vue](https://vuejs.org)

## 许可证

### 字体

原始字体来源不明，作者以及版权不明。

因此，本字体并非公有领域，您在使用时，请务必谨慎考量并自负版权风险。

此外，原始字体的版权声明可能是不正确的，其它元信息字符串也存在非法字符，转换后已将其移除。

### 构建程序

使用 [「MIT 许可证」](LICENSE-MIT) 授权。
