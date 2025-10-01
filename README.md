# Kronos WebUI for Mac

这是一个为Mac系统优化的Kronos WebUI版本，适配无GPU的Mac系统（特别是2015年及更早版本）。

## 项目介绍

本项目是将原本为Windows GPU环境设计的Kronos WebUI项目改造为可在Mac上运行的版本。主要改动包括：

1. 路径兼容性修改（硬编码Windows路径替换为跨平台路径）
2. 脚本兼容性修改（PowerShell脚本转换为shell脚本）
3. 环境配置修改（更新R和Python路径配置以适应Mac系统）
4. 模型运行机制改造（适配无GPU的Mac系统）

## 文件说明

- `CPU_OPTIMIZATION_SUMMARY.md` - CPU优化版本修改总结
- `CPU_OPTIMIZED_TEST_PLAN.md` - CPU优化版本测试计划
- `GITHUB_UPLOAD_SUMMARY.md` - GitHub上传总结
- `create_zip_package.py` - 创建安装包的脚本

## 完整安装包

由于模型文件较大，完整安装包已创建为ZIP文件：
[kronos_mac_cpu_optimized_package.zip](kronos_mac_cpu_optimized_package.zip)

## 注意事项

- 本仓库不包含大型模型文件，仅包含项目的核心代码和文档
- 如需完整功能，请下载ZIP安装包
- CPU推理速度较慢，需要耐心等待预测结果