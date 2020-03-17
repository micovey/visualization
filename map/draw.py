# -*- coding: utf-8 -*-
from pandas import read_csv
import pyecharts.options as opts
from pyecharts.commons.utils import JsCode
from pyecharts.charts import Timeline, Grid, Map

class Draw:
	def __init__(self,file):
		self.save = "test"
		self.world = read_csv(file)
		self.day = self.world.columns.to_list()[2:]
		self.min_data = self.world[self.day].max().max()
		self.max_data = self.world[self.day].min().min()
		self.type = "world"
		self.zoom = 1
		self.center = None
		self.areaColor = "MistyRose"
		self.title = "title"
		self.range_color=["LightSalmon", "red"]
		self.theme = "black"
		self.titlesize = 22
		self.titlecolor = "rgba(255,255,255, 0.9)"
		self.vis = "label"


	def __get_country_daily(self,w,dayind,k):
		once = {}
		lst = []
		once["name"] = str(w["indicator"][k])
		lst.append(int(w[dayind][k]))
		lst.append(str(w["ct"][k]))                  
		once["value"] = lst
		return once

	def __get_all_daily(self,w,dayind):
		daily = {}
		daily["time"] = dayind
		daily["data"] = []
		for k in range(len(w)):
			daily["data"].append(self.__get_country_daily(w,dayind,k))
		return daily

	def __get_all(self,world):
		data = []
		for dayind in world.columns.to_list()[2:]:
			w = world.sort_values(by = [dayind],ascending = [False]) 
			w.index = range(len(w))
			if self.dropzero ==1: # Whether to drop 0
				w = w[~w[dayind].isin([0])].dropna(axis = 0)
			data.append(self.__get_all_daily(w,dayind))
		return data 

	def __get_year_chart(self,data,day_ind):
		if self.vis == "label":
			formatter = JsCode("""function(params){
		                    if (params.data) {
		                        return params.data.value[0];
		                    }
		                    else{
		                        return ' ';
		                    }
		                }""")
		else:
			formatter = JsCode("""function(params){
	            			if (params.data) {
	                			return params.data.value[1] + ':' + params.data.value[0];
	            			}
	            			else{
	                			return ' ';
	            			}
	        			}""")
		if self.type == "world":
			self.center = [20,10]
		map_data = [[[x["name"], x["value"]] for x in d["data"]] for d in data if d["time"] == day_ind][0]
		map_chart = (
	        Map()
	        .add("",map_data,self.type,
	        	center = self.center,
	        	zoom = self.zoom,
	        	is_map_symbol_show = False,
	        	itemstyle_opts={
	        		"normal": {"areaColor": self.areaColor, "borderColor": "#404a59"},
	                "emphasis": {
	                	"label": {"show": Timeline},
	                	"areaColor": "oranged",
	               		},
	           		},
	        )
	        
	        .set_global_opts(
	            title_opts=opts.TitleOpts(
	                title="" + str(day_ind) + self.title,
	                subtitle="",
	                pos_left="center",
	                pos_top="5%",
	                title_textstyle_opts=opts.TextStyleOpts(font_size=self.titlesize, color=self.titlecolor),
	            ),
	            tooltip_opts=opts.TooltipOpts(
	                is_show=True,
	            ),
	            visualmap_opts=opts.VisualMapOpts(
	                is_calculable=True,
	                dimension=0,
	                pos_left="30",
	                pos_top="5%",
	                range_text=["High", "Low"],
	                range_color=self.range_color,
	                textstyle_opts=opts.TextStyleOpts(color="#ddd"),
	                min_=self.min_data,
	                max_=self.max_data,
	            ),
	        )
	    	.set_series_opts(
	            label_opts=opts.LabelOpts(
	                color = "gray",
	                is_show=True,
	                formatter = formatter
	            )
	        )
    	)
		grid_chart = (
			Grid()
			.add(map_chart, grid_opts=opts.GridOpts())
        )

		return grid_chart

	def timeline(self):
		time_list = [str(d) for d in self.day]
		timeline = Timeline(
			init_opts=opts.InitOpts(width="1600px", height="900px", theme=self.theme)
		)
		for y in time_list:
			g = self.__get_year_chart(self.data,y)
			timeline.add(g, time_point=str(y[5:]))
		timeline.add_schema(
			orient="vertical",
			is_auto_play=True,
			is_inverse=True,
			play_interval=1000,
			pos_left="null",
			pos_right="5",
			pos_top="20",
			pos_bottom="20",
			width="60",
		)
		save = self.save + ".html"
		print(save)

		timeline.render(save)

	def run(self):
		self.data = self.__get_all(self.world)
		self.timeline()


if __name__=='__main__':
    file = input("please input file name (eg: D:\\p\\example_world.csv):") 
    D = Draw(file)
    D.dropzero = input("drop the country or province value 0? (1:drop, 0: do not drop)") 
    D.title = input("title:") 
    D.titlecolor = input("titlecolor:") 
    D.vis = input("if you only want label please input 'label'(you do not need to input' '), else if you also want value please input 'value':")
    D.save = input("filename to save?")
    D.type = input("world or china?")
    D.theme = input("backgroud:dark or white?")
    D.areaColor = input("color of countries or provinces that lack of data?(eg:wheat)")
    min1 = input("color of min:(eg:pink)")
    max1 = input("color of max:(eg:red)")
    D.range_color=[min1, max1]
    D.run()
