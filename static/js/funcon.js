/**
 * Created by administer on 2017/8/11.
 */
// JavaScript Document
//modalģ̬���
function modal_layer(){
    var modal=document.createElement('div');
    modal.id="black_modal";
    modal.className="modal";
    document.body.appendChild(modal);
};

//��¼��
function login_box(){
    //����ģ̬��
    modal_layer();
    var modal=document.getElementById('black_modal');

    //��������
    var oDiv=document.createElement('div');
    oDiv.id="logon_box";
    oDiv.className="popBox popBox_logon";

    var html='<h4>用户登录</h4>'+
        '<a id="closeBtn" class="close_btn" href="javascript:;">×</a>'+
        '<p><label>用户名：<input type="text"></label></p>'+
        '<p><label>密&nbsp;&nbsp;&nbsp;&nbsp;码：<input type="password"></label></p>'+
        '<p><button id="logonBtn" class="logonBtn" type="button">登录</button></p>';

    //oDiv�ڲ���������Ԫ��
    oDiv.innerHTML=html;

    document.body.appendChild(oDiv);//���뵽ҳ��

    var closeBtn=document.getElementById('closeBtn');
    var title=oDiv.getElementsByTagName('h4')[0];
    var input=document.getElementsByTagName('input');

    input[0].onmousedown=function(ev){//�������ֹð�ݣ�������������
        var oEv=ev ||window.event;
        oEv.cancelBubble=true;
    };
    input[1].onmousedown=function(ev){//�������ֹð�ݣ�������������
        var oEv=ev ||window.event;
        oEv.cancelBubble=true;
    }

    modal.style.display="block";//��ʾģ̬��

    popShow(oDiv,title);//������ʾ
    drag(oDiv,title);//������ק

    //�رյ���
    closeBtn.onclick=function(){
        document.body.removeChild(modal);
        document.body.removeChild(oDiv);
    };
}