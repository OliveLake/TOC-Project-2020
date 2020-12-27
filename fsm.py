from transitions.extensions import GraphMachine
from utils import send_text_message
from linebot import LineBotApi, WebhookParser
from linebot.models import *
import os

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

# is_going_to
    
    def is_going_to_helper(self, event):
        return True
    def is_going_to_ingredient(self, event):
        text = event.message.text
        return text.lower() == "食材"

    def is_going_to_state1(self, event):
        text = event.message.text
        return text.lower() == "go to state1"

    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "go to state2"

# all states
    #helper
    def on_enter_helper(self, event):
        channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
        line_bot_api = LineBotApi(channel_access_token)
        buttons_template = ButtonsTemplate(
        title='今晚我想來點...', text='選擇料理', actions=[

        ])
        template_message = TemplateSendMessage(
            alt_text='請用手機看此訊息！', template=buttons_template)
        line_bot_api.reply_message(event.reply_token, template_message)
        print("I'm entering helper")


'''
        print("enter helper")
        
        helper_text = ""
        helper_text += "薩爾達料理： 指令列表\n"
    
        reply_token = event.reply_token
        send_text_message(reply_token, help_text)
        self.go_back()
'''
'''        channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
        line_bot_api = LineBotApi(channel_access_token)
        buttons_template = ButtonsTemplate(
        title='今晚我想來點...', text='選擇料理', actions=[
            PostbackAction(lable='食材', text='食材')

        ])
        template_message = TemplateSendMessage(
            alt_text='請用手機看此訊息！', template=buttons_template)
        line_bot_api.reply_message(event.reply_token, template_message)
        print("I'm entering helper")
'''
'''
    def on_exit_helper(self,event):
        print("leaving helper")   
'''
'''
    #ingredient
    def on_enter_ingredient(self,event):
        print("I'm entering ingredient")
        
        reply_token = event.reply_token
        send_text_message(event.reply_token,text = "Trigger ingredient")
        self.go_back()

    def on_exit_ingredient(self):
        print("Leaving state1")
'''
