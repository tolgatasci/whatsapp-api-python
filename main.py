from api import Api

if __name__ == '__main__':
    api = Api(device_token="")
    '''
    messages = api.messages(limit=20)
    print(messages)
    
    incoming_message = api.incoming_messages()
    print(incoming_message)
    
    show_message = api.show_message("")
    print(show_message)
    
    files = {'file': ('test.jpg', open('test.jpg', 'rb'))}
    send_message = api.send_message(message_body="test", phone_numbers=["+905467751802"], files=files)
    print(send_message)
  
    send_code = api.send_code(code="053666", phone="+905467751802")
    print(send_code) 
    info = api.info()
    print(info)
    
    core_get  = api.GET(method='test',params=dict(test="1"))
    core_post = api.GET(method='test', params=dict(test="1"))
    '''
