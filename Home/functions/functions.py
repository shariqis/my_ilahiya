

def upload_file(f):
    with open("Home/static/upload/"+f.name,"wb+") as des:
        for i in f.chunks():
            des.write(i)
    