<%@ page import="youngmin.bbs.ReviewbbsDTO" %>
<%@ page import="youngmin.bbs.ReviewbbsDAO" %><%--
  Created by IntelliJ IDEA.
  User: user
  Date: 2019-11-18
  Time: 오전 12:42
  To change this template use File | Settings | File Templates.
--%>
<% request.setCharacterEncoding("UTF-8"); %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Review Write</title>
</head>
<body>
<%
    ReviewbbsDAO reviewDAO = new ReviewbbsDAO();
    String userID = session.getAttribute("userID").toString();
    int writeResult = reviewDAO.write(userID, userID,
            request.getParameter("reviewTitle"),
            request.getParameter("reviewContent"));

    response.sendRedirect("review_list.jsp?pageName=Review_List");
%>
</body>
</html>
