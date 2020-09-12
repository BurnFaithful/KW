<%@ page import="youngmin.login.UserDAO" %>
<% request.setCharacterEncoding("UTF-8"); %>
<%--
  Created by IntelliJ IDEA.
  User: user
  Date: 2019-11-13
  Time: 오후 4:24
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<jsp:useBean id="user" class="youngmin.login.UserDTO" scope="page" />
<jsp:setProperty name="user" property="*"/>
<html>
<head>
    <title>Join Action</title>
</head>
<body>
<%
    UserDAO userDAO = new UserDAO();
    int joinResult = userDAO.join(user);

    if (joinResult >= 1) {
        session.setAttribute("userID", user.getUserID());
        response.sendRedirect("main.jsp?pageName=Main");
    }
%>
</body>
</html>
