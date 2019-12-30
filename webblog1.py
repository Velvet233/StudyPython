#基本网站
form http.server import HTTPServer.BaseHTTPRequestHeader
form urllib,parse import parse_qs

memory=[]

# design form
form'''<!DOCTYPE html>
<title>Dy's testing web</title>
<html>
  <form medthod="POST">
    <textarea name="message">
      <br>
      <botton type="submit">提交</button>
    </textarea>
  
  </form>
  <pre>
  
  </pre>

</html>
'''

class Handler(BaseHTTPRequestHandler):
  def do_POST(self):
    length=int(self.harders.get('Contant-length',0))
    data=self.rfile.read(length).decode() #decode
    message=parse_qs(data)["message"](0)  #解析
    message=message.replace("<","&lt;")
    memory.append(message)
    
    self.send_respond(303)
    self.send_header('Content_type','text/plain;charest:utf-8')
    self.and_header()
    
    
