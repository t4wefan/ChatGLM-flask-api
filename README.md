## 注意
本项目暂不支持提供一键包，也不会提供官方的一键包。未来会支持 Docker 镜像。

## 我们做了什么
我们使用flask框架创建了并且定制了一个ChatGLM的api

## 什么是定制的 API？
为了满足一些应用场景的需要，我们定制了一个 API（原作者尚不清楚，可能是 ChatGPT），可以使用简单的 `GET` 或 `POST` 请求与 ChatGLM 进行对话。

## 如何使用 API？
1. 首先需要部署 Python 环境，版本要求大于 3.10。
2. 克隆本仓库并转到本仓库的目录。
3. 安装 `requirements.txt` 中的依赖：
```
pip install -r requirements.txt
```
4. 运行 `api_fp16.py` 文件，需要至少 13GB 的显存，在不启用量化模型的前提下：
```
python api_fp16.py
```
5. 等待模型加载（下载）完毕，输出地址时即可使用。
6. 使用 `GET` 或者 `POST` 方式调用 API，例如：
```
GET https://api.chat.t4wefan.pub/chatglm?msg=hello&usrid=0&source=0
```
可以获得输出：“Hello! How can I help you today?”

## 关于 API
API 的请求要求三个参数并且缺一不可，分别是 `msg`、`usrid` 和 `source`。可以使用 `GET` 或者 `POST` 请求
- `msg`：请求的正文内容。
- `usrid`：确定上下文及用户身份所用的 ID。
- `source`：请求的来源（为了安全和其他开发的需要）。

## API 的一些特殊用法
- 当 `msg`（正文部分）为 `clear` 时，清空当前 `usrid` 下的历史记录（记忆或者说上下文）。
- 当 `msg` 为 `ping` 时，将返回后端状态。
- 这个 API 可以用于 koishi 机器人的搭建。
- 如果使用 AutoDL 算力平台，在安装完依赖后启动 api_autodl.py 即可在 AutoDL 的自定义服务中使用 API。