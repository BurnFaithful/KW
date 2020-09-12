<%@ page import="youngmin.bbs.ReviewbbsDAO" %><%--
  Created by IntelliJ IDEA.
  User: user
  Date: 2019-11-20
  Time: 오후 2:28
  To change this template use File | Settings | File Templates.
--%>
<% request.setCharacterEncoding("UTF-8"); %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Review Modify</title>
</head>
<body>
<%
    ReviewbbsDAO reviewDAO = new ReviewbbsDAO();
    String userID = session.getAttribute("userID").toString();
    int modifyResult = reviewDAO.modify(Integer.parseInt(request.getParameter("reviewID")),
            request.getParameter("reviewTitle"),
            request.getParameter("reviewContent"));

    response.sendRedirect("review_list.jsp?pageName=Review_List");
%>
</body>
</html>
