phantom.outputEncoding="GBK";//中文乱码问题
var url = 'http://www.baidu.com/';
var page = require('webpage').create();
page.onResourceRequested = function(request){
    console.log('Request ' + JSON.stringify(request,undefined,4));
};
page.onResourceReceived = function(response){
    console.log('Receive ' + JSON.stringify(response,undefined,4));
};
page.open(url);