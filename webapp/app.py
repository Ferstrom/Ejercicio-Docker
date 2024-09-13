import web

urls = (
    '/', 'index'
)

app = web.application(urls, globals())

class index:
    def GET(self):
        return "Hola Docker world by Luis Fernando"

if __name__ == "__main__":
    app.run()
