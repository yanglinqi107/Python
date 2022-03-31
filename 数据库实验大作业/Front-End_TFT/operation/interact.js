
let home = document.getElementById('Home');
let main = document.getElementById('Main');
let cardPage = document.getElementById('card-page');
location.hash = '/';            //解决浏览器刷新路由不跳转问题
class Router{
    constructor(){
        this.routs = {};
        this.curURL = '';
    }

    //监听路由变化
    init(){
        window.addEventListener('hashchange',this.reloadPage.bind(this)); //this指代当前路由hash
    }
    //获取路由参数
    reloadPage(){
        this.curURL = location.hash.substring(1)||'/';        //获取页面路由，以第一个字符(即#)做分割，没有内容则取"/"
        this.routs[this.curURL]();
    }
    //保存路由对应的函数
    map(key,callback){
        this.routs[key] = callback;
    }
}

const iRouter = new Router();
//初始页
iRouter.map('/',()=>{
    home.style.display = 'inline';
    main.style.display = 'none';
    cardPage.style.display = 'none';

})
//主界面
iRouter.map('/main',()=>{
    home.style.display = 'none';
    main.style.display = 'inline';
    cardPage.style.display = 'none';
})

iRouter.map('/page',()=>{
    home.style.display = 'none';
    main.style.display = 'none';
    cardPage.style.display = 'inline';
})

//启动监听
iRouter.init();

// //无条件刷新页面（用于不改变路由的浏览器刷新响应）
// iRouter.reloadPage();

//管理员登录
//打开登录界面
let login = document.getElementById('login');       //实际上包含id属性元素的都不需要筛选
let AdLogin = document.getElementsByClassName('login-Ad')[0];
let isLogin = 0;
AdLogin.onclick = function(){
    let login = document.getElementById('login');
    login.style.display = 'block';
    if(!isLogin)
    {
        //显示登录界面
        loginInPage.style.display = 'block';
        loginOutPage.style.display = 'none';

    }else{
        //显示退出界面
        loginInPage.style.display = 'none';
        loginOutPage.style.display = 'block';
    }
}

//刷新登录状态
function flesh_login_status(){
    let loginStatus = document.getElementsByClassName('login-status')[0];
    let AdText = document.getElementsByClassName('Administer-text')[0];
    backUp.style.display = 'none';
    AdText.style.display = 'none';
    remove_detele();
    //用户或非登录状态背景
    document.body.style.backgroundColor = '#648ca4';
    
    if(isLogin === 1){
        loginStatus.firstChild.data = "用户--已登录";
    }else if(isLogin === 2){
        loginStatus.firstChild.data = "管理员--已登录";
        backUp.style.display = 'inline-block';
        AdText.style.display = 'inline-block';
        //管理员登录背景
        document.body.style.backgroundColor = '#191f25';
        Ad_delete();        

    }else{
        loginStatus.firstChild.data = "未登录...";
    }
}

//关闭登录界面
let loginClose = document.getElementsByClassName('close')[0];
loginClose.onclick = function(){
    login.style.display = 'none';
}
//登录--退出登录实现
let loginBtn = document.getElementById('login-submit');
let loginInPage = document.getElementsByClassName('login-page')[0];
let loginOutPage = document.getElementsByClassName('login-page')[1];
//登录事件
loginBtn.onclick = function(){
    let account = document.getElementsByClassName('input-act')[0].value;
    let password = document.getElementsByClassName('input-pwd')[0].value;

    $.ajax({
        url: 'http://127.0.0.1:8000/users/login/',
        data: {id: account,pwd: password},
        success: function(Str){
            if(Str === "1"||Str === "2"){           
                // login_success();
                alert_trans(true,'登录成功！');
                isLogin = parseInt(Str);
                login.style.display = 'none';
                getAll();
                flesh_login_status();
            }else{              //打印错误信息
                alert_trans(false,Str);
            }
        },
        error: function(){
            alert_trans(false,"登录出错！");
        },
    })
}
//已登录按钮
let affirm = document.getElementsByClassName('OK')[0];
let loginOut = document.getElementsByClassName('login-out')[0];
affirm.onclick = function(){
    login.style.display = 'none';
}
loginOut.onclick = function(){
    isLogin = 0;
    login.style.display = 'none';
    alert_trans(true,"已退出");
    getAll();
    flesh_login_status();
}

