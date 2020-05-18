phantom.outputEncoding="GBK";//中文乱码问题
var url = 'http://www.baidu.com/';
var page = require('webpage').create();
//page.open(url,function(status){//function是网页打开后的回调函数
//    var title = page.evaluate(function(){
//    return document.title;
//    });
//    console.log('Page title is ' + title);
//    phantom.exit();
//});


page.onConsoleMessage = function(msg){
    console.log('Page title is ' + msg);
};
page.open(url,function(status){//function是网页打开后的回调函数
    page.evaluate(function(){
    console.log(document.title);
    });
    phantom.exit();
});