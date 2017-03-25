from http.server import HTTPServer, CGIHTTPRequestHandler
import settings
import sqlite3
#settings.init_directory()

port = 8080
httpd = HTTPServer(('', port), CGIHTTPRequestHandler)

#connection = sqlite3.connect(settings.path_to_ddbb)
#cursor = connection.cursor()
#results = cursor.execute("SELECT name FROM athletes")
# print(results.fetchall())

print("Starting simple_httpd on port: " + str(httpd.server_port))
httpd.serve_forever()

