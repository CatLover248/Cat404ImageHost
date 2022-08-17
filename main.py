import tornado.web
import tornado.ioloop

# Followed tutorial -> https://youtu.be/00bLHDtU7U4

class uploadHandler(tornado.web.RequestHandler):
  def get(self):
    self.render("index.html")
  def post(self):
    files = self.request.files["imgFile"]
    for f in files:
      fh = open(f"img/{f.filename}", "wb")
      fh.write(f.body)
      fh.close()
    self.write("Navigate to -> localhost:8080/" + "img/"+ f.filename +"  to see your image!")

if(__name__ == "__main__"):
  app=tornado.web.Application([
    ("/", uploadHandler),
    ("/img/(.*)",tornado.web.StaticFileHandler, {"path":"img"})
    
  ])
  app.listen(8080)

  tornado.ioloop.IOLoop.instance().start()