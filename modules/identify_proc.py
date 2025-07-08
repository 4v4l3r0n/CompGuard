import hashlib

def get_file_hash(file_path):
    try:
        h = hashlib.sha256() #create a new sha256 hash object
        with open(file_path, "rb") as f: #open the file in binary mode
            #read the file in chunks to avoid memory issues with large files
            while chunk := f.read(8192): #read the file in 8192 byte (8 KB) chunks
                h.update(chunk) #add every chunk to the hash object
        return h.hexdigest() #return the hash object in hexadecimal string format
    except (FileNotFoundError): #some processes may not have an executable file
        return None

