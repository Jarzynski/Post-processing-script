import os
read_path = ""
output_path = ""
#处理dump文件，获得按列排布的离子位置信息


# 获取文件路径
def get_file_path():
    read_path = r"E:/mica/Na/jw/E=3/8000/pass"
    output_path = r"E:/mica/Na/jw/E=3/8000/z"
    return read_path,output_path

# 读取文件名称和内容
def deal_files():
    # 获取read_path下的所有文件名称（顺序读取的）
    files = os.listdir(read_path)
    i=1
    for file_name in files:
        # 读取单个文件内容
        file_input = open(read_path+"/"+file_name,'r')
        file_output = open(output_path+"/"+"traj"+file_name,'w+')
        while True:
            eachline = file_input.readline().split("\n")[0]
            if not eachline:
                file_input.close()
                file_output.close()
                break
            if i < 9:
                i += 1
            else:
                i=1
                file_output.write(eachline+"\n")
            
        file_input.close()
        file_output.close()


# 主函数
if __name__=="__main__":
    # 获取文件输入和输出路径
    read_path,output_path = get_file_path()
    # 开始处理文件，并输出处理文件结果
    deal_files()