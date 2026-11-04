from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <head>
        <title>Sample Web Page</title>
    </head>
    <body>
        <h1>Kapil Viknesh(260187991)</h1>
        <table border="3" cellspacing="2" cellpadding="15">
            <caption>Device Info</b></caption>
            <tr bgcolor="lime">
                <th>S.No.</th>
                <th>Specification</th> 
                <th>Details</th>
            </tr>
            <tr>
                <td>1</td>
                <td>Device name</td>
                <td>LAPTOP-CVP36L5U</td>
            </tr>
            <tr>
                <td>2</td>
                <td>Processor</td>
                <td>11th Gen Intel(R) Core(TM) i5-11400H @ 2.70GHz (2.69 GHz)</td>
            </tr>
            <tr>
                <td>3</td>
                <td>Installed RAM</td>
                <td>8.00 GB (7.73 GB usable)</td>
            </tr>
            <tr>
                <td>4</td>
                <td>Graphics card</td>
                <td>NVIDIA GeForce RTX 3050 Laptop GPU (4 GB)
Intel(R) UHD Graphics (128 MB)</td>
            </tr>
            <tr>
                <td>5</td>
                <td>Storage</td>
                <td>260 GB of 954 GB used</td>
            </tr>
            <tr>
                <td>6</td>
                <td>Device ID</td>
                <td>280AC25B-2F61-457C-9914-66100CCCF91A</td>
            </tr>
            <tr>
                <td>7</td>
                <td>Product ID</td>
                <td>00327-35944-45989-AAOEM</td>
            </tr>
            <tr>
                <td>8</td>
                <td>System type</td>
                <td>64-bit operating system, x64-based processor</td>
            </tr>
            <tr>
                <td>9</td>
                <td>Pen and touch</td>
                <td>No pen or touch input is available for this displayvenv</td>
            </tr>
        </table>
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Client request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my own webserver is running successfully...")
httpd.serve_forever()