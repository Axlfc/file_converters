import src
import data
from data import audio as a
from data import compressed as c
from data import document as d
from data import ebook as e
from data import hash as h
from data import image as i
from data import service
from data import software
from data import video as v

audio_ext = list(a.audio_extensions.values())
compressed_ext = list(c.compressed_extensions.values())
document_ext = list(d.document_extensions.values())
ebook_ext = list(e.ebook_extensions.values())
image_ext = list(i.image_extensions.values())
software_ext = list(software.software_extensions.values())
video_ext = list(v.video_extensions.values())


hash_format_names = h.hash_formats


def services():
    my_dict = service.services_proportions
    fps = [23.976, 25, 30]
    for keyname in my_dict:
        print(keyname)
        elem = my_dict[keyname]
        for w in elem:
            print(w)
        print()
    #return my_dict

def main():

    services()
    #print(services())


if __name__ == '__main__':
    main()