// //登陆成功淡出提示
// function login_success(){}

//注册
let regisiter = document.getElementById('regisiter');
regisiter.onclick = function(){
    let account = document.getElementsByClassName('input-act')[0].value;
    let password = document.getElementsByClassName('input-pwd')[0].value;

    $.ajax({
        url: 'http://127.0.0.1:8000/user/register/',
        data: {id: account,pwd: password},
        success: function(Str){
            if(Str){           
                alert_trans(true,'用户注册成功！已自动登录...');
                isLogin = parseInt(Str);
                login.style.display = 'none';
                getAll();
                flesh_login_status();
            }else{              //打印错误信息
                alert_trans(false,Str);
            }
        },
        error: function(){
            alert_trans(false,"注册出错！");
        },
    })
}


//获取所有卡片
//使用div并将点击事件设置在监听触发之后
//不用a标签跳转，防止在监听生效之前用户就已经触发hash变更，导致BUG
let coming_btn = document.getElementsByClassName('coming-btn')[0];

coming_btn.onclick = function(){
    document.body.style.backgroundImage = 'url(' + 'http://game.gtimg.cn/images/lol/tft/content-site/bg-top.png' + ')';
    document.body.style.backgroundSize = '100% 100%';
    getAll();
};

//封装函数--获取所有数据（+背景）
function getAll(){
    location.hash = "/main";
    //发送GET请求获取卡片列表数据并展示
    const xhr = new XMLHttpRequest();
    xhr.open('GET','http://127.0.0.1:8000/cards/all');
    xhr.send();
    xhr.onreadystatechange = function(){
        if(xhr.readyState === 4){
            if(xhr.status >= 200 && xhr.status < 300){
                Cards = JSON.parse(xhr.response);
                //数据展示--动态卡片生成
                card_list_create(Cards);
            }else{
                alert_trans(false,"请求失败");
            }
        }
    }
}


//卡片集生成
function card_list_create(Card_array){
    //刷新列表
    let Ul = document.getElementsByClassName('champion-list')[0];
    Ul.innerHTML = "";
    //生成卡片
    for(let i = 0;i < Card_array.length;i ++){
        let Card = Card_array[i];
        card_create(Card);
    }
}
//获取卡片集
let cardUl = document.getElementsByClassName('champion-list')[0];
//动态卡片生成
function card_create(Card){
    //生成卡片结构（图片框架--图片块+描述块）
    let cardLi = document.createElement('li');
    cardLi.setAttribute('class','champion-item');
    let cardPic = document.createElement('div');
    cardPic.setAttribute('class','card-pic');
    let cardInfo = document.createElement('div');
    cardInfo.setAttribute('class','card-info');
    let cardName = document.createElement('span');
    cardName.setAttribute('class','name');
    let cardPrice = document.createElement('span');
    cardPrice.setAttribute('class','price');
    let cardIcon = document.createElement('i');
    cardIcon.setAttribute('class','iconfont icon-jinbi');
    cardPrice.appendChild(cardIcon);
    cardUl.appendChild(cardLi);
    cardLi.append(cardPic,cardInfo);
    cardInfo.append(cardName,cardPrice);

    
    //角色图片
    cardPic.style.backgroundImage = 'url(' + Card.img + ')';
    cardPic.style.backgroundSize = "cover";
    cardLi.setAttribute('value',Card.id);      //卡片绑定ID，便于点击搜索
    //羁绊 --动态生成span加到图片div末尾
    //生成羁绊框架
    let cardFetter = document.createElement('p');
    cardFetter.setAttribute('class','fetter');
    cardPic.append(cardFetter);
    //添加羁绊图标+描述
    for(let i = 0;i < Card.fetters.length;i ++){
    //生成使每个羁绊独占一行的容器
    let FetterInline = document.createElement('p');
    let fetter = Card.fetters[i];
    let fetterIcon = document.createElement('div');
    fetterIcon.setAttribute('class','fetter-img');
    fetterIcon.style.backgroundImage = 'url(' + fetter.img + ')';
    fetterIcon.style.backgroundSize = 'cover';
    FetterInline.appendChild(fetterIcon);
    let fetterName = document.createElement('span');
    fetterName.setAttribute('class','fetter-fname');

    fetterName.append(fetter.fname);
    FetterInline.appendChild(fetterName);
    cardFetter.appendChild(FetterInline);
    }
    //名称+价格
    // let cardInfo = document.getElementsByClassName('card-info')[i];
    cardInfo.firstElementChild.append(Card.name);
    cardInfo.lastElementChild.append(Card.price + "金币");
}

