<%@ page import="youngmin.login.UserDAO" %><%--
  Created by IntelliJ IDEA.
  User: user
  Date: 2019-11-13
  Time: 오후 1:27
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>login_Action</title>
    <script src="../../js/check_user.js"></script>
</head>
<body>
<%
    String userID = null;
    if (session.getAttribute("userID") != null)
        userID = session.getAttribute("userID").toString();
%>
    <script> checkLoginSession(<%= userID %>, "main.jsp?pageName=Main")</script>
<%
    UserDAO userDAO = new UserDAO();
    int loginResult = userDAO.login(request.getParameter("userID"), request.getParameter("userPW"));

    if (loginResult == 1) {
        session.setAttribute("userID", request.getParameter("userID"));
        response.sendRedirect("main.jsp?pageName=Main");
    }
%>
</body>
</html>