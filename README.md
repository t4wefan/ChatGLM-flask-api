## 我们做了什么
- 我们folk了一份chatglm6b源码
- 我们进行了一些改编使其可以运行一个定制的api

## 什么是定制的api
- 为了满足一些应用场景的需要，我们定制了一个api（原作者尚不清楚，可能是ChatGPT），可以使用简单的get请求与ChatGLM对话。

## 如何使用api
- 首先部署python环境（不多赘述）
- 克隆本仓库并转入本仓库的目录
- 安装requirements.txt中的依赖
pip install -r requirements.txt
- 运行api文件，这需要至少13g的显存，在不启用量化模型的前提下
python api_fp16.py
- 等待模型加载（下载）完毕，输出地址时即可使用
- 使用get方式调用api，比如
get https://api.chat.t4wefan.pub/chatglm?msg=hello&usrid=0&source=0
可以获得输出“Hello! How can I help you today?”

## 关于api 
- api的请求要求三个参数并且缺一不可，分别是 msg,usrid,source
- msg 即为请求的正文内容
- usrid 为确定上下文及用户身份所用的id
- source 为请求的来源（为了安全和其他开发的需要）

## api的一些特殊用法
- 当msg（正文部分）为clear时，清空当前usrid下的历史记录（记忆或者说上下文）
- 这个api可以用于koishi机器人的搭建