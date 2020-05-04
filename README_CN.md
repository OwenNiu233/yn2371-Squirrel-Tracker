(仅是[Squirrel Tracker](https://docs.google.com/document/d/1SPv3fMDKiemrR86rD-S9ecvI2npz3PljDzwCfxK2x5g/edit)的部分翻译，未调整格式）

怪异的亿万富翁Joffrey Hosencratz刚刚购买了您从事的网站开发公司。您曾经在电梯上遇到过他。他对您使用Django框架开发Web应用程序的技巧印象深刻。他还说，他最近一次去亚利桑那州塞多纳的行程给他带来了一些麻烦。看得出来，他喜欢《瑞克与莫迪》，里面一个涉及童年时期留下的对松鼠的心理阴影以及在瑟多纳的糟糕水晶浴经历的场景让他念念不忘。

他计划从中央公园开始, 跟踪所有已知的松鼠。他被要求您构建一个应用程序，该应用程序可以导入2018年中央公园松鼠普查数据，并允许他的团队添加、更新、和查看松鼠数据。

该项目应基于Django，并应具有以下功能（features）：
 
-	管理命令（Management commands）：        
•	导入（import）：可用于从2018年人口普查文件（CSV格式）导入数据的命令。文件路径应在管理命令名称后的命令行中指定。
-	$ python manage.py import_squirrel_data /path/to/file.csv         
-	松鼠普查文件可以在这里下载：
https://data.cityofnewyork.us/api/views/vfnx-vebw/rows.csv
•	导出（export）：可用于以CSV格式导出数据的命令。文件路径应在管理命令名称后的命令行中指定。
-	$ python manage.py export_squirrel_data /path/to/file.csv         

-	视图（Views:）：         
-	显示地图，该地图在OpenStreets地图上显示松鼠瞄准点的位置。         
-	位于（Located at）：/ map         
-	支持的方法（Methods Supported）：GET         
-	将使用https://leafletjs.com/库进行绘图         
	请注意：如果一次绘制100点以上，您的浏览器将冻结。我们将假定客户对这个问题没有意见。任何100个唯一坐标都可以。         
-	您可以在此处找到HTML模板：https://gist.github.com/logston/0b6f2cbb928a386decd63fd616d084dd         
-	列出所有松鼠目击事件的视图，并带有查看每个目击事件的链接         
-	位于：/ sightings         
-	支持的方法：GET         
-	要显示的字段：         
-	唯一(unique)的松鼠ID         
-	日期         
-	到每个松鼠目击事件的链接         
-	此视图还应具有指向“添加”瞄准视图的单个链接

-	更新特定目击事件的视图         
-	位于：/ sightings / <unique-squirrel-id>         
-	支持的方法：GET ＆POST         
-	要显示的字段：         
-	纬度         
-	经度         
-	唯一的松鼠ID         
-	转变         
-	日期         
-	年龄         
-	添加新的目击事件        
-	位于：/ sightings / add         
-	支持的方法：GET ＆POST         
-	支持的字段：         
-	纬度         
-	经度         
-	唯一的松鼠ID         
-	转变         
-	日期         
-	年龄         
-	皮毛原色         
-	位置         
-	具体位置         
-	跑步         
-	追逐         
-	攀登         
-	吃         
-	觅食         
-	其他活动         
-	库克斯         
-	夸斯         
-	呻吟         
-	尾巴标志         
-	尾巴抽搐         
-	方法         
-	冷漠         
-	从哪里跑出来     

-	有关目击事件的一般统计数据的视图         
-	具体统计信息由您决定，但必须包括初始CSV下载中列出的五个属性。         
-	位于：/ sightings / stats        
-	方法：GET         
