# Github Action 部署

> 前提：确保您已获取到所有配置，详见：[【DouYinSparkFlow 配置生成器】使用说明](配置生成器使用.md)

本项目已经预设Action配置，只需填写相关配置即可启用。

## 1. Fork 仓库

采用Action部署本项目需要先 Fork 仓库。

操作步骤如下：

1. 打开本项目主页，点击右上角 Fork，将仓库复制到你的 GitHub 账号下。
2. 进入你账号下新生成的仓库，完成后续配置

> 项目有用别忘了点Star支持开发者

## 2. 启用workflow与action

首次fork后需要手动启用`workflow`和对应`action`

在自己fork后的仓库上方点击`Actions`按照下方图示启用工作流

![启用workflow](images/启用workflow.png)

![启用action](images/启用action.png)

## 3. 创建 Environment（环境）

这一步在你 Fork 后的仓库中创建名为 `user-data` 的 Environment（环境）。

操作路径：进入你Fork项目后的 GitHub 仓库，依次点击 `Settings` -> `Environments` -> `New environment`，名称填写 `user-data` 并创建。

说明：这里创建的是部署环境（Environment），后续再在该环境下配置 Secrets 和 Variables。

![创建`user-data`环境图](images/屏幕截图%202026-02-14%20224915.png)

## 4. 配置 Secrets 和 Variables

在你刚创建的 `user-data` Environment 中，分别配置 Variables 和 Secrets。

操作步骤如下：

1. 打开已经填写好的配置生成器页面，先查看左侧上方`Environment Variables` 区域。
2. 进入 GitHub 仓库的 `Settings` -> `Environments` -> `user-data` -> `Environment variables`，逐条新增对应变量。
3. 回到配置生成器，查看左侧下方 `Environment Secrets` 区域。
4. 进入 GitHub 仓库的 `Settings` -> `Environments` -> `user-data` -> `Environment secrets`，逐条新增对应密钥。

注意事项：

- 变量名和变量值请与配置生成器保持完全一致（包含大小写）建议直接使用复制按钮复制粘贴。
- 不要把 Secrets 内容填到 Variables，也不要把 Variables 内容填到 Secrets。

![配置生成器](images/配置生成器.png)

## 5. 修改执行时间（可选）

如需调整自动执行时间，编辑仓库文件 `.github/workflows/schedule.yml`，找到下方配置：

```yaml
on:
  workflow_dispatch: # 允许手动触发
  schedule: # 定时任务
    - cron: "0 1 * * *" # 每天 1:00 UTC（对应北京时间 9:00）
```

将 `cron: "0 1 * * *"` 修改为你需要的时间表达式即可。

注意事项：

- GitHub Actions 的 `cron` 使用 UTC 时区，不是北京时间。
- 北京时间（UTC+8） = UTC 时间 + 8 小时。
- 建议先手动触发一次工作流，确认配置无误后再依赖定时任务。

Cron 基础语法（5 段）：

`分钟 小时 日 月 星期`

常用写法：

- `*`：任意值
- `*/n`：每 n 个单位执行一次
- `a,b`：在多个指定值执行
- `a-b`：在一个范围内执行

示例（UTC）：

- `0 1 * * *`：每天 UTC 01:00（北京时间 09:00）
- `30 13 * * *`：每天 UTC 13:30（北京时间 21:30）
- `0 */6 * * *`：每 6 小时执行一次
- `0 1 * * 1-5`：工作日 UTC 01:00 执行

> 可以交给 AI 生成，下面给出提示词示例可以直接套用：
>
> GitHub Actions 的默认时区是 UTC。我需要每天在北京时间 XXX 自动触发工作流，请换算后给出 cron 表达式。除 `cron: "..."` 这一行外，不需要输出其他内容。

## 6. 手动触发测试（可选）

> 建议执行此步骤，可以验证配置是否达到预期，此外首次fork后也需要手动触发后续才会自动执行

仓库的工作流中添加了`workflow_dispatch`以便允许进行手动触发，在初次配置完成后可以通过手动触发Action来进行验证，操作方式如下图所示：

![手动测试](images/屏幕截图%202026-02-14%20224614.png)