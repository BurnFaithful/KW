<%--
  Created by IntelliJ IDEA.
  User: user
  Date: 2019-11-13
  Time: 오후 3:51
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ page import="youngmin.login.UserDTO" %>
<%@ page import="youngmin.login.UserDAO" %>
<html>
<head>
    <%@include file="file_header.jsp" %>

    <script type="text/javascript">
        function validate()
        {
            var userName = document.getElementById("userName");
            var nickname = document.getElementById("nickname");
            var phoneNumber = document.getElementById("phoneNumber");

            if (!userName.value || !nickname.value || !phoneNumber.value)
            {
                alert("입력되지 않은 사항이 있습니다.");
                return false;
            }

            return true;
        }
    </script>

    <title>Sign up</title>
</head>
<body>
<%@include file="page_header.jsp" %>
<%--<nav class="navbar navbar-default">--%>
<%--    <div class="navbar-header">--%>
<%--        <button type="button" class="navbar-toggle collapsed"--%>
<%--                data-toggle="collapse" data-target="#bs-example-navbar-collapse-1"--%>
<%--                aria-expanded="false">--%>
<%--            <span class="icon-bar"></span>--%>
<%--            <span class="icon-bar"></span>--%>
<%--            <span class="icon-bar"></span>--%>
<%--        </button>--%>
<%--        <a class="navbar-brand" href="main.jsp">영민이의 JSP 웹사이트</a>--%>
<%--    </div>--%>
<%--    <div class="collapse navbar-collapse" id="#bs-example-navbar-collapse-1">--%>
<%--        <ul class="nav navbar-nav">--%>
<%--            <li><a href="main.jsp">메인</a></li>--%>
<%--        </ul>--%>
<%--        <ul class="nav navbar-nav navbar-right">--%>
<%--            <li class="dropdown">--%>
<%--                <a href="#" class="dropdown-toggle"--%>
<%--                   data-toggle="dropdown" role="button" aria-haspopup="true"--%>
<%--                   aria-expanded="false">접속하기--%>
<%--                    <span class="caret"></span></a>--%>
<%--                <ul class="dropdown-menu">--%>
<%--                    <li class="active"><a href="join.jsp">회원가입</a></li>--%>
<%--                </ul>--%>
<%--            </li>--%>
<%--        </ul>--%>
<%--    </div>--%>
<%--</nav>--%>

<%
    UserDTO user = new UserDAO().getUserInfo(session.getAttribute("userID").toString());
%>
<div class="container">
    <div class="col-lg-3"></div>
    <div class="col-lg-6">
        <div class="jumbotron">
            <form name="updateForm" method="post" onsubmit="return validate();" action="userinfo_update_Action.jsp">
                <h3 style="text-align: center;">회원정보 수정</h3>
                <div class="form-group">
                    <label>아이디 : <%= user.getUserID()%></label>
                </div>
                <div class="form-group form-inline">
                    <label for="userName">이름 : </label>
                    <input type="text" class="form-control" id="userName" name="userName" placeholder="이름" value="<%= user.getUserName()%>" maxlength="15">
                </div>
                <div class="form-group form-inline">
                    <label for="userNickname">닉네임 : </label>
                    <input type="text" class="form-control" id="userNickname" name="userNickname" placeholder="닉네임" value="<%= user.getUserNickname()%>" maxlength="20">
                </div>
                <div class="form-group form-inline">
                    <label for="phoneNumber">전화번호 : </label>
                    <input type="text" class="form-control" id="phoneNumber" name="phoneNumber" placeholder="전화번호" value="<%= user.getPhoneNumber()%>" maxlength="30">
                </div>
                <div class="form-group form-inline">
                    <label for="userMail">이메일 : </label>
                    <input type="email" class="form-control" id="userMail" name="userMail" placeholder="이메일" value="<%= user.getUserMail()%>" maxlength="30">
                </div>
                <div class="form-group">
                    <input type="submit" class="btn btn-primary form-control" value="회원정보 수정">
                </div>
            </form>
        </div>
    </div>
    <div class="col-lg-3"></div>
</div>

<%@include file="page_footer.jsp" %>
</body>
</html>