//下拉按钮调出菜单
let selectBox = document.getElementsByClassName('select-box');
let flags = [false,false,false];               //flag除了自己，还供下拉菜单调用

//下拉菜单状态刷新
function refleshMenu(){
    let selectMenus = document.getElementsByClassName('select-options');
    //关闭所有菜单
    for(let i = 0;i < selectMenus.length;i ++){
        selectMenus[i].style.display = 'none';
    }
    //重置为未打开状态
    for(let i = 0;i < flags.length;i ++){
        flags[i] = false;
    }
}
//绑定点击下拉事件
for(let i = 0; i < selectBox.length;i ++){
    selectBox[i].onclick = function(){
        let thisMenu = this.lastElementChild;       //最后的子元素为下拉菜单
        if(!flags[i]){                              //关闭其他选项菜单,打开该菜单
            refleshMenu();
            //打开该菜单
            thisMenu.style.display = 'block';
        }
        else{thisMenu.style.display = 'none';}
        flags[i] = !flags[i];
    }
}

//选项--点击事件委托
let chooceUls = document.getElementsByClassName('select-options');

//清空选项文本
function clearSelect(){
    let selectTexts = document.getElementsByClassName('select-text');
    selectTexts[0].firstChild.data = "费用";
    selectTexts[1].firstChild.data = "特质";
    selectTexts[2].firstChild.data = "职业";

}

//不同type设置不同站点
function searchUrl(type){
    switch(type){
        case 1 :
            return 'http://127.0.0.1:8000/cards/search/price/';
        case 2 :
            return 'http://127.0.0.1:8000/cards/search/fetters/';
        case 3 :
            return 'http://127.0.0.1:8000/cards/search/name/';
        case 4 :
            return 'http://127.0.0.1:8000/cards/';       //详细页
        default :
        return console.error("搜索出错!");
    }
}

// //头部引入jQuery--实现按需调用       //改为直接在html文件里引入了，防止异步加载过慢
// let jQueryLink = document.createElement('script');
// jQueryLink.setAttribute('src','https://upcdn.b0.upaiyun.com/libs/jquery/jquery-2.0.2.min.js');
// document.head.appendChild(jQueryLink);
// jQueryLink.onload = function(){};

for(let i = 0; i < chooceUls.length;i ++){
    (function(k){
        let selectSpan = chooceUls[k].previousElementSibling.previousElementSibling;     //前两个节点为对应选项文本
        //点击操作
        chooceUls[k].onclick = function(e){
            let event = e || window.event;
            //取消冒泡
            event.stopPropagation?event.stopPropagation():event.stopBubble = false;
            let target = event.target || event.srcElement;
            if(target.nodeName == 'UL')return;          //如果只点到了ul则无操作

            refleshMenu();
            clearSelect();
            document.getElementsByClassName('search-input')[0].value = "";   //清空搜索文本

            //改变文本显示
            let valueText = selectSpan.firstChild.data = target.firstChild.data;

            if(valueText != "全部"){
                //确定搜索类型
                let searchType = 0;
                let targetData ;
                if(parseInt(valueText)){
                    searchType = 1;
                    targetData = 'price='+parseInt(valueText);
                }
                else{
                    searchType = 2;
                    targetData = 'fname='+valueText;
                }
                //请求发送
                $.ajax({
                    url:searchUrl(searchType),
                    data:targetData,
                    type:'GET',
                    dataType:'json',
                    success:function(data){
                        card_list_create(data);
                    },
                    timeout:3000,
                    error:function(){
                        alert_trans(false,"请求失败！");
                    },
                    processData: false,
                    // 告诉jQuery不要去处理发送的数据
                });

            }
            else{
                getAll();
            }
        }
    }(i))
}

