from microdot import Microdot, Response,send_file
from microdot_utemplate import render_template
from led_module import LEDModule
import uasyncio
import json


app = Microdot()
Response.default_content_type = 'text/html'

LED1=LEDModule(13)
LED2=LEDModule(18)

@app.route('/', methods=['GET', 'POST'])
def index(req):
    #status = None
#     if req.method == 'POST':
#         status = req.form.get('status')
#         if (status=="on"):
#             LED1.on()
#         elif (status=="off"):
#             LED1.off()
    return render_template('index.html', status=LED1.get_value())

@app.route('/on', methods=['GET', 'POST'])
def on(req):
    LED1.on()
    jsonstr={"result": "ON"}
    return Response(body=jsonstr)
    
    #return str(LED1.get_value())


@app.route('/on/<int:id>', methods=['GET', 'POST'])
def on1(req,id):
    if (id==1):
        LED1.on()
    elif (id==2):
        LED2.on()
    else:
        jsonstr={"result": "NO EXIST"}
        return Response(body=jsonstr)
    jsonstr={"result": "ON"}
    return Response(body=jsonstr,headers={'Access-Control-Allow-Origin':'*'})
    
    #return str(LED1.get_value())



@app.route('/off/<int:id>', methods=['GET', 'POST'])
def off1(req,id):
    if (id==1):
        LED1.off()
    elif (id==2):
        LED2.off()
    else:
        jsonstr={"result": "NO EXIST"}
        return Response(body=jsonstr)
    jsonstr={"result": "OFF"}
    return Response(body=jsonstr,headers={'Access-Control-Allow-Origin':'*'})



@app.route('/status/<int:id>', methods=['GET', 'POST'])
def status1(req,id):
    status=''
    if (id==1):
        status=LED1.get_value()
    elif (id==2):
        status=LED2.get_value()
    else:
        jsonstr={"result": "NO EXIST"}
        return Response(body=jsonstr)
    jsonstr={"result": status}
    return Response(body=jsonstr,headers={'Access-Control-Allow-Origin':'*'})




@app.route('/off', methods=['GET', 'POST'])
def off(req):
    LED1.off()
    jsonstr={"result": "OFF"}
    return Response(body=jsonstr)
    
@app.route('/static/<path:path>')
def static(request, path):
    if '..' in path:
        # directory traversal is not allowed
        return 'Not found', 404
    return send_file('static/' + path)


if __name__ == '__main__':
    app.run()
