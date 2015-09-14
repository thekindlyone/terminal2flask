import requests

def make_request(msg):
    r=requests.get('http://127.0.0.1:5000/message',params={'message':msg})
    return r.content

while True:
    msg=raw_input('Enter message(q to quit)')
    if msg=='q':
        break
    response = make_request(msg)
    print 'response: ',response

