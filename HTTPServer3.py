import http.server as hs  
import sys, os  
  
      
class myHandler(hs.BaseHTTPRequestHandler):  
      
    def send_content(self, page, status = 200):  
        try:  
            self.send_response(status)
            if 'css' in self.path :
                self.send_header("Content-type", "text/css")
            elif 'html' in self.path :
                self.send_header("Content-type", "text/html")
            elif ('png' in self.path) or ('ico' in self.path) :
                self.send_header("Content-type", "image/apng")
            elif 'jpg' in self.path:
                self.send_header("Content-type", "image/jpeg")
            else :
                self.send_header("Content-type", "text/html")   
            self.send_header("Content-Length", str(len(page)))  
            self.end_headers()  
            self.wfile.write(page)  
        except TypeError:
            pass 
      
    def do_GET(self):        
        if self.path == '/':
            self.path = '/index.html'  
            #获取文件路径  
        full_path = os.getcwd() + self.path
            
        if os.path.exists(full_path) and os.path.isfile(full_path):  
            self.handle_file(full_path)  
        else :
            self.send_content(self.path,404)
     
  
      
    def handle_file(self, full_path): 
        try: 
            with open(full_path, 'rb') as file:  
                content = file.read()  
                  
            self.send_content(content,200) 
        except e :
            print(e)
            self.send_content(self.path,404)
  
  
if __name__ == '__main__':

    print('The server is ready to receive') 
    httpAddress = ('', 6699)  
    httpd = hs.HTTPServer(httpAddress, myHandler)  
    httpd.serve_forever()
    


