import settings
import importlib

def send_xxxx(content):
    for path in settings.NOTIFY_LIST:
        # 'notify.email.Email',
        # 'notify.msg.Msg',
        # 'notify.wechat.Wechat'
        module_path,class_name = path.rsplit('.',maxsplit=1)
        # importlib.import_module("notify.email")
        # 根据字符串导入模块：notify.email
        module = importlib.import_module(module_path)
        # 根据类名称去模块中获取类
        cls = getattr(module,class_name)
        # 根据类实例化
        obj = cls()
        obj.send(content)

