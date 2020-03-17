# visualization
📣 Introduction<br>
  Input data, color the map with gradient color day by day  <br> 
📝 Usage<br>
+ First, you need to install Python3<br>
+ Second, you need to install pandas and pyecharts<br>
  + if you are in China:<br>
      pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pandas<br>
	    pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyecharts<br>
  + else:<br>
	    pip install pandas<br>
	    pip install pyecharts<br>

+ Third, you need to alter the data(See example).<br>
  + Tips:<br>
	  "indicator": the names countries or cities that pyecharts could recognize <br>
	  "ct": the names of countries or cities that you want to show<br>
+ Fourth, open cmd<br>
	  1. Alter to the current file path<br>
	  2. python draw.py<br>
      note:   not F:\123 python draw.py<br>
      should:<br>
        D:<br>
        cd D:\123<br>
        python draw.py<br>
    3. Add the attribute:
          fileplace  -- eg: example_world.csv<br>
          dropzero -- to show the countries that value 0 or not <br>
          title  -- picture title<br>
          titlecolor<br>
          labelindicator  -- label: eg China:30<br>
                                        value:eg 30<br>
          type  -- world or china<br>
          backgroud  -- dark(black) or white<br>
          reaColor  -- the color of the countries that lack data<br>
          minColor  -- the color of the countries that have the min value <br>
          maxColor  -- the color of the countries that have the min value <br>
          
📣 简介<br>
  输入数据，按照数据大小填充颜色，如果没有数据的国家可以设置为一种特定的颜色<br>
📝 使用<br>
+ 首先，安装python3<br>
+ 其次，安装相应库<br>
  + 境内可以使用清华源,这样更快<br>
      pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pandas<br>
	    pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyecharts<br>
  + 境外直接安装<br>
	    pip install pandas<br>
	    pip install pyecharts<br>

+ 再次，更改数据，变成你想要的数据，见例子<br>
  + 注意：<br>
	  "indicator": 是地图可以识别的名字<br>
	  "ct": 是你想要展示出来的名字<br>
+ 最后，打开cmd<br>
	  1. 改变目录<br>
	  2. 运行python draw.py<br>
      不是:  F:\123 python draw.py<br>
      而是:<br>
        D:<br>
        cd D:\123<br>
        python draw.py<br>
    3. 可以调的属性值:<br>
          文件名  -- eg: example_world.csv<br>
          0值的国家是否显示<br>
          标题、标题颜色<br>
          标签如何显示  -- label: eg China:30<br>
                           value:eg 30<br>
          地图类型<br>
          没有数值的国家颜色<br>
          最小值颜色<br>
          最大值颜色<br>
          文件储存名称<br>
