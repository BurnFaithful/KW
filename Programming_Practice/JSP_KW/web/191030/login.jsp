<%--
  Created by IntelliJ IDEA.
  User: user
  Date: 2019-10-30
  Time: 오후 1:12
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<jsp:useBean id="login" class="youngmin.login.LoginBean" scope="page"/> <%-- LoginBean 자바클래스를 login이란 식별자를 쓰는 빈즈 객체로 사용 --%>
<jsp:setProperty name="login" property="*"/> <%-- name이 login인 빈즈 객체의 프로퍼티를 모두 set하여 사용 --%>
<html>
<head>
    <title> </title>
    <style type="text/css">
        div {
            text-align: center;
            margin-left: auto;
            margin-right: auto;
        }
    </style>
</head>
<body>
    <div>
        <h2>로그인 예제</h2>
        <hr>
<%
    if (!login.checkUser()) // 아이디와 패스워드가 일치하는지 검사
        out.println("로그인 실패 !!");
    else
        out.println("로그인 성공 !!");
%>

        <hr>
        사용자 아이디 : <jsp:getProperty name="login" property="userId"/><br/> <%-- userId 값을 get --%>
        사용자 패스워드 : <jsp:getProperty name="login" property="userPw"/> <%-- userPw 값을 get --%>
    </div>
</body>
</html>
