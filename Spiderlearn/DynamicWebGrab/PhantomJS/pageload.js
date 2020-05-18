var page = require('webpage').create();

//缩放与裁剪
page.viewportSize = {width:1024, height:768};
page.clipRect = { top:0, left:0, width:512, height:256 };

page.open('http://www.cnblogs.com/qiyeboy/',function(status){
	console.log("Status: " + status);//加载
	if(status === "success"){
		page.render('qiye.png');  //保存图片
	}
	phantom.exit();
})