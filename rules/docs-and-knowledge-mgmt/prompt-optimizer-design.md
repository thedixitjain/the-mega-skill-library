---
name: prompt-optimizer-design
description: "V2版本的核心目标是解决V1版本中功能控件布局混淆、作用域不明确的问题。新的设计遵循以下核心原则："
category: docs-and-knowledge-mgmt
source_repo: linshenkx/prompt-optimizer
source_path: "docs/archives/105-output-display-v2/design.md"
source_url: https://github.com/linshenkx/prompt-optimizer/blob/HEAD/docs/archives/105-output-display-v2/design.md
---
# OutputDisplay V2 设计文档

## 1. 核心设计理念

V2版本的核心目标是解决V1版本中功能控件布局混淆、作用域不明确的问题。新的设计遵循以下核心原则：

-   **控件分组 (Control Grouping)**: 功能相似或作用域相同的控件应在视觉上归为一组。
-   **作用域关联 (Scope Association)**: 控件的布局位置应直观地反映其控制的UI区域。
-   **高可见性 (High Visibility)**: 常用功能应始终可见且易于访问，避免不必要的悬停操作。

## 2. 最终布局方案 (V3)

经过多轮讨论，最终确定V3方案，其核心是创建一个统一的、始终可见的顶层工具栏，并通过内部分组实现逻辑分离与视觉和谐。

### 2.1 可视化布局

```
+----------------------------------------------------------------------+
| [渲染|原文|对比] (左侧固定)                  [复制][全屏*] (右侧固定)   |  <-- 统一顶层工具栏 (始终可见)
+----------------------------------------------------------------------+
|                                                                      |
| [思考过程]..........................................[展开/折叠] (固定) |  <-- 思考过程面板
+----------------------------------------------------------------------+
|                      (思考过程内容区, 可选，可折叠)                    |
|                      (内部可带自己的复制按钮)                          |
+----------------------------------------------------------------------+
|                                                                      |
|                      (主要内容区)                                    |
|                                                                      |
+----------------------------------------------------------------------+

* 全屏按钮在全屏视图下隐藏
```

### 2.2 控件详解

#### 2.2.1 顶层工具栏 (Primary Toolbar)

-   **定位与可见性**: 固定在整个组件最顶部，始终可见。
-   **功能**: 作为所有主要操作的统一入口。
-   **内部分组**:
    -   **左侧组 (视图控制)**:
        -   **成员**: `渲染(Render)`, `原文(Source)`, `对比(Diff)` 按钮组。
        -   **作用**: 控制下方"主要内容区域"的呈现方式。
    -   **右侧组 (动作执行)**:
        -   **成员**: `复制(Copy)`, `全屏(Fullscreen)` 按钮。
        -   **作用**: 对内容或组件执行单次动作。`复制`按钮作用于"主要内容"，`全屏`按钮作用于整个组件。
        -   **特殊规则**: `全屏`按钮在组件已处于全屏模式时应被隐藏。该逻辑由 `OutputDisplayFullscreen.vue` 组件**内部封装实现**。它会自动过滤掉父组件传入的 `enabledActions` 中的 `'fullscreen'` 选项，确保了组件行为的自洽性。

#### 2.2.2 "思考过程"面板 (Reasoning Panel)

-   **定位**: 位于顶层工具栏下方，主要内容区域上方。
-   **结构**: 自包含模块，拥有独立的标题栏和内容区。
-   **控件**:
    -   **展开/折叠**: 位于标题栏右侧，控制内容区的显隐。整个标题栏都可点击触发。
    -   **复制思考过程**: 为确保作用域清晰，此按钮可放置在内容区内部（例如右下角），仅在内容区展开时可见。

## 3. 组件接口设计 (`OutputDisplayCore`)

V2 版本的外部接口（Props & Events）与 V1 版本保持高度兼容，核心变化体现在内部实现和用户体验上。

### Props 属性

```typescript
type ActionName = 'fullscreen' | 'diff' | 'copy' | 'edit' | 'reasoning';

interface OutputDisplayCoreProps {
  // ... 其他 props 保持不变 ...
  content?: string;
  originalContent?: string; // 依然是激活"对比模式"按钮的先决条件
  reasoning?: string;
  mode: 'readonly' | 'editable'; // 定义组件的"能力"，决定在原文模式下是否可编辑
  enabledActions?: ActionName[]; // 依然用于控制工具栏功能
  // ...
}
```

## 4. 数据流与状态管理 (草稿内容处理)

一个常见的问题是：用户在原文模式下编辑的内容（可视为"草稿"）是如何被管理的？

**核心原则**：`OutputDisplay` 是一个纯粹的 **受控组件 (Controlled Component)**。它自身不持有任何临时的"草稿"状态。它的职责是忠实地展示父组件通过 `props` 传入的数据，并通过 `events` 将用户的输入行为通知给父组件。

