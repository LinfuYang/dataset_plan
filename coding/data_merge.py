import pandas as pd
import numpy as np

def data_Merge(path, name):

    name_list = 'pems_'


    df_1 = pd.read_excel(path + name_list + '1.xlsx')
    # print(np.shape(df_1))
    for i in range(2, 10):
        df_2 = pd.read_excel(path + name_list + str(i)+'.xlsx')
        # print(np.shape(df_2))
        df_1 = pd.concat([df_1, df_2])

    # print(np.shape(df_1))
    column = ['5 Minutes', 'Lane 1 Flow (Veh/5 Minutes)', '% Observed']
    df_1[column].to_csv('../data_merge/'+name + '.csv', index=False)




# 目标函数点
# 主干道
data_Merge('../dataset/data_object_line/object_point_760643/', 'M_point')
# 下匝道1
data_Merge('../dataset/data_object_line/OffRampofPoint_760646/', 'offramp_point_760646')
#  下匝道2
data_Merge('../dataset/data_object_line/OffRampofPoint_768608/', 'offramp_point_768608')
# 上匝道1
data_Merge('../dataset/data_object_line/OnRampOfpoint__716521/', 'onramp_point_716521')


# 上游传感器节点
data_Merge('../dataset/object_up_line/object_point_774671/', 'M_point_1')


# 下游传感器节点
data_Merge('../dataset/object_down_line/object_point_718173/', 'M_point_2')

# 上匝道
data_Merge('../dataset/object_down_line/OnRampOfpoint_716523/', 'onramp_point__2_716523')





# data_Merge('../dataset/object_point_1/', 'M_point_1')
# print('object_point_1:ending')

# data_Merge('../dataset/object_point_2/', 'M_point_2')
# print('object_point_2:ending')