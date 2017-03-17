/**
 * Created by lenovo on 2017/3/16.
 */
 $(document).ready(function() {
    $("#login").click(function () {
        var username = $("#un").val();
        var password = $("#psw").val();

        $.ajax({
            url:"",
            data:{u:username,p:password},
            type:"POST",
            dataType:"TEXT",
            success:function (data) {
                if(data.trim()=="OK"){
                    window.location.href="index.html";
                }
                else{
                    alert("用户名或密码错误");
                }

            }

        });

    })
});