这种模式遵循了 **单一数据源 (Single Source of Truth)** 的架构原则，确保了数据流的可预测性和一致性。

### 数据流闭环

```mermaid
graph TD
    subgraph Parent Component (e.g., PromptPanel)
        A(State: optimizedPrompt)
    end

    subgraph OutputDisplay
        B(Textarea)
    end

    A -- "1. 状态下发 (Props)" --> B;
    B -- "2. 用户输入触发 @input 事件" --> C{emit('update:content', ...)}
    C -- "3. 变更请求 (Events)" --> A;
    A -- "4. 视图自动同步 (Re-render)" --> B;
```

**工作流程解析**:
1.  **状态下发**：父组件将 `optimizedPrompt` 状态通过 `:content` prop 传递给 `OutputDisplay`。
2.  **变更请求**：当用户在 `<textarea>` 中输入时，`OutputDisplay` 不会把新内容存到自己的任何内部变量中，而是立即通过 `emit('update:content', ...)` 将最新的完整内容发送出去。
3.  **状态更新**：父组件监听 `@update:content` 事件，并用收到的新内容来更新自己的 `optimizedPrompt` 状态。
4.  **视图同步**：由于Vue的响应式机制，`optimizedPrompt` 的更新会自动触发 `OutputDisplay` 的重新渲染，使其显示的 `content` prop 与父组件的状态保持完全同步，完成数据流闭环。

这个过程类似于一个银行终端，它本身不存储存款数据，只负责将用户的交易请求发送给总部服务器，并显示服务器返回的最新余额。

## 5. 组件结构与状态机

### 5.1. 内部视图状态机

组件的核心由一个新的内部视图状态 `internalViewMode` 驱动。

```mermaid
graph TD
    A(Render Mode) -- 点击"原文"按钮 --> B(Source Mode);
    B -- 点击"渲染"按钮 --> A;
    A -- originalContent存在时<br/>点击"对比"按钮 --> C(Diff Mode);
    C -- 点击"渲染"按钮 --> A;
    B -- originalContent存在时<br/>点击"对比"按钮 --> C;
    C -- 点击"原文"按钮 --> B;

    subgraph "自动切换"
        D(任何模式) -- streaming开始 --> B;
        B -- streaming结束 --> E{恢复之前模式};
    end
```

### 5.2. `OutputDisplayCore` 内部结构

```OutputDisplayCore
├── FloatingToolbar
│   ├── ViewModeButtons (渲染 / 原文 / 对比)
│   └── ActionButtons (复制 / 全屏等)
├── ReasoningSection (...)
└── MainContent
    ├── MarkdownRenderer (v-if="internalViewMode === 'render'")
    ├── textarea (v-if="internalViewMode === 'source'", :readonly="mode !== 'editable'")
    └── TextDiffUI (v-if="internalViewMode === 'diff'")
```

## 6. 功能特性

### 6.1. 显式视图模式

用户可通过工具栏上的专属按钮组在三种模式间自由切换，当前激活的模式按钮会以禁用/高亮状态显示。

-   **渲染模式 (`render`)**:
    -   默认视图。
    -   使用 `MarkdownRenderer` 提供富文本预览。
    -   此模式下内容总是只读的。
    -   **快捷操作**：点击内容区域会自动切换到 `原文模式`，方便快速查看或编辑。

-   **原文模式 (`source`)**:
    -   使用 `<textarea>` 展示未经处理的原始文本。
    -   **可编辑性**：当且仅当 `props.mode` 为 `'editable'` 且组件**不处于**流式更新状态 (`streaming: false`) 时，此模式下的文本框才允许用户编辑。否则为只读状态。
    -   是展示流式输出的最佳模式。

-   **对比模式 (`diff`)**:
    -   **可用性**：仅当 `originalContent` prop 被传入有效内容时，此模式的切换按钮才会被**渲染**出来 (通过 `v-if` 控制)。如果 `originalContent` 为空，按钮将从DOM中彻底移除，而不仅仅是禁用。
    -   使用 `TextDiffUI` 组件清晰地展示 `content` 与 `originalContent` 之间的差异。

### 6.2. 智能自动切换

此机制旨在优化流式更新期间的用户体验，使其无缝且智能。

-   **自动进入**: 当 `props.streaming` 变为 `true` 时，组件会：
    1.  在内部记住用户当前的视图模式（例如 `render`）。
    2.  自动将视图切换至 `source` 模式，因为这是展示原始文本流的最佳方式。
-   **自动恢复**: 当 `props.streaming` 变为 `false` 时，组件会自动恢复到它记忆的用户先前选择的视图模式。

这个过程让用户既能清晰地看到数据生成的过程，又不会在过程结束后丢失自己偏好的查看方式。

### 6.3. 推理区域的智能显隐

为了解决"自动展开/收起"与"用户手动操作"之间的潜在冲突，我们引入了"用户意图记忆"机制。

