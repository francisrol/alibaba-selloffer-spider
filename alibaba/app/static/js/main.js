/**
 * Created by whiteHouse on 17/8/17.
 */


var table_template = '<tr> <td>{0}</td> <td>{1}</td> <td>{2}</td> <td>{3}</td> <td>{4}</td> <td>{5}</td> <td>{6}</td> <td>{7}</td> <td><a href="user/user.html"><i class="icon-pencil"></i></a><a href="#myModal" role="button" data-toggle="modal"><i class="icon-remove"></i></a> </td> </tr>';
var spider_manage_btn_template = ' <a href="javascript:void(0);" onclick="start_spider({0}, {1})" class="btn btn-primary"><i class="icon-caret-right"></i> 启动爬虫</a> <a href="javascript:void(0);" onclick="stop_spider({0}, {1})" class="btn btn-danger"><i class="icon-stop"></i> 停止爬虫</a> <a href="javascript:void(0);" onclick="check_spider()" class="btn btn-info"> 查看爬虫</a>'

// 获取商家信息列表
function get_selloffer_list(cid, sid, page){
    $.ajax({
        "url": "/api/selloffers/",
        "type": "GET",
        "data": {
            "cid": cid,
            "sid": sid,
            "page": page
        },
        "success": function(data){
            html='';
            var data = JSON.parse(data);
            var page_count = data.page_count;
            pagination(data.page, page_count, cid, sid);    // 分页
            var selloffers = data.result;
            for(var i=0; i<selloffers.length; i++){
                var temp = selloffers[i];
                var str = table_template.format(
                    i+1,
                    temp.name,
                    temp.business_model,
                    temp.linkman,
                    temp.landline_phone,
                    temp.mobile_phone,
                    temp.address,
                    temp.create_time
                );
                html += str;
            }
            var spider_btn = spider_manage_btn_template.format(cid, sid);
            $("#spider-btn").html(spider_btn);    //更新表格中的数据
            $("#tbody").html(html);
            $(".itemcount .num").html(data.count);
            $(".page-title").html(data.sub_category.name);
        }
    })
}

// 实现分页
function pagination(page, page_count, cid, sid){
    var pre = '';    //上一页
    var middle = '';    //中间
    var next = '';    //下一页
    var pagenation_template = '<li {4}><a {5} href="javascript:void(0);" onclick="get_selloffer_list({0}, {1}, {2})">{3}</a></li>';

    if (page>1){  // 判断是否有上一页
        pre = pagenation_template.format(cid, sid, page-1, "<<", '', '');
    }else{
        pre = pagenation_template.format(cid, sid, page, "<<", 'class="disabled"', '');
    }

    if (page<page_count){    // 判断是否有下一页
        next = pagenation_template.format(cid, sid, page+1, ">>", '');
    }else{
        next = pagenation_template.format(cid, sid, page, ">>", 'class="disabled"', '');
    }

    if (page_count<=7){    //页数低于7页
        for(var i=1; i<=page_count; i++){
            if (i==page){
                middle+=pagenation_template.format(cid, sid, i, i, 'class="active"', 'class="btn-primary"')
            }else{
                middle+=pagenation_template.format(cid, sid, i, i, '', '')
            }
        }
    }else{    //页数高于7页
        if (page>=1&&page<=6){  //页码在1-6页之间
            for(var i=1;i<=6;i++){
                if (i==page){
                    middle+=pagenation_template.format(cid, sid, i, i, 'class="active"', 'class="btn-primary"')
                }else{
                    middle+=pagenation_template.format(cid, sid, i, i, '', '');
                }
            }
            middle += pagenation_template.format(cid, sid, 7, '...', '', '');
            middle+=pagenation_template.format(cid, sid, page_count, page_count, '', '');
        }else if(page>6&&page_count<=10){    //页码在第6页之后，总页数不超过10页时
            middle+=pagenation_template.format(cid, sid, 1, 1, '', '');
            middle+=pagenation_template.format(cid, sid, 2, '...', '', '');
            for(var i=3;i<=page_count;i++){
                if (i==page){
                    middle+=pagenation_template.format(cid, sid, i, i, 'class="active"', 'class="btn-primary"')
                }else{
                    middle+=pagenation_template.format(cid, sid, i, i, '', '');
                }
            }
        }else if(page>6&&page_count>10&&page_count-page>3){   //页码在第6页之后，总页数超过10页，页码不在最后三页内时
            middle+=pagenation_template.format(cid, sid, 1, 1, '', '');
            middle+=pagenation_template.format(cid, sid, page-3, '...', '', '');
            for(var i=page-2;i<=page+2;i++){
                if (i==page){
                    middle+=pagenation_template.format(cid, sid, i, i, 'class="active"', 'class="btn-primary"')
                }else{
                    middle+=pagenation_template.format(cid, sid, i, i, '', '');
                }
            }
            middle+=pagenation_template.format(cid, sid, page+3, '...', '', '');
            middle+=pagenation_template.format(cid, sid, page_count, page_count, '', '');
        }else if(page>6&&page_count>10&&page_count-page<=3){    //页码在第6页之后，总页数超过10页，页码在最后三页内时
            middle+=pagenation_template.format(cid, sid, 1, 1, '', '');
            middle+=pagenation_template.format(cid, sid, page_count-6, '...', '', '');
            for(var i=page_count-5;i<=page_count;i++){
                if (i==page){
                    middle+=pagenation_template.format(cid, sid, i, i, 'class="active"', 'class="btn-primary"')
                }else{
                    middle+=pagenation_template.format(cid, sid, i, i, '', '');
                }
            }
            //middle+=pagenation_template.format(cid, sid, page_count, page_count, '', '');
        }
    }
    $(".pagination ul").html(pre+middle+next);
    $(".disabled a").removeAttr("onclick");
    $(".active a").removeAttr("onclick");
}

// 启动爬虫
function start_spider(cid, sid){
    $.ajax({
        "url": "/api/spider/start/",
        "type": "GET",
        "data": {
            "cid": cid,
            "sid": sid
        },
        "success": function(data){
            alert(data)
        }
    })
}

// 停止爬虫
function stop_spider(cid, sid){
    $.ajax({
        "url": "/api/spider/stop/",
        "type": "GET",
        "data": {
            "cid": cid,
            "sid": sid
        },
        "success": function(data){
            alert(data)
        }
    })
}
// 检查爬虫
function check_spider(){
    $.ajax({
        "url": "/api/spider/check/",
        "type": "GET",
        "success": function(data){
            alert(data)
        }
    })
}
