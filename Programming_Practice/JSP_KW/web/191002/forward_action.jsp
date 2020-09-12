<%--
  Created by IntelliJ IDEA.
  User: user
  Date: 2019-10-02
  Time: 오후 1:30
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Forward Action</title>
</head>
<body>
    <h2>forward_action</h2>
    <jsp:forward page="footer.jsp">
        <jsp:param name="email" value="burnfaithful@gmail.com"/>
        <jsp:param name="tel" value="010-3346-9910"/>
    </jsp:forward>
</body>
</html>
