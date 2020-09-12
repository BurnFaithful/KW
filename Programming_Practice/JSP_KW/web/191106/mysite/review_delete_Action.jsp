<%@ page import="youngmin.bbs.ReviewbbsDAO" %><%--
  Created by IntelliJ IDEA.
  User: user
  Date: 2019-11-20
  Time: 오후 1:33
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Review Delete</title>
</head>
<body>
<%
    ReviewbbsDAO reviewDAO = new ReviewbbsDAO();
    int deleteResult = reviewDAO.delete(Integer.parseInt(request.getParameter("reviewID")));

    response.sendRedirect("review_list.jsp?pageName=Review_List");
%>
</body>
</html>
