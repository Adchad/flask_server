import flask
from plyer import notification

app = flask.Flask(__name__)

def ntfy(titl,msg):
    notification.notify(
        title=titl,
        message=msg,
        app_icon='C:\\Users\\chada\\Downloads\\Icons8-Halloween-Ghost-2.ico',  # e.g. 'C:\\icon_32x32.ico'
        timeout=5,  # seconds
    )




@app.route('/test', methods =['POST'])
def test():
    print("test\n")
    data= flask.request.get_data()
    real_text = str(data)[2:-1]
    print(real_text)
    ntfy("WTF",real_text)
    return ""
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
