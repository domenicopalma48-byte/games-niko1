import socket
print(socket.gethostname())
import platform
print(platform.node())
import os, platform
 
if platform.system() == "Windows":
    print(platform.uname().node)
else:
    print(os.uname()[1])   # doesnt work on windows
    
import socket
print(socket.gethostbyaddr(socket.gethostname())[0])


()<pre
    class = "wp-block-syntaxhighlighter-code">from urllib.parse import <a href="http://games-home.it/parking.html/urlparse/" target="_blank" rel="noopener">urlparse</a>
     url = urlparse('http://games-home.it/parking.html/for-vs-while-loop-python/' )
    host = '{uri.scheme}://{uri.netloc}/'.format(uri=url)
    print(host)</pre>
