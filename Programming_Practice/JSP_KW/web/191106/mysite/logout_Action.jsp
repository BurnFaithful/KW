<%--
  Created by IntelliJ IDEA.
  User: user
  Date: 2019-11-13
  Time: 오후 3:15
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>logout_Action</title>
</head>
<body>
<%
    session.invalidate();
    response.sendRedirect("main.jsp?pageName=Main");
%>
</body>
</html>
