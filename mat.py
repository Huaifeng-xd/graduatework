import numpy as np
import matplotlib
import h5py
import radiomics
import scipy.io as scio
import pydicom
import os
from matplotlib import pyplot as plt
import pylab

def getsegmentimage():
    countfile = 0
    temp = []
    while countfile<2:
        data_path = r"D:\gdesign\H&N data"
        patientid = os.listdir(data_path)
        patientid_filename_add = 'CT\image'
        ct_image_path = r"D:\gdesign\H&N data"+'\\'+patientid[countfile]+'\\'+patientid_filename_add
        #得到ct影像文件名
        ct_image_name= os.listdir(ct_image_path)
        i = 0
        ct_list = []
        dcm_data = []
        ct_pixel = []
        rtss_filename_add = 'CT\RTS\RTSS.mat'
        rtss_filename = data_path+'\\'+patientid[countfile]+'\\'+rtss_filename_add
        # print(rtss_filename)
        rtss_per = h5py.File(rtss_filename,'r')
        con = rtss_per['contours']  # 类型是group
        seg = con['Segmentation']  # 类型是dataset
        while i<len(ct_image_name):
            # print(ct_image_path+'\\'+ct_image_name[i])#一个病人ct影像文件名称
            ct_list.append(ct_image_path+'\\'+ct_image_name[i])
            dcm_data.append(pydicom.read_file(ct_list[i]))#dcm文件内容，病人数据
            ct_pixel.append(dcm_data[i].pixel_array)
            # seg_alone.append(seg[i])#得到的是一层层二值图512*512
            i = i+1
        ct_pixel = np.array(ct_pixel)#ct图像的像素信息转到np里面
        seg_np = np.array(seg)#rtss里面的二值数据转到np数组模式
        i = 0
        get_segment = ct_pixel*seg_np
        print(get_segment.shape)
        print(type(get_segment))
        temp.append(get_segment.tolist())
        # print(len(temp))
        countfile = countfile+1
    return temp
if __name__=='__main__':
    get_segment=getsegmentimage()
    get_segment=np.array(get_segment)
    print(get_segment.ndim)
    i = 50
    while i<168:
        plt.imshow(get_segment[0][i],'gray')
        pylab.show()
        i = i+1
