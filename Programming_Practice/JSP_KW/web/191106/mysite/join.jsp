<%--
  Created by IntelliJ IDEA.
  User: user
  Date: 2019-11-13
  Time: 오후 3:51
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <%@include file="file_header.jsp" %>

    <script type="text/javascript">
    function validate()
    {
        var userId = document.getElementById("userId");
        var userPw = document.getElementById("userPw");
        var userName = document.getElementById("userName");
        var nickname = document.getElementById("nickname");
        var phoneNumber = document.getElementById("phoneNumber");
        var sex = document.getElementsByName("sex");

        var sexChecked = null;
        for (var i = 0; i < sex.length; ++i)
        {
            if (sex[i].checked === true)
            sexChecked = sex[i].value;
        }

        if (!userId.value || !userPw.value || !userName.value || !nickname.value || !phoneNumber.value || !sexChecked)
        {
            alert("필수사항 중 입력되지 않은 사항이 있습니다.");
            return false;
        }

        return true;
    }
    </script>

    <title>Sign up</title>
</head>
<body>
<%@include file="page_header.jsp" %>

<div class="container">
    <div class="col-lg-4"></div>
    <div class="col-lg-4">
        <div class="jumbotron">
            <form name="joinForm" method="post" onsubmit="return validate();" action="join_Action.jsp">
                <h3 style="text-align: center;">채널 회원가입</h3>
                <div class="form-group">
                    <input type="text" class="form-control" id="userID" name="userID" placeholder="아이디" maxlength="15">
                </div>
                <div class="form-group">
                    <input type="password" class="form-control" id="userPW" name="userPW" placeholder="비밀번호" maxlength="15">
                </div>
                <div class="form-group">
                    <input type="text" class="form-control" id="userName" name="userName" placeholder="이름" maxlength="15">
                </div>
                <div class="form-group">
                    <input type="text" class="form-control" id="userNickname" name="userNickname" placeholder="닉네임" maxlength="20">
                </div>
                <div class="form-group">
                    <input type="text" class="form-control" id="phoneNumber" name="phoneNumber" placeholder="전화번호" maxlength="30">
                </div>
                <div class="form-group">
                    <input type="email" class="form-control" id="userMail" name="userMail" placeholder="이메일" maxlength="30">
                </div>
                <div class="radio">
                    <label class="radio-inline control-label" for="sex-radio-male">
                        <input type="radio" id="sex-radio-male" name="sex" value="남자"><strong>남자</strong>
                    </label>
                    <label class="radio-inline control-label" for="sex-radio-female">
                        <input type="radio" id="sex-radio-female" name="sex" value="여자"><strong>여자</strong>
                    </label>
                </div>
                <div class="form-group">
                    <input type="submit" class="btn btn-primary form-control" value="회원가입">
                </div>
            </form>
        </div>
    </div>
    <div class="col-lg-4"></div>
</div>

<%@include file="page_footer.jsp" %>
</body>
</html>
