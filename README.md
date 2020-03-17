# visualization
📣 Introduction
  Input data, color the map with gradient color day by day   
📝 Usage
+ First, you need to install Python3
+ Second, you need to install pandas and pyecharts
  + if you are in China:
      pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pandas
	    pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyecharts
  + else:
	    pip install pandas
	    pip install pyecharts

+ Third, you need to alter the data(See example).
  + Tips:
	  "indicator": the names countries or cities that pyecharts could recognize 
	  "ct": the names of countries or cities that you want to show
+ Fourth, open cmd
	  1. Alter to the current file path
	  2. python draw.py
      note:   not F:\123 python draw.py
      should:
      """
        D:
        cd D:\123
        python draw.py
      """
    3. Add the attribute:
          fileplace  -- eg: example_world.csv
          dropzero -- to show the countries that value 0 or not 
          title  -- picture title
          titlecolor
          labelindicator  -- label: eg China:30
                                        value:eg 30
          type  -- world or china
          backgroud  -- dark(black) or white
          reaColor  -- the color of the countries that lack data
          minColor  -- the color of the countries that have the min value 
          maxColor  -- the color of the countries that have the min value 
          
📣 简介
  输入数据，按照数据大小填充颜色，如果没有数据的国家可以设置为一种特定的颜色
📝 使用
+ 首先，安装python3
+ 其次，安装相应库
  + 境内可以使用清华源,这样更快
      pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pandas
	    pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyecharts
  + 境外直接安装
	    pip install pandas
	    pip install pyecharts

+ 再次，更改数据，变成你想要的数据，见例子
  + 注意：
	  "indicator": 是地图可以识别的名字
	  "ct": 是你想要展示出来的名字
+ 最后，打开cmd
	  1. 改变目录
	  2. 运行python draw.py
      不是:  F:\123 python draw.py
      而是:
      """
        D:
        cd D:\123
        python draw.py
      """
    3. 可以调的属性值:
          文件名  -- eg: example_world.csv
          0值的国家是否显示
          标题、标题颜色
          标签如何显示  -- label: eg China:30
                           value:eg 30
          地图类型
          没有数值的国家颜色
          最小值颜色
          最大值颜色
          文件储存名称
