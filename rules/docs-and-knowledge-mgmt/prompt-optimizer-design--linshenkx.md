---
name: prompt-optimizer-design
description: "桌面端自动更新系统采用双版本显示设计，同时展示正式版和预览版更新信息，让用户自主选择更新路径。"
category: docs-and-knowledge-mgmt
source_repo: linshenkx/prompt-optimizer
source_path: "docs/archives/118-desktop-auto-update-system/design.md"
source_url: https://github.com/linshenkx/prompt-optimizer/blob/HEAD/docs/archives/118-desktop-auto-update-system/design.md
---
# 桌面端自动更新系统 - 设计文档

## 🎯 设计概述

桌面端自动更新系统采用双版本显示设计，同时展示正式版和预览版更新信息，让用户自主选择更新路径。

### 核心设计原则
1. **信息层次清晰**：当前版本 → 最新正式版 → 最新预览版
2. **操作直观明确**：每个版本独立的操作按钮
3. **状态标识醒目**：右上角红色"有更新"标签
4. **底部按钮固定**：只有"关闭"和"检查更新"两个按钮

## 📱 界面布局设计

### 完整布局结构
```
┌─────────────────────────────────────────┐
│ 应用更新                                 │
├─────────────────────────────────────────┤
│ ┌─ 当前版本 ─────────────────────────┐   │
│ │ 当前版本: v1.2.0                   │   │
│ └───────────────────────────────────┘   │
│                                         │
│ ┌─ 最新正式版 ─────────────────────────┐ │
│ │ 正式版 v1.2.1        [有更新] ↗    │ │
│ │ [详情] [忽略] [下载]                │ │
│ └─────────────────────────────────────┘ │
│                                         │
│ ┌─ 最新预览版 ─────────────────────────┐ │
│ │ 预览版 v1.3.0-beta.1  [有更新] ↗    │ │
│ │ [详情] [忽略] [下载]                │ │
│ └─────────────────────────────────────┘ │
│                                         │
├─────────────────────────────────────────┤
│              [关闭] [检查更新]           │
└─────────────────────────────────────────┘
```

### 状态显示逻辑
- **有更新**：显示红色"有更新"标签和右上角链接图标
- **已是最新**：显示绿色"已是最新"文字
- **检查中**：显示加载动画和"检查中..."文字
- **检查失败**：显示错误信息和重试提示

## 🔧 技术架构设计

### 双版本检查机制
```typescript
// 主进程统一管理，避免并发冲突
const checkAllVersions = async () => {
  // 串行检查正式版
  autoUpdater.allowPrerelease = false
  const stableResult = await autoUpdater.checkForUpdates()
  
  // 延迟后检查预览版
  await new Promise(resolve => setTimeout(resolve, 1000))
  autoUpdater.allowPrerelease = true
  const prereleaseResult = await autoUpdater.checkForUpdates()
  
  return { stable: stableResult, prerelease: prereleaseResult }
}
```

### 版本比较逻辑
- **正式版比较**：使用semver标准比较
- **预览版比较**：先比较基础版本，再比较预发布标识
- **忽略版本处理**：支持分别忽略正式版和预览版

### 状态管理设计
```typescript
interface UpdaterState {
  // 检查状态
  isChecking: boolean
  hasStableUpdate: boolean
  hasPrereleaseUpdate: boolean
  
  // 版本信息
  currentVersion: string
  stableVersion: string | null
  prereleaseVersion: string | null
  
  // 下载状态
  isDownloading: boolean
  downloadProgress: number
  isDownloaded: boolean
  
  // 忽略状态
  isStableVersionIgnored: boolean
  isPrereleaseVersionIgnored: boolean
}
```

## 🎨 UI组件设计

### 版本信息卡片
- **标题区域**：版本类型 + 版本号 + 状态标签
- **操作区域**：详情链接 + 忽略按钮 + 下载按钮
- **状态指示**：右上角链接图标（有更新时显示）

### 按钮状态设计
- **下载按钮**：
  - 有更新且未忽略：显示"下载"
  - 下载中：显示进度条
  - 下载完成：显示"安装并重启"
- **忽略按钮**：只在有更新时显示
- **详情链接**：始终显示，点击打开GitHub发布页面

### 响应式设计
- **最小宽度**：480px
- **最大宽度**：600px
- **高度自适应**：根据内容动态调整
- **移动端适配**：按钮大小和间距优化

## 🔄 交互流程设计

### 检查更新流程
1. 用户点击"检查更新"
2. 显示加载状态
3. 主进程串行检查两个版本
4. 更新UI显示结果
5. 根据结果显示相应的操作按钮

### 下载安装流程
1. 用户选择版本并点击"下载"
2. 显示下载进度
3. 下载完成后显示"安装并重启"按钮
4. 用户点击安装，应用重启并更新

### 忽略版本流程
1. 用户点击"忽略"按钮
2. 保存忽略状态到本地存储
3. 隐藏该版本的更新提示
4. 更新主界面的红点状态

## 🛡️ 错误处理设计

### 网络错误处理
- **超时处理**：30秒超时，显示重试提示
- **连接失败**：显示网络错误信息
- **认证失败**：显示权限错误提示

### 下载错误处理
- **下载中断**：支持断点续传
- **文件损坏**：重新下载
- **磁盘空间不足**：显示空间不足提示

### 安装错误处理
- **权限不足**：提示以管理员身份运行
- **文件占用**：提示关闭相关程序
- **安装失败**：显示详细错误信息

## 📊 性能优化设计

### 缓存策略
- **版本信息缓存**：2小时有效期
- **下载文件缓存**：保留最新版本文件
- **状态持久化**：忽略状态本地存储

### 资源优化
- **按需加载**：只在需要时检查更新
- **后台检查**：应用启动时自动检查
- **智能提醒**：避免频繁打扰用户

---

**设计目标**：提供直观、可靠、用户友好的自动更新体验，让用户能够轻松管理应用版本更新。

---

**Source:** [`linshenkx/prompt-optimizer`](https://github.com/linshenkx/prompt-optimizer) → `docs/archives/118-desktop-auto-update-system/design.md`
