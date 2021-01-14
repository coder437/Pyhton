
import dropbox
class TransferData :
    def __init__(self,token):
        self.token=token
    def uploadFile(self,source,destination):
        dbx = dropbox.Dropbox(self.token)
        f = open(source,"rb")
        dbx.files_upload(f.read(),destination)
def main():
    at="sl.ApMdljFNVC2AeR4zGk8qlTjbDqPbbNvi18owTKXiJcRdkTnhDanEWcuHflRlJJx4m1be3G45GPnjL26kpOsXrtevSDkWCsLN7OI0_DdrZ4iOmpKNfXzARxXQJWIJe_kSUsf1KPg"
    t = TransferData(at)
    s = input("enter file path to transfer")
    d = input("enter path to upload dropbox")
    t.uploadFile(s,d)
    print("file uploaded")

main()