//名称搜索--1、监控搜索文本变化；2、按钮搜索

let search_btn = document.getElementsByClassName('search-btn')[0];
let search_text = document.getElementsByClassName('search-input')[0];
//重复请求处理
let jQ = null;
let isSending = false;  //标注是否正在发送Ajax请求
search_btn.onclick = function(){
    let valueText = search_text.value;
    if(isSending)jQ.abort();
    refleshMenu();
    clearSelect();
    if(valueText==""){
        getAll();
        return;
    }
    jQ = $.ajax({
        url:searchUrl(3),
        data:'name='+valueText,
        type:'GET',
        dataType:'json',
        success:function(data){
            card_list_create(data);
            isSending = false;
        },
        timeout:3000,
        error:function(){
            alert_trans(false,"请求失败！");
            isSending = false;
        },
        processData: false,
        // 告诉jQuery不要去处理发送的数据
    })
    isSending = true;
}
// search_btn.onclick = search_text.oninput;


//卡片点击事件委托绑定
cardUl.onclick = function(e){
    let event = e || window.event;
    let target = event.target || event.srcElement;
    if(target.nodeName == 'UL')return;
    //解决target指向问题
    while(target.nodeName != 'LI'){target = target.parentNode;}
    if(!isLogin){
        alert_trans(false,'请先登录');
        AdLogin.onclick();
        return;
    }
    let valueText = target.getAttribute('value');   //int型
    location.hash = "/page";            //更换显示页面
    $.ajax({
        url: searchUrl(4),
        data: {id : valueText},         //发送点击卡片的ID号进行搜索
        type: 'GET',
        dataType: 'json',
        success: function(card){
            detail_config(card);
        },
        timeout: 3000,
        error: function(){
            alert_trans(false,'请求失败！');
        }

    })
}

//详细页面配置
function detail_config(card){
    let cardTitle = document.getElementsByClassName('card-title')[0];
    let championPic = document.getElementsByClassName('champion-pic')[0];
    let championIcon = document.getElementsByClassName('champion-icon')[0];

    let skillPic = document.getElementsByClassName('skill-pic')[0];
    let skillName = document.getElementsByClassName('skill-name')[0];
    let skillType = document.getElementsByClassName('skill-type')[0];
    let skillDesc = document.getElementsByClassName('skill-desc')[0];

    let detailDescs = document.querySelectorAll('.detail-desc p');

    //头像 技能
    cardTitle.innerHTML = "";
    cardTitle.append(card.name);
    championPic.style.backgroundImage='url('+card.img+')';
    championPic.style.backgroundSize = '100% 100%';
    championIcon.style.backgroundImage='url('+card.icon+')';
    championIcon.style.backgroundSize = '100% 100%';
    skillPic.style.backgroundImage='url('+card.skill_img+')';
    skillPic.style.backgroundSize = '100% 100%';
    skillName.innerHTML = "";
    skillName.append(card.skill_name);
    skillType.innerHTML = "";
    skillType.append(card.skill_type);
    skillDesc.innerHTML = "";
    skillDesc.append(card.skill_desc);
    // detailDescs.innerHTML ="";
    // 属性
    let Property = card.property;
    for(let i = 0;i < Property.length;i ++){
        let propertySpan = detailDescs[i].firstElementChild;
        console.log(propertySpan);
        propertySpan.innerHTML = "";
        propertySpan.append(Property[i]);
    }

    //羁绊详细
    let info3 = document.getElementsByClassName('info3')[0];
    info3.innerHTML = "";
    let fetters = card.fetters;
    for(let number in fetters){
        let fetter = fetters[number];       //for in 拿到的是数组下标！不是项！
        let detailBox = document.createElement('div');
        detailBox.setAttribute('class','detail-box');
        info3.appendChild(detailBox);

        let detailTitle = document.createElement('div');
        detailTitle.setAttribute('class','detail-title');
        let fetterImg = document.createElement('img');
        fetterImg.setAttribute('src',fetter.icon);
        detailTitle.append(fetterImg,fetter.fname);

        let detailDesc = document.createElement('div');
        detailDesc.setAttribute('class','detail-desc');
        detailBox.append(detailTitle,detailDesc);

        let descText = document.createElement('p');
        descText.setAttribute('class','desc-text');
        descText.append(fetter.desc);
        detailDesc.appendChild(descText);
        //羁绊描述分割拼接
        let usages = fetter.level.split('$');
        for(number in usages){
            let usage = usages[number];

            let fetterDescSpan = document.createElement('p');
            fetterDescSpan.setAttribute('class','fetter-desc-span');
            let use = usage.split(':');
            let fetterLevel = document.createElement('span');
            fetterLevel.setAttribute('class','fetter-level');
            fetterLevel.append(use[0]);
            fetterDescSpan.append(fetterLevel,use[1]);
            detailDesc.appendChild(fetterDescSpan);
        }
    }

}

