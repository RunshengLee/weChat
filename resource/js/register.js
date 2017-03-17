/**
 * Created by lenovo on 2017/3/16.
 */
 $(document).ready(function () {
     var username = $("#un").val();
     var password = $("#psw").val();
     var phoneNum = $("#pn").val();
     var checkNum = $("#chn").val();

     $("#un").blur(function () {
         $.ajax({
             url:"",
             data:{u:username},
             type:"POST",
             dataType:"TEXT",
             success:function (data) {
                 if(data>0){
                     $("#hint").html("该用户名已存在");
                     $("#hint").css("color","red");
                 }
                 else{
                     $("#hint").html("该用户名可用");
                     $("#hint").css("color","blue");
                 }

             }
         });
     });

     $("#reg").click(function () {

         $.ajax({
             url:"",
             data:{u:username,p:password,pn:phoneNum,chn:checkNum},
             type:"POST",
             dataType:"TEXT",
             success:function (data) {
                 if(data=="OK"){
                     window.location.href="index.html";
                 }
                 else{
                     alert("Failed!");
                 }

             }

         });

     })
 });
