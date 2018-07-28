# @Author  : ShiRui

import xlrd
from pylab import *
import matplotlib.pyplot as plt


def data_visualization_education():

	mpl.rcParams['font.sans-serif'] = ['SimHei']  # 定义显示的字体，不然中文会出现乱码
	workbook = xlrd.open_workbook('PythonWorkAnalysis.xls')  # 打开文件
	SheetList = workbook.sheet_names()  # 创建sheetlist
	SheetName = SheetList[0]  # sheetname
	Sheet1 = workbook.sheet_by_name(SheetName)

	shuoshi = 0   # 四个变量
	benke = 0
	dazhuan = 0
	buxian = 0

	for i in range(Sheet1.nrows):

		rows = Sheet1.row_values(i)  # 表格中的数据

		if rows[2] == '硕士':  # row[2] 就是学历那一栏
			shuoshi += 1   # 如果是就+1

		elif rows[2] == '本科':
			benke += 1

		elif rows[2] == '大专':

			dazhuan += 1

		elif rows[2] == '不限':

			buxian += 1

	name_list = ['硕士', '本科', '大专', '不限']  # 要显示的数据
	num_list = [shuoshi, benke, dazhuan, buxian]  # 显示的数量列表
	plt.bar(range(len(num_list)), num_list, color='rgb', tick_label=name_list)  # 绘制图片
	plt.show()  # 展示图片


def visual_education_of_educational_background():

	mpl.rcParams['font.sans-serif'] = ['SimHei']
	workbook = xlrd.open_workbook('PythonWorkAnalysis.xls')
	SheetList = workbook.sheet_names()
	SheetName = SheetList[0]
	Sheet1 = workbook.sheet_by_name(SheetName)

	a_year = 0
	one_three = 0
	three_five = 0
	five_ten = 0
	buxian = 0

	for i in range(Sheet1.nrows):

		rows = Sheet1.row_values(i)

		if rows[1] == '1年以下':

			a_year += 1

		elif rows[1] == '1-3年':

			one_three += 1

		elif rows[1] == '3-5年':

			three_five += 1

		elif rows[1] == '5-10年':

			five_ten += 1

		elif rows[1] == '不限':

			buxian += 1

	name_list = ['1年以下', '1-3年', '3-5年', '5-10年', '不限']
	num_list = [a_year, one_three, three_five, five_ten, buxian]
	plt.bar(range(len(num_list)), num_list, color='rgb', tick_label=name_list)
	plt.show()

if __name__ == "__main__":

	print("1:学历, 2:工作经验。")  # 博主绘制了两个表格，一个是学历，一个是工作经验的
	num = int(input("请输入你想可视化的序号："))

	if num == 1:

		data_visualization_education()

	elif num == 2:

		visual_education_of_educational_background()