// 添加管理员模式下右键提供删除功能
let targetCard ;    //被点击到的卡片
let delBtn = document.getElementsByClassName('delete')[0]
function Ad_delete(){
    //禁用系统右键菜单
    document.oncontextmenu = function(e){return false;}

    cardUl.onmouseup = function(e){
        let event = e || window.event;
        let target = event.target || event.srcElement;
        if(target.nodeName == "UL")return;
        while(target.nodeName != 'LI'){target = target.parentNode;}
        targetCard = target;
        if(event.button == 2){
            delBtn.style.display = 'inline-block';
            let x = event.pageX || e.clientX +(document.body.scrollLeft || document.documentElement.scrollLeft);
            let y = e.pageY || e.clientY +(document.body.scrollTop || document.documentElement.scrollTop);
            delBtn.style.left = x;
            delBtn.style.top = y;
        }
    }
    //左键任意区域使删除按钮消失
    document.onclick = function(){
        delBtn.style.display = 'none';
    }
}
//解除右键提供删除功能--恢复系统右键菜单
function remove_detele(){
    cardUl.onmouseup = null;
    document.oncontextmenu = function(e){return true;}
}

//删除功能--指定id删除
delBtn.onclick = function(){
    let valueText = targetCard.getAttribute('value');
    $.ajax({
        url: 'http://127.0.0.1:8000/cards/delete/',
        type: 'GET',
        data: {id : valueText},
        success: function(){
            alert_trans(true,'---已从数据列表移除---');
            targetCard.remove();
        },
        timeout:2000,
        error: function(){
            alert_trans(false,'删除失败');
        }
        
    });
    this.style.display = 'none';
}

//数据恢复按钮
let backUp = document.getElementsByClassName('back-up')[0];
backUp.onclick = function(){
    $.ajax({
        url: 'http://127.0.0.1:8000/database/resume/',
        type: 'GET',
        success: function(){
            alert_trans(true,"---数据恢复完成---");
            getAll();
            clearSelect();
        },
        timeout:5000,
        error: function(){
            alert_trans(false,'数据恢复失败');
        }
        
    });
}

//弹窗优化--淡出窗口
function alert_trans(flag,str){
    let alertWind = document.createElement('div');
    alertWind.className = 'alert-trans';
    alertWind.append(str);
    //区别--成功和失败的弹窗样式
    if(flag){
        alertWind.style.color = '#deb55c';
    }else{
        alertWind.style.color = 'red';
    }
    document.body.appendChild(alertWind);
    setTimeout(() => {              //需要设置延迟，即使按先后顺序立即添加也会被当做同时添加，不会出现淡出效果
        alertWind.classList.add('fadeout');
    }, 500);
    setTimeout(() => {
        alertWind.remove();
    }, 2500);
}