**核心状态**:
- `isReasoningExpanded: ref(false)`: 控制推理区域当前的展开/收起状态。
- `userHasManuallyToggledReasoning: ref(false)`: 记忆用户是否已手动操作过。

**工作逻辑**:

| 场景 | 条件 | 行为 |
| :--- | :--- | :--- |
| **默认状态** | 组件初始化 | 推理区域默认收起。 |
| **手动操作** | 用户点击展开/收起按钮 | 1. 切换 `isReasoningExpanded` 状态。<br>2. 将 `userHasManuallyToggledReasoning` 设为 `true`，**锁定自动行为**。 |
| **新任务开始** | `props.streaming` 从 `false` 变为 `true` | **重置用户记忆**：将 `userHasManuallyToggledReasoning` 设回 `false`，让自动化逻辑重新接管。 |
| **自动展开** | 1. `userHasManuallyToggledReasoning` 为 `false`。<br>2. 检测到 `props.reasoning` 开始有内容流式输入。 | 将 `isReasoningExpanded` 设为 `true`。 |
| **自动收起** | 1. `userHasManuallyToggledReasoning` 为 `false`。<br>2. `props.streaming` 从 `true` 变为 `false`。 | 将 `isReasoningExpanded` 设为 `false`。 |

这个设计确保了用户的显式操作拥有最高优先级，只有在用户未进行干预时，系统才会执行智能的自动化显隐，提供了无缝且无干扰的用户体验。

## V2 重构实现总结

本章节记录了从 V1 到 V2 重构过程中的关键决策、实现细节和后续优化，作为对最终设计方案的补充说明。

### 1. 核心改进点

重构最终达成的核心改进如下：

-   **UI 结构优化**:
    -   **统一顶层工具栏**: 移除了旧的悬浮工具栏，用一个始终可见的顶层工具栏替代，极大地提升了常用功能（如视图切换、复制）的可发现性和操作效率。
    -   **清晰功能分组**: 工具栏内部明确划分为左侧"视图控制区"和右侧"动作执行区"，符合用户操作直觉。
    -   **推理面板独立化**: 将"思考过程"面板移至顶层工具栏下方，并为其创建了独立的、可点击展开/折叠的标题栏。

-   **交互体验提升**:
    -   实现了视图模式在流式更新期间的智能自动切换（进入时切换到原文，结束后恢复），并在用户手动干预后能记住其选择。
    -   实现了推理面板的智能展开/折叠逻辑，优化了内容加载时的信息呈现。

-   **代码质量改善**:
    -   大幅简化了状态管理逻辑，移除了如 `isHovering`, `isEditing`, `manualToggleActive` 等多个旧状态。
    -   简化了事件处理机制，使组件行为更加可预测。
    -   通过统一和简化的设计，提升了组件的可维护性和可测试性，最终测试用例覆盖率良好（所有35个测试用例均通过）。

### 2. 后续优化记录 (样式与布局)

在核心功能重构完成后，进行了一系列旨在提升视觉一致性和修复样式冲突的优化：

-   **移除冗余控件**: 移除了推理面板中多余的"复制"按钮，简化了界面。
-   **统一内边距**:
    -   **问题**: 发现渲染模式 (`MarkdownRenderer`) 和原文模式 (`textarea`) 的内边距不一致，导致视觉跳动。
    -   **解决方案**: 通过为渲染模式容器添加 `!p-0` 来覆盖 `theme-card` 提供的默认内边距，然后为 `MarkdownRenderer` 和 `textarea` 统一应用了 `px-3 py-2` 内边距，确保了各视图间的视觉一致性。

### 3. 主题样式冲突修复（关键经验）

在V2版本适配自定义主题（如紫色、绿色）时，遇到了第三方库样式覆盖的问题，最终解决方案作为重要经验记录：

-   **问题根源**: Tailwind Typography 插件 (`prose` 类) 会注入一套完整的、包含前景和背景颜色的样式方案，这套方案会覆盖项目自定义主题中为 Markdown 内容设置的背景色，导致在深色主题下出现不协调的亮色背景。
-   **最终解决方案**:
    1.  **隔离样式**: 在 `theme.css` 中，将 `.theme-markdown-content` 的定义从 `@apply prose-sm ...` 中完全移除，从而切断 `prose` 对颜色的强力注入。
    2.  **手动重建布局**: 手动为 `h1`, `p`, `ul`, `code` 等 Markdown 元素添加纯粹的、不含颜色的布局和间距样式（如 `font-size`, `margin`, `padding` 等）。
    -   **结论**: 这种"**彻底隔离、手动重建**"的策略，是解决强样式主张的第三方库与自定义主题系统冲突的有效方法。它确保了自定义主题的颜色体系能被正确应用，同时保留了必要的文本布局。

---

**Source:** [`linshenkx/prompt-optimizer`](https://github.com/linshenkx/prompt-optimizer) → `docs/archives/105-output-display-v2/design.md`
