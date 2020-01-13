# -*- coding: utf-8 -*-
# created on 20200120
# @ author : bookong

import pandas
import os, sys
def here() :
    """
    """
    if 3 != len(sys.argv) :
        print("python3 " + sys.argv[0] + " [function no.] [src_csv]")
        exit()
    src_csv = sys.argv[2]
    out_csv = src_csv.replace(".csv", "_here.csv")
    file = pandas.read_csv(src_csv, encoding='utf-8', na_filter=False)
    f_os = open(out_csv, "w")
    f_os.write("wav_filename,wav_filesize,transcript\n")
    len_file = len(file)
    print("len_file : ", len_file)
    for i in range(len_file) :
        wav_path = file['wav_filename'][i].replace("\n", "").replace("\r", "")
        transcript = file['transcript'][i].replace("\n", "").replace("\r", "")
        with open(transcript, "r") as t_is :
            transcript_content = t_is.read().replace("\n", "").replace("\r", "")
        wav_filesize = os.path.getsize(wav_path)
        f_os.write(wav_path + "," + str(wav_filesize) + "," + transcript_content + "\n")
    f_os.close()


#
if __name__ == "__main__" :
    if 2 > len(sys.argv) :
        print("python3 " + sys.argv[0] + " [function no.] [...]")
        exit()
    func_no = int(sys.argv[1])
    if 1 == func_no :
        here()
