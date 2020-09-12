<%@ page import="youngmin.login.UserDAO" %><%--
  Created by IntelliJ IDEA.
  User: user
  Date: 2019-11-17
  Time: 오후 11:07
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>회원 탈퇴</title>
</head>
<body>
<%
    UserDAO userDAO = new UserDAO();
    int deleteResult = userDAO.delete(session.getAttribute("userID"));

    if (deleteResult == 1)
    {
        session.invalidate();
        response.sendRedirect("main.jsp?pageName=Main");
    }
    else
    {
        response.sendRedirect("main.jsp?pageName=Main");
    }
%>
</body>
</html>
