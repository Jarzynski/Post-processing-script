import numpy as np
import pandas as pd
import os

read_path = ""
output_path = ""
#处理dump文件，获得按列排布的离子位置信息


# 获取文件路径
def get_file_path():
    read_path = r"E:/mica/Na/jw/E=3/8000/traj"
    output_path = r"E:/mica/Na/jw/E=3/8000/pass"
    return read_path,output_path

# 读取文件名称和内容
def deal_files():
    # 获取read_path下的所有文件名称（顺序读取的）
    files = os.listdir(read_path)
    coordinates=np.empty(28)
    for file_name in files:
        # 读取单个文件内容
        file_input = open(read_path+"/"+file_name,'r')
        file_output = open(output_path+"/"+file_name+".txt",'w+')
        while True:
            eachline = file_input.readline().split("\n")[0]
            if not eachline:
                file_input.close()
                file_output.close()
                break
            try:  #读取第一个位置
                b = eachline.index(' ')
                ionID = eachline[0:b]   #离子序号
                ionID = int(ionID,10)
                transition = eachline[(b+1):]
                try:
                    c = transition.index(' ')
                    ioncoord = transition[(c+1):] #粒子坐标
                    if ionID == 3:
                        coordinates[0]=ioncoord
                    if ionID == 87:
                        coordinates[1]=ioncoord
                    if ionID == 171:
                        coordinates[2]=ioncoord
                    if ionID == 255:
                        coordinates[3]=ioncoord
                    if ionID == 591:
                        coordinates[4]=ioncoord
                    if ionID == 675:
                        coordinates[5]=ioncoord
                    if ionID == 759:
                        coordinates[6]=ioncoord
                    if ionID == 843:
                        coordinates[7]=ioncoord
                    if ionID == 1179:
                        coordinates[8]=ioncoord
                    if ionID == 1263:
                        coordinates[9]=ioncoord
                    if ionID == 1347:
                        coordinates[10]=ioncoord
                    if ionID == 1431:
                        coordinates[11]=ioncoord
                    if ionID == 1767:
                        coordinates[12]=ioncoord
                    if ionID == 1851:
                        coordinates[13]=ioncoord
                    if ionID == 1935:
                        coordinates[14]=ioncoord
                    if ionID == 2019:
                        coordinates[15]=ioncoord
                    if ionID == 339:
                        coordinates[16]=ioncoord
                    if ionID == 423:
                        coordinates[17]=ioncoord
                    if ionID == 507:
                        coordinates[18]=ioncoord
                    if ionID == 927:
                        coordinates[19]=ioncoord
                    if ionID == 1011:
                        coordinates[20]=ioncoord
                    if ionID == 1095:
                        coordinates[21]=ioncoord
                    if ionID == 1515:
                        coordinates[22]=ioncoord
                    if ionID == 1599:
                        coordinates[23]=ioncoord
                    if ionID == 1683:
                        coordinates[24]=ioncoord
                    if ionID == 2103:
                        coordinates[25]=ioncoord
                    if ionID == 2187:
                        coordinates[26]=ioncoord
                    elif ionID == 2271:
                        coordinates[27]=ioncoord
                    else:
                        pass
                except ValueError:
                    pass
            except ValueError:
                str2 = ' '.join(str(i) for i in coordinates)
                file_output.write(str2 + "\n")
                pass
        file_input.close()
        file_output.close()


# 主函数
if __name__=="__main__":
    # 获取文件输入和输出路径
    read_path,output_path = get_file_path()
    # 开始处理文件，并输出处理文件结果
    deal_files()