/**
 * Created by administer on 2017/8/11.
 */
//������ʾ����
function popShow(elm){
    elm.style.display="block";
    var l=(document.documentElement.clientWidth-elm.offsetWidth)/2;
    var t=(document.documentElement.clientHeight-elm.offsetHeight)/2;
    elm.style.left=l+'px';
    elm.style.top=t+'px';
};


//��ק�齨
function drag(box,title){
    //���Ҵ���1������box����קbox
    //���Ҵ���2����������ק����title
    var handle;
    title?handle=title:handle=box;
//----------------------------------------
//����¼� title
    handle.onmousedown=function(ev){//����ʱ��  ��¼�����Ĵ�λλ��
        var oEv=ev || window.event;
        var disX=oEv.clientX-box.offsetLeft;//left����
        var disY=oEv.clientY-box.offsetTop;// top ����

        //����ƶ��Ķ���Ӧ����document
        document.onmousemove=function(ev){//�ƶ���ק
            var oEv=ev || window.event;
            var l=oEv.clientX-disX;
            var t=oEv.clientY-disY;

            //�ж���Ļ��Χ
            if(l<0)l=0;
            if(t<0)t=0;
            if(l>document.documentElement.clientWidth-box.offsetWidth)l=document.documentElement.clientWidth-box.offsetWidth;
            if(t>document.documentElement.clientHeight-box.offsetHeight)t=document.documentElement.clientHeight-box.offsetHeight;

            //���ֵ
            box.style.left=l+'px';
            box.style.top=t+'px';
        };

        //�ͷ����move�¼�
        document.onmouseup=function(){
            document.onmouseup=document.onmousemove=null;
            if(box.releaseCapture)	box.releaseCapture();//ȡ����
        }
        if(box.setCapture)	box.setCapture();//���ò���
        return false;
    };
};