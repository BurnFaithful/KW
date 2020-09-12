<%--
  Created by IntelliJ IDEA.
  User: user
  Date: 2019-10-02
  Time: 오후 1:35
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <meta charset="UTF-8">
    <title>Footer</title>
</head>
<body>
    <h2>Footer.jsp</h2>
    <hr>
    <%= request.getParameter("email") %>
    <%= request.getParameter("tel") %>

    <% out.println(request.getParameter("tel")); %>
</body>
</html>
