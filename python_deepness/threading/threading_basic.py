import threading, zipfile
from helpers import get_timestamp


class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print(get_timestamp() + 'Finished background zip of:', self.infile)

background = AsyncZip('mydata.txt', 'myarchive.zip')
background.start()
print(get_timestamp() + 'The thread task just started to zip file in background.')
print(get_timestamp() + 'The main program continues to run in foreground.')

background.join()    # Wait for the background task to finish
print(get_timestamp() + 'Main program waited until background was done.')
