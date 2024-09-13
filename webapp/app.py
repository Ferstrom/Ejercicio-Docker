import web

urls = (
    '/', 'index'
)

app = web.application(urls, globals())

class index:
    def GET(self):
        hola = """
        hola⡄
"""

        return hola
if __name__ == "__main__":
    app.run()
