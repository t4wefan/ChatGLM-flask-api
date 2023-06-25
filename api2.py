import platform
from transformers import AutoTokenizer, AutoModel
from flask import Flask, request

#load chatglm v2
tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm2-6b", trust_remote_code=True)
model = AutoModel.from_pretrained("THUDM/chatglm2-6b", trust_remote_code=True, device='cuda')
model = model.eval()
max_length = 10240

#chatglm v1
#tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True)
#model = AutoModel.from_pretrained("THUDM/chatglm-6b", trust_remote_code=True).half().cuda()

def prepare_model():
    global model
    model = model.eval()    

prepare_model()
model = model.eval()

port = 7860
os_name = platform.system()
app = Flask(__name__)
history = {}

@app.route('/chatglm', methods=["GET"])
def main():
    global history
    preset = request.args.get('preset') or request.form.get('preset') or []
    if request.method == "GET":
        prompt = request.args.get('msg')
        usrid = request.args.get('usrid')
        source = request.args.get('source')
        #temp = request.args.get('temp') if temp else 0.95
        #top_p = request.args.get('topp') if top_p else 0.7
        #preset = request.args.get('preset') if preset else ''
    
    if prompt == None:
        return '请提供内容'
    if prompt == 'ping':
        return 'pong!服务端连接正常'    
    if source == None:   
        return '无来源的请求，请更新插件'
    if usrid == None:
        return '请提供用户id'
    if not usrid in history:
        history[usrid] = preset
    
    print(f"usrid：{usrid},content：{prompt}")
    if prompt in ['clear', 'reset', '重置对话','重置会话',]:
        history[usrid] = preset
        print(f"usrid：{usrid},清空历史")
        return '已重置当前对话'
    
    response, history[usrid] = model.chat(tokenizer, prompt, history=history[usrid],max_length=max_length, )
    print(f"ChatGLM：{response}")
    return response

if __name__ == '__main__':
    print(f"欢迎使用 ChatGLM-6B API，可通过发送GET请求到http://127.0.0.1:{port}/chatglm来调用。")
    app.run(host='0.0.0.0', port=port)