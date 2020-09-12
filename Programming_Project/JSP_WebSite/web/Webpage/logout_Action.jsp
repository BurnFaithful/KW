<%--
  Created by IntelliJ IDEA.
  User: user
  Date: 2019-10-05
  Time: 오전 3:36
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Logout_Action</title>
</head>
<body>
    <%
        session.invalidate();
    %>
    <script>
        location.href = "main.jsp";
    </script>
</body>
</html>
