<%@ page import="youngmin.login.UserDAO" %>
<% request.setCharacterEncoding("UTF-8"); %><%--
  Created by IntelliJ IDEA.
  User: user
  Date: 2019-11-16
  Time: 오전 2:20
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<jsp:useBean id="user" class="youngmin.login.UserDTO" scope="page"/>
<jsp:setProperty name="user" property="*"/>
<html>
<head>
    <title>Title</title>
</head>
<body>
<%
    UserDAO userDAO = new UserDAO();
    int updateResult = userDAO.update(user);

    response.sendRedirect("main.jsp?pageName=Main");
%>
</body>
</html>
