# example/views.py
from datetime import datetime
import platform

from django.http import HttpResponse

def index(request):
    now = datetime.now()
    version = platform.python_version()
    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
            <p>The current time is { version }.</p>
            
        </body>
    </html>
    '''
    return HttpResponse(html